n = int(input())
word_list = [input() for _ in range(n)]
word_list = list(set(word_list))

word_list = sorted(word_list, key = lambda x : (len(x),x))

for word in word_list:
    print(word)