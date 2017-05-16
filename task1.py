# -*- coding: utf-8 -*-
import numpy
import core
import model


print("Проверим свойства отношения частичного порядка: ")
step = 1
adds = 0
ourGraph = model.Graph("task1/task.txt")
print(str(step)+") Проверим свойства отношения: \n ",ourGraph.checkRelations())
step = step+1


print(str(step)+") Чтобы отношение было отношением частичного порядка нужно чтобы оно было рефлексивным, антисимметричным, транзитивным:")



if ourGraph.checkReflexive():
    print("а) Отношение рефлексивно.")
else:
    print("а) Отношение не рефлексивно.")
    reflex_adds = ourGraph.makeReflexive()
    adds = adds+reflex_adds
    print("а) При дополнении до рефлексивности добавлено " + str(reflex_adds) + " ребер:")
    print(ourGraph.data)
    print("")

if ourGraph.checkTransitive():
    print("б) Отношение транзитивно.")
else:
    print("б) Отношение не транзитивно.")
    transitive_adds = ourGraph.makeTransitive()
    adds = adds+transitive_adds

    print("При дополнении до транзитивности добавлено " + str(transitive_adds) + " ребер:")
    print(ourGraph.data)
    print("")

print("Всего, чтобы дополнть до частичного порядка нужно добавить минимум "+str(adds)+" ребер.")


if ourGraph.checkAntisymmetric():
    print("в) Отношение антисимметрично.")
else:
    print("в) Отношение не антисимметрично. Скорее всего неверные данные. Отношение частичного порядка невозможно")

if ourGraph.checkAntisymmetric() and ourGraph.checkReflexive() and ourGraph.checkTransitive():
    print("Итого матрица с отношением частичного порядка: ")
    print(ourGraph.data)
else:
    print("Отношение порядка не удалось.")

del ourGraph




print("")
print("")
print("")
print("")
print("Проверим свойства отношения эквивалентности: ")
step = 1
adds = 0
ourGraph = model.Graph("task1/task.txt")
print(str(step)+") Проверим свойства отношения: \n ",ourGraph.checkRelations())
print("1) Чтобы отношение было отношением эквивалентности нужно чтобы оно было рефлексивным, симметричным, транзитивным: ")
if ourGraph.checkReflexive():
    print("а) Отношение рефлексивно.")
else:
    print("а) Отношение не рефлексивно.")
    reflex_adds = ourGraph.makeReflexive()
    adds = adds+reflex_adds
    print("При дополнении до рефлексивности добавлено " + str(reflex_adds) + " ребер:")
    print(ourGraph.data)
    print("")

cycle = 0
variants = 0
while not (ourGraph.checkTransitive() and ourGraph.checkSymmetric()):
    cycle+=1
    if ourGraph.checkSymmetric():
        print("б) Отношение симметрично.")
    else:
        print("б) Отношение не симметрично.")
        sym_adds, sym_variants = ourGraph.makeSymmetric()
        variants+=sym_variants
        print("При дополнении до симметричности добавлено " + str(sym_adds) + " ребер:")
        adds = adds+sym_adds
        print(ourGraph.data)

    if ourGraph.checkTransitive():
        print("в) Отношение транзитивно.")
    else:
        print("в) Отношение не транзитивно.")
        transitive_adds = ourGraph.makeTransitive()
        adds = adds+transitive_adds

        print("При дополнении до транзитивности добавлено " + str(transitive_adds) + " ребер:")
        print(ourGraph.data)
        print("")
    print("Цикл подгона транзитивности и симметричности номер "+str(cycle))

if ourGraph.checkSymmetric() and ourGraph.checkReflexive() and ourGraph.checkTransitive():
    print("Отношение можно привести к отношениею эквивалентности "+ str(variants)+"! способами" )
    print("Итого матрица с отношением частичного порядка: ")
    print(ourGraph.data)
else:
    print("Отношение порядка не удалось.")

del ourGraph

print("Приведем к отношения линейного порядка: ")
step = 1
adds = 0
variants = 0
ourGraph = model.Graph("task1/task.txt")
print(str(step)+") Проверим свойства отношения линейного порядка: \n ",ourGraph.checkRelations())
ourGraph.makeReflexive()
variants = ourGraph.makeLinearOrder()
if variants==1:
    print("Отношение линейного порядка и так есть.")
else:
    print("Можно привести к линейному порядку "+str(variants)+" сопсобами.")
    print(ourGraph.data)
