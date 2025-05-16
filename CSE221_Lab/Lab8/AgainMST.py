import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(u, v):
    rootU = find(u)
    rootV = find(v)
    if rootU == rootV:
        return False
    if rank[rootV] > rank[rootU]:
        rootU, rootV = rootV, rootU
    if rank[rootU] == rank[rootV]:
        rank[rootU] += 1
    parent[rootV] = rootU
    return True


N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
edges = sorted(enumerate(edges), key=lambda x: x[1][2])  


parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)
mst_indices = []
mst_weight = 0

for idx, (u, v, w) in edges:
    if union(u, v):
        mst_indices.append(idx)
        mst_weight += w

if len(mst_indices) != N - 1:
    print(-1)
    exit()

result = float('inf')


for skip_idx in mst_indices:
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    weight = 0
    count = 0
    for idx, (u, v, w) in edges:
        if idx == skip_idx:
            continue
        if union(u, v):
            weight += w
            count += 1
    if count == N - 1 and weight > mst_weight:
        result = min(result, weight)


non_mst_indices = set(range(M)) - set(mst_indices)

for include_idx in non_mst_indices:
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    u, v, w = edges[include_idx][1]
    if not union(u, v):
        continue
    weight = w
    count = 1
    for idx, (a, b, c) in edges:
        if idx == include_idx:
            continue
        if union(a, b):
            weight += c
            count += 1
    if count == N - 1 and weight > mst_weight:
        result = min(result, weight)

print(result if result != float('inf') else -1)