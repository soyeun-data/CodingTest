from itertools import permutations

n = int(input())

hints = [list(map(int, input().split())) for _ in range(n)]

num_perm = list(permutations(range(1,10),3))
cnt = 0

for perm in num_perm:
    valid = True

    for hint in hints:
        hint_num = list(map(int, str(hint[0])))
        strike = hint[1]
        ball = hint[2]

        temp_strike = 0
        temp_ball = 0

        for i in range(3):
            if hint_num[i] == perm[i]:
                temp_strike += 1
            elif hint_num[i] in perm:
                temp_ball += 1
        if strike != temp_strike or ball != temp_ball:
            valid = False
    
    if valid:
        cnt += 1

print(cnt)