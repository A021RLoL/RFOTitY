# 代码生成时间: 2025-08-19 07:04:43
import numpy as np
import threading
import time
from datetime import datetime, timedelta
from queue import Queue

# 定时任务调度器类
class Scheduler:
    def __init__(self):
        # 初始化任务队列
        self.task_queue = Queue()
        # 锁对象
        self.lock = threading.Lock()
        # 启动调度器线程
        self.scheduler_thread = threading.Thread(target=self._run)
        self.scheduler_thread.daemon = True
        self.scheduler_thread.start()

    # 添加任务
    def add_task(self, task, interval):
        """
        添加任务到队列
        :param task: 要执行的任务函数
        :param interval: 任务执行的间隔时间（秒）
        """
        with self.lock:
            self.task_queue.put((task, interval))

    # 移除任务
    def remove_task(self, task):
        """
        从队列中移除任务
        :param task: 要移除的任务函数
        """
        with self.lock:
            self.task_queue.queue.clear()
            self.task_queue.queue.extend([(t, i) for t, i in self.task_queue.queue if t != task])

    # 调度器运行方法
    def _run(self):
        while True:
            # 检查队列是否为空
            if self.task_queue.empty():
                time.sleep(1)
                continue
            # 获取队列中的任务
            task, interval = self.task_queue.get()
            # 执行任务
            try:
                task()
            except Exception as e:
                print(f"Error executing task: {e}")
            # 重新计算下次运行时间
            next_run_time = datetime.now() + timedelta(seconds=interval)
            # 将任务重新放入队列
            self.task_queue.put((task, interval))
            # 等待直到下次运行时间
            while (datetime.now() - next_run_time).total_seconds() < 0:
                time.sleep(0.1)

# 示例任务函数
def example_task():
    print(f"Task executed at {datetime.now()}")

# 创建调度器实例
scheduler = Scheduler()

# 添加任务
scheduler.add_task(example_task, 5)  # 每5秒执行一次example_task

# 让主线程保持运行，调度器线程会持续执行任务
while True:
    time.sleep(1)