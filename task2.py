# -*- coding: utf-8 -*-
import model
import numpy
import core

ourGraph = model.Graph("task2/task.txt")
print(ourGraph.data)

somelist = []
i=0
for line in ourGraph.data:
    j=0
    for col in line:
        if col!=0:
            somelist.append([i,j,col])
        j+=1
    i+=1

print(somelist)
somelist.sort(key=lambda somelist: somelist[2])
print(somelist)
vertex = []
for line in range(len(somelist)):
    vertex.append(0)
print(vertex)

result = []

for edge in somelist:
    if vertex[edge[0]]==0:
        vertex[edge[0]]=1
        vertex[edge[1]]=1
        result.append(edge)
    if vertex[edge[1]]==0:
        vertex[edge[1]]=1
        vertex[edge[0]]=1
        result.append(edge)

print(result)
for edge in result:
    edge[0] = core.big_letters[edge[0]]
    edge[1] = core.big_letters[edge[1]]
print(result)


