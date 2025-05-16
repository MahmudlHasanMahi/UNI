import sys
import heapq
from collections import deque


def pathPrint(arr,x):
    if x == None:
        return 
    pathPrint(arr,arr[x])
    print(x,end=" ")
 
def Dijkstra(matrix,weight,s):
    d = [float("inf")] * len(matrix)
    minheap = [(weight[s-1],s)]
    d[s] = weight[s-1]
    while minheap:
        pw,n = heapq.heappop(minheap)
        if pw > d[n]:
            continue
        for adj in matrix[n]:
            if d[n] + weight[adj-1] < d[adj]:
                d[adj] = d[n]+weight[adj-1]
                heapq.heappush(minheap,(d[adj],adj)) 
    return d

def main():
    v,e,s,d = map(int,input().split(" "))
    weight = list(map(int,input().split(" ")))
    matrix = [[] for _ in range(v+1)]

    for _ in range(e):
        x,y= map(int,input().split(" "))
        matrix[x].append(y)
    x = Dijkstra(matrix,weight,s)   
    if x[d] == float("inf"):
        print(-1)
    else:
        print(x[d])
    

    



if __name__ == "__main__":
    main()