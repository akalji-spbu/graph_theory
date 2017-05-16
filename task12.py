import model
import core
import pyeda.inter as bo


ourGraph = model.Graph("task12/task.txt")
ourGraph.makeTransitive()
print(ourGraph.data)