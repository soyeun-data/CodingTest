# 1. 블록 제거 후 인벤토리에 넣기 => 2초
# 2. 인벤토리에서 블록 하나를 꺼내 블록 위에 놓기 => 1초
# 땅 고르기 작업 최소 시간과 땅의 높이 출력
# 작업 시작 시, 인벤토리에 B개의 블록이 있음
# 브루트포스로 풀기
# 0 ~ 256층일 때 넘치는 블록 수와 모자란 블록 수를 세기
import sys

n, m, b = map(int, sys.stdin.readline().split())

ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

time = sys.maxsize
max_height = -1

for floor in range(257):
    exceed_floor, lack_floor = 0,0

    for row in range(n):
        for column in range(m):
            if ground[row][column] > floor:
                exceed_floor += ground[row][column] - floor
            else:
                lack_floor += floor - ground[row][column]
    
    if exceed_floor + b >= lack_floor:
        if (exceed_floor*2 + lack_floor) <= time:
            time = exceed_floor*2 + lack_floor
            max_height = floor

print(time, max_height)