# 첫 풀이
# 1. 시작 시간을 기준으로 정렬
# 2. 회의가 끝나는 시간과 시작하는 시간을 비교하여 최대로 가능한 회의 개수를 갱신
# => 시간 초과

# for i in range(n):
#     index = i + 1
#     cnt = 1
#     start, end = time[i]

#     if i == n-max:
#         break

#     while index < n:
#         if end <= time[index][0]:
#             cnt += 1
#             start, end = time[index]
#         index += 1

#     if max < cnt:
#         max = cnt

# print(max)

# 두번째 풀이
# 1. 끝나는 시간을 기준으로 정렬
# 2. 회의가 가장 빨리 끝나는 시간과 다음에 가능한 회의 시간을 확인
# 3. 가능한 회의 시간의 끝나는 시간으로 갱신하고 사용할 수 있는 회의 개수를 +1

n = int(input())
time = [[start, end] for start, end in (map(int, input().split()) for _ in range(n))]
cnt = 1

time = sorted(time, key=lambda x: (x[1],x[0]))

start, end = time[0]

for i in range(1,n):
    if end <= time[i][0]:
        cnt += 1
        start, end = time[i]
print(cnt)

