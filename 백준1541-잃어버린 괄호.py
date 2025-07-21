
str_input = input().split('-')
num = []

for str in str_input:
    sum = 0
    temp = str.split('+')
    for tmp in temp:
        sum += int(tmp)
    
    num.append(sum)

first = num[0]

for n in range(1, len(num)):
    first -= num[n]
print(first)