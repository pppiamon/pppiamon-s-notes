#当前时间七段数码管的的绘制.py
from turtle import *
from time import *
pu()
goto(-300,0)
speed(10)                                                        
pencolor('black')
pensize(5)
def drawgap():
    pu()
    fd(5)
def drawer(draw):                 #控制绘图函数 
        drawgap()
        penup()if draw else pendown()
        fd(40)
        right(90)
def judge(digit):              #根据digit给draw赋值（BOOL形式),并执行数字绘制程序
    drawer(True) if digit in [0,1,7] else drawer(False)
    drawer(True) if digit in [2] else drawer(False)
    drawer(True) if digit in [1,4,7] else drawer(False)
    drawer(True) if digit in [1,3,4,5,7,9] else drawer(False)
    left(90)
    drawer(True) if digit in [1,2,3,7] else drawer(False)
    drawer(True) if digit in [1,4] else drawer(False)
    drawer(True) if digit in [5,6] else drawer(False)
    pu()
    seth(0)
    fd(30)
def total(data):
    for i in data:
        if i=='-':
            pencolor('red')
            write('年')
            fd(20)
        elif i=='+':
            pencolor('purple')
            write('月')
            fd(20)
        elif i=='=':
            pencolor('green')
            write('日')
            fd(20)
        else:
            judge(int(i))
data=strftime('%Y-%m+%d=',gmtime())
total(data)
hideturtle()
