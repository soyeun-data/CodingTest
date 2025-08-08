# 그리디

n, l = map(int, input().split())
leak_list = list(map(int, input().split()))
leak_list.sort()

start = leak_list[0]
cnt = 1

for location in leak_list[1:]:
    if location in range(start,start+l):
        continue
    else:
        cnt += 1
        start = location

print(cnt)