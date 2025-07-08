n = int(input())
x_y = [list(map(int, input().split())) for _ in range(n)]

x_y = sorted(x_y, key = lambda x:(x[1],x[0]))

for x,y in x_y:
    print(x,y)
