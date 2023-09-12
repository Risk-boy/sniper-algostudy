import sys 
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()
N = int(input())
parents = list(map(int, input().split()))
node_to_remove = int(input())

# 트리 생성
tree = defaultdict(list)
for i, parent in enumerate(parents):
    if parent != -1:
        tree[parent].append(i)
print(tree)

def remove_node(tree, node_to_remove):
    # 노드와 그 자손들을 제거
    if node_to_remove in tree:
        children = tree[node_to_remove][:]
        for child in children:
            remove_node(tree, child)
            tree[node_to_remove].remove(child)
    if node_to_remove in tree:
        del tree[node_to_remove]

# 주어진 노드와 그 자손 제거
remove_node(tree, node_to_remove)