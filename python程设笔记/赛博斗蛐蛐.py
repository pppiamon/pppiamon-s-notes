#模拟比赛.py
print('这是一个模拟体育竞技的程序，规则为2n-1局n胜，在每一局中得到15分者获胜，你可以输入能力值和场次模拟比赛')
print('得分条件:当前发球局下获胜')
print('发球权归属胜者')
a_win=0
b_win=0
import random
def getinput():
    s_a=eval(input('请输入a的能力值：'))
    s_b=eval(input('请输入b的能力值：'))
    n=eval(input('请输入你需要模拟的场次数量(奇数次）：'))
    if n%2==0:
       print('输入错误')
    return s_a,s_b,n
def cal(s_a,s_b):
       a=s_a/(s_a+s_b)
       b=s_b/(s_a+s_b)
       return a,b
def simulate(a,b):
    global a_win
    global b_win
    score=0
    sa=0
    sb=0
    t=1
    while score<15:
          if t==1:
             if random.random()<a:
                sa+=1
                score=max(sa,sb)
             else:
                 score=max(sa,sb)
                 t=0
          elif t==0:
              if random.random()<b: 
                 sb+=1
                 score=max(sa,sb)
              else:
                  score=max(sa,sb)
                  t=1
    if sa==15:
        a_win+=1
    else:
        b_win+=1
def gamesimulator():
    s_a,s_b,n=getinput() 
    a,b=cal(s_a,s_b)
    for i in range(n):
        simulate(a,b) 
        if a_win==(n//2)+1 or b_win==(n//2)+1:
            break
def main():
    gamesimulator()
    print('a获胜的场次为{},b获胜的场次为{}'.format(a_win,b_win))
    if a_win>b_win:
        print('a胜')
    else:
        print('b胜')
    input('程序执行完毕后按任意键退出')
main()
a_win=0
b_win=0   