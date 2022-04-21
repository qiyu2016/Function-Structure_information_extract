# -*- coding: UTF-8 -*-
"""
@author: Qiyu
"""

from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# 获取单词的词性
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


#sentence = 'football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal.'
#sentence = 'UAVs are adept at gathering an immense amount of visual information and displaying it to human operators'
#sentence = 'facilitating wide_view_video conferencing through a drone_network'

#tokens = word_tokenize(sentence)  # 分词
#tagged_sent = pos_tag(tokens)     # 获取单词词性
wnl = WordNetLemmatizer()

def Lemmatizating(tag):
	# 赋值后有 or, 如果or左边为真，那么or右边不参与运算，取左边的值，不然取右边的值
	wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
	wordLemati = wnl.lemmatize(tag[0], pos=wordnet_pos)
	return wordLemati


def Lemmati_sentence(sentence):
	tokens = word_tokenize(sentence)
	tagged_sent = pos_tag(tokens)
	lemmas_sent = []
	for tag in tagged_sent:
		wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
		lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))	
	sent_Lemma = ' '.join(lemmas_sent)
	
	return sent_Lemma

	
if __name__ == '__main__':
	sentence = 'The present disclosure relates to facilitating video conferencing through unmanned aerial vehicle'
	tokens = word_tokenize(sentence)
	tagged_sent = pos_tag(tokens)
	print(tagged_sent)
	tag = tagged_sent[0]
	wordLemati = Lemmatizating(tag)
	print(wordLemati)
	
	sent_Lemma = Lemmati_sentence(sentence)
	print(sent_Lemma)
	
	