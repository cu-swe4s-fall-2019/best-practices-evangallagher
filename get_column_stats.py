import sys
import math
import argpars

def new_mean(X):
    return sum(X)/len(X)

def new_std(X):
    return math.sqrt(sum([((sum(X)/len(X))-x)**2 for x in X]) / len(X))

    try:
        test_mean(X)

    except: None:
        print 'Could not Calculate Mean'

if _name_ == . '_main_':
    unitest.main()
