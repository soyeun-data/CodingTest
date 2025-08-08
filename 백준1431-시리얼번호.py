# 1. 길이 확인 -> 짧은것부터
# 2. 길이가 같으면 자리수의 합 -> 작은 것부터
# 3. 모두 같으면 사전순


def num_sum(input_str):
    temp_sum = 0
    for str in input_str:
        if str.isdigit():
            temp_sum += int(str)
    return temp_sum

n = int(input())
serial = [input() for _ in range(n)]

serial = sorted(serial, key = lambda x: (len(x), num_sum(x),x))

for s in serial:
    print(s)
