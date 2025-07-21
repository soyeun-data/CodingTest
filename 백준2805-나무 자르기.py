# 이분탐색

n,m = map(int, input().split())
tree_list = list(map(int, input().split()))

min_tree = 0
max_tree = max(tree_list)
result = 0

while min_tree <= max_tree:
    mid = (min_tree+max_tree)//2
    sum = 0
    for tree in tree_list:
        if tree-mid > 0:
            sum += (tree-mid)
    if sum >= m:
        result = mid
        min_tree = mid + 1
    else:
        max_tree = mid - 1
print(result)