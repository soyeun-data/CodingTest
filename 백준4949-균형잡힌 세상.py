while True:
    str_input = input()
    stack = []

    if str_input == '.':  
        break

    for s in str_input:
        if (s == "[") or (s == "("):
            stack.append(s)
        elif s == ")":
            if len(stack)!=0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s)
                break
        elif s == "]":
            if len(stack)!=0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(s)
                break
    
    if len(stack) == 0:
        print("yes")
    else:
        print("no")