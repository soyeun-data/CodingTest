from collections import deque

n, m = map(int, input().split())

x = [1,-1,0,0]
y = [0,0,-1,1]

check = [[0]*m for _ in range(n)]
campus = [list(input()) for _ in range(n)]
queue = deque()
cnt = 0

for row in range(n):
    for column in range(m):
        if campus[row][column] == "I":
            queue.append([row,column])
        elif campus[row][column] == "X":
            check[row][column] = 1

while queue:
    nx, ny = queue.popleft()

    for i in range(4):
        dx = nx + x[i]
        dy = ny + y[i]

        if dx >= 0 and dx < n and dy >= 0 and dy < m:
            if check[dx][dy] == 0:
                check[dx][dy] = 1
                queue.append([dx,dy])
                if campus[dx][dy] == 'P':
                    cnt += 1

if cnt == 0:
    print("TT")
else:
    print(cnt)