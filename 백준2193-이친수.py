# 첫번째 풀이
# 완전 탐색 -> 시간 초과
# 두번재 풀이
# DP
# n-1 자리 수의 이친수에 0 붙임
# n-2 자리 수의 이친수에 01을 붙임
# => 1이 연속으로 나타나지 않음

n = int(input())
dp = [0] * (n+1)
dp[1] = 1

if n >=2 :
    dp[2] = 1

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])