import math

def is_decimal(num):
    if num == 1:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        # print("i:",i)
        if num % i == 0:
            return False
    
    return True

m, n = map(int, input().split())

for j in range(m,n+1):
    if is_decimal(j):
        print(j)