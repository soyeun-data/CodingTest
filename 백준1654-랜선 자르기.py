k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]

start = 1
end = max(cables)
result = 0

while start <= end:
    mid = (start + end)//2
    total = 0

    for cable in cables:
        total += cable // mid

    if total >= n:
        result = mid
        start = mid+1
    else:
        end = mid -1

print(result)