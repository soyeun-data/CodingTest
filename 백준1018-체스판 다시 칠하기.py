# 체스판을 색칠하는 경우
# 1) 맨 왼쪽 위가 흰색인 경우
# 2) 맨 왼쪽 위가 검은색인 경우
# 브루트포스 알고리즘(완전탐색)으로 2가지 경우에 덧칠을 진행해야 하는 횟수 구하기
# 둘 중 한 가지의 덧칠 횟수는 64에서 다른 덧칠 횟수를 뺀 값과 동일
# => 한가지 경우의 덧칠 횟수만 구해도 됨
# min() 함수로 2가지 경우 중 다시 칠해야 하는 정사각형의 최소 개수 구하기

n,m = map(int, input().split())
board = [list(input()) for _ in range(n)]
min_cnt = 64

chess = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

for i in range(n-7):
    for j in range(m-7):
        cnt = 0
        for a in range(8):
            for b in range(8):
                if board[i+a][j+b] != chess[a][b]:
                    cnt += 1

        min_cnt = min(min_cnt, cnt, 64-cnt)

print(min_cnt)