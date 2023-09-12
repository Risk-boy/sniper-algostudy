import sys
from collections import deque 

def input():
    return sys.stdin.readline().rstrip()

# 노드 개수
N = int(input())

# 노드 정보 저장
tree = {}

for _ in range(N):
    node, left, right = input().split()
    tree[node] = [left, right]

#print(tree)

#전위
def pre(node):
    if node == '.':
        return
    print(node, end='')
    pre(tree[node][0])
    pre(tree[node][1])
#중위
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0]) #왼쪽
    print(node,end='')
    inorder(tree[node][1]) #오른쪽

def post(node):
    if node == '.':
        return
    post(tree[node][0])
    post(tree[node][1])
    print(node, end='')

pre('A')
print()
inorder('A')
print()
post('A')

