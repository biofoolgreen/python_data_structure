'''
@Description: 递归-整数转换为任一进制的字符串
@Version: 
@Author: biofool2@gmail.com
@Date: 2019-01-03 11:53:27
@LastEditTime: 2019-01-03 17:29:19
@LastEditors: Please set LastEditors
'''
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def int2str(n, base=10):
    cvt_str = "0123456789ABCDEF"
    if n < base:
        return cvt_str[n]
    else:
        return int2str(n//base, base) + cvt_str[n%base]


# 使用栈帧实现递归
def int2str_stack(n, base=10):
    cvt_str = "0123456789ABCDEF"
    rstack = Stack()
    while n > 0:
        if n < base:
            rstack.push(cvt_str[n])
        else:
            rstack.push(cvt_str[n%base])
        n = n // base
    res = ""
    while not rstack.isEmpty():
        res += str(rstack.pop())
    return res

if __name__ == "__main__":
    print(int2str(1453, 2))
    print(int2str_stack(1453, 2))
