# 방법1
# 1-1 입력 순서와 나이, 이름을 같이 입력 받음
# 1-2 정렬
# 시간 2700ms

n = int(input())

age_name = [[index, int(age), name] for index, (age, name) in enumerate(input().split() for i in range(n))]

age_name = sorted(age_name, key=lambda x:(x[1],x[0]))

for index, age, name in age_name:
    print(age,name)

