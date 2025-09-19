# 代码生成时间: 2025-09-19 15:46:47
import numpy as np
import schedule
import time
from datetime import datetime

"""
定时任务调度器
"""

class TaskScheduler:
    def __init__(self):
        """初始化调度器"""
        self.tasks = {}

    def add_task(self, task_id, func, time_interval):
        """添加任务
        Args:
            task_id (str): 任务ID
            func (callable): 任务函数
            time_interval (int): 任务执行间隔时间（秒）
        """
        if not callable(func):
            raise ValueError("任务函数必须是可调用的")
        
        # 将任务添加到调度器中
        self.tasks[task_id] = {
            'func': func,
            'time_interval': time_interval
        }
        
        # 安排任务
        schedule.every(time_interval).seconds.do(self._run_task, task_id)
        
    def _run_task(self, task_id):
        """运行任务"""
        try:
            task = self.tasks[task_id]
            task['func']()
            print(f"{datetime.now()} - 任务 {task_id} 执行成功")
        except Exception as e:
            print(f"{datetime.now()} - 任务 {task_id} 执行失败: {str(e)}")
        
    def run(self):
        "