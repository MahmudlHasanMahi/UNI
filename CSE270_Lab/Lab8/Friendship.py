from collections import deque
import heapq
import sys
sys.setrecursionlimit(10**6)
def find(x,parent):
    if parent[x] != x:
        parent[x] = find(parent[x],parent)
    return parent[x]

def main():
    n,k = map(int,input().split(" "))
    parent = [i for i in range(n+1)]
    size = [1] * (n + 1)
    for _ in range(k):
        a, b = map(int,input().split(" "))
        f1 = find(a,parent)   
        f2 = find(b,parent)

        if f1 != f2:
            parent[f2] = f1  
            size[f1] += size[f2]  
            size[f2] = 0

        print(size[f1])

if __name__ == "__main__":
    main()