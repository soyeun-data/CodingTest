# 1. 아무 의견이 없으면 문제 난이도는 0
# 2. 의견이 하나 이상 있으면, 위 아래 15% 제외하고 평균 계산
# 20명 위 아래 3명 20*0.15 => 반올림
import sys

def roundUp(num):
    if (num-int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())

if n == 0:
    print(0)
else:
    grade_list = []
    
    for i in range(n):
        grade_list.append(int(sys.stdin.readline().rstrip()))
        
    grade_list.sort()
    num = roundUp(n*0.15)
    grade_list =  grade_list[num:n-num]

    print(roundUp(sum(grade_list)/len(grade_list)))