'''
@Description: 递归-迷宫游戏
@Version: 
@Author: biofool2@gmail.com
@Date: 2019-01-04 10:44:42
@LastEditTime: 2019-01-07 14:56:20
@LastEditors: Please set LastEditors
'''
import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


class Maze(object):
    def __init__(self, maze_file):
        self.maze_list, self.rows, self.cols = self.__load_file(maze_file)

        self.tur = turtle.Turtle(shape='turtle')
        self._x = -self.cols / 2
        self._y = self.rows / 2
        self.win = turtle.Screen()
        self.win.setworldcoordinates(-(self.cols - 1) / 2 - 0.5, -(self.rows - 1) / 2 - 0.5,
                                    (self.cols - 1) / 2 + 0.5, (self.rows - 1) / 2 + 0.5
                                    )
    

    def __load_file(self, maze_file):
        """
        读取迷宫的数据文件，并找到乌龟的起始位置。
        通过使用 + 字符表示墙壁， 空格表示空心方块， 并使用字母 S 表示起始位置
        """
        rows, cols = 0, 0
        maze_list = []
        with open(maze_file, 'r') as f:
            for line in f:
                row_list = []
                col = 0
                line = line[:-1]    # 去掉换行符

                for ch in line:
                    row_list.append(ch)
                    if ch == "S":
                        self.start_row = rows
                        self.start_col = col
                    col += 1
                
                rows += 1
                maze_list.append(row_list)
                cols = len(row_list)
        return maze_list, rows, cols


    def draw_maze(self):
        """
        在屏幕上的一个窗口中绘制迷宫
        """
        self.tur.speed(10)
        self.win.tracer(0)  # 设置每隔多少帧（如果有第二个参数-延迟多少秒）更新一次图像，
        for y in range(self.rows):
            for x in range(self.cols):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_center_box(x+self._x, -y+self._y, 'orange')
        self.tur.color("black")
        self.tur.fillcolor("blue")
        self.win.update()
        self.win.tracer(1)
    

    def draw_center_box(self, x, y, color):
        """
        画迷宫的墙（方块）
        """
        self.tur.up()
        self.tur.goto(x-0.5, y-0.5)
        self.tur.color(color)
        self.tur.fillcolor(color)
        self.tur.setheading(90)     # 设置海龟前进方向为90（北）
        self.tur.down()
        self.tur.begin_fill()
        for i in range(4):
            self.tur.forward(1)
            self.tur.right(90)
        self.tur.end_fill()
    
    def move(self, x, y):
        """
        移动乌龟
        """
        self.tur.up()
        # tur.towards(x, y)返回tur当前位置与坐标(x, y)到原点的两条之间之间的夹角
        # 依赖于tur开始的方向
        self.tur.setheading(self.tur.towards(x+self._x, -y+self._y))
        self.tur.goto(x+self._x, -y+self._y)
    
    def drop_bread_crumb(self, color):
        """
        丢面包屑。记录走过的位置
        """
        # 画一个直径为10， 颜色为color的圆点
        self.tur.dot(10, color)
    
    def update_position(self, row, col, val=None):
        """
        更新迷宫的内部表示， 并更改窗口中乌龟的位置
        """
        if val:
            self.maze_list[row][col] = val
        self.move(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None
        
        if color:
            self.drop_bread_crumb(color)
    
    def is_exit(self, row, col):
        """
        检查当前位置是否是迷宫的退出位置
        """
        return (row == 0 or row == self.rows-1 or col == 0 or col == self.cols-1)
    
    def __getitem__(self, idx):
        """
        重载[]方法
        """
        return self.maze_list[idx]


def search_from(maze, start_row, start_col):
    """
    从起始坐标（start_row, start_col）尝试4个方向的路径，直到找到路径走出迷宫。
    考虑以下4种情况：
    1. 乌龟撞到了墙。 由于这一格被墙壁占据， 不能进行进一步的探索。
    2. 乌龟找到一个已经探索过的格。 我们不想继续从这个位置探索， 否则会陷入循环。
    3. 我们发现了一个外边缘， 没有被墙壁占据。 换句话说， 我们发现了迷宫的一个出口。
    4. 我们探索了一格在四个方向上都没有成功
    """
    maze.update_position(start_row, start_col)
    # 1.撞到墙，停止
    if maze[start_row][start_col] == OBSTACLE:
        return False
    # 2.找到个已经探索过的格子，停止
    if maze[start_row][start_col] == TRIED:
        return False
    # 3.找到出口
    if maze.is_exit(start_row, start_col):
        maze.update_position(start_row, start_col, PART_OF_PATH)
        return True
    # 更新走过的格子为Tried
    maze.update_position(start_row, start_col, TRIED)

    # 4.否则，不断从4个方向尝试(北南西东)
    found = search_from(maze, start_row-1, start_col) or \
            search_from(maze, start_row+1, start_col) or \
            search_from(maze, start_row, start_col-1) or \
            search_from(maze, start_row, start_col+1)
    
    if found:
        maze.update_position(start_row, start_col, PART_OF_PATH)
    else:
        # 死胡同，退出
        maze.update_position(start_row, start_col, DEAD_END)
    return found


if __name__ == "__main__":
    maze_file = r"D:\GitHub\data_structure\recursion\maze.txt"
    my_maze = Maze(maze_file)
    my_maze.draw_maze()
    my_maze.update_position(my_maze.start_row, my_maze.start_col)
    search_from(my_maze, my_maze.start_row, my_maze.start_col)