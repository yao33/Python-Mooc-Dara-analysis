from nltk import *
import jieba
import collections
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
#from wordcloud import WordCloud
stop_words = stopwords.words('english')
#print(stop_words)
with open ('D:/毕业设计/class central/pinglun1.txt','r',encoding = 'utf-8') as f :
    fenxi = f.read()
    #print(fenxi)
    cuted = []
    words = jieba.lcut(fenxi)
    frequency = collections.Counter(words)
    for key in frequency:
        if len(key)<2:
            cuted.append(key)
    for key in cuted:
        del frequency[key]
    for key in stop_words:
        del frequency[key]
    delete = ["MOOC","Andrew","course","NG","ML","get","The","This","class","It","really","much","one","lot","first","would"]
    for key in delete:
        del frequency[key]
    #print (frequency)
    tops = frequency.most_common(30)
    
#生成词云图，这里需要注意的是WordCloud默认不支持中文，所以这里需已下载好的中文字库
#无自定义背景图：需要指定生成词云图的像素大小，默认背景颜色为黑色,统一文字颜色：mode='RGBA'和colormap='pink'
    #wc = WordCloud(font_path=r"D:/毕业设计/class central/pinglun1.txt.ttf",background_color='white',width=800,height=600,max_font_size=50,max_words=1000)#,min_font_size=10)#,mode='RGBA',colormap='pink')
    #wc.generate(result)
    #wc.to_file(r"D:\Python\test\wordcloud\output\wordcloud.png") #按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰
 
# 显示图片
   # plt.figure("词云图") #指定所绘图名称
    #plt.imshow(wc)       # 以图片的形式显示词云
    #plt.axis("off")      #关闭图像坐标系
    #plt.show()

    
   
            
    
