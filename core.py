# -*- coding: utf-8 -*-
import model
import numpy


def normalise(matrix):
    resmat = []
    for line in matrix:
        preres = []
        for col in line:
            if col == 0:
                preres.append(0)
            else:
                preres.append(1)
        resmat.append(preres)


    return numpy.matrix(resmat)

def boolease(matrix):
    resmat = []
    for line in matrix:
        preres = []
        for col in line:
            if col == 0:
                preres.append(False)
            else:
                preres.append(True)
        resmat.append(preres)


    return numpy.matrix(resmat)

small_letters = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
    6:"f",
    7:"j",
    8:"h",
    9:"i",
    10:"j",
    11:"k",
    12:"l",
    13:"m",
    14:"n",
    15:"o",
    16:"p",
    17:"q",
    18:"r",
    19:"s",
    20:"t",
    21:"u",
    22:"v",
    23:"w",
    24:"x",
    25:"y",
    26:"z"
}

big_letters = {
    0:"A",
    1:"B",
    2:"C",
    3:"D",
    4:"E",
    5:"F",
    6:"G",
    7:"H",
    8:"I",
    9:"J",
    10:"K",
    11:"L",
    12:"M",
    13:"N",
    14:"O",
    15:"P",
    16:"Q",
    17:"R",
    18:"S",
    19:"T",
    20:"U",
    21:"V",
    22:"W",
    23:"X",
    24:"Y",
    25:"Z"
}