#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu
@date : 2020/5/23 17:03

探索功能重用，查找功能三元组中包含了 查询关键词的功能三元组

先将不重复的三元组存入 FunctionList02列表
"""

'''
# -----------------------------------------------------------------------------------
# 先把所用的功能三元组写进一个text文件
import linecache

TotalNum = 1448   # 设置文本文件总数
count = 1



FuncList = []

while True:
# 五个空格分开的
    linepath = "D:/5_PatentData/Data/SVO_v3/" + str(count) + ".txt"
    linecontent = linecache.getline(linepath, 1)
    if "论文页>" not in linecontent:
        for line in open(linepath, encoding='utf8'):
            FuncList.append(line)
    linecache.clearcache()
    count = count + 1
    if count > TotalNum:
        break

FuncList_NoRepe = list(set(FuncList))

path = "D:/5_PatentData/Data/Functions/FunctionList02.txt"
filefunc = open(path, 'a', encoding='utf8')

for ilist in FuncList_NoRepe:
    filefunc.write(ilist)

filefunc.close()
# -----------------------------------------------------------------------------------
'''

'''
# -----------------------------------------------------------------------------------
queryword = ['drone', 'deliver', 'package']

path = "D:/5_PatentData/Data/Functions/FunctionList02.txt"

NumCum = 0
for line in open(path, encoding='utf8'):
    wordlist = []
    items = line.strip().split('     ')
    for iconcept in items:
        words = iconcept.split(' ')
        for i in words:
            wordlist.append(i)

    DetNumber = 0
    for j in queryword:
        if j in wordlist:
            DetNumber = DetNumber + 1
    if DetNumber > 0:
        print(line.strip('\n'))
        NumCum = NumCum + 1

print(str(NumCum))
# -----------------------------------------------------------------------------------
'''


# 查询含有关键词 drone, deliver, package 的功能三元组，并计算与这个三元组的相似度，以累加取平均计算相似度
queryword = ['drone', 'deliver', 'package']

path = "D:/5_PatentData/Data/Functions/FunctionList02.txt"
NumCum = 0
FunDet = []
for line in open(path, encoding='utf8'):
    wordlist = []
    items = line.strip().split('     ')
    for iconcept in items:
        words = iconcept.split(' ')
        for i in words:
            wordlist.append(i)

    DetNumber = 0
    for j in queryword:
        if j in wordlist:
            DetNumber = DetNumber + 1
    if DetNumber > 0:
        FunDet.append(line.strip('\n'))
        NumCum = NumCum + 1

print(str(NumCum))
print(len(FunDet))
print(FunDet[0:10])

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models.keyedvectors import KeyedVectors
model_DeepWalk = KeyedVectors.load('D:/5_PatentData/Data/Training_Model/Network_DeepWalk.model')   # 加载DeepWalk训练的模型文件


FunctionSim = []       # 带相似度的功能三元组列表
for itri in FunDet:
    triple = itri.split('     ')
    tripleSim = []
    SimSum = 0                      # 相似度累加值
    Nasterisk = 0                   # 三元组中有几个 * 号，一般只有一个
    for k in range(3):                      # 此处改用range循环，详细查看 Detect_FunctionReuse03.py

        if triple[k].strip() == '*':
            ki = triple[k]
            Nasterisk = Nasterisk + 1
        else:
            ki = triple[k].replace(' ', '_')
            ySim = model_DeepWalk.similarity(queryword[k], ki)
            SimSum = SimSum + ySim
        tripleSim.append(ki)

    SimMean = SimSum/(3-Nasterisk)
    tripleSim.append(SimMean)
    FunctionSim.append(tripleSim)

print(len(FunctionSim))
print(FunctionSim[0:20])


# 根据相似度排序并输出前30个功能三元组
FuncSim_Sort = sorted(FunctionSim,key=(lambda x:x[3]), reverse=True)
for ii in range(30):
    print(FuncSim_Sort[ii])

# 写入CSV文件
'''
pathsort = "D:/5_PatentData/Data/Functions/Function_Sorted.txt"
fileFunSVO = open(pathsort, 'a', encoding='utf8')
for kk in FuncSim_Sort:
    fileFunSVO.write(kk[0] + )

fileFunSVO.close()
'''

import csv
pathsort = "D:/5_PatentData/Data/Functions/Function_Sorted.csv"
CSVFunc = open(pathsort, 'w', newline='')
writer = csv.writer(CSVFunc)
writer.writerow(['Concept', 'Function', 'Concept', 'Similarity'])
for iFS in FuncSim_Sort:
    writer.writerow(iFS)
CSVFunc.close()
