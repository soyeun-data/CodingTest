# 1. A의 값을 DSLR을 적용한 값을 queue에 넣기

from collections import deque
import sys

n = int(input())

for _ in range(n):
    queue = deque()
    a, b = map(int,sys.stdin.readline().rstrip().split())
    queue.append(['',a])
    visited = [0]*10001
    visited[a] = 1

    while queue:
        temp_str , num = queue.popleft()

        if num == b:
            print(temp_str)
            break
        d = (num * 2) % 10000
        if visited[d] == 0:
            visited[d] = 1
            queue.append([temp_str+'D',d])

        s = (num-1) % 10000
        if visited[s] == 0:
            visited[s] = 1
            queue.append([temp_str+'S',s])

        l = num//1000 + (num%1000)*10
        if visited[l] == 0:
            visited[l] = 1
            queue.append([temp_str+'L',l])

        r = num//10 + (num % 10)*1000
        if visited[r] == 0:
            visited[r] = 1
            queue.append([temp_str+'R',r])
        