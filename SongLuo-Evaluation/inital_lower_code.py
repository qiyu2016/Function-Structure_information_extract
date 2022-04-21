#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu

判断句子首字母大写改小写，前两个字母均为大写或含有数字不做修改
"""


def inital_lower(sentence):
	if (
		(sentence[0:1].isalnum() is True) and
		(sentence[0:1].isupper() is True)
		): 
		if (
			(sentence[1:2].isalnum() is True) and
			(sentence[1:2].isupper() is True)
			):
			pass
		elif sentence[1:2].isdigit() is True:
			pass
		else:
			sentence = sentence.replace(sentence[0:1], sentence[0:1].lower())
	else:
		pass
		
	return sentence

if __name__ == '__main__':
	sentence = 'F6 Acilitating wide view video conferencing through a drone network'
	sentence = inital_lower(sentence)