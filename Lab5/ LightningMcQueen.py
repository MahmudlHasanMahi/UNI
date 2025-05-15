import sys
import heapq
from collections import deque

sys.setrecursionlimit(2*100000+5)

def rec(path,x):
    if path[x] == -1:
        return 
    rec(path,path[x])
    print(path[x],end=" ")


def bfs(matrix,s,d):
    path = [-1] * len(matrix)
    length = [-1] * len(matrix)
    q = deque([s])

    length[s] = 0
    while q and length[d] == -1:
        node = q.popleft()
        matrix[node].sort()

        for i in matrix[node]:
            if length[i] == -1:
                length[i] = length[node] + 1
                path[i] = node;
                q.append(i)
                if i == d:
                    break
    
    print(length[d])
    if length[d] != -1:
        rec(path,d)
        print(d)
    
    

def main():
    v,e,s,d = map(int,input().split(" "))

    matrix = [[] for _ in range(v+1)]
    arr1 = input().split(" ")
    arr2 = input().split(" ")
    for i in range(e):
        matrix[int(arr1[i])].append(int(arr2[i]))
        matrix[int(arr2[i])].append(int(arr1[i]))
  
    
    bfs(matrix,s,d)


if __name__ == "__main__":
    main()