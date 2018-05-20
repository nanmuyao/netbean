# # -*- coding: utf-8 -*-
#
# from selenium import webdriver
# # from scrapy.selector import Selector
# import time
#
# # 设置chromedriver不加载图片
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.add_argument("--headless")
# browser = webdriver.Chrome(executable_path="E:\pythonDoc\chromedriver.exe", chrome_options=chrome_options)
#
# # browser = webdriver.Chrome(executable_path="E:\pythonDoc\chromedriver.exe")
#
# browser.get("https://music.163.com/song?id=449818741")
#
# time.sleep(3)
# # 切换到contentFrame
# browser.switch_to.frame("contentFrame")
# fo = open("comments.txt", "w+", encoding='utf-8')
#
# commentCount = 0
#
# def getPageData():
#     global commentCount
#     #解析每一条数据
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
#             commentCount+=1
#         except:
#             print("出错了怎么回事")
#
# # 下一页按钮
# def getNextPageData():
#     # browser.switch_to.frame("contentFrame")
#     browser.find_element_by_class_name('znxt').click()
#     # print(browser.find_element_by_id('comment-box').text)
#
# #先拿10页的数据
# getPageData()
# time.sleep(1)
# for index in range(2500):
#     print("当前抓取的页数"+ str(index + 2) + "页")
#     getNextPageData()
#     time.sleep(1)
#     getPageData()
#
# fo.close()
# print("一共抓取到了" + str(commentCount) + "条数据")
# #全部数据处理 时间 姓名 评论
# # def getAddPageData():
# #     nameList = browser.find_element_by_id('comment-box').find_elements_by_css_selector('.m-cmmt .cmmts .itm .cntwrap')
# #     for name in nameList:
# #        print (name.text)
# #
# # getAddPageData()
# # time.sleep(1)
# # for index in range(1000):
# #     print("====================================================================================当前抓取的页数"+ str(index + 2) + "页")
# #     browser.find_element_by_class_name('znxt').click()
# #     time.sleep(0.2)
# #     getAddPageData()
#
# browser.quit()
