n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list = set(n_list)
for m_num in m_list:
    if m_num in n_list:
        print(1)
    else:
        print(0)
