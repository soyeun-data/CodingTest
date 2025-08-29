# x와 y의 차이를 기준으로 수행
# 이진 탐색

x,y = map(int, input().split())
num = (100*y)//x
answer = -1

start = 0
end = x

while start <= end:
    mid = (start + end)//2

    if (100*(y+mid))//(x+mid) > num:
        answer = mid
        end = mid-1
    else:
        start = mid+1

print(answer)
