#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu

此代码包含 Lemmatization过程
"""

from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tokenize.stanford_segmenter import StanfordSegmenter
from nltk.tag import StanfordPOSTagger
from nltk.parse.stanford import StanfordDependencyParser
from nltk.parse.stanford import StanfordParser
import pickle as pkl

from Lemmatization_code import Lemmatizating


def extract_svo(sentence):
	eng_dependency_parser = StanfordDependencyParser(path_to_jar=r"D:/jars/stanford-parser.jar",
													 path_to_models_jar=r"D:/jars/stanford-parser-3.9.2-models.jar")
	
	
	outputs = sentence
	print(outputs)
	
	stanlabel = []
	
	result = list(eng_dependency_parser.parse(outputs.split()))
	for each in result[0].triples():
		stanlabel.append(each[1])     # 将获得的Stanford依存分析中的标签 写到list中；
		print(each)
	print(stanlabel) #打印所有的依存关系标签
	
	triplelist = [] #三元组list

	# python代码换行，(1)代码中直接换行，空格+\ (2)加上括号，(){}[]中不需要特别加换行符 (3)三引号实现	
	#抽取S-V; 由rule1:  nsubj
	if (
		('nsubj' in stanlabel) and
		('nsubjpass' not in stanlabel) and
		('dobj' not in stanlabel) and
		('xsubj' not in stanlabel) and
		('agent' not in stanlabel) and  
		('xcomp' not in stanlabel) and
		('aux' not in stanlabel) and
		('cop' not in stanlabel)
		):
		#triple = ['null', 'null', '*' ]
		for each in result[0].triples():
			if each[1] == 'nsubj':
				triple = [Lemmatizating(each[2]), Lemmatizating(each[0]), '*' ]
				#triple[0] = each[2][0]
				#triple[1] = each[0][0]
				#print(triple), triplelist.append(triple)   两句代码可以写在同一行，用 , 隔开
				triplelist.append(triple)


	#抽取S-V-O; 由rule2: nsubj & aux & cop 
	# The video data transmission by the given UAV to the video data processing center can be through a UAV network
	# The video stream can be output at a location of a given party in the video conference
	if (
		('nsubj' in stanlabel) and
		('nsubjpass' not in stanlabel) and
		('dobj' not in stanlabel) and
		('xsubj' not in stanlabel) and
		('agent' not in stanlabel) and
		('xcomp' not in stanlabel) and
		('aux' in stanlabel) and
		('cop' in stanlabel)
		):
		for each in result[0].triples():
			if each[1] == 'nsubj':
				tri_nsubj = [Lemmatizating(each[2]), '*', Lemmatizating(each[0])]			
			elif each[1] == 'aux':
				tri_aux = ['*', Lemmatizating(each[2]), Lemmatizating(each[0])]
			elif each[1] == 'cop':
				tri_cop = ['*', Lemmatizating(each[2]), Lemmatizating(each[0])]	

		if (
			(tri_nsubj[2] == tri_aux[2]) and
			(tri_nsubj[2] == tri_cop[2])
			):
			tri_NAC = [tri_nsubj[0], tri_cop[1], tri_nsubj[2]]
			triplelist.append(tri_NAC)		
		

	#抽取S-V-O; 由rule3: nsubj & xcomp 
	# the boy looks healthy
	if (
		('nsubj' in stanlabel) and
		('nsubjpass' not in stanlabel) and
		('dobj' not in stanlabel) and
		('xsubj' not in stanlabel) and
		('agent' not in stanlabel) and
		('xcomp' in stanlabel)
		):
		for each in result[0].triples():
			if each[1] == 'nsubj':
				tri_nsubj = [Lemmatizating(each[2]), Lemmatizating(each[0]), '*']
				#print(tri_nsubjpass)
			elif each[1] == 'xcomp':
				tri_xcomp = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
				#print(tri_dobj)
		if tri_nsubj[1] == tri_xcomp[1]:
			triple = [tri_nsubj[0], tri_nsubj[1], tri_xcomp[2]]
			triplelist.append(triple)


	#抽取S-V-O; 由rule4: nsubj & dobj 
	#由 nsubj(y,x) & dobj(z,x) 组成主动语态的 SVO  
	if (
		('nsubj' in stanlabel) and
		('nsubjpass' not in stanlabel) and
		('dobj' in stanlabel) and
		('xsubj' not in stanlabel) and
		('agent' not in stanlabel) and
		('advcl' not in stanlabel) and
		('xcomp' not in stanlabel)
	    ):
		tri_nsubj = []
		tri_dobj = []
		for each in result[0].triples():
			if each[1] == 'nsubj':
				triple = [Lemmatizating(each[2]), Lemmatizating(each[0]), '*' ]
				tri_nsubj.append(triple)
			elif each[1] == 'dobj':
				triple = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
				tri_dobj.append(triple)
			
		tri_list = tri_nsubj + tri_dobj
		for a in tri_nsubj:
			for b in tri_dobj:
				if a[1] == b[1]:
					triple[0] = a[0]
					triple[1] = a[1]
					triple[2] = b[2]
					triplelist.append(triple)
					if a in tri_list:
						tri_list.remove(a)
					if b in tri_list:
						tri_list.remove(b)
		for c in tri_list:
			triplelist.append(c)


	#抽取S-V-O; 由rule5: nsubj & dobj & advcl <advcl 修饰动词的状语从句> {主句中的动词>>从句中的主要成分}
	# 句子中只有一个主语
	# 解决多个dobj (多个谓语动词),以及含有nmod 依存关系
	# The present disclosure relates to facilitating video conferencing through unmanned aerial vehicle
	# UAVs are adept at gathering an immense amount of visual information and displaying it to human operators
	if (
		('nsubj' in stanlabel) and
		('nsubjpass' not in stanlabel) and
		('dobj' in stanlabel) and
		('xsubj' not in stanlabel) and
		('agent' not in stanlabel) and
		('advcl' in stanlabel)
		):
		#tri_nsubj = []
		#tri_dobj = []
		for each in result[0].triples():
			if each[1] == 'nsubj':
				tri_nsubj = [Lemmatizating(each[2]), Lemmatizating(each[0]), '*']
				#print(tri_nsubjpass)
			elif each[1] == 'advcl':
				tri_advcl = [Lemmatizating(each[0]), '*', Lemmatizating(each[2])]
				#print(tri_advcl)
		
		if tri_nsubj[1] == tri_advcl[0]:
			for each in result[0].triples():
				if each[1] == 'dobj':
					tri_dobj = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
					triple = [tri_nsubj[0], tri_dobj[1], tri_dobj[2]]
					triplelist.append(triple)


	#抽取S-V-O; 由rule6: nsubj & dobj & xcomp 
	# they demanded to see my passport
	# Tom likes to eat fish
	if (
		('nsubj' in stanlabel) and
		('nsubjpass' not in stanlabel) and
		('dobj' in stanlabel) and
		('xsubj' not in stanlabel) and
		('agent' not in stanlabel) and
		('advcl' not in stanlabel) and
		('xcomp' in stanlabel)
		):
		for each in result[0].triples():
			if each[1] == 'nsubj':
				tri_nsubj = [Lemmatizating(each[2]), Lemmatizating(each[0]), '*']
			elif each[1] == 'dobj':
				tri_dobj = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
			elif each[1] == 'xcomp':
				tri_xcomp = [Lemmatizating(each[0]), '*', Lemmatizating(each[2])]

		if (
			(tri_xcomp[0] == tri_nsubj[1]) and
			(tri_xcomp[2] == tri_dobj[1])
			):
			tri_NDX = [tri_nsubj[0], tri_dobj[1], tri_dobj[2]]
			triplelist.append(tri_NDX)


	#抽取S-V; 由rule7: nsubjpass
	if (
		('nsubj' not in stanlabel) and
		('nsubjpass' in stanlabel) and
		('dobj' not in stanlabel) and
		('xsubj' not in stanlabel) and
		('agent' not in stanlabel) and 
		('nmod' not in stanlabel)
		):
		for each in result[0].triples():
			if each[1] == 'nsubjpass':
				triple = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
				triplelist.append(triple)


	#抽取S-V-O; 由rule8: nsubjpass & nmod 
	# <nmod 复合名词修饰> {复合短语>>形容修饰语}
	if (
		('nsubj' not in stanlabel) and
		('nsubjpass' in stanlabel) and
		('dobj' not in stanlabel) and
		('xsubj' not in stanlabel) and
		('agent' not in stanlabel) and
		('nmod' in stanlabel)
		):
		tri_nsubjpass = []
		tri_nmod = []
		for each in result[0].triples():
			if each[1] == 'nsubjpass':
				triple = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]			
				tri_nsubjpass.append(triple)
			elif each[1] == 'nmod':
				triple = [Lemmatizating(each[2]), Lemmatizating(each[0]), '*']
				tri_nmod.append(triple)

		tri_list = tri_nsubjpass
		print(tri_list)
		for a in tri_nsubjpass:
			for b in tri_nmod:
				if a[1] == b[1]:
					triple[0] = b[0]
					triple[1] = a[1]
					triple[2] = a[2]
					triplelist.append(triple)
					#print(a)
					if a in tri_list:
						tri_list.remove(a)

		for c in tri_list:
			triplelist.append(c)


	#抽取S-V-O; 由rule9: agent & nsubjpass
	if (
		('nsubj' not in stanlabel) and
		('nsubjpass' in stanlabel) and
		('dobj' not in stanlabel) and
		('xsubj' not in stanlabel) and
		('agent' in stanlabel)
	    ):
		tri_nsubjpass = []
		tri_agent = []
		for each in result[0].triples():
			if each[1] == 'nsubjpass':
				triple = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
				tri_nsubjpass.append(triple)
			elif each[1] == 'agent':
				triple = [Lemmatizating(each[2]), Lemmatizating(each[0]), '*']
				tri_agent.append(triple)
			
		tri_list = tri_nsubjpass + tri_agent
		for a in tri_nsubjpass:
			for b in tri_agent:
				if a[1] == b[1]:
					triple[0] = a[0]
					triple[1] = a[1]
					triple[2] = b[2]
					triplelist.append(triple)
					if a in tri_list:
						tri_list.remove(a)
					if b in tri_list:
						tri_list.remove(b)
		for c in tri_list:
			triplelist.append(c)


	#抽取S-V-O; 由rule10: nsubjpass & dobj & advcl <advcl 修饰动词的状语从句> {主句中的动词>>从句中的主要成分}
	# Embodiments are provided for facilitating a wide-view video conference through a UAV network
	if (
		('nsubj' not in stanlabel) and
		('nsubjpass' in stanlabel) and
		('dobj' in stanlabel) and
		('xsubj' not in stanlabel) and
		('agent' not in stanlabel) and
		('advcl' in stanlabel)
		):
		#tri_nsubj = []
		#tri_dobj = []
		for each in result[0].triples():
			if each[1] == 'nsubjpass':
				tri_nsubjpass = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
				#print(tri_nsubjpass)
			elif each[1] == 'dobj':
				tri_dobj = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
				#print(tri_dobj)
			elif each[1] == 'advcl':
				tri_advcl = [Lemmatizating(each[0]), '*', Lemmatizating(each[2])]
				#print(tri_advcl)
		
		if (
			(tri_advcl[0] == tri_nsubjpass[1]) and
			(tri_advcl[2] == tri_dobj[1])
			):
			triple = [tri_nsubjpass[2], tri_dobj[1], tri_dobj[2]]
			triplelist.append(triple)	


	#抽取S-V-O; 由rule11: nsubjpass & dobj & xcomp
	# <xcomp 开放从句(缺少主语的从句)补语> {开放从句的补足对象(动词)>>开放从句的动词}
	# the shaft is used to transmit torque
	if (
		('nsubj' not in stanlabel) and
		('nsubjpass' in stanlabel) and
		('dobj' in stanlabel) and
		('xsubj' not in stanlabel) and
		('agent' not in stanlabel) and
		('advcl' not in stanlabel) and
		('xcomp' in stanlabel) and
		('conj' not in stanlabel)
		):
		tri_NDX = []
		for each in result[0].triples():
			if each[1] == 'nsubjpass':
				tri_nsubjpass = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
				#print(tri_nsubjpass)
			elif each[1] == 'dobj':
				tri_dobj = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
				#print(tri_dobj)
			elif each[1] == 'xcomp':
				tri_xcomp = [Lemmatizating(each[0]), '*', Lemmatizating(each[2])]
				#print(tri_advcl)
				
		if (
			(tri_xcomp[0] == tri_nsubjpass[1]) and
			(tri_xcomp[2] == tri_dobj[1])
			):
			tri_NDX = [tri_nsubjpass[2], tri_dobj[1], tri_dobj[2]]
			triplelist.append(tri_NDX)


	#抽取S-V-O; 由rule12: nsubjpass & dobj & xcomp & conj 
	# <xcomp 开放从句(缺少主语的从句)补语> {开放从句的补足对象(动词)>>开放从句的动词}
	# <conj 用协同连词(and, or) 连接的两个元素> {第一个元素>>第二个元素}
	# UAVs can be employed to capture and transmit video data at locations of parties involved in the wide-view video conference
	if (
		('nsubj' not in stanlabel) and
		('nsubjpass' in stanlabel) and
		('dobj' in stanlabel) and
		('xsubj' not in stanlabel) and
		('agent' not in stanlabel) and
		('advcl' not in stanlabel) and
		('xcomp' in stanlabel) and
		('conj' in stanlabel)
		):
		tri_conj = []
		tri_NDX = []
		for each in result[0].triples():
			if each[1] == 'nsubjpass':
				tri_nsubjpass = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
				#print(tri_nsubjpass)
			elif each[1] == 'dobj':
				tri_dobj = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
				#print(tri_dobj)
			elif each[1] == 'xcomp':
				tri_xcomp = [Lemmatizating(each[0]), '*', Lemmatizating(each[2])]
				#print(tri_advcl)
			elif each[1] == 'conj':
				tri_conj = [Lemmatizating(each[0]), '*', Lemmatizating(each[2])]
				
		if (
			(tri_xcomp[0] == tri_nsubjpass[1]) and
			(tri_xcomp[2] == tri_dobj[1])
			):
			tri_NDX = [tri_nsubjpass[2], tri_dobj[1], tri_dobj[2]]
			triplelist.append(tri_NDX)
		
		if (
			(tri_conj != []) and
			(tri_NDX != [])
			):
			if tri_NDX[1] == tri_conj[0]:
				tri_NDX2 = [tri_NDX[0], tri_conj[2], tri_NDX[2]]
				triplelist.append(tri_NDX2)


	#抽取S-V; 由rule13:dobj
	if (
		('nsubj' not in stanlabel) and
		('nsubjpass' not in stanlabel) and
		('dobj' in stanlabel) and
		('xsubj' not in stanlabel) and
		('agent' not in stanlabel)
	    ):
		for each in result[0].triples():
			if each[1] == 'dobj':
				triple = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
				triplelist.append(triple)


	#抽取S-V-O; 由rule14:xsubj & dobj
	if (
		('nsubj' not in stanlabel) and
		('nsubjpass' not in stanlabel) and
		('dobj' in stanlabel) and
		('xsubj' in stanlabel) and
		('agent' not in stanlabel)
	    ):
		tri_xsubj = []
		tri_dobj = []
		for each in result[0].triples():
			if each[1] == 'xsubj':
				triple = [Lemmatizating(each[2]), Lemmatizating(each[0]), '*' ]
				tri_xsubj.append(triple)
			elif each[1] == 'dobj':
				triple = ['*', Lemmatizating(each[0]), Lemmatizating(each[2])]
				tri_dobj.append(triple)
			
		tri_list = tri_xsubj + tri_dobj
		for a in tri_xsubj:
			for b in tri_dobj:
				if a[1] == b[1]:
					triple[0] = a[0]
					triple[1] = a[1]
					triple[2] = b[2]
					triplelist.append(triple)
					if a in tri_list:
						tri_list.remove(a)
					if b in tri_list:
						tri_list.remove(b)
		for c in tri_list:
			triplelist.append(c)


	
	triplelist01 = []	#实现去除triplelist中的重复元素	
	for triplesingle in triplelist:
		if triplesingle not in triplelist01:
			triplelist01.append(triplesingle)
			
	
	for i in triplelist01:
		print(i)
		
	return triplelist01

if __name__ == '__main__':
	sentence = "Facilitating wide view video conferencing through a drone network"
	#extract_svo(sentence)
	triplelist01 = extract_svo(sentence)


		










