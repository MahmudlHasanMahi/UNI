from collections import deque
import heapq
import sys
def printPath(arr,x):
    if x == None:
        return 
    printPath(arr,arr[x])
    print(x,end=" ")

def djikstra(matrix,s,d):
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

    if s == d:
        print(0)
        print(s)
    elif prev[d] == None:
        print(-1)
    else:
        print(dis[d])
        printPath(prev,d)
    



def main():
    v,e,s,d = map(int,input().split(" "))

    a = input().split(" ")
    b = input().split(" ")
    w = input().split(" ")

    matrix = [[]for _ in range(v+1)]

    for i in range(e):
        matrix[int(a[i])].append((int(b[i]),int(w[i])))
    djikstra(matrix,s,d)



if __name__ == "__main__":
    main()