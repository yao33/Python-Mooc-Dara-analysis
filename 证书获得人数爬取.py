from selenium import webdriver
import time
from time import sleep
import os
import re
from pyquery import PyQuery as pq
from selenium.webdriver import ActionChains
import csv
import os
from lxml import etree
import re
import random

with open ('D:\毕业设计\database\课程url.txt','r',encoding='utf-8')as f:
    course_url = []
    course_test = f.read()
    course_url = course_test.split("\n")
    f.close()

shenfen = []
shichang = []
  #print(new_user)
student = 0.0
youxiao_shenfen = []
youxiao_shichang = []
wuxiao_shenfen = []
wuxiao_shichang = []
j = 0
length = len(course_url)-1
while j < length:#couse_url最后一个元素是空格
   print(j)
   chrome=webdriver.PhantomJS(executable_path="D:\python\PhantomJS\phantomJs.exe")
   chrome.get(course_url[j])
   time.sleep(5)
   cont1=pq(chrome.page_source)             #获得初始页面代码，接下来进行简单的解析
#print(cont1)
   course = cont1(".course-title-wrapper").text()
#print(course)
   ele=chrome.find_element_by_id("review-tag-button")  #模仿浏览器就行点击查看课程评价的功能
   ele.click()                      #上边的id，下边的classname都可以在源码中看到
   time.sleep(5)
   cont2 = pq(chrome.page_source) 
#print(cont2)  #爬取网页源代码
   print(cont2(".ux-mooc-comment-course-comment_head_rating-action_tips").text())
   people = cont2(".ux-mooc-comment-course-comment_head_rating-action_tips").text()
   if people:#如果存在评论则记录
             xueshi = cont2(".course-enroll-info_course-info_term-workload").text()
             people = re.findall("\d+\.?\d",people)
             people = list(map(int, people))
#print (people)#总的评论人数,循环的控制量
             user_url=[]
             new_user = []#用户个人url存储
#爬取用户个人的url
             a = cont2(".ux-pager_itm").text()
             a = max(a) #最大页数
             x = 0
             while x < int(a):#筛选用户个人的url
                      time.sleep(5)
                      cont2 = pq(chrome.page_source)
                      href = cont2("#comment-section a")
                      for i in href:
                                temp = "http:"+str(cont2(i).attr("href"))
                      if temp.__contains__("userId"):
                                 user_url.append(temp)
                      for user in user_url:
                             if user not in new_user:
                                   new_user.append(user) #去重并保持顺序不变
    #user_url.sort(key = user_url.index)
                      x += 1
                      if a !=1:
                           element = chrome.find_element_by_xpath("//li[@class='ux-pager_btn ux-pager_btn__next']")#翻页功能
                           element.click()
#print(new_user)用户url爬取结束
             chrome.quit()
             k = 0
             student = 0
             while k < people[0]:
                       url = new_user[k]
                       driver.get(url)
                       time.sleep(random.randint(5,10))
                       user_data = pq(driver.page_source)
#print(user_data)#网页源代码
                       shenfen.append(user_data(".u-ui-tag").text())
                       shichang.append(user_data(".u-ui-time-cont").text())
#进行对这一门课是否取得了证书的判断
                       zhengshu = driver.find_element_by_class_name("u-st-cert_a5")
                       zhengshu.click()
                       time.sleep(5)
                       zhengshu_data = pq(driver.page_source)
 #print(zhengshu_data)
 #print(shenfen,shichang)
                       panduan = zhengshu_data(".certCard-courseFunc-f").text()
 #print(panduan)
                       if course in panduan:
                                 student += 1#通过评论统计通过人数
         #如果获得了证书则记录其url
                       youxiao_shenfen.append(user_data(".u-ui-tag").text())
                       youxiao_shichang.append(user_data(".u-ui-time-cont").text())
         #print(user_data(".u-ui-tag").text(),user_data(".u-ui-time-cont").text())
                       driver.quit()
                       k += 1
 #print(x)
 #print(student)
             tongguo = (student/people[0])*100
#print(str(tongguo) +"%")
#print(shenfen)
#print(shichang)
             with open ('D:\毕业设计\database\无效学习时长.txt','a',encoding='utf-8')as f:
                           f.write(course)
                           f.write("\n")
                           for xuexi in shichang:
                                if not xuexi in youxiao_shichang:
                                            wuxiao_shichang.append(xuexi)
                           for i in wuxiao_shichang:
                                f.write(i+'\n')
             with open ('D:\毕业设计\database\无效学习身份.txt','a',encoding='utf-8')as f:
                           f.write(course)
                           f.write("\n")
                           for xuexiji in shenfen:
                                if not xuexiji in youxiao_shenfen:
                                         wuxiao_shenfen.append(xuexiji)
                           for namae in wuxiao_shenfen:
                                   f.write(namae+'\n')
             with open ('D:\毕业设计\database\有效学习身份.txt','a',encoding='utf-8')as f:
                           f.write(course)
                           f.write("\n")
                           for youxiao in youxiao_shenfen:
                                   f.write(youxiao+'\n')
             with open ('D:\毕业设计\database\有效学习时长.txt','a',encoding='utf-8')as f:
                           f.write(course)
                           f.write("\n")
                           for youxiao in youxiao_shichang:
                                   f.write(youxiao+'\n')
             with open ('D:\毕业设计\database\学习通过率.txt','a',encoding='utf-8')as f:
                           f.write(course+":  "+xueshi)
                           f.write('\n')
                           tongguo = str(tongguo)
                           f.write(tongguo+"%")
                           f.write('n')
   print("一次写入完毕")
   j += 1
print("写入完毕")

    
    
