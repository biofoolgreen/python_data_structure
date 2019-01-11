'''
@Description: 排序
@Version: 
@Author: biofool2@gmail.com
@Date: 2019-01-11 10:42:18
@LastEditTime: 2019-01-11 18:50:20
@LastEditors: Please set LastEditors
'''


# 冒泡排序
# 时间复杂度：O(n^2)
def bubble_sort(arr):
    for arrlen in range(len(arr)-1, 0, -1):
        for idx in range(arrlen):
            if arr[idx] > arr[idx+1]:
                # tmp = arr[idx]
                # arr[idx] = arr[idx+1]
                # arr[idx+1] = tmp
                # 原地交换，原始列表改变
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
        print("Round %s : arr = %s" % (len(arr)-arrlen, arr))
    # 可以不用return， 因为arr已经改变了
    return arr


if __name__ == "__main__":
    arr = [54,26,93,17,77,31,44,55,20]
    bubble_arr = bubble_sort(arr)
    # print(bubble_arr, arr) 