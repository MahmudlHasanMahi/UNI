from collections import deque
import heapq
import sys
sys.setrecursionlimit(10**6)
def find(x,parent):
    if parent[x] != x:
        parent[x] = find(parent[x],parent)
    return parent[x]

def main():
    n,m = map(int,input().split(" "))
    matrix= []
    parent = [i for i in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split(" "))
        matrix.append((w,u,v))
    matrix.sort()
 
    cost = 0
    for w,u, v in matrix:
        rootU = find(u,parent)
        rootV = find(v,parent)
        if rootU != rootV:
            parent[rootV] = rootU
            cost += w
    print(cost)
        

if __name__ == "__main__":
    main()