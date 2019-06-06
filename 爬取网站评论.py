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
#总共要人为控制三个变量：1.网站地址2.搜索结果页数3.课程总数量
service_args=[]
service_args.append('--load-images=no')  ##关闭图片加载
service_args.append('--disk-cache=yes')  ##开启缓存
service_args.append('--ignore-ssl-errors=true') ##忽略https错误
chrome=webdriver.PhantomJS(executable_path="D:\python\PhantomJS\phantomjs.exe")
chrome.get("http://www.icourse163.org/search.htm?search=%E9%80%9A%E4%BF%A1#/")
time.sleep(3)
code=pq(chrome.page_source)
#print(code)
class1 = code('.u-course-name.f-thide').text()
#print(class1)
x=0 #页数
element = chrome.find_element_by_xpath("//li[@class='ux-pager_btn ux-pager_btn__next']")#翻页功能
#print(content)
urlList=[]
url = []
with open('D:\毕业设计\database\mooc_url.txt', 'a', encoding='utf-8') as f:
     while x < 12:
      time.sleep(5)#延时不够的话会加载之前的数据
      cont3 = pq(chrome.page_source)
      content=cont3("#j-courseCardListBox a")
      #print(content)
      for i in content:
            temp = "http:" +str(code(i).attr("href"))
            if temp.__contains__("www") and not temp.__contains__("https") and not temp.__contains__("topics"):
                #print(temp)
                urlList.append(temp + " ")
         
      for i in urlList:
          if not i in url:
              url.append(i)# 去除重复的url地址
      #print(url)
      #print(urlList)
      x +=1
      element.click()#翻页
      ActionChains(chrome).move_to_element(element).click(element).perform()
     for i in url:
         f.write(i)
     print("url爬取完成")
     print(len(url))#总的课程数
chrome.quit()
#print(url)
with open('D:\毕业设计\database\pinglun_modle.txt','a',encoding='utf-8')as f:
 number = int(len(url))
 j = 0
 while j < number:#总的课程数
  driver=webdriver.PhantomJS(executable_path="D:\python\PhantomJS\phantomJs.exe")
  print(url[j])
  driver.get(url[j])
  j += 1
  time.sleep(5)
  cont1=pq(driver.page_source)             #获得初始页面代码，接下来进行简单的解析
  #print(cont1)
  ele=driver.find_element_by_id("review-tag-button")  #模仿浏览器就行点击查看课程评价的功能
  ele.click()                      #上边的id，下边的classname都可以在源码中看到
  time.sleep(10)
  cont2=pq(driver.page_source) 
  #print(cont2)
  print(cont2(".ux-mooc-comment-course-comment_head_rating-action_tips").text())
  b = cont2(".ux-mooc-comment-course-comment_head_rating-action_tips").text()
  if b:#不为空
       people = re.findall("\d+\.?\d",b)
       people = list(map(int, people))
       #print (people[0])#总的评论人数
       a = cont2(".ux-pager_itm").text()
       if people[0] <= 20:
                 a = [1]#只有一页时
                 time.sleep(5)
                 cont3 = pq(driver.page_source)
                 content=cont3(".ux-mooc-comment-course-comment_comment-list_item_body_content").text()
                 #print(content)
                 for i in content :
                                 f.write(i)
       else:
                 a = max(a) #最大页数，存在复数页时
                 int(a)
                 #print(a)
                 element = driver.find_element_by_xpath("//li[@class='ux-pager_btn ux-pager_btn__next']")#翻页功能
#print(content)
#print(connt)
#content=cont2(".ux-mooc-comment-course-comment_comment-list_item_body").text()#包含全部评论项目的总表标签
#content=cont2(".ux-mooc-comment-course-comment_comment-list_item_body_content").text()
#print(content)
                 x=0 #页数
#element.click()#翻页
                 while x < int(a):
                           sleeptime=random.randint(5, 10)
                           time.sleep(5)
                           cont3 = pq(driver.page_source)
                           content=cont3(".ux-mooc-comment-course-comment_comment-list_item_body_content").text()
                           #8print(content)
                           element.click()#翻页
                           ActionChains(driver).move_to_element(element).click(element).perform()
                           x = x+1
                           for i in content :
                                 f.write(i)
  else:print("没有人评论")
  time.sleep(5)
  driver.quit()


         
