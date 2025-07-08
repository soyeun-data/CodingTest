# 5의 개수 세기(소인수분해)
n = int(input())
cnt = 0
while (n > 1):
    cnt += n // 5
    n //= 5

print(cnt)