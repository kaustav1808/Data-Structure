#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bfs function below.
def bfs(n, m, edges, s):
    adjacencyList = initAdjacencyList(n,edges)
    visited = dict.fromkeys(range(1,n+1),False)
    weight  = dict.fromkeys(range(1,n+1),-1)
    queue = []
    weight[s] = 0
    
    queue.append(s)
    
    while len(queue):
        processed = queue.pop(0)
        for i in adjacencyList[processed]:
            if not visited[i]:
                visited[i] = True
                weight[i] = weight[processed] + 6   
                queue.append(i)        
    weight.pop(s) 
    return weight.values()           
                

def initAdjacencyList(n,edges):
    adjacencyList = dict((key,[]) for key in range(1,n+1))
    
    for i,j in edges:
        if i not in adjacencyList[j]:
            adjacencyList[j].append(i) 
        if j not in adjacencyList[i]:
            adjacencyList[i].append(j) 
    return adjacencyList               

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
