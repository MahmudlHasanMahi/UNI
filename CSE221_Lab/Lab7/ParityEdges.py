from collections import deque
import heapq
import sys


def djikstra(matrix,s,d):
    dis = [[float("inf")]*2 for i in range(len(matrix))] 
    dis[s][0]=dis[s][1] = 0
    q = [(0,s,-1)]

    while q:
        wu,u,p = heapq.heappop(q)
        if wu > dis[u][p]:
            continue
        for v,wv in matrix[u]:
            parity = wv %2;
            if wv+wu < dis[v][parity] and parity != p:
                dis[v][parity] = wv+wu
                heapq.heappush(q,(dis[v][parity],v,parity))
    ans = min(dis[d])
    return -1 if ans == float("inf") else ans



def main():
    ver,e = map(int,input().split(" "))
    matrix = [[] for _ in range(ver+1)]
    v = input().split(" ")
    u = input().split(" ")
    w = input().split(" ")

    for i in range(e):
        matrix[int(v[i])].append((int(u[i]),int(w[i])))
    
    a = djikstra(matrix,1,ver)
    print(a)



       

    
    
   
   

if __name__ == "__main__":
    main()