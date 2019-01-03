'''
@Description: 递归-汉诺塔游戏
@Version: 
@Author: biofool2@gmail.com
@Date: 2019-01-03 17:26:25
@LastEditTime: 2019-01-03 17:33:23
@LastEditors: Please set LastEditors
'''


def move_disk(fp, tp):
    print("Moving disk from %s to %s" % (fp, tp))

def move_tower(height, from_pole, to_pole, with_pole):
    """
    1. 使用目标杆（to_pole）将 height-1 的塔移动到中间杆(with_pole)。
    2. 将剩余的盘子移动到目标杆（to_pole）。
    3. 使用起始杆(from_pole)将 height-1 的塔从中间杆(with_pole)移动到目标杆(to_pole)
    """
    if height >= 1:
        # 将初始杆上的底部圆盘移动到中间
        move_tower(height-1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        # 将塔从中间杆移动到最大盘子的顶部
        move_tower(height-1, with_pole, to_pole, from_pole)


if __name__ == "__main__":
    move_tower(5, "a", "b", "c")