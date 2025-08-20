# 첫 번째 방법 - 모든 조합 구하기 => 메모리 초과
# 두 번째 방법
# 1. 정렬
# 2. 첫 값과 끝 값 더하기
# 3. target 값과 같으면 cnt+1, 작으면 왼쪽 값 위로 이동, 크면 오른 쪽 값 아래로 이동

n = int(input())
num_list = list(map(int, input().split()))
target = int(input())
cnt = 0
left = 0
right = n-1
num_list.sort()

while(left < right):
    temp_sum = num_list[left] + num_list[right]
    if temp_sum == target:
        cnt += 1
        left += 1
    elif temp_sum < target:
        left += 1
    elif temp_sum > target:
        right -= 1
print(cnt)