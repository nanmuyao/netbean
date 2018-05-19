# _*_ coding:utf-8 _*_
__author__ = 'tars'
_date__ = '2018/5/19 22:45'


from wordcloud import WordCloud
import codecs
import jieba

f = codecs.open('comments.txt',encoding='utf-8').read()
f = ' '.join(jieba.cut(f))

font = r'C:\Windows\Fonts\simfang.ttf'

wordcloud = WordCloud(font_path=font, background_color="white",width=1000, height=860, margin=2).generate(f)

# width,height,margin可以设置图片属性

# generate 可以对全部文本进行自动分词,但是他对中文支持不好,对中文的分词处理请看我的下一篇文章
#wordcloud = WordCloud(font_path = r'D:\Fonts\simkai.ttf').generate(f)
# 你可以通过font_path参数来设置字体集

#background_color参数为设置背景颜色,默认颜色为黑色

import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file('netBeanMusic.png')
# 保存图片,但是在第三模块的例子中 图片大小将会按照 mask 保存


# file = open("comments.txt", encoding='utf-8')
#
# while 1:
#     line = file.readline()
#     if line:
#         print (line)
