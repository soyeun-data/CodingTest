# 브루트포스 => 시간 초과
# product를 이용하여 조합구하기 => 메모리 초과
# 이분 탐색 => 해결

T = int(input())


for _ in range(T):
    cnt = 0
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()

    for a_num in a:
        start, end = 0, m-1
        
        while start <= end:
            mid = (start + end)//2

            if a_num > b[mid]:
                start = mid + 1
            else:
                end = mid-1
        
        cnt += start

    print(cnt)