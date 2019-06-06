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
#总共要人为控制三个变量：1.网站地址2.搜索结果页数
service_args=[]
service_args.append('--load-images=no')  ##关闭图片加载
service_args.append('--disk-cache=yes')  ##开启缓存
service_args.append('--ignore-ssl-errors=true') ##忽略https错误
with open('D:\毕业设计\database\爬取url&学校名&评论数&课程名.txt', 'a', encoding='utf-8') as f:
    chrome=webdriver.PhantomJS(executable_path="D:\python\PhantomJS\phantomjs.exe")
    chrome.get("http://www.icourse163.org/category/computer")
    time.sleep(5)
    code=pq(chrome.page_source)
#print(code)
    class1 = code('.u-course-name.f-thide').text()
#print(class1)
    x=0 #页数
    element = chrome.find_element_by_xpath("//li[@class='ux-pager_btn ux-pager_btn__next']")#翻页功能
#print(content)
    urlList=[]
    url = []
    course_name = []
    university_name = []
    pinglun_number = []
    while x < 15:
      time.sleep(10)#延时不够的话会加载之前的数据
      cont3 = pq(chrome.page_source)
      content=cont3("#j-courseCardListBox a")#爬取url
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
      #print(course)
      #course_name.append(course)
      university = cont3(".t21").text()
      university_name += university.split()
      #print(university)
      #university_name.append(university)
      x +=1
      element.click()#翻页
    #print(course_name)
    #print(university_name)
    print("url爬取完成")
    print(len(url))#总的课程数
    number = int(len(url))
    j = 0
    while j < number:#总的课程数
            driver=webdriver.PhantomJS(executable_path="D:\python\PhantomJS\phantomJs.exe")
            print(url[j])
            driver.get(url[j])
            time.sleep(5)
            cont1=pq(driver.page_source)             #获得初始页面代码，接下来进行简单的解析
  #print(cont1)
            course = cont3(".course-title-wrapper").text()
            course_name.append(course)
            ele=driver.find_element_by_id("review-tag-button")  #模仿浏览器就行点击查看课程评价的功能
            ele.click()                      #上边的id，下边的classname都可以在源码中看到
            time.sleep(10)
            cont2=pq(driver.page_source) 
  #print(cont2)
            print(cont2(".ux-mooc-comment-course-comment_head_rating-action_tips").text())
            pinglun = cont2(".ux-mooc-comment-course-comment_head_rating-action_tips").text()
            pinglun = re.findall(r"\d+\.?\d*",pinglun)
            pinglun_number.append(pinglun[0])
            driver.quit()
            f.write(university_name[j]+"  "+course_name[j]+"  "+pinglun_number[j]+"  "+url[j]+"\n")
            print(j)
            j +=1

with open('D:\毕业设计\database\课程url.txt', 'a', encoding='utf-8') as f:
    for i in url:
        f.write(i+"\n")
chrome.quit()

  


         
