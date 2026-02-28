#生日悖论.py
year=int(input('请输入年份:'))
number=int(input('请输入人数:'))
i=0
poss=1
if year%4==0 and year%400!=0:
    datetotal=366
else:
    datetotal=365
while i<number:
    poss=poss*(datetotal-i)/datetotal
    i=i+1
print('至少有两个人生日日期相同的概率为:{:.2f}'.format(poss))