import sys
input=sys.stdin.readline

n=int(input())
num_list=[]

for i in range(n):
    num_list.append(int(input()))

num_list = sorted(num_list)

#산술평균
print(round(sum(num_list)/len(num_list)))

#중앙값
print(num_list[len(num_list)//2])

#최빈값
temp_dict = dict()

for num in num_list:
    if num in temp_dict:
        temp_dict[num] += 1
    else:
        temp_dict[num] = 1

mx=max(temp_dict.values())
mx_dict=[]

for i in temp_dict:
    if mx == temp_dict[i]:
        mx_dict.append(i)

if len(mx_dict)>1:
    print(mx_dict[1])
else:
    print(mx_dict[0])

#범위
print(max(num_list)-min(num_list))
