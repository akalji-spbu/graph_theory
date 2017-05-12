# -*- coding: utf-8 -*-
import model

fname = "task1.txt"
ourGraph = model.Graph(fname)
ourGraph.makeReflexive()
ourGraph.makeTransitive()
print(ourGraph.data)
print(ourGraph.checkAntisymmetric())