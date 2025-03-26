from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
result = []

while queue:
    queue.rotate(-(k-1))
    result.append(queue.popleft())

print('<', end='')
for i in range(n-1):
    print(result[i], end=', ')

print(result[n-1],end='')
print('>',end="")