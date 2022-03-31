#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu

包含了Lemmatization过程
"""

import linecache

from Parser_code import parser
from stanfordparser_code import extract_svo
from sentence_token_code import sentence_token
from inital_lower_code import inital_lower


def everypatent_Extract(doc):
	sentlist = sentence_token(doc)
	
	svo = []
	for sentence in sentlist:
		#Parser_code.parser(sentence)
		
		sentence = inital_lower(sentence)   #把句子的首字母改为小写
		NPlist = parser(sentence)
		triplelist = extract_svo(sentence)
	
		svo_list = []
		for i in triplelist:
			for j in NPlist:
				if i[0] in j:
					i[0] = ' '.join(j)
				if i[2] in j:
					i[2] = ' '.join(j)
			svo_list.append(i)
		
		for i in svo_list:
			if i not in svo:
				svo.append(i)
	
	print(svo)
	path = "D:/5_PatentData/Data/SVO_v3/" + doc + ".txt"   # SVO保存路径
	file_txt = open(path, 'a', encoding='utf8')
	for ilist in svo:
		file_txt.write(ilist[0] + "     " + ilist[1] + "     " + ilist[2] + "\n")
	file_txt.close()
		
if __name__ == '__main__':
	TotalNum = 1448   #爬取的数量
	count = 1307
	while True:
		linepath = "D:/5_PatentData/Data/Post_txt/" + str(count) + ".txt"
		linecontent = linecache.getline(linepath, 1)
		if "论文页>" in linecontent:
			path = "D:/5_PatentData/Data/SVO_v3/" + str(count) + ".txt"   # 写 论文页>
			file_ddd = open(path, 'a', encoding='utf8')
			file_ddd.write(linecontent)
			file_ddd.close()
		else:
			everypatent_Extract(str(count))
	
		linecache.clearcache()   #清除现有的文件缓存
		count = count + 1
		if count > TotalNum:
			break	
		
	
	
	