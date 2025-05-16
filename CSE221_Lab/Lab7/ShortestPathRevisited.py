from collections import deque
import heapq
import sys


def djikstra(matrix,s,d):
    dis = [[float("inf")]*2 for i in range(len(matrix))] 
    dis[s][0] = 0
    q = [(0,s)]

    while q:
        wu,u= heapq.heappop(q)
        if wu > dis[u][1]:
            continue
        for v,wv in matrix[u]:
            cost = wv+wu
            if cost < dis[v][0]:
                dis[v][1] = dis[v][0]
                dis[v][0] = cost
                heapq.heappush(q,(cost,v))
            elif dis[v][0]< cost < dis[v][1]:
                dis[v][1] = cost
                heapq.heappush(q,(cost,v))
    return -1 if dis[d][1] == float("inf") else dis[d][1]


def main():
    ver,e,s,d = map(int,input().split(" "))
    matrix = [[] for _ in range(ver+1)]
    for _ in range(e):
        x,y,z = map(int,input().split(" "))
        matrix[x].append((y,z))
        matrix[y].append((x,z)) 
    print(djikstra(matrix,s,d))



       

    
    
   
   

if __name__ == "__main__":
    main()