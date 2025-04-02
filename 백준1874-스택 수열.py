# 1. 스택을 2개 준비
# 2. 1 ~ n까지의 숫자를 1번 스택에 넣기
# 3. 1번 스택의 마지막이 주어진 수열의 처음과 같다면 pop

n = int(input())
num_list = [int(input()) for _  in range(n)]
result = []

stack1 = []
stack2 = []
index = 0

for i in range(1, n+1):
    stack1.append(i)
    result.append('+')

    while stack1:
        if stack1[-1] == num_list[index]:
            stack2.append(stack1.pop())
            index += 1
            result.append('-')
        else:
            break

if len(stack1) == 0:
    for ii in result:
        print(ii)
else:
    print("NO")