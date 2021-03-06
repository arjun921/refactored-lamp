#!/bin/python3
# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0]*n
    for q in queries:
        x, y, incr = q[0],q[1],q[2]
        array[x-1] += incr
        # if((y)<=len(array)-1): array[y] -= incr
    print(array)
    return max(array)

if __name__ == '__main__':
    fopen = open('in_large-prob2.txt','r')
    txt = fopen.read()
    fopen.close()
    txt = txt.split('\n')
    large_nm = list(map(int,txt[0].split()))
    large_queries = []

    for _ in txt[1:]:
        large_queries.append(list(map(int,_.split())))

    tests = {
        'case1': {
            'nm': [4,3],
            'queries': [[2,3,603],[1,1,286],[4,4,882]],
            'expected': 882
        },
        'case2': {
            'nm': [10,4],
            'queries': [[2,6,8],[3,5,7],[1,8,1],[5,9,15]],
            'expected': 31
        },
        'case3': {
            'nm': [5,3],
            'queries': [[1,2,100],[2,5,100],[3,4,100]],
            'expected': 200
        },
        'case4': {
            'nm': [10,3],
            'queries': [[1,5,3],[4,8,7],[6,9,1]],
            'expected': 10
        },
        # 'case5': {
        #     'nm': large_nm,
        #     'queries': large_queries,
        #     'expected': 2497169732
        # }
    }

    # nm = input().split()
    # n = int(nm[0])
    # m = int(nm[1])
    # queries = []

    # for _ in range(m):
    #     queries.append(list(map(int, input().rstrip().split())))

    
    # n = 10
    # m = 4
    # queries = [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]

    for test in tests.items():
        print(test[0])
        nm = test[1]['nm']
        n = nm[0]
        m = nm[1]
        queries = test[1]['queries']
        expected = test[1]['expected']
        result = arrayManipulation(n, queries)
        if result == expected:
            print('Test passed')
        else:
            print(test)
            print('Test failed')
        print('-'*10)

