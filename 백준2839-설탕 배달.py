# 3kg, 5kg
# 5kg으로 최대한 채우고 3kg으로 나머지가 안되면 5kg을 하나씩 줄이면서 해보기
# 마지막까지 안되면 -1 출력

n = int(input())
result = -1
max_five = n // 5

for i in range(max_five,-1,-1):
    remain = n - (i * 5)
    if remain % 3 == 0:
        result = i + (remain // 3)
        break

print(result)