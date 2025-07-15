# 0,0 부터 시작 
# 상하좌우 확인
# 1이면 큐에 넣어
from collections import deque

t = int(input())

x = [-1,1,0,0]
y = [0,0,-1,1]

for _ in range(t):
    m,n,k = map(int, input().split())

    cabbage = [[0]*m for _ in range(n)]
    check = [[0]*m for _ in range(n)]
    queue = deque()
    cnt = 0

    for i in range(k):
        cabbage_y,cabbage_x = map(int, input().split())
        cabbage[cabbage_x][cabbage_y] = 1

    for a in range(n):
        for b in range(m):
            if check[a][b] == 0 and cabbage[a][b] == 1:
                queue.append([a,b])
                cnt += 1
            
            while queue:
                temp_x, temp_y = queue.popleft()
                
                for c in range(4):
                    dx = temp_x + x[c]
                    dy = temp_y + y[c]

                    if 0 <= dx and dx < n and 0 <= dy and dy < m:
                        if check[dx][dy] == 0:
                            check[dx][dy] = 1
                            if cabbage[dx][dy] == 1:
                                queue.append([dx,dy])
    print(cnt)