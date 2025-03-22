def cal_cnt(n):
    check_list = [[0]*n for i in range(n)]
    x = [-1,1,0,0]
    y = [0,0,-1,1]

    cnt = 0
    for row in range(n):
        for column in range(n):
            if check_list[row][column] == 0:
                cnt += 1
                check_list[row][column] = 1
                queue.append([row, column])
                first = RGB[row][column]

                while queue:
                    tmp_x, tmp_y = queue.popleft()
                    for i in range(4):
                        dx = tmp_x + x[i]
                        dy = tmp_y + y[i]
                
                        if dx >= 0 and dx < n and dy >= 0 and dy < n:
                            if first == RGB[dx][dy] and check_list[dx][dy] == 0:
                                check_list[dx][dy] = 1
                                queue.append([dx,dy])
    return cnt

from collections import deque

n = int(input())
RGB = [list(input()) for i in range(n)]
queue = deque()

# 적록 색약 X
cnt1 = cal_cnt(n)
# 적록 색약인 사람인 경우
for j in range(n):
    for k in range(n):
        if RGB[j][k] == 'G':
            RGB[j][k] = 'R'

cnt2 = cal_cnt(n)
print(cnt1, cnt2)