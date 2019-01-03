'''
@Description: 递归-计算列表的和
@Version: 
@Author: biofool2@gmail.com
@Date: 2019-01-03 10:48:50
@LastEditTime: 2019-01-03 11:44:47
@LastEditors: Please set LastEditors
'''


import time

# 计算函数运行时间的装饰器
def timeit(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        func(*args, **kwargs)
        et = time.time()
        return "函数 %s 的运行时间为： %s s" % (func.__name__, (st - et))
    return wrapper


# 一般方法：
@timeit
def list_sum(num_list):
    s = 0
    for i in num_list:
        s += i
    return s

# 递归方法：
# @timeit
def list_num_rec(num_list):
    if not isinstance(num_list, list):
        return num_list
    elif len(num_list) == 0:
        return 0
    elif len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_num_rec(num_list[1:])


if __name__ == '__main__':
    num_list = list(range(10))
    print(list_sum(num_list))
    print(list_num_rec(num_list))