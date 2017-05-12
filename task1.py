# -*- coding: utf-8 -*-
import numpy
import core
import model



step = 1
adds = 0
ourGraph = model.Graph("task1.txt")
print(str(step)+") Проверим свойства отношения: \n ",ourGraph.checkRelations())
step = step+1


print(str(step)+") Чтобы отношение было отношением частичного порядка нужно чтобы оно было рефлексивным, антисимметричным, транзитивным")
if ourGraph.checkReflexive():
    print("Отношение рефлексивно")
else:
    adds = adds+ourGraph.makeReflexive()

if ourGraph.checkTransitive():
    print("Отношение транзитивно")
else:
    adds = adds+ourGraph.makeTransitive()
print(ourGraph.data)


