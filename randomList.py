#! /usr/bin/env python

import sys
import random

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'Error! please print like this : ./randomList.py 5 3'
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        #print n,m
        if m > n:
            print 'Input error,the first number must large than or equal to the second number'
        else:
            originList = range(1,n+1)
            randomList = []
            for i in range(m):
                x = random.randint(1,len(originList))       
                randomList.append(originList[x - 1])
                originList.remove(originList[x - 1]) 
            else:
                randomList.sort()
                print randomList
