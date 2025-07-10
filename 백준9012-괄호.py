n = int(input())
result = []

for _ in range(n):
    ps = input()
    stack = []
    for p in ps:
        if p == "(":
            stack.append(p)
        else:
            if len(stack) == 0:
                stack.append(p)
                break
            else:
                stack.pop()

    if len(stack) == 0:
        result.append("YES")
    else:
        result.append("NO")

for res in result:
    print(res)