import sys
import heapq
from collections import deque

def bfs(matrix):
    visited= [0] * len(matrix)

    q = deque([1])
    visited[1] = 1
    while q:
        node = q.popleft()
        print(node,end=" ")
        for i in matrix[node]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    

def main():
    v,e = map(int,input().split(" "))
    matrix = [[] for _ in range(v+1)]
    for _ in range(e):
        x,y = map(int,input().split(" "))
        matrix[x].append(y)
        matrix[y].append(x)
    bfs(matrix)

    



    

if __name__ == "__main__":
    main()