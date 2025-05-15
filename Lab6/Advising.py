from collections import deque

def topsort(v,matrix,parents):
    q = deque()   
    for i in range(1,len(parents)):
        if parents[i] == 0:
            q.append(i)
    res = []
    while q:
        node = q.popleft()
        res.append(str(node))
        for adj in matrix[node]:
            parents[adj] -= 1;    
            if parents[adj] == 0:
                q.append(adj)
    
    if len(res) == v:
        print(" ".join(res))
    else:
        print(-1)
def main():
    v,e = map(int,input().split(" "))
    matrix = [[] for _ in range(v+1)]
    parents = [0] * (v+1)
    
    for _ in range(e):
        x,y = map(int,input().split(" "))
        matrix[x].append(y)
        parents[y]+=1

    topsort(v,matrix,parents)


if __name__ == "__main__":
    main()