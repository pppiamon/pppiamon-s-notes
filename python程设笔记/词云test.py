#歌曲词云.py
import wordcloud
import jieba
def f(t):
    cut=jieba.lcut(t)
    m=[]
    for i in cut:
        if len(i)==1:
            continue
        elif i==' ':
            continue
        elif i in ('[];.,/!@#$%^&*()'):
            continue
        else:
            m.append(i)
    return m
t=input('请输入歌词文件以及路径（示例:C:\\Users\\Username\\Downloads\\lyrics.txt）:')
colour=input('请输入你喜欢的背景颜色(请使用常见颜色，英语输入):')
lyrics=open(t,'r',encoding='utf-8')
resource=f(lyrics.read())
lyrics.close()
w=wordcloud.WordCloud(height=1000,width=1000,\
                      font_path='msyh.ttc',background_color=colour)
w.generate(' '.join(resource))
w.to_file('歌曲词云.png')