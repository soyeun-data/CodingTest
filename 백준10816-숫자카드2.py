n = int(input())
card_list = map(int, input().split())
card_dict = dict()

for card in card_list:
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

m = int(input())
card_cnt = map(int, input().split())

for i in card_cnt:
    if i in card_dict:
        print(card_dict[i], end=' ')
    else:
        print(0, end=' ')
