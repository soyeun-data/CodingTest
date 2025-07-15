# 각 문서의 중요도와 순서를 하나로 묶기
from collections import deque

n = int(input())

for _ in range(n):
    num_len, index = map(int, input().split())
    priority_list = list(map(int, input().split()))
    priority = sorted(priority_list)
    doc_list = deque()
    cnt = 1
    for i,j in enumerate(priority_list):
        doc_list.append([i,j])

    while len(doc_list) > 0:
        ind, num = doc_list.popleft()

        if num == priority[-1]:
            if ind == index:
                print(cnt)
                break
            else:
                priority.pop()
                cnt += 1
        else:
            doc_list.append([ind,num])
