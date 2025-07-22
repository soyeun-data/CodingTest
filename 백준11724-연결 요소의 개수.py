import sys

def dfs(num):
    visited[num] = True

    for k in graph[num]:
        if visited[k] == False:
            dfs(k)

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

cnt = 0
for j in range(1, n+1):
    if visited[j] == False:
        cnt += 1
        dfs(j)

print(cnt)