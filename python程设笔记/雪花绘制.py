import turtle
turtle.pensize(2)
turtle.speed(10)
turtle.pencolor('pink')
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main(level):
    turtle.pu()
    turtle.goto(-300,200)
    turtle.pd()   
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
level=int(input('请输入雪花阶数:'))
main(level)
turtle.hideturtle()
turtle.done()
