#!/bin/python

import math
import os
import random
import re
import sys
import itertools
import array

# Complete the climbingLeaderboard function below.

def climbingLeaderboard(scores, alice):
    #get the scores in order
    d = sorted(list(set(scores)))
    #get total amount of values
    a = len(d)
    #create an array
    b = []
    #set a base comparison value
    c = 0

    # iterate with placeholder, i like k, for each value in her submission
    for k in alice:
        # until base = total and iterated value equal or less than sorted last value  
        while (a > c and k >= d[c]):
            #add a step to base
            c += 1
        #add to the empty array total+1-iteration (known commodity two directions right)
        b.append(a+1-c)
    #return our values 
    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    alice_count = int(raw_input())

    alice = map(int, raw_input().rstrip().split())

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()