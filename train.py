#!/usr/bin/python3    
import cmath
import string
import time
import random
import csv
import json
import math
import numpy as np
import os
import math
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import metrics #metrics.confusion_matrix, metrics.accuracy_score, metrics.precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score 
from sklearn.model_selection import train_test_split



labels = []
matrix = []


def accuracy(mat, lab):
    print("Accuracy:",accuracy_score(lab, mat))

def confusion(mat, lab):
    print(confusion_matrix(lab, mat))

def precision(mat, lab):
    print("Precision:",precision_score(lab, mat,average='macro'))

 
# with open("rad_d1_train.txt", 'r') as f:
#     for line in f:
#         words = line.split()
#         temp = []

#         for i in words:
#             if(i[0] == 'a'):
#                 labels.append(i[0]+i[1]+i[2])
#             else:
#                 temp.append(float(i))
#                 # temp.append(i)
#             #print(i[0])
      
#         matrix.append(temp)


# matrix.pop(0)


def rad_train():
    with open("rad_d1_train.txt", 'r') as f:

        for line in f:
            words = line.split()
            temp = []

            for i in words:
                if(i[0] == 'a'):
                    labels.append(i[0]+i[1]+i[2])
                else:
                    temp.append(float(i))
                    # temp.append(i)
            #print(i[0])
      
            matrix.append(temp)

    
    clf = svm.SVC(kernel='linear', C=0.000023455) 
    clf.fit(matrix, labels)
    var = clf.predict(matrix)

    accuracy(var, labels)
    precision(var, labels) 
    confusion(var, labels)
    print()

    ###############
    clf = svm.SVC(kernel='poly', C=.00000004348354333) 
    clf.fit(matrix, labels)
    var = clf.predict(matrix)

    accuracy(var, labels)
    precision(var, labels)
    confusion(var, labels)
    print()

    ###############
    clf = svm.SVC(kernel='rbf', C=.00000000000000000000000000000000000000000434835433324546743694325623465436543654643656232276487) 
    clf.fit(matrix, labels)
    var = clf.predict(matrix)

    accuracy(var, labels)
    precision(var, labels)
    confusion(var, labels)
    print()

    labels.clear()
    matrix.clear()


def rad_test():
    with open("rad_d1_test.txt", 'r') as f:

        for line in f:
            words = line.split()
            temp = []

            for i in words:
                if(i[0] == 'a'):
                    labels.append(i[0]+i[1]+i[2])
                else:
                    temp.append(float(i))
                    # temp.append(i)
            #print(i[0])
      
            matrix.append(temp)

    
    # print(len(matrix))
    #print(matrix)
  

    #print(len(matrix))
    
    clf = svm.SVC(kernel='linear', C=0.000023455) 
    clf.fit(matrix, labels)
    var = clf.predict(matrix)

    accuracy(var, labels)
    precision(var, labels) 
    confusion(var, labels)
    print()

    ###############
    clf = svm.SVC(kernel='poly', C=.00000004348354333) 
    clf.fit(matrix, labels)
    var = clf.predict(matrix)

    accuracy(var, labels)
    precision(var, labels)
    confusion(var, labels)
    print()

    ###############
    clf = svm.SVC(kernel='rbf', C=.00000000000000000000000000000000000000000434835433324546743694325623465436543654643656232276487) 
    clf.fit(matrix, labels)
    var = clf.predict(matrix)

    accuracy(var, labels)
    precision(var, labels)
    confusion(var, labels)
    print()

    labels.clear()
    matrix.clear()

def custom_train():
    with open("cust_d1_train.txt", 'r') as f:

        for line in f:
            words = line.split()
            temp = []

            for i in words:
                if(i[0] == 'a'):
                    labels.append(i[0]+i[1]+i[2])
                else:
                    temp.append(float(i))
                    # temp.append(i)
            #print(i[0])
      
            matrix.append(temp)

    
    clf = svm.SVC(kernel='linear', C=0.000023455) 
    clf.fit(matrix, labels)
    var = clf.predict(matrix)

    accuracy(var, labels)
    precision(var, labels) 
    confusion(var, labels)
    print()

    ###############
    clf = svm.SVC(kernel='poly', C=.00000004348354333) 
    clf.fit(matrix, labels)
    var = clf.predict(matrix)

    accuracy(var, labels)
    precision(var, labels)
    confusion(var, labels)
    print()

    ###############
    clf = svm.SVC(kernel='rbf', C=.00000000000000000000000000000000000000000434835433324546743694325623465436543654643656232276487) 
    clf.fit(matrix, labels)
    var = clf.predict(matrix)

    accuracy(var, labels)
    precision(var, labels)
    confusion(var, labels)
    print()

    labels.clear()
    matrix.clear()

def custom_test():
    with open("cust_d1_test.txt", 'r') as f:

        for line in f:
            words = line.split()
            temp = []

            for i in words:
                if(i[0] == 'a'):
                    labels.append(i[0]+i[1]+i[2])
                else:
                    temp.append(float(i))
                    # temp.append(i)
            #print(i[0])
      
            matrix.append(temp)



    
    clf = svm.SVC(kernel='linear', C=0.000023455) 
    clf.fit(matrix, labels)
    var = clf.predict(matrix)

    accuracy(var, labels)
    precision(var, labels) 
    confusion(var, labels)
    print()

    ###############
    clf = svm.SVC(kernel='poly', C=.00000004348354333) 
    clf.fit(matrix, labels)
    var = clf.predict(matrix)

    accuracy(var, labels)
    precision(var, labels)
    confusion(var, labels)
    print()

    ###############
    clf = svm.SVC(kernel='rbf', C=.00000000000000000000000000000000000000000434835433324546743694325623465436543654643656232276487) 
    clf.fit(matrix, labels)
    var = clf.predict(matrix)

    accuracy(var, labels)
    precision(var, labels)
    confusion(var, labels)
    print()

    labels.clear()
    matrix.clear()

print("RAD train: ")
rad_train()
print("RAD test: ")
rad_test()

print("Custom train: ")
custom_train()
print("Custom test: ")
custom_test()

# clf = svm.SVC(kernel='linear', C=0.000023455) 
# clf.fit(matrix, labels)
# var = clf.predict(matrix)

# accuracy(var, labels)
# precision(var, labels) 
# confusion(var, labels)
# print()

# ###############
# clf = svm.SVC(kernel='poly', C=.00000004348354333) 
# clf.fit(matrix, labels)
# var = clf.predict(matrix)

# accuracy(var, labels)
# precision(var, labels)
# confusion(var, labels)
# print()

# ###############
# clf = svm.SVC(kernel='rbf', C=.00000000000000000000000000000000000000000434835433324546743694325623465436543654643656232276487) 
# clf.fit(matrix, labels)
# var = clf.predict(matrix)

# accuracy(var, labels)
# precision(var, labels)
# confusion(var, labels)
# print()



