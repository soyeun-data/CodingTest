# 처음엔 리스트와 in 연산을 사용하였지만 시간초과가 발생함
# set 자료구조와 & 비트 연산자를 이용하여 문제 해결
# in 연산자의 시간 복잡도 => O(n)
# set 연산자의 시간 복잡도 => O(1)


n, m = map(int, input().split())

hear = []
see = []

for i in range(n):
    name = input()
    hear.append(name)

for ii in range(m):
    name = input()
    see.append(name)

hear_see = list(set(hear)&set(see))
hear_see.sort()

print(len(hear_see))
for iii in hear_see:
    print(iii)
