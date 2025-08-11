# rotate 활용
from collections import deque

n = int(input())
input_list = list(map(int, input().split()))
ballons = deque()
answer = []

for index, b in enumerate(input_list):
    ballons.append([index+1, b])

while(ballons):
    tmp_index, tmp_num = ballons.popleft()
    if tmp_num > 0:
        tmp_num = tmp_num-1
    else:
        tmp_num = tmp_num

    answer.append(tmp_index)
    ballons.rotate(-tmp_num)

print(*answer)