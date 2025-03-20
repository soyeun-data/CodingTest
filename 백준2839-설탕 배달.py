# 일단 5 kg 짜리를 최대한 많이 해야겠네 => 그리디

n = int(input())
max_five = n // 5
result = n
flag = -1

for i in range(max_five,-1,-1):
    if (n - (5*i)) % 3 == 0:
        temp = i + (n - 5*i) // 3
        result = min(result, temp)
        flag = 1

if flag == -1:
    print(-1)
else:
    print(result)