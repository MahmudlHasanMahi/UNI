from collections import deque

def bipartite_graph(matrix):
    color = [0] * len(matrix)
    visited = [False] * len(matrix)

    q = deque([])
    res = 0
    for k in range(1,len(matrix)):
        if visited[k]:
            continue
        count = [0,0]
        visited[k] = True
        color[k] = 1
        count[color[k]] += 1
        q.append(k)

        while q:
            node = q.popleft()
            for adj in matrix[node]:
                if not visited[adj]:
                    color[adj] = 1 - color[node]
                    count[color[adj]] += 1
                    visited[adj]= True
                    q.append(adj)
        res += max(count)
    return res

def main():
    v,e = map(int,input().split(" "))
    matrix = [[] for _ in range(v+1)]
    
    for _ in range(e):
        x,y = map(int,input().split(" "))
        matrix[x].append(y)
        matrix[y].append(x)
    
    print(bipartite_graph(matrix))


if __name__ == "__main__":
    main()