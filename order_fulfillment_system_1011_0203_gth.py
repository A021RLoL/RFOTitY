# 代码生成时间: 2025-10-11 02:03:23
import numpy as np

"""
订单履行系统模块
提供订单处理功能，包括订单创建、订单取消、订单查询等
"""

class OrderFulfillmentSystem:
    """订单履行系统类"""
    def __init__(self):
        """初始化订单列表"""
        self.orders = []

    def create_order(self, order_id, product_name, quantity):
        """创建订单"""
        if not isinstance(order_id, int):
            raise ValueError("订单ID必须是整数")
        if not isinstance(product_name, str):
            raise ValueError("产品名称必须是字符串")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("数量必须是正整数")

        order = {"order_id": order_id, "product_name": product_name, "quantity": quantity}
        self.orders.append(order)
        return order

    def cancel_order(self, order_id):
        """取消订单"""
        for i, order in enumerate(self.orders):
            if order["order_id"] == order_id:
                del self.orders[i]
                return order
        raise ValueError("订单不存在")

    def query_order(self, order_id):
        """查询订单"""
        for order in self.orders:
            if order["order_id"] == order_id:
                return order
        raise ValueError("订单不存在")

    def get_all_orders(self):
        """获取所有订单"""
        return self.orders

# 示例用法
if __name__ == "__main__":
    system = OrderFulfillmentSystem()

    try:
        # 创建订单
        order1 = system.create_order(1, "苹果", 10)
        order2 = system.create_order(2, "香蕉", 5)
        print("创建的订单：", order1)
        print("创建的订单：", order2)

        # 查询订单
        query_order = system.query_order(1)
        print("查询的订单：", query_order)

        # 取消订单
        cancelled_order = system.cancel_order(2)
        print("取消的订单：", cancelled_order)

        # 获取所有订单
        all_orders = system.get_all_orders()
        print("所有订单：", all_orders)

    except ValueError as e:
        print("错误：", e)