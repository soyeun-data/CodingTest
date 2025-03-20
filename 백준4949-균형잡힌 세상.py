# 1. 입력의 종료 조건 : .(온점)

while True:
    input_str = input()
    stack = []

    if input_str =='.':
        break

    for str in input_str:
        if str == '(' or str == '[':
            stack.append(str)

        elif str == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(str)
                break
        elif str == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(str)
                break
            
    if len(stack) == 0:
        print("yes")
    else:
        print('no')
