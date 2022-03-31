#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu

sent_tokenize(line.replace(",", ".").replace(":", ".").replace(";", ".")) 将句子中的，：；替换成句号后分句
line = re.sub("\s\(.*?\)+", "", line)   正则表达：将括号中的补充文本去除 (非贪婪表达)
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import re



def sentence_token(doc):
	#docpath = './' + doc + '.txt'
	docpath = 'D:/5_PatentData/Data/Post_txt/' + doc + '.txt'
	sentlist = []
	file = open(docpath, encoding='utf8')
	# 将：； 替换为. 以实现分词
	for line in file:
		line = re.sub("\s\(.*?\)+", "", line)
		for s in sent_tokenize(line.replace(",", ".").replace(":", ".").replace(";", ".")):
			sentence = s.strip()
			sents = re.sub("[\[\]\.\!\?\/_,$%^*()+\"\':;]+|[+——！，。？、~@#￥%……&*（）]+", "",sentence)
			if sents.strip() == "":
				continue
			else:
				sentlist.append(sents)
	
	return sentlist

if __name__ == '__main__':
	doc = '01text'
	sentlist = sentence_token(doc)








#string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",sentlist[3]) 正则过滤掉标点和特殊符号
#sents = sentence.strip()   去除字符串开头或者结尾的空格
#lstrip()方法，去除字符串开头的空格
#rstrip()方法，去除字符串结尾的空格


#利用正则表达式过滤掉标点和特殊符号
#string = re.sub("[\[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",sentence)