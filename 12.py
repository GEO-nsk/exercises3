
from turtle import *
from math import *


screen = Screen()
screen.setup(width=1.0, height=1.0)


speed(0)

def draw_rectangle(width, length, angle, border_color, fill_color):

    pd()
    begin_fill()
    color(border_color, fill_color)
    rt(angle)
    fd(width)
    rt(90)
    fd(length)
    rt(90)
    fd(width)
    rt(90)
    fd(length)
    end_fill()
    rt(90)
    pu()
    goto(0,0)

def draw_circle(radius, border_color, fill_color):

    pd()
    begin_fill()
    color(border_color, fill_color)
    circle(radius)
    end_fill()
    pu()
    goto(0,0)

def draw_triangle(a, b, c, angle, border_color, fill_color):

    pd()
    rt(angle)
    begin_fill()
    color(border_color, fill_color)
    fd(a)
    lt(120)
    fd(b)
    lt(120)
    fd(c)
    end_fill()
    lt(120)
    pu()
    goto(0,0)


goto(0, 0)
pu()


def draw_figure(x,y):

    goto(x,y)
    draw_rectangle(25,100,45,'black','blue')
    lt(45)

    goto(x - 140,y)
    draw_rectangle(25,100,225,'black','blue')
    lt(225)

    goto(x - 70,y - 70)
    draw_rectangle(25,100,135,'black','blue')
    lt(135)

    goto(x - 70,y + 70)
    draw_rectangle(25,100,315,'black','blue')
    lt(315)

    goto(x - 70,y - 30)
    draw_circle(30,'black','red')

    goto(x + 42 , y + 100)
    draw_triangle(50,50,50,180,'black','red')
    lt(180)

    goto(x - 8, y - 100)
    draw_triangle(50, 50, 50, 0, 'black', 'red')

draw_figure(-350,0)
draw_figure(-175,0)
draw_figure(0,0)
draw_figure(175,0)
draw_figure(350,0)



done()