# 1. D(뒤집기) : 배열에 있는 수의 순서 뒤집기
# 2. D(버리기) : 첫 번째 수 버리기
# 3. 배열이 빈 상태에서 D사용하면 에러 발생
# import ast

# t = int(input())
# result = []

# for _ in range(t):
#     p = input()
#     n = int(input())
#     array = ast.literal_eval(input())
#     error = "false"

#     for order in p:
#         if order == 'R':
#             array = array[::-1]
#         else:
#             if len(array) == 0:
#                 result.append("error")
#                 error = "true"
#                 break
#             else:
#                 array.pop(0)

#     if error == "false":
#         result.append(array)

# for i in result:
#     print(i)

# 시간 초과
# 배열을 뒤집는 부분에서 시간이 오래 걸리는것으로 보임
# R이 나왔을 경우 실제로 뒤집지 않은 상태에서 수행
import ast

t = int(input())
result = []


for _ in range(t):
    p = input()
    n = int(input())
    array = ast.literal_eval(input())
    error = False
    reverse = False

    for order in p:
        if order == 'R':
            reverse = not reverse
        else:
            if len(array) == 0:
                result.append("error")
                error = True
                break
            else:
                if reverse == False:
                    array.pop(0)
                else:
                    array.pop()

    if error == False:
        if reverse == True:
            array = array[::-1]

        result.append("["+",".join(map(str,array))+"]")

for i in result:
    print(i)
