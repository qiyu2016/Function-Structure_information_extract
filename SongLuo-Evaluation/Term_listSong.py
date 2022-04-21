#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu
@date : 2020/6/3 18:16

将Song & Luo 论文中概念术语写入一个 txt文件

and
将抽取的 Song&Luo 论文中专利三元组，写入一个三元组文件
包括去重的步骤
"""

import linecache

PatID = ['3933115', '4057929', '4192094', '4377982', '4386787', '4391224', '4438588', '4455962', '4471567', '4501434', '4501569', '4505346', '4541814', '4571192', '4601675', '4671779', '4726800', '4729446', '4733737', '4808141', '4861053', '4927401', '5297981', '5409414', '5439408', '5533920', '5533921', '5676582', '5692946', '5720644', '5871386', '5893791', '5924909', '5934968', '5947793', '5964639', '6066026', '6071167', '6227933', '6289263', '6298934', '6378634', '6402630', '6414457', '6458008', '6502657', '6550089', '6569025', '6571415', '6634593', '6855028', '6902464', '6938298', '6964572', '6966523', '6976899', '7055777', '7104222', '7165637', '7207081', '7210816', '7217170', '7229029', '7254859', '7327112', '7434638', '7467579', '7484447', '7490681', '7726422', '7770523', '7794300', '7963350', '7963351', '8054198', '8099189', '8137152', '8165814', '8197298', '8210289', '8220408', '8269447', '8316970', '8322471', '8467925', '8499862', '8528854', '8571781', '8670889', '8751063', '8768548', '8788130', '8894465', '8910734', '8912892', '9020639', '9061558', '9090214', '9114838', '9150069', '9150263', '9152148', '9193404', '9211920', '9218316', '9272743', '9280717', '9290220', '9292758', '9342073']


TotalNum = len(PatID)
count = 0

#TotalNum = 1448   #爬取的数量
#count = 1

Term_list = []
FuncList = []

while True:
    linepath = "D:/5_PatentData/Data/SongLuo_Patent/Song_Term/" + PatID[count] + ".txt"
    linecontent = linecache.getline(linepath, 1)
    if "论文页>" in linecontent:
        path = "D:/5_PatentData/Data/SongLuo_Patent/Song_Term/TermList/" + PatID[count] + ".txt"  # 写 论文页>
        file_dddterms = open(path, 'a', encoding='utf8')
        file_dddterms.write(linecontent)

        file_dddterms.close()
    else:
        for line in open(linepath, encoding = 'utf8'):
            items = line.strip().split('     ')
            tmp = []
            for item in items:
                tmp.append(item)
            for item in tmp:
                if item != "":
                    Term_list.append(item)
    linecache.clearcache()

    svopath = "D:/5_PatentData/Data/SongLuo_Patent/Song_SVO/" + PatID[count] + ".txt"
    svocontent = linecache.getline(linepath, 1)
    if "论文页>" not in svocontent:
        for line in open(svopath, encoding='utf8'):
            FuncList.append(line)
    linecache.clearcache()

    count = count + 1
    if count >= TotalNum:
        break

#print(Term_list)

#去除Term_list中的重复项
TermList_Undup = []
for i in Term_list:
    if i not in TermList_Undup:
        TermList_Undup.append(i)
path_write = "D:/5_PatentData/Data/SongLuo_Patent/Song_Term/TermList//Song_Termlist.txt"
file_TermList = open(path_write, 'a', encoding='utf8')
for item in TermList_Undup:
    file_TermList.write(item + "\n")
file_TermList.close()


# 列表内的功能三元组 去重
FuncList_NoRepe = list(set(FuncList))

path = "D:/5_PatentData/Data/SongLuo_Patent/Song_SVO/FuncList_Song/FunctionList_song.txt"
filefunc = open(path, 'a', encoding='utf8')

for ilist in FuncList_NoRepe:
    filefunc.write(ilist)

filefunc.close()
