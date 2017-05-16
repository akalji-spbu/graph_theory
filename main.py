# -*- coding: utf-8 -*-
import model

fname = "task1/task.txt"
ourGraph = model.Graph(fname)
ourGraph.makeTransitive()
print(ourGraph.data)