from collections import deque
import sys

sys.setrecursionlimit(10**6)

def bfs(matrix,root):
    visits = [False] * len(matrix)
    distance = [0] * len(matrix)
    q = deque([root])
    visits[root] = True

    while q:
        node = q.popleft()
        for i in matrix[node]:
            if not visits[i]:
                distance[i] += 1 + distance[node]
                visits[i] = True
                q.append(i)

    node = root
    m = 0

    for i in range(1,len(distance)):
        if distance[i] > m:
            node = i
            m = distance[i]

    return node,m


def main():
    n = int(input())
    matrix = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x,y = map(int,input().split(" "))
        matrix[x].append(y)
        matrix[y].append(x)
    node1,m = bfs(matrix,1)
    node2, n = bfs(matrix,node1)
    print(n)
    print(node1,node2)


if __name__ == "__main__":
    main()