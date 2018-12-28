'''
@Description: 链表的实现
@Version: 
@Author: biofool2@gmail.com
@Date: 2018-12-27 16:15:02
@LastEditTime: 2018-12-28 17:41:55
@LastEditors: Please set LastEditors
'''

"""
List()              : 创建一个新的空列表。它不需要参数，并返回一个空列表。
add(item)           : 向列表中添加一个新项。它需要 item 作为参数，并不返回任何内容。假定该 item 不在列表中。
remove(item)        : 从列表中删除该项。它需要 item 作为参数并修改列表。假设项存在于列表中。
search(item)        : 搜索列表中的项目。它需要 item 作为参数，并返回一个布尔值。
isEmpty()           : 检查列表是否为空。它不需要参数，并返回布尔值。
size()              : 返回列表中的项数。它不需要参数，并返回一个整数。
append(item)        : 将一个新项添加到列表的末尾，使其成为集合中的最后一项。它需要 item 作为参数，并不返回任何内容。假定该项不在列表中。
index(item)         : 返回项在列表中的位置。它需要 item 作为参数并返回索引。假定该项在列表中。
insert(pos, item)   : 在位置 pos 处向列表中添加一个新项。它需要 item 作为参数并不返回任何内容。假设该项不在列表中，并且有足够的现有项使其有 pos 的位置。
pop()               : 删除并返回列表中的最后一个项。假设该列表至少有一个项。
pop(pos)            : 删除并返回位置 pos 处的项。它需要 pos 作为参数并返回项。假定该项在列表中。
"""


class Node(object):
    """
    链表节点。一个节点包含一个值，以及指向下一个节点的指针
    """
    
    def __init__(self, init_data):
        self._data = init_data
        self._next = None

    def get_data(self):
        return self._data
    
    def get_next(self):
        return self._next
    
    def set_data(self, data):
        self._data = data
    
    def set_next(self, new_next):
        self._next = new_next


class UnorderList(object):
    """
    无序链表

    链表类本身不包含任何节点对象。相反，它只包含对链接结构中第一个节点的单个引用。
    """
    def __init__(self):
        self._head = None
    
    def is_empty(self):
        """ isEmpty 方法只是检查链表头是否是 None 的引用"""
        return self._head == None
    
    def add(self, item):
        nd = Node(item)
        nd.set_next(self._head)
        self._head = nd
    
    def size(self):
        curr = self._head
        cnt = 0
        while curr is not None:
            cnt += 1
            curr = curr.get_next()
        
        return cnt
    
    def search(self, item):
        curr = self._head
        found = False
        while not found and curr is not None:
            if curr.get_data() == item:
                found = True
            else:
                curr = curr.get_next()
        return found
    
    def remove(self, item):
        """先找到item，再删除"""
        curr = self._head
        previous = None
        found = False
        while not found:
            if curr.get_data() == item:
                found = True
            else:
                previous = curr
                curr = curr.get_next()
        
        if previous is None:
            # 第一个就找到了
            self._head = curr.get_next()
        else:
            # 其他情况下，把前一个节点的引用指向下一个节点
            previous.set_next(curr.get_next())
    
    def append(self, item):
        """
        将一个新项添加到列表的末尾，使其成为集合中的最后一项。
        它需要 item 作为参数，并不返回任何内容。假定该项不在列表中。
        """
        nd = Node(item)
        curr = self._head
        previous = None
        while curr is not None:
            previous = curr
            curr = curr.get_next()
        
        if previous is None:
            # 如果列表为空
            self._head = nd
        else:
            previous.set_next(nd)

    def insert(self, pos, item):
        """
        在位置 pos 处向列表中添加一个新项。它需要 item 作为参数并不返回任何内容。
        假设该项不在列表中，并且有足够的现有项使其有 pos 的位置。
        """
        nd = Node(item)
        curr = self._head
        prev = None
        cpos = 0
        while curr is not None:
            if cpos == pos:
                prev.set_next(nd)
                nd.set_next(curr)
                break
            else:
                prev = curr
                curr = curr.get_next()
                cpos += 1
        if prev is None:
            # 空列表
            self._head = nd
        if  cpos != pos:
            print("插入位置不合法，默认插到链表尾部")
            prev.set_next(nd)

    def pop(self, pos=None):
        """
        删除并返回列表中的最后一个项。假设该列表至少有一个项。
        如果pos参数不为空，则删除并返回位置 pos 处的项。它需要 pos 作为参数并返回项。假定该项在列表中。
        """
        cpos = 0
        curr = self._head
        prev = None
        while curr is not None:
            if cpos == pos:
                popnode = curr.get_data()
                prev.set_next(curr.get_next())
                break
            else:
                prev = curr
                curr = curr.get_next()
                cpos += 1
        return popnode

    def index(self, item):
        """
        返回项在列表中的位置。它需要 item 作为参数并返回索引。假定该项在列表中。
        """
        curr = self._head
        cpos = 0
        found = False
        while not found and curr is not None:
            if curr.get_data() == item:
                found = True
            else:
                curr = curr.get_next()
                cpos += 1
        return cpos 
            

if __name__ == "__main__":

    mylist = UnorderList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))

    mylist.add(100)
    print(mylist.search(100))
    print(mylist.size())

    mylist.remove(54)
    print(mylist.size())
    mylist.remove(93)
    print(mylist.size())
    mylist.remove(31)
    print(mylist.size())
    print(mylist.search(93))
    mylist.append(250)
    print(mylist.size())
