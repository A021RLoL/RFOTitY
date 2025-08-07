# 代码生成时间: 2025-08-08 06:21:40
import numpy as np
# 改进用户体验

"""
消息通知系统

该系统允许用户发送和接收消息。

Attributes:
    None
# NOTE: 重要实现细节

Methods:
    send_message(sender_id, receiver_id, message): 发送消息
# NOTE: 重要实现细节
    receive_message(receiver_id): 接收消息
"""

class MessageNotificationSystem:
    def __init__(self):
        # 初始化一个字典来存储用户的消息
        self.messages = {}

    def send_message(self, sender_id, receiver_id, message):
        """发送消息"""
        # 检查发送者和接收者ID是否有效
# 优化算法效率
        if not isinstance(sender_id, int) or not isinstance(receiver_id, int):
            raise ValueError("发送者和接收者ID必须是整数")

        # 将消息添加到接收者的列表中
        if receiver_id not in self.messages:
            self.messages[receiver_id] = []
        self.messages[receiver_id].append((sender_id, message))

    def receive_message(self, receiver_id):
# 优化算法效率
        """接收消息"""
        # 检查接收者ID是否有效
        if not isinstance(receiver_id, int):
            raise ValueError("接收者ID必须是整数")

        # 获取接收者的消息列表
        messages = self.messages.get(receiver_id, [])

        # 清空接收者的消息列表
        self.messages[receiver_id] = []

        # 返回消息列表
# 优化算法效率
        return messages

# 示例用法
if __name__ == "__main__":
    system = MessageNotificationSystem()
    system.send_message(1, 2, "Hello!")
    system.send_message(3, 2, "How are you?")
    messages = system.receive_message(2)
# NOTE: 重要实现细节
    print(messages)  # 输出: [(1, 'Hello!'), (3, 'How are you?')]
# FIXME: 处理边界情况
