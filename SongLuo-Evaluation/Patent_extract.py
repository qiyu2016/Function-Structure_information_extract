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
	path = "D:/5_PatentData/Data/SongLuo_Patent/Song_SVO/" + doc + ".txt"   # SVO保存路径
	file_txt = open(path, 'a', encoding='utf8')
	for ilist in svo:
		file_txt.write(ilist[0] + "     " + ilist[1] + "     " + ilist[2] + "\n")
	file_txt.close()

# 110个专利文本已经存储在本地，根据专利号命名了文本文件，根据文本文件的名称 进行功能三元组的解析
if __name__ == '__main__':
	PatID = ['3933115', '4057929', '4192094', '4377982', '4386787', '4391224', '4438588', '4455962', '4471567',
			'4501434', '4501569', '4505346', '4541814', '4571192', '4601675', '4671779', '4726800', '4729446',
			'4733737', '4808141', '4861053', '4927401', '5297981', '5409414', '5439408', '5533920', '5533921',
			'5676582', '5692946', '5720644', '5871386', '5893791', '5924909', '5934968', '5947793', '5964639',
			'6066026', '6071167', '6227933', '6289263', '6298934', '6378634', '6402630', '6414457', '6458008',
			'6502657', '6550089', '6569025', '6571415', '6634593', '6855028', '6902464', '6938298', '6964572',
			'6966523', '6976899', '7055777', '7104222', '7165637', '7207081', '7210816', '7217170', '7229029',
			'7254859', '7327112', '7434638', '7467579', '7484447', '7490681', '7726422', '7770523', '7794300',
			'7963350', '7963351', '8054198', '8099189', '8137152', '8165814', '8197298', '8210289', '8220408',
			'8269447', '8316970', '8322471', '8467925', '8499862', '8528854', '8571781', '8670889', '8751063',
			'8768548', '8788130', '8894465', '8910734', '8912892', '9020639', '9061558', '9090214', '9114838',
			'9150069', '9150263', '9152148', '9193404', '9211920', '9218316', '9272743', '9280717', '9290220',
			'9292758', '9342073']
	TotalNum = len(PatID)
	count = 0
#	TotalNum = 1448   #爬取的数量
#	count = 1307

	while True:
		linepath = "D:/5_PatentData/Data/SongLuo_Patent/" + PatID[count] + ".txt"
		linecontent = linecache.getline(linepath, 1)
		if "论文页>" in linecontent:
			path = "D:/5_PatentData/Data/SongLuo_Patent/Song_SVO/" + PatID[count] + ".txt"   # 写 论文页>
			file_ddd = open(path, 'a', encoding='utf8')
			file_ddd.write(linecontent)
			file_ddd.close()
		else:
			everypatent_Extract(PatID[count])
	
		linecache.clearcache()   #清除现有的文件缓存
		count = count + 1
		if count >= TotalNum:
			break	
		
	
	
	