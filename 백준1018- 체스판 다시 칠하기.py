# 맨 왼쪽 위 칸은 흰색 또는 검은색
# 8*8로 잘랐을 때 다시 칠해야하는 정사각형의 개수를 모두 구해

m,n = map(int, input().split())
min_num = 64
w_b_list = [["W","B","W","B","W","B","W","B"],
            ["B","W","B","W","B","W","B","W"],
            ["W","B","W","B","W","B","W","B"],
            ["B","W","B","W","B","W","B","W"],
            ["W","B","W","B","W","B","W","B"],
            ["B","W","B","W","B","W","B","W"],
            ["W","B","W","B","W","B","W","B"],
            ["B","W","B","W","B","W","B","W"]]
w_b_input = [list(input()) for _ in range(m)]

for row_start in range(0,m-7):
    for column_start in range(0,n-7):
        w_cnt = 0
        b_cnt = 0
        for row in range(8):
            for column in range(8):
                # print("row_start+row:",row_start+row)
                # print("column_start+column:",column_start+column)
                # W 부터 시작할 경우 다시 색칠해야하는 개수
                if w_b_list[row][column] != w_b_input[row_start+row][column_start+column]:
                    w_cnt += 1
                # B 부터 시작할 경우 다시 색칠해야하는 개수
                if w_b_list[row][column] == w_b_input[row_start+row][column_start+column]:
                    b_cnt += 1
        if w_cnt < min_num:
            min_num = w_cnt
        if b_cnt < min_num:
            min_num = b_cnt
print(min_num)