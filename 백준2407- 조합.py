def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

n, m = map(int, input().split())

print(int(factorial(n)//(factorial(m)*factorial(n-m))))

# / 와 //의 차이
# (int // int)는 결과가 int 이지만 (int/int)는 결과가 float이 되어 답과 다르게 나올 수 있음

# print(int(gob1//(gob2*gob3)))
# 100891344545564193334812497256 (O)
# print(int(gob1/(gob2*gob3)))
# 100891344545564202071714955264 (X)