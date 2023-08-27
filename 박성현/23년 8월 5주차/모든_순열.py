import sys
def input():
    return sys.stdin.readline().rstrip()

def permute(nums):
    # 초기 결과는 빈 리스트 안의 빈 리스트로 시작 ([[]])
    result = [[]]
    for n in nums:
        new_permutations = []
        for perm in result:
            # 각 숫자를 가능한 모든 위치에 삽입
            for i in range(len(perm) + 1):
                # n을 i 위치에 삽입한 리스트를 복제
                new_permutations.append(perm[:i] + [n] + perm[i:])
        result = new_permutations
    return result

nums = list(range(1,int(input())+1))
for i in sorted(permute(nums)):
    print(*i)