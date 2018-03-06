# -*-coding:utf-8-*-
from docx import Document   # for reading docx
import glob # for file location
import jieba # for splitting
#import os #cwd = os.getcwd()
# import operator # for sort
import matplotlib.pyplot as plt # for plot
from matplotlib import font_manager # for font
import numpy as np
import random




# calculate number of documents contain a word
def idf_like(word, text_list):
    number = 0
    for item in text_list:
        if item.count(word):
            number += 1
    return number









# extract texts from docx files
count = 0;
text_file_list = []
# obtain all files that end with ".docx"
for filepath in glob.iglob("/Users/tongli/OneDrive/teaching/course/SE/2017-2018/作业/*/*/*/*.docx"): # generator, search immediate subdirectories
    count+=1
    document = Document(filepath)
    text = ''
    for p in document.paragraphs:
        text += p.text

    text_file_list.append(text)


print("number of input files: " + str(len(text_file_list)))


# merge all texts
all_texts = ''
for text in text_file_list:
    all_texts+=text


# segment sentences
seg_list = jieba.cut(all_texts, cut_all=False, HMM=True)
# print("Default Mode: " + "/ ".join(seg_list))  # 默认模式


# count occurrence of words
seg_dict = {}
for seg in seg_list:
    seg_dict[seg] = seg_dict.get(seg,0) + 1


# consider the following words
useful_words_0 = ['学习','界面设计','框架','编程','编码',"软件开发",'资料','用户','选择','总结','存储','bug','比较','调试','图形界面',
                '版本','讨论','界面','编写','系统','流程图','测试','数据','数据结构','代码','分析','模块','算法','程序','软件','需求',
                '开发','实现','设计','功能']

useful_words_1 = ['学习','界面设计','框架','编程','编码',"软件开发",'资料','用户','选择','总结','存储','bug','比较','调试','图形界面',
                '版本']

useful_words_2 = ['讨论','界面','编写','系统','流程图','测试','数据','数据结构','代码','分析','模块','算法','程序','软件','需求',
                '开发','实现','设计','功能']

useful_words = useful_words_1


# sort the list
# sorted_seg_list = sorted(seg_dict.items(), key=operator.itemgetter(1))


# idf_like_dict ={}
# for word in useful_words:
#     idf_like_dict[word] = idf_like(word, text_file_list)
# print(idf_like_dict)


# data preparation for making charts
color = ['red','deepskyblue','cyan','palegreen', 'orange']
color_list =[]
word_list= []
occurrence_list = []
idf_like_list = []
for word in useful_words:
    word_list.append(word)
    occurrence_list.append(seg_dict[word])
    idf_like_list.append(idf_like(word, text_file_list))
    color_list.append(color[(random.randint(1,5)-1)])
np_occurrence_list = np.array(occurrence_list)
np_occurrence_list = np_occurrence_list*8


# plot
# plt.scatter(occurrence_list, idf_like_list, s =np_occurrence_list, c=color_list)
# # Strings
xlab = '总出现次数'
ylab = '相关作业数'
title = '第一次作业关键词分析'
# deal with font
fontP = font_manager.FontProperties()
fontP.set_size(14)
# Add axis labels
# plt.xlabel(xlab, fontproperties=fontP)
# plt.ylabel(ylab, fontproperties=fontP)
# # Add title
# plt.title(title, fontproperties=fontP)



fig, ax = plt.subplots()
ax.scatter(occurrence_list, idf_like_list,s =np_occurrence_list, c=color_list, alpha = 0.5)
for i, txt in enumerate(useful_words):
    ax.annotate(txt, (occurrence_list[i]-0.5, idf_like_list[i]))
# Add axis labels
ax.set_xlabel(xlab, fontproperties=fontP)
ax.set_ylabel(ylab, fontproperties=fontP)
# Add title
ax.set_title(title, fontproperties=fontP)


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()