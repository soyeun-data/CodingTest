# 2 <= n <= 100000, 1 < k < n
# 숫자가 크지 않으니까 완전 탐색으로 가능할수도
# 리스트 슬라이싱 -> 시간 초과
n, k = map(int, input().split())
temper_list = list(map(int,input().split()))

temp_sum = sum(temper_list[:k])
max_temp = temp_sum

left = 0
right = k-1

for _ in range(n-k):
    temp_sum -= temper_list[left]
    temp_sum += temper_list[right+1]
    
    left += 1
    right += 1
    max_temp = max(max_temp, temp_sum)

max_temp = max(max_temp, temp_sum)    
print(max_temp)