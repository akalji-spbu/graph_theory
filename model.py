# -*- coding: utf-8 -*-
import numpy
import core

from scipy.sparse.csgraph import floyd_warshall

class Graph():
    data = []
    m = 0
    n = 0

    def __init__(self, fname):
        self.data = numpy.genfromtxt(fname,delimiter=" ")
        self.m, self.n = self.data.shape

    def checkRelations(self):
        result = {
            "Рефлексивность": self.checkReflexive(),
            "Антирефлексивность": self.checkIrreflexive(),
            "Симметричность": self.checkSymmetric(),
            "Антисимметричность": self.checkAntisymmetric(),
            "Транзитивность": self.checkTransitive()
        }
        return result

    def checkReflexive(self):
        diag = numpy.diagonal(self.data)
        result = True
        for n in diag:
            result = result*(n != 0)

        return result

    def checkIrreflexive(self):
        diag = numpy.diagonal(self.data)
        result = True
        for n in diag:
            result = result*(n == 0)
        return result

    def checkSymmetric(self):
        return numpy.allclose(self.data, self.data.T)

    def checkAntisymmetric(self):
        pre = self.data*self.data.T
        i=0
        while i<self.m:
            pre[i][i]=0
            i=i+1
        return numpy.allclose(pre,numpy.zeros(self.data.shape))

    def checkTransitive(self):
        sum = self.data
        prepow = self.data

        i=1
        while i<self.m:
            prepow = numpy.dot(prepow,self.data)
            sum = sum+prepow
            i=i+1

        nsum = core.normalise(sum)
        ndata = core.normalise(self.data)

        return numpy.allclose(nsum, ndata)

    def makeReflexive(self):
        i = 0
        adds = 0
        while i < self.m:
            if self.data[i][i]==0:
                self.data[i][i] = 1
                adds = adds+1
            i=i+1
        return adds

    # def makeTransitive(self):
    #     sum = self.data
    #     prepow = self.data
    #
    #     i=1
    #
    #     nsum = core.normalise(sum)
    #     ndata = core.normalise(self.data)
    #     bdata = core.boolease(self.data)
    #     bdot = numpy.dot(bdata, bdata)
    #
    #     powlist = []
    #     powlist.append(bdata)
    #
    #     sum = powlist[0]
    #
    #     for i in range(1,self.m):
    #         powlist.append(numpy.dot(powlist[i-1],bdata))
    #         sum+=powlist[i]
    #     tsum = sum.T
    #     s = numpy.multiply(sum, tsum)+core.boolease(numpy.eye(self.m))
    #     print(s)

    def makeTransitive(self):
        tc = floyd_warshall(self.data)
        i=0
        adds=0
        while i<self.m:
            j = 0
            while j < self.n:
                if tc[i][j]==float("inf"):
                    self.data[i][j]=0
                else:
                    if self.data[i][j]==0:
                        adds = adds + 1
                    self.data[i][j] = 1
                j=j+1
            i=i+1
        return adds

    def makeSymmetric(self):
        i = 0
        adds = 0
        while i < self.m:
            j=0
            while j< self.n:
                if self.data[i][j]==1:
                    self.data[j][i] = 1
                    adds = adds+1
                j=j+1
            i=i+1

        variants = 1
        i=0
        while i < self.m:
            j = i+1
            while j < self.n:
                if self.data[i][j]==0:
                    print(i,j)
                    variants+=1
                j+=1
            i+=1
        return adds, variants

    def makeLinearOrder(self):
        variants = 1
        i = 0
        while i < self.m:
            j = i+1
            print("Варианты добавления вершин до линейного порядка:")
            while j < self.n:
                if (self.data[i][j]+self.data[j][i]==0 and i!=j):
                    self.data[i][j] = 1
                    variants=variants*3
                    print(i,j)
                    print(j,i)
                    print()
                j+=1
            i+=1
        return variants
