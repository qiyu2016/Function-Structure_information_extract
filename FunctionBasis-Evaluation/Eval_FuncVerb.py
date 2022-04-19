#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu
@date : 2020/6/1 16:25

评估功能词汇对功能基中的功能动词的覆盖情况
"""

FuncBasis = ['brance', 'separate', 'distribute', 'divide', 'extract', 'remove', 'isolate', 'sever', 'disjoin', 'detach', 'isolate', 'release', 'sort', 'split', 'disconnect', 'subtract', 'refine', 'filter', 'purify', 'percolate', 'strain', 'clear', 'cut', 'drill', 'lathe','polish', 'sand', 'diffuse', 'dispel', 'disperse', 'dissipate', 'diverge', 'scatter', 'channel', 'import', 'export', 'transfer', 'guide', 'transport', 'transmit', 'translate', 'rotate', 'allow', 'form', 'entrance', 'allow', 'input', 'capture', 'dispose', 'eject', 'emit', 'empty', 'remove', 'destroy', 'eliminate', 'carry', 'deliver', 'advance', 'lift', 'move', 'conduct', 'convey', 'direct', 'shift', 'steer', 'straighten', 'switch', 'move', 'relocate', 'spin', 'turn', 'constrain', 'unfasten', 'unlock', 'connect', 'couple', 'mix', 'join', 'link', 'associate', 'connect', 'assemble', 'fasten', 'attach', 'add', 'blend', 'coalesce', 'combine', 'pack', 'control', 'actuate', 'regulate', 'increase', 'decrease', 'enable', 'initiate', 'start', 'turn-on', 'control', 'equalize', 'limit', 'maintain', 'allow', 'open', 'close', 'delay', 'interrupt', 'magnitude', 'change', 'stop', 'increment', 'decrement', 'shape', 'condition', 'prevent', 'inhibit', 'adjust', 'modulate', 'clear', 'demodulate', 'invert', 'normalize', 'rectify', 'reset', 'scale', 'vary', 'modify', 'amplify', 'enhance', 'magnify', 'multiply', 'attenuate', 'dampen', 'reduce', 'compact', 'compress', 'crush', 'pierce', 'deform', 'form', 'prepare', 'adapt', 'treat', 'end', 'halt', 'pause', 'interrupt', 'restrain', 'disable', 'turn-off', 'shield', 'insulate', 'protect', 'resist', 'convert', 'convert', 'condense', 'create', 'decode', 'differentiate', 'digitize', 'encode', 'evaporate', 'generate', 'integrate', 'liquefy', 'process', 'solidify', 'transform', 'provision', 'store', 'supply', 'contain', 'collect', 'accumulate', 'capture', 'enclose', 'absorb', 'consume', 'fill', 'reserve', 'provide', 'replenish', 'retrieve', 'signal', 'sense', 'indicate', 'process', 'detect', 'measure', 'track', 'display', 'feel', 'determine', 'discern', 'perceive', 'recognize', 'identify', 'locate', 'announce', 'show', 'denote', 'record', 'register', 'mark', 'time', 'emit', 'expose', 'select', 'compare', 'calculate', 'check', 'support', 'stabilize', 'secure', 'position', 'steady', 'constrain', 'hold', 'place', 'fix', 'align', 'locate', 'orient']

print('功能基列表长度：', len(FuncBasis))

# 去除FuncBasis 中的重复项
FuncBasis_NoRepe = []
for i in FuncBasis:
    if i not in FuncBasis_NoRepe:
        FuncBasis_NoRepe.append(i)

print('功能基列表中去除重复项后的列表长度：', len(FuncBasis_NoRepe))
print(FuncBasis_NoRepe)


# 提取功能三元组中的功能动词
path = "D:/5_PatentData/Data/Functions/FunctionList02.txt"
verbs = []
for line in open(path, encoding='utf8'):
    items = line.strip().split('     ')
    verbs.append(items[1])

FuncVerbs = list(set(verbs))   # 去重
print(FuncVerbs)

# 探测提取的功能动词覆盖了多少个 功能基动词
FunCover = []   # 覆盖的功能动词有哪些
Num = 0
for i in FuncBasis_NoRepe:
    if i in FuncVerbs:
        FunCover.append(i)
#        print(len(FunCover))
        Num = Num + 1
#print(len(FunCover))
print('功能动词覆盖了多少个功能基动词：', Num)
print('功能动词覆盖功能动词的比例：', (Num/len(FuncBasis_NoRepe)))

# 每一个覆盖了的功能动词有多少个功能三元组
for i in FunCover:
    SumFC = 0
    for j in verbs:
        if i == j:
            SumFC = SumFC + 1
    print(i, SumFC)




