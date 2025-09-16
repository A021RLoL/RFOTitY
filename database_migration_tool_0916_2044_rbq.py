# 代码生成时间: 2025-09-16 20:44:22
import numpy as np
import sqlite3
import logging
from contextlib import closing

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def migrate_database(source_db_path, target_db_path):
    """
    数据库迁移函数，将数据从一个SQLite数据库迁移到另一个SQLite数据库。
    
    参数:
    source_db_path (str): 源数据库文件路径。
    target_db_path (str): 目标数据库文件路径。
    
    返回:
    bool: 迁移是否成功。
    """
    try:
        # 使用上下文管理器确保数据库连接正确关闭
        with closing(sqlite3.connect(source_db_path)) as source_conn, \
             closing(sqlite3.connect(target_db_path)) as target_conn:
            
            # 获取游标
            source_cursor = source_conn.cursor()
            target_cursor = target_conn.cursor()
            
            # 查询源数据库中的表
            source_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = source_cursor.fetchall()
            
            # 遍历每个表并迁移数据
            for table in tables:
                table_name = table[0]
                logging.info(f'Migrating table: {table_name}')
                
                # 查询表结构
                source_cursor.execute(f'PRAGMA table_info({table_name});')
                columns = source_cursor.fetchall()
                column_names = [column[1] for column in columns]
                
                # 创建目标数据库中的表结构
                column_definitions = ', '.join([f'{column_name} TEXT' for column_name in column_names])
                target_cursor.execute(f'CREATE TABLE {table_name} ({column_definitions});')
                target_conn.commit()
                
                # 插入数据
                source_cursor.execute(f'SELECT * FROM {table_name};')
                rows = source_cursor.fetchall()
                for row in rows:
                    placeholders = ', '.join(['?'] * len(row))
                    target_cursor.execute(f'INSERT INTO {table_name} ({