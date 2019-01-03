'''
@Description: 递归-可视化递归过程
@Version: 
@Author: biofool2@gmail.com
@Date: 2019-01-03 17:27:31
@LastEditTime: 2019-01-03 17:28:59
@LastEditors: Please set LastEditors
'''

import turtle

def draw_spiral(tur, line_len):
    if line_len > 0:
        tur.forward(line_len)
        tur.right(90)
        draw_spiral(tur, line_len-5)

def draw_tree(tur, branch_len):
    if branch_len > 5:
        tur.forward(branch_len)
        tur.right(20)
        draw_tree(tur, branch_len-15)
        tur.left(40)
        draw_tree(tur, branch_len-15)
        tur.right(20)
        tur.backward(branch_len)

def draw_triangle(tur, points, color):
    tur.fillcolor(color)
    tur.up()
    tur.goto(points[0][0], points[0][1])
    tur.down()
    tur.begin_fill()
    tur.goto(points[1][0], points[1][1])
    tur.goto(points[2][0], points[2][1])
    tur.goto(points[0][0], points[0][1])
    tur.end_fill()

def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

def draw_sierpinski(tur, points, degree):
    colors = [
        'blue', 'red', 'green', 
        'yellow', 'violet', 'white', 'orange'
        ]
    draw_triangle(tur, points, colors[degree])
    if degree > 0:
        draw_sierpinski(tur, [points[0], 
                                get_mid(points[0], points[1]),
                                get_mid(points[0], points[2])],
                        degree-1)
        draw_sierpinski(tur, [points[1], 
                                get_mid(points[0], points[1]),
                                get_mid(points[1], points[2])],
                        degree-1)
        draw_sierpinski(tur, [points[2], 
                                get_mid(points[2], points[1]),
                                get_mid(points[0], points[2])],
                        degree-1)

if __name__ == "__main__":
    my_tur = turtle.Turtle()
    my_win = turtle.Screen()
    # my_tur.left(90)
    # my_tur.up()
    # my_tur.backward(150)
    # my_tur.down()
    # my_tur.color("green")
    # # draw_spiral(my_tur, 100)
    # draw_tree(my_tur, 120)
    points = [
        [-200, -100],
        [0, 200],
        [200, -100]
    ]
    draw_sierpinski(my_tur, points, 3)
    my_tur.fillcolor()
    my_win.exitonclick()