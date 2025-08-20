# BFS => 시간 초과

from collections import deque

n = int(input())
min_cnt = 10**6
visited = [0]*(n+1)
queue = deque()
queue.append((n,0))
visited[n] = 1

while(queue):
    num, temp_cnt = queue.popleft()

    if temp_cnt >= min_cnt:
        continue

    if num == 1:
        min_cnt = min(min_cnt, temp_cnt)
        continue
    
    if num % 3 == 0 and visited[num//3] == 0:
        queue.append((num//3, temp_cnt+1))
        visited[num//3] = 1
    if num % 2 == 0 and visited[num//2] == 0:
        queue.append((num//2, temp_cnt+1))
        visited[num//2] = 1
    if not visited[num-1]:
        queue.append((num-1, temp_cnt+1))
        visited[num-1] = 1

print(min_cnt)