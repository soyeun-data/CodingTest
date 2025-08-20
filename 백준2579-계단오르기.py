# 마지막 계단은 꼭 밟아야하므로 마지막 계단부터 시작
# 그리디 알고리즘
# 다음 계단을 밟는 것과 다다음 계단을 밟는 것 중 큰 값을 가질 수 있는 것을 선택
# 두번 연속된 계단이면 다다음을 계단을 무조건 선택
# 그리디 실패
# dp

n = int(input())
stairs = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1,n+1):
    stairs[i] = int(input())

if n <= 2:
    print(sum(stairs))
else:
    dp[1] = stairs[1]
    dp[2] = dp[1] + stairs[2]

    for j in range(3, n+1):
        dp[j] = max(dp[j-3] + stairs[j-1],dp[j-2]) + stairs[j]

    print(dp[n])