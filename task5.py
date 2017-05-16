import model
import core
import pyeda.inter as bo

ourGraph = model.Graph("task5/task.txt")
print(ourGraph.data)

print("Внутренняя устойчивость. Построим ДНФ:")
A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z = map(bo.exprvar, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

letters = {
    0:A,
    1:B,
    2:C,
    3:D,
    4:E,
    5:F,
    6:G,
    7:H,
    8:I,
    9:J,
    10:K,
    11:L,
    12:M,
    13:N,
    14:O,
    15:P,
    16:Q,
    17:R,
    18:S,
    19:T,
    20:U,
    21:V,
    22:W,
    23:X,
    24:Y,
    25:Z
}

i=0
function = True
while i<ourGraph.m:
    j=0
    while j<ourGraph.n:
        if ourGraph.data[i][j]!=0:
            function = bo.And(function,bo.Or(letters[i],letters[j]))
        j+=1
    i+=1

print(function)
print(function.to_dnf())

print("Внешняя устойчивость. Построим ДНФ:")
A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z = map(bo.exprvar, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

letters = {
    0:A,
    1:B,
    2:C,
    3:D,
    4:E,
    5:F,
    6:G,
    7:H,
    8:I,
    9:J,
    10:K,
    11:L,
    12:M,
    13:N,
    14:O,
    15:P,
    16:Q,
    17:R,
    18:S,
    19:T,
    20:U,
    21:V,
    22:W,
    23:X,
    24:Y,
    25:Z
}

ourGraph = model.Graph("task5/task.txt")
ourGraph.makeReflexive()

i=0
function = True
while i<ourGraph.m:
    subfunction = False
    j=0
    while j<ourGraph.n:
        if ourGraph.data[i][j]!=0:
            subfunction = bo.Or(subfunction,letters[j])
        j+=1
    if not subfunction:
        subfunction = True

    function = bo.And(function, subfunction)
    i+=1


print(function)
print(function.to_dnf())

