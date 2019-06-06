from nltk import *
import jieba
import collections
import matplotlib.pyplot as plt
with open ('D:/毕业设计/database/20190413中国大学/pinglun_modle.txt','r',encoding = 'utf-8') as f :
    cuted = []
    fenxi = f.read()
    #print(fenxi)
    words = jieba.lcut(fenxi)
    frequency = collections.Counter(words)
    for key in frequency:
        if len(key)<2:
            cuted.append(key)
    for key in cuted:
        del frequency[key]
    delet = ["学生","有点","老师","讲课","感觉","这门","非常","课程","学习","内容","比较","没有","自己","觉得","这个","那个","可以","讲得","希望","了解","东西","就是","还是","特别","真的","一些","一个","但是","课程内容","授课","很大"]
    for key in delet:
        del frequency[key]
    tops = frequency.most_common(100)
        
    
   
            
    
    
    
    

    
    
    
           
