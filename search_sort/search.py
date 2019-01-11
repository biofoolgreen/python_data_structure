'''
@Description: 查找
@Version: 
@Author: biofool2@gmail.com
@Date: 2019-01-10 10:33:38
@LastEditTime: 2019-01-11 10:42:45
@LastEditors: Please set LastEditors
'''

# 1. 顺序查找
# 时间复杂度： 最好O(1)，最差O(n)，平均O(n/2)--> O(n)

def sequential_search(arr, item):
    pos = 0
    found = False
    while pos < len(arr) and not found:
        if arr[pos] == item:
            found = True
        else:
            pos += 1
    
    return found

# 2. 二分查找（仅针对有序列表）
# 时间复杂度： O(logn)

def binary_search(arr, item):
    first = 0
    last = len(arr) - 1
    found = False

    while first < last and not found:
        mid = (first + last) // 2
        if arr[mid] == item:
            found = True
        elif arr[mid] < item:
            # 查找的项在右边
            first = mid
        elif arr[mid] > item:
            # 查找的项在左边
            last = mid
        # else:
        #     if arr[mid] < item:
        #         first += 1
        #     else:
        #         last -= 1
    
    return found


# 3. hash查找
# 时间复杂度：O(1)

class HashTable(object):
    def __init__(self, size=11):
        self._size = size
        self.slots = [None] * self._size    # key
        self.data = [None] * self._size     # value
    
    def _hash(self, key):
        return key % self._size
    
    def _rehash(self, old_hash):
        """出现冲突时，使用加1线性探测"""
        return (old_hash + 1) % self._size

    def put(self, key, value):
        """
        将键值对插入hash列表。
        如果key对应的值hash列表位置上已有数据项，则使用加1线性探测重新计算hash值，
        直到出现空槽，然后插入key和value。
        如果对应的key上已经有value，则将旧数据项替换成新数据项
        """
        hash_key = self._hash(key)

        if self.slots[hash_key] == None:
            self.slots[hash_key] = key
            self.data[hash_key] = value
        else:
            if self.slots[hash_key] == key:
                self.data[hash_key] = value     # update
            else:
                next_slot = self._rehash(hash_key+1)
                while self.slots[next_slot] != None and \
                        self.slots[next_slot] != key:
                        next_slot = self._rehash(next_slot)
                
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = value
                else:
                    self.data[next_slot] = value  # update
    
    def get(self, key):
        """
        搜索hash表
        """
        start_slot = self._hash(key)

        found = False
        pos = start_slot
        stop = False
        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self._rehash(pos)
                if pos == start_slot:
                    stop = True
        return data
    

    def __getitem__(self, idx):
        return self.get(idx)
    
    def __setitem__(self, key, value):
        self.put(key, value)


if __name__ == '__main__':
    H = HashTable()
    H[54] = 'cat'
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print("Slots : %s\n Data : %s" % (H.slots, H.data))
    print("H[20] = %s" % H[20])
    H[20] = "duck"
    print("H[20] = %s" % H[20])
    print("Data : ", H.data)