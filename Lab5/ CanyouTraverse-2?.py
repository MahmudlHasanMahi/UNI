import sys
import heapq
from collections import deque

sys.setrecursionlimit(2*100000+5)

def bfs(matrix,i,visited):
    if visited[i]:
        return
    print(i,end=" ")
    visited[i] = True
    for j in matrix[i]:
        if not visited[j]:
            bfs(matrix,j,visited)



def main():
    v,e = map(int,input().split(" "))

    matrix = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    arr1 = list(map(int,input().split(" ")))
    arr2 = list(map(int,input().split(" ")))
    for i in range(e):
        matrix[arr1[i]].append(arr2[i])
        matrix[arr2[i]].append(arr1[i])
    for i in range(1,v+1):
        if not visited[i]:
            bfs(matrix,i,visited)



if __name__ == "__main__":
    main()