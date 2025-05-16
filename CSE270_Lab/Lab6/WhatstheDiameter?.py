from collections import deque
import heapq
import sys

sys.setrecursionlimit(10**6)

def topsort(matrix,indeg):
    heap = []
    for k,v in indeg.items():
        if v == 0:
            heapq.heappush(heap,k)

    result = []
    while heap:
        node = heapq.heappop(heap)
        result.append(node)
        for adj in matrix[node]:
            indeg[adj] -= 1
            if indeg[adj] == 0:
                heapq.heappush(heap,adj)
    
    if len(result) != len(indeg.keys()):
        print(-1)
    else:
        print("".join(result))


def main():
    
    n = int(input())
    words = [input().strip() for _ in range(n)]
    
    adj = {c:[] for w in words for c in w}
    indeg = {c:0 for w in words for c in w}

    for i in range(n-1):
        word1,word2 = words[i],words[i+1]
        m = min(len(word1),len(word2))
        flag = False
        for j in range(m):
            if word1[j] != word2[j]:
                adj[word1[j]].append(word2[j])
                indeg[word2[j]]+=1
                flag = True
                break
        if not flag and len(word1) > len(word2):
            print(-1)
            return 
    topsort(adj,indeg)



if __name__ == "__main__":
    main()