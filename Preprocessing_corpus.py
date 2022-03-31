#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu
"""

from Parser_code import parser
from stanfordparser_code import extract_svo
from sentence_token_code import sentence_token
from inital_lower_code import inital_lower

from Lemmatization_code import Lemmati_sentence
import linecache


def everypatent_Preprocessing(doc):
	sentlist = sentence_token(doc)
	
	svo = []
	for sentence in sentlist:
		#Parser_code.parser(sentence)
		sentence = inital_lower(sentence)
		
#		path = "D:/5_PatentData/function_SVO/Test_corpus/" + doc + ".txt"
#		file_corpus = open(path, 'a', encoding='utf8')
#		file_corpus.write(sentence + "\n")
		
		NPlist = parser(sentence)
		
		path = "D:/5_PatentData/Data/Terms/" + doc + ".txt"
		file_terms = open(path, 'a', encoding='utf8')
		pathcorpus = "D:/5_PatentData/Data/Training_corpus/" + doc + ".txt"
		file_corpus = open(pathcorpus, 'a', encoding='utf8')
		
		sentence = Lemmati_sentence(sentence)   #此处实现将句子中的每个单词根据POS进行词形还原
		
		for iterm in NPlist:
			termrepls = ' '.join(iterm)
			term = '_'.join(iterm)
			file_terms.write(term + "     ")
			sentence = sentence.replace(termrepls, term)
		file_terms.write("\n")
		file_corpus.write(sentence + "\n")
		
	file_corpus.close()
	file_terms.close()

	
if __name__ == '__main__':
#	doc = '001-Test'
#	doc = '1'
#	everypatent_Extract(doc)
	TotalNum = 1448   #爬取的数量
	count = 1201
	while True:
		linepath = "D:/5_PatentData/Data/Post_txt/" + str(count) + ".txt"
		linecontent = linecache.getline(linepath, 1)
		if "论文页>" in linecontent:
			path = "D:/5_PatentData/Data/Terms/" + str(count) + ".txt"   # 写 论文页>
			file_dddterms = open(path, 'a', encoding='utf8')
			file_dddterms.write(linecontent)
			pathcorpus = "D:/5_PatentData/Data/Training_corpus/" + str(count) + ".txt"   # 写 论文页>
			file_dddcorpus = open(pathcorpus, 'a', encoding='utf8')
			file_dddcorpus.write(linecontent)			
			
			file_dddterms.close()
			file_dddcorpus.close()
		else:
			everypatent_Preprocessing(str(count))
	
		linecache.clearcache()   #清除现有的文件缓存
		count = count + 1
		if count > TotalNum:
			break	