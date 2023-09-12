import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def find_path_to_root(parents, start):
    path = set()
    while start in parents:
        path.add(start)
        start = parents[start]
    path.add(start)  # 루트를 추가
    return path

T = int(input())

for _ in range(T):
    N = int(input())
    parents = {}
    
    for _ in range(N-1):
        A, B = map(int, input().split())
        parents[B] = A

    u, v = map(int, input().split())

    u_to_root = find_path_to_root(parents, u)
    
    while v not in u_to_root:
        if v in parents:
            v = parents[v]
        else:  # B가 A의 경로에 없는 경우
            break

    if v in u_to_root:
        print(v)
    else:
        print("No common ancestor")  # 이런 경우는 문제 조건상 존재하지 않으므로 실제로 이 출력이 나오면 안됩니다.