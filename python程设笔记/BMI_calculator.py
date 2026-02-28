#BMI_calculator.py
weight=eval(input('请输入您的体重(kg):'))
height=eval(input('请输入您的身高(m):'))
try:
    BMI=weight/pow(height,2)
except NameError:
    print('身高/体重输入错误，请输入数字')
else:
    if BMI>100:
        print('byd是不是把体重输错了')
    elif BMI<10:
        print('byd又把身高输错了')
    elif BMI<18.5:
        print('您的BMI偏瘦')
    elif BMI<=24:
        print('您的BMI正常')
    elif BMI<=28:
        print('您的BMI超重')
    else:
        print('您的BMI肥胖')
print('您的BMI指数为{:.1f}'.format(BMI))