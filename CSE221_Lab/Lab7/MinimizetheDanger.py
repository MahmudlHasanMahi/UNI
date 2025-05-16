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
            highest = max(wv,wu)

            if highest < dis[v]:
                dis[v] = highest
                heapq.heappush(q,(dis[v],v))
                prev[v] = u

    
    return dis



def main():
    v,e = map(int,input().split(" "))
    matrix = [[] for _ in range(v+1)]
    
    for _ in range(e):
        u,vv,w = map(int,input().split(" "))
        matrix[u].append((vv,w))
        matrix[vv].append((u,w))

    dis = djikstra(matrix,1)
    for i in range(1,v+1):
        if dis[i] == float("inf"):
            print(-1,end=" ")
        else:
            print(dis[i],end=" ")
    
   
   

if __name__ == "__main__":
    main()