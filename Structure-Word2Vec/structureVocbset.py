#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu
@date : 2021/1/4 20:57

构建 structure & component 词汇集;
并存储到 一个 txt文档；

得到的 结构词汇集的保存文件是： D:/6_OpportunityData/StructWordSet.txt ；数量结构与组件词汇列表(StructureVocb)中元素的个数 1774；
"""

pathArtifact = 'D:/6_OpportunityData/structuralvophrase.txt'
ArtifactList = []
for line in open(pathArtifact, encoding='utf8'):
    items = line.strip().split(' ')
    ArtifactList.extend(items)

# extend()是使用一个列表来扩展另一个列表
print(ArtifactList[0:9])

# 加上WordlistComponents中的词汇
# strip() 用于移除字符串头尾指定的字符(默认为空格或换行符)
CompList = []
for line in open('D:/6_OpportunityData/WordlistComponents.txt', encoding='utf8'):
    items = line.strip()
    CompList.append(items)

WholeList = []
print("空列表中WholeList元素的个数 %s" % (len(WholeList)))
WholeList.extend(ArtifactList)
print("列表WholeList元素的个数(OSU设计知识库中的组件词汇数) %s" % (len(WholeList)))
WholeList.extend(CompList)
print("列表WholeList元素的个数(组件词汇+component) %s" % (len(WholeList)))

# 列表中元素的去重
StructureVocb = sorted(set(WholeList), key=WholeList.index)

#for i in BoWList:
#    print(i)
print("结构与组件词汇列表(StructureVocb)中元素的个数 %s" % (len(StructureVocb)))
print(StructureVocb[0:9])


fileStruct = open("D:/6_OpportunityData/StructWordSet.txt", 'a', encoding='utf8')
for j in StructureVocb:
    fileStruct.write(j + '\n')
fileStruct.close()




