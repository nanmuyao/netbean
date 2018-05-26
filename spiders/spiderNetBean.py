# # -*- coding: utf-8 -*-
#
# from selenium import webdriver
# # from scrapy.selector import Selector
# import time
#
# print("startTime", time.time())
# # 设置chromedriver不加载图片
# chrome_options = webdriver.ChromeOptions()
# #设置游览器不加载图片，节省网络流量提高速度
# prefs = {"profile.managed_default_content_settings.spiderData": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# #新版本chrome支持无界面游览了
# chrome_options.add_argument("--headless")
# browser = webdriver.Chrome(executable_path="E:\pythonDoc\chromedriver.exe", chrome_options=chrome_options)
#
# # 光年之外
# browser.get("https://music.163.com/song?id=449818741")
# time.sleep(3)
# #原本的page_source中没有评论用到的数据切换到contentFrame
# browser.switch_to.frame("contentFrame")
# fo = open("comments.txt", "w+", encoding='utf-8')
#
# commentCount = 0
# def getPageData():
#     global commentCount
#     # 解析每一条数据
#     nameList = browser.find_element_by_id('comment-box').find_elements_by_css_selector(".f-brk")
#     for content in nameList:
#         try:
#             nameContent = content.find_element_by_css_selector('a')
#             name = nameContent.text
#             # print(name)
#             contents = content.text
#             comment = contents[len(name) + 1:len(contents)] + '\n'
#             fo.write(comment)
#             fo.flush()
#             commentCount += 1
#         except:
#             print("出错了怎么回事")
#
#
# #点击下一页按钮
# def getNextPageData():
#     browser.find_element_by_class_name('znxt').click()
#
#
# # 先拿10页的数据
# getPageData()
# time.sleep(1)
# for index in range(2500):
#     print("当前抓取的页数" + str(index + 1) + "页")
#     getNextPageData()
#     time.sleep(0.7)
#     getPageData()
#
# print("endTime", time.time())
# fo.close()
# print("一共抓取到了" + str(commentCount) + "条数据")
#
# browser.quit()
