# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 19:38:45 2026

@author: Charles0507
"""

#PythonDraw.py
import turtle  # 导入海龟绘图库
turtle.setup(650, 350, 200, 200)  # 设置画布大小（宽650，高350）和窗口位置（距离屏幕左/上200像素）
turtle.penup()  # 抬起画笔（移动时不画线）
turtle.fd(-250)  # 向后移动250像素（fd是forward，负数表示反向）
turtle.pendown()  # 落下画笔（移动时开始画线）
turtle.pensize(25)  # 设置画笔粗细为25像素
turtle.pencolor("purple")  # 设置画笔颜色为紫色
turtle.seth(-40)  # 设置海龟初始朝向为-40度（即向右下方倾斜）

# 核心花瓣绘制：循环4次，每次画两个圆弧组成一个花瓣
for i in range(4):
    turtle.circle(40, 80)  # 以当前左侧40像素为圆心，绘制80度的右向圆弧
    turtle.circle(-40, 80)  # 以当前右侧40像素为圆心，绘制80度的左向圆弧

# 花柄和收尾部分
turtle.circle(40, 80/2)  # 绘制40度的右向圆弧，完成最后半个花瓣
turtle.fd(40)  # 向前移动40像素，延伸花柄
turtle.circle(16, 180)  # 绘制16像素半径的半圆，形成花柄的弧度
turtle.fd(40 * 2/3)  # 向前移动约26.7像素，完成花柄收尾
turtle.done()  # 保持绘图窗口，防止自动关闭