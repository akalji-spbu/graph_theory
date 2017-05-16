import core
import model
import graphs

fname = "task3/task.txt"
ourGraph = model.Graph(fname)
ourGraph.makeTransitive()

print(ourGraph.data)