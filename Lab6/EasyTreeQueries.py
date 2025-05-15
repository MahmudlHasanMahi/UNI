from collections import deque
import sys
sys.setrecursionlimit(10**6)
def dfs(root,matrix,visits,sizes):
    if visits[root] == 1:
        return 0
    visits[root] = 1
    c = 1
    for i in matrix[root]:
        c += dfs(i,matrix,visits,sizes)

    visits[root] = 2
    sizes[root] = c
    return c


def main():
    v,r = map(int,input().split(" "))
    matrix = [[] for _ in range(v+1)]

    sizes = [0]*(v+1)
    visits = [0] * (v+1)

    for _ in range(v-1):
        x,y = map(int,input().split(" "))
        matrix[x].append(y)
        matrix[y].append(x)

    sizes[r] = dfs(r,matrix,visits,sizes)
    for _ in range(int(input())):
        print(sizes[int(input())],end=" ")
if __name__ == "__main__":
    main()