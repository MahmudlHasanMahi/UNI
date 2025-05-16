import sys
import heapq
from collections import deque

sys.setrecursionlimit(2*100000+5)



def hasCycle(matrix,node,visited):
    
    if visited[node] == 1:
        return True
    if visited[node] == 2:
        return False
    visited[node] = 1
    for i in matrix[node]:
        if hasCycle(matrix,i,visited):
            return True
    visited[node] = 2
    return False
            


def main():
    v,e = map(int,input().split(" "))

    matrix = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for _ in range(e):
        x,y = map(int,input().split(" "))
        matrix[x].append(y)

    for i in range(1,v+1):
        if visited[i] == 0:
            if hasCycle(matrix,i,visited):
                print("YES")
                return 
    
    print("NO")

            


    
    


if __name__ == "__main__":
    main()