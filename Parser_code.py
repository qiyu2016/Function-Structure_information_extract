#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu

包括了Lemmatization过程；
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from Lemmatization_code import Lemmatizating

#{<DT|PP\$>?<JJ>*<NN>}   匹配一个可选的限定词或所有格代名词，零个或多个形容词，然后跟一个名词
#{<DT|PP\$>?<JJ>*<NN>+}  匹配一个可选的限定词或所有格代名词，零个或多个形容词，然后跟一个或多个名词

# 正则表达式的NP分块器设置，此处仍然存在问题需要解决
'''
grammar = r"""NP: 
                {<JJ>*<NN>+} 
                {<NNP>+}
                {<NN><NN>}
                """
'''
#第一条规则匹配零个或多个形容词，然后跟一个或多个名词
#第二条规则匹配一个或多个专有名词
#第三条规则匹配一个或多个名词

#{<JJ.*>*<N.*>+} 匹配零个或多个任意类型形容词，然后跟一个或多个 N.
# 可以定义多条分块规则；面对多条规则，分块器会轮流应用分块规则，依次更新块结构，所有的规则都被调用后才返回。

def parser(sentence):
	grammar = r"""NP:
					{<JJ.*>*<N.*>+}    
					{<NNP>+}
					{<NN>+}"""
	cp = nltk.RegexpParser(grammar)
	s = sentence
	text = nltk.pos_tag(word_tokenize(s))
	print(text)
	result = cp.parse(text)
	#result.draw()
	
	NPlist = []
	for subtree in result.subtrees():
		NPhase = []
		if subtree.label() == 'NP':
			print(subtree)
			for i in range(len(subtree)):
				wordLemati = Lemmatizating(subtree[i])
				NPhase.append(wordLemati)
				#NPhase.append(subtree[i][0])
			NPlist.append(NPhase)
	
	print(NPlist)
	return NPlist
	

if __name__ == '__main__':
	sentence = "UAVs are adept at gathering an immense amount of visual information and displaying it to human operators"
	#parser(sentence)
	NPlist = parser(sentence)