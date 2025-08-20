# dfs

def dfs(n):
    if check[n] == 0:
        check[n] = 1
        for j in com_line[n]:
            dfs(j)
    else:
        return

com_n = int(input())
line = int(input())

com_line = [[] for _ in range(com_n+1)]
check = [0]*(com_n+1)

for i in range(line):
    start, end = map(int,input().split())
    com_line[start].append(end)
    com_line[end].append(start)

dfs(1)
print(sum(check)-1)