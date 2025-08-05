# 첫번째 풀이
# 시간 초과 발생
# input_str = list(input())
# m = int(input())
# cursor = len(input_str)

# for _ in range(m):
#     tmp_input = input().split()

#     if len(tmp_input) >= 2:
#         order, tmp_str = tmp_input
#     else:
#         order = tmp_input[0]

#     if order == "L":
#         if cursor > 0:
#             cursor -= 1
#     elif order == "D":
#         if cursor < len(input_str):
#             cursor += 1
#     elif order == "B":
#         if cursor > 0:
#             del input_str[cursor-1]
#             cursor -= 1
#     elif order == "P":
#         input_str.insert(cursor, tmp_str)
#         cursor += 1
# print(''.join(input_str))

# 두번째 풀이
from sys import stdin

left_stack = list(input())
right_stack = []
m = int(input())

for _ in range(m):
    order = list(stdin.readline().split())

    if order[0] == "L" and left_stack:
        right_stack.append(left_stack.pop())
    elif order[0] == "D" and right_stack:
        left_stack.append(right_stack.pop())
    elif order[0] == "B" and left_stack:
        left_stack.pop()
    elif order[0] == "P":
        left_stack.append(order[1])

print(''.join(left_stack + right_stack[::-1]))

'''
정리
첫번째 풀이에서 insert와 del을 사용하여 시간 초과가 남
=> 최악의 경우 각각 O(N)의 시간이 걸릴수 있음
=> M개의 명령어가 있다면 O(MN) 까지 걸릴 수 있음
push와 pop을 사용하면 각각 O(1) 시간 복잡도를 가지고 최종 출력시에만 O(N)의 시간 복잡도로 인해 전체 O(M+N) 밖에 안걸림
'''