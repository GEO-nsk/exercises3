
from turtle import *
from math import *


screen = Screen()
screen.setup(width=1.0, height=1.0)


speed(0)

def draw_triangle(a, b, c, angle, border_color, fill_color):

    pd()
    rt(angle)
    begin_fill()
    color(border_color, fill_color)
    fd(a)
    lt(90)
    fd(b)
    lt(135)
    fd(c)
    end_fill()
    lt(135)
    pu()
    goto(0,0)

def draw_square_1(x,y):

    goto(x,y)
    draw_triangle(50, 50, sqrt(50), 270, 'white', 'Medium blue')
    lt(270)

    goto(x - 50, y + 50)
    draw_triangle(50, 50, sqrt(50), 90, 'white', 'deepskyblue')
    lt(90)

def draw_square_2(x,y):

    goto(x,y)
    draw_triangle(50, 50, sqrt(50), 270, 'white', 'deepskyblue')
    lt(270)

    goto(x - 50, y + 50)
    draw_triangle(50, 50, sqrt(50), 90, 'white', 'Medium blue')
    lt(90)

def draw_square_3(x,y):

    goto(x,y)
    draw_triangle(50, 50, sqrt(50), 270, 'white', 'lightskyblue')
    lt(270)

    goto(x - 50, y + 50)
    draw_triangle(50, 50, sqrt(50), 90, 'white', 'deepskyblue')
    lt(90)

def draw_square_4(x,y):

    goto(x,y)
    draw_triangle(50, 50, sqrt(50), 270, 'white', 'deepskyblue')
    lt(270)

    goto(x - 50, y + 50)
    draw_triangle(50, 50, sqrt(50), 90, 'white', 'lightskyblue')
    lt(90)

def draw_square_5(x,y):

    goto(x - 50,y)
    draw_triangle(50, 50, sqrt(50), 0, 'white', 'deepskyblue')
    lt(0)

    goto(x, y + 50)
    draw_triangle(50, 50, sqrt(50), 180, 'white', 'lightskyblue')
    lt(180)

def draw_square_6(x,y):

    goto(x - 50,y)
    draw_triangle(50, 50, sqrt(50), 0, 'white', 'Medium blue')
    lt(0)

    goto(x, y + 50)
    draw_triangle(50, 50, sqrt(50), 180, 'white', 'deepskyblue')
    lt(180)

def draw_square_7(x,y):

    goto(x - 50,y)
    draw_triangle(50, 50, sqrt(50), 0, 'white', 'deepskyblue')
    lt(0)

    goto(x, y + 50)
    draw_triangle(50, 50, sqrt(50), 180, 'white', 'Medium blue')
    lt(180)

def draw_square_8(x,y):

    goto(x - 50,y)
    draw_triangle(50, 50, sqrt(50), 0, 'white', 'lightskyblue')
    lt(0)

    goto(x, y + 50)
    draw_triangle(50, 50, sqrt(50), 180, 'white', 'deepskyblue')
    lt(180)

goto(0, 0)
pu()


draw_square_1(0,0)
draw_square_2(50,0)
draw_square_3(100,0)
draw_square_4(0,-50)
draw_square_1(50,-50)
draw_square_2(100,-50)
draw_square_3(0,-100)
draw_square_4(50,-100)
draw_square_1(100,-100)

draw_square_2(150,-150)
draw_square_3(200,-150)
draw_square_4(250,-150)
draw_square_1(150,-200)
draw_square_2(200,-200)
draw_square_3(250,-200)
draw_square_4(150,-250)
draw_square_1(200,-250)
draw_square_2(250,-250)

draw_square_5(150,0)
draw_square_6(200,0)
draw_square_7(250,0)
draw_square_6(150,-50)
draw_square_7(200,-50)
draw_square_8(250,-50)
draw_square_7(150,-100)
draw_square_8(200,-100)
draw_square_5(250,-100)

draw_square_8(0,-150)
draw_square_5(50,-150)
draw_square_6(100,-150)
draw_square_5(0,-200)
draw_square_6(50,-200)
draw_square_7(100,-200)
draw_square_6(0,-250)
draw_square_7(50,-250)
draw_square_8(100,-250)

done()