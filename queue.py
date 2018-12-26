'''
@Description: 队列的实现
@Version: 
@Author: biofool2@gmail.com
@Date: 2018-12-26 14:10:20
@LastEditTime: 2018-12-26 18:44:05
@LastEditors: Please set LastEditors
'''


import random

class Queue(object):
    """
    - Queue() 创建一个空的新队列。 它不需要参数，并返回一个空队列。
    - enqueue(item) 将新项添加到队尾。 它需要 item 作为参数，并不返回任何内容。
    - dequeue() 从队首移除项。它不需要参数并返回 item。 队列被修改。
    - is_empty() 查看队列是否为空。它不需要参数，并返回布尔值。
    - size() 返回队列中的项数。它不需要参数，并返回一个整数。
    """
    def __init__(self):
        self._q = []
    
    def is_empty(self):
        return len(self._q) == 0
    
    def enqueue(self, item):
        self._q.insert(0, item)
    
    def dequeue(self):
        return self._q.pop(-1)
    
    def size(self):
        return len(self._q)


def hot_potato(name_list, num):
    """烫手山芋游戏"""
    name_queue = Queue()
    for name in name_list:
        name_queue.enqueue(name)
    cn = 1
    while name_queue.size() > 1:
        for i in range(num):
            name_queue.enqueue(name_queue.dequeue())
        leave = name_queue.dequeue()
        print("Round %d : %s is leaving, size is %s." % (cn, leave, name_queue.size()))
        cn += 1
    
    last_name = name_queue.dequeue()
    return last_name


# -----打印机问题-----
class Printer(object):
    """
    打印机类
    
    需要跟踪它当前是否有任务。如果有，则它处于忙碌状态，并且可以从任务的页数计算所需的时间。
    """
    def __init__(self, pages_per_mins):
        # 每分钟可以处理的页数
        self.page_rate = pages_per_mins
        self.cur_task = None
        self.time_remaining = 0

    def tick(self):
        """
        tick 方法将内部定时器递减直到打印机设置为空闲
        """
        if self.cur_task:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.cur_task = None
    
    def is_busy(self):
        """打印机忙碌状态判定"""
        if self.cur_task:
            return True
        return False
    
    def start_next(self, new_task):
        """开始下一个任务"""
        self.cur_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Task(object):
    """
    打印任务类，表示单个打印任务。
    
    创建任务时，随机数生成器将提供 1 到 20 页的长度。
    每个任务还需要保存一个时间戳用于计算等待时间。此时间戳将表示任务被创建并放置到打印机队列中的时间。
    """
    def __init__(self, timestamp):
        self._ts = timestamp
        self._pages = random.randrange(1, 21)
    
    def get_timestamp(self):
        return self._ts
    
    def get_pages(self):
        return self._pages
    
    def wait_time(self, cur_time):
        return cur_time - self._ts


def is_new_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    return False

def simulate(seconds, pages_per_mins):
    """模拟打印机问题"""
    printer = Printer(pages_per_mins)
    print_queue = Queue()
    wait_times = []

    for cur_seconds in range(seconds):
        if is_new_task():
            task = Task(cur_seconds)
            print_queue.enqueue(task)
        
        if (not printer.is_busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            wait_times.append(next_task.wait_time(cur_seconds))
            printer.start_next(next_task)
        
        printer.tick()
    
    avg_wait_time = sum(wait_times) / len(wait_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (avg_wait_time, print_queue.size()))


# ------- 双端队列实现 -------

class Deque(object):
    """
    实现双端队列

    Deque()          ： 创建一个空的新 deque。它不需要参数，并返回空的 deque。
    add_front(item)  ： 将一个新项添加到 deque 的首部。它需要 item 参数 并不返回任何内容。
    add_rear(item)   ： 将一个新项添加到 deque 的尾部。它需要 item 参数并不返回任何内容。
    remove_front()   ： 从 deque 中删除首项。它不需要参数并返回 item。deque 被修改。
    remove_rear()    ： 从 deque 中删除尾项。它不需要参数并返回 item。deque 被修改。
    is_empty()       ： 测试 deque 是否为空。它不需要参数，并返回布尔值。
    size()           ： 返回 deque 中的项数。它不需要参数，并返回一个整数。
    """
    def __init__(self):
        self._dq = []
    
    def is_empty(self):
        return len(self._dq) == 0
    
    def size(self):
        return len(self._dq)
    
    def add_front(self, item):
        self._dq.append(item)
    
    def add_rear(self, item):
        self._dq.insert(0, item)
    
    def remove_front(self):
        return self._dq.pop()
    
    def remove_rear(self):
        return self._dq.pop(0)

def palindromer_checker(strings):
    """检查是否为回文字符"""
    char_dq = Deque()

    for char in strings:
        char_dq.add_rear(char)
    
    is_pal = True

    while (char_dq.size() > 1) and is_pal:
        first = char_dq.remove_front()
        last = char_dq.remove_rear()

        if first != last:
            is_pal = False
    
    return is_pal


if __name__ == '__main__':
    # q = Queue()
    # print(q.is_empty())
    # q.enqueue(8)
    # q.enqueue(4.0)
    # q.enqueue(True)
    # print(q.size())
    # q.dequeue()
    # print(q.size())
    
    # name_list = ["Bill","David","Susan","Jane","Kent","Brad"]
    # num = 7
    # print(hot_potato(name_list, num))

    # for i in range(10):
    #     simulate(3600, 5)

    print(palindromer_checker("lsdkjfskf"))
    print(palindromer_checker("radar"))