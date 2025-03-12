# 방법2
# heapq 활용
# 시간 : 2680ms
# heapq를 활용할 경우 시간이 크게 단축될 것 같았으나 나이, 들어온 순서대로 정렬을 다시 해줘야하기 때문에 방법1과 시간 차이가 크지 않음음
import heapq

n = int(input())
heap = []

for i in range(n):
    age, name = input().split()
    heapq.heappush(heap,(int(age), i, name))

heap = sorted(heap, key=lambda x:(x[0],x[1]))

for age, index, name in heap:
    print(age,name)
