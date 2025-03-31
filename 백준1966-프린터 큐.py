from collections import deque, defaultdict

case = int(input())

for _ in range(case):
    n, m = map(int, input().split())
    doc_list = map(int, input().split())
    importance_dict = defaultdict(int)
    doc_queue = deque()
    cnt = 0

    for index, importance in enumerate(doc_list):
        doc_queue.append([index, importance])
        importance_dict[importance] += 1

    while doc_queue:
        temp_index, temp_importance = doc_queue.popleft()
        
        if temp_importance == max(importance_dict):
            cnt += 1
            if (importance_dict[temp_importance] - 1) == 0:
                del importance_dict[temp_importance]
            else:
                importance_dict[temp_importance] -= 1

            if temp_index == m:
                print(cnt)
                break
        else:
            doc_queue.append([temp_index, temp_importance])
