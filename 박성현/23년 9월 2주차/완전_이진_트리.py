import sys
def input():
    return sys.stdin.readline().rstrip()

K = int(input())
order = list(map(int, input().split()))
answer = {i: [] for i in range(K)}

def construct_tree(level, nodes):
    n = len(nodes)
    if n == 0:
        return
    
    mid = n // 2
    answer[level].append(nodes[mid])

    # 왼쪽 서브트리와 오른쪽 서브트리에 대해 재귀 호출
    construct_tree(level + 1, nodes[:mid])  # 왼쪽 서브트리
    construct_tree(level + 1, nodes[mid+1:])  # 오른쪽 서브트리

construct_tree(0, order)
print(answer)
for i in range(K):
    print(" ".join(map(str, answer[i])))