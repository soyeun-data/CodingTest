# 100까지 갈 수 있는 최단거리를 찾아줘야함
# 방향이 앞과 뒤로 갈 수 있으므로 1차원 배열의 BFS를 구현
# 사다리 칸과 뱀 칸의 경우 dict를 이용하여 값을 저장
# 주사위를 굴렸을 때, 사다리 & 뱀 칸에 도착했을 경우 3번에서 만든 dict에서 값을 찾아서 해당 위치로 이동

from collections import deque

n, m = map(int, input().split())
lad_snake_dict = dict()

for _ in range(n+m):
    x,y = map(int, input().split())
    lad_snake_dict[x] = y

visited = [0 for _ in range(101)]
queue = deque()
queue.append(1)

while queue:
    num = queue.popleft()

    if num == 100:
        break

    for i in range(1,7):
        temp = num + i

        if temp < 101 and visited[temp] == 0:
            if temp in lad_snake_dict:
                temp = lad_snake_dict[temp]
            
            if visited[temp] == 0:
                visited[temp] = visited[num] + 1
                queue.append(temp)

print(visited[100])



