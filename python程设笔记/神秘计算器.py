#神秘计算器.py
numbers=[]
def getnumber():
    t=input('请输入数字(回车结束）：')
    while t!='':
        numbers.append(eval(t))
        t=input('请输入数字(回车结束）：')
    return numbers
def plus():
    a=0
    for i in numbers:
        a+=i
    return a 
def avg():
    avg=plus()/len(numbers)
    return avg
def med():
    numbers.sort()
    if len(numbers)%2==0:
        med=(numbers[len(numbers)//2-1]+numbers[(len(numbers)//2)])/2
    else:
        med=numbers[(len(numbers)//2)]
    return med
getnumber()
plus()
avg()
med()
print('运算的结果为:求和:{},平均数:{},中位数:{}'.format(plus(),avg(),med()))
input=('按任意键退出')
