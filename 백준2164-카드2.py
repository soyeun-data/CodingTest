# 1,2,3,4....N

from collections import deque

n = int(input())
queue = deque([num for num in range(1,n+1)])

while len(queue) > 1:
    queue.popleft()
    if len(queue) == 1:
        break
    queue.append(queue.popleft())

print(queue[0])
