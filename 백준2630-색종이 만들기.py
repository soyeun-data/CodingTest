# 마무리는 어떻게? 모든 수의 합?
# check list를 활용?
from collections import deque

n = int(input())

papper = [list(map(int, input().split())) for _ in range(n)]

queue = deque()

queue.append([0,0])
result = [0,0]
flag = 0
flag_num = n*n

while True:
    temp_queue = deque()

    while queue:
        x, y = queue.popleft()
        temp_cnt = 0

        for i in range(n):
            for j in range(n):
                temp_cnt += papper[x+i][y+j]

        if temp_cnt == n*n:
            result[1] += 1
            flag += n*n

        elif temp_cnt == 0:
            result[0] += 1
            flag += n*n
            
        else:
            temp_queue.append([x,y])
            temp_queue.append([x+n//2,y+n//2])
            temp_queue.append([x+n//2,y])
            temp_queue.append([x,y+n//2])

    queue = temp_queue
    n //= 2
    
    if flag == flag_num:
        break

print(result[0])
print(result[1])