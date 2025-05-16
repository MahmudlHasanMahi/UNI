from collections import deque
import heapq
import sys


def djikstra(matrix,s):
    dis = [float("inf")] * len(matrix)
    prev = [None] * len(matrix)
    dis[s] = 0
    q = [(0,s)]
    while q:
        wu,u = heapq.heappop(q)
        if wu > dis[u]:
            continue

        for v,wv in matrix[u]:
            if wu + wv < dis[v]:
                dis[v] = wu + wv
                heapq.heappush(q,(dis[v],v))
                prev[v] = u

    
    return dis



def main():
    v,e,x,y = map(int,input().split(" "))
    matrix = [[] for _ in range(v+1)]
    
    for _ in range(e):
        u,vv,w = map(int,input().split(" "))
        matrix[u].append((vv,w))

    if x == y:
        print(0,x)
        return
    a = djikstra(matrix,x)
    b = djikstra(matrix,y)
    

    inf = float("inf")
    node = -1
    dis = inf
 
    for i in range(v+1):
        if a[i] != inf and b[i] != inf:
            m = max(a[i],b[i])
            if m < dis:
                dis = m
                node = i
    if node == -1:
        print(-1)
    else:
        print(dis,node)

if __name__ == "__main__":
    main()