# 代码生成时间: 2025-10-13 20:17:39
import numpy as np

# 模拟数据库中物流信息的存储和查询
class LogisticsDatabase:
    def __init__(self):
        # 使用numpy数组存储物流信息，模拟数据库
        self.data = np.array([], dtype=[('id', '<U10'), ('status', '<U20'), ('location', '<U50')])

    def add_logistics(self, logistics_id, status, location):
        """添加新的物流信息到数据库"""
        new_logistics = np.array([(logistics_id, status, location)], dtype=[('id', '<U10'), ('status', '<U20'), ('location', '<U50')])
        self.data = np.append(self.data, new_logistics)

    def get_logistics_info(self, logistics_id):
        """根据物流ID查询物流信息"""
        try:
            result = self.data[self.data['id'] == logistics_id]
            if len(result) == 0:
                return '物流信息不存在'
            return result
        except Exception as e:
            return f'查询出错: {e}'

# 物流跟踪系统
class LogisticsTrackingSystem:
    def __init__(self):
        self.database = LogisticsDatabase()

    def add_tracking(self, logistics_id, status, location):
        """添加物流跟踪信息"""
        try:
            self.database.add_logistics(logistics_id, status, location)
            return '物流信息添加成功'
        except Exception as e:
            return f'添加物流信息出错: {e}'

    def track_logistics(self, logistics_id):
        """跟踪物流信息"""
        try:
            info = self.database.get_logistics_info(logistics_id)
            if isinstance(info, str):
                return info  # 返回错误信息
            return {'id': info[0]['id'], 'status': info[0]['status'], 'location': info[0]['location']}
        except Exception as e:
            return f'跟踪物流信息出错: {e}'

# 使用示例
if __name__ == '__main__':
    tracking_system = LogisticsTrackingSystem()
    print(tracking_system.add_tracking('001', '运输中', '上海'))
    print(tracking_system.add_tracking('002', '已到达', '北京'))
    print(tracking_system.track_logistics('001'))
    print(tracking_system.track_logistics('003'))  # 测试不存在的物流ID