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
		
		path = "D:/5_PatentData/Data/SongLuo_Patent/Song_Term/" + doc + ".txt"
		file_terms = open(path, 'a', encoding='utf8')
		pathcorpus = "D:/5_PatentData/Data/SongLuo_Patent/Song_TrainCorpus/" + doc + ".txt"
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
#	count = 1201
	while True:
		linepath = "D:/5_PatentData/Data/SongLuo_Patent/" + PatID[count] + ".txt"
		linecontent = linecache.getline(linepath, 1)
		if "论文页>" in linecontent:
			path = "D:/5_PatentData/Data/SongLuo_Patent/Song_Term/" + PatID[count] + ".txt"   # 写 论文页>
			file_dddterms = open(path, 'a', encoding='utf8')
			file_dddterms.write(linecontent)
			pathcorpus = "D:/5_PatentData/Data/SongLuo_Patent/Song_TrainCorpus/" + PatID[count] + ".txt"   # 写 论文页>
			file_dddcorpus = open(pathcorpus, 'a', encoding='utf8')
			file_dddcorpus.write(linecontent)			
			
			file_dddterms.close()
			file_dddcorpus.close()
		else:
			everypatent_Preprocessing(PatID[count])
	
		linecache.clearcache()   #清除现有的文件缓存
		count = count + 1
		if count >= TotalNum:
			break	