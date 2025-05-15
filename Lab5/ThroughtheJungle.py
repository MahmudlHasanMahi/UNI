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
    parent = [-1] *len(matrix)
    dis = [-1] * len(matrix)
    q = deque([s])
    dis[s] = 0
    while q :
        node = q.popleft()
        for i in matrix[node]:
            if dis[i] == -1:
                dis[i]  = dis[node]+1
                parent[i] = node
                q.append(i)
               
    return dis[d],parent


def main():
    v,e,a,b,c = map(int,input().split(" "))

    matrix = [[] for _ in range(v+1)]
   
    for _ in range(e):
        x,y = map(int,input().split(" "))
        matrix[x].append(y)

    dis1,path1 = bfs(matrix,a,c)
    dis2,path2 = bfs(matrix,c,b)
    if dis1 !=-1 and dis2 !=-1:
        print(dis1+dis2)
        rec(path1,c)
        # print(c,end=" ")
        rec(path2,b)
        print(b,end=" ")
    else:
        print(-1)
    


if __name__ == "__main__":
    main()