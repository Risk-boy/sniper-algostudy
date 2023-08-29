N, K = map(int, input().split())
muscle_kits = list(map(int, input().split()))

def backtrack(day, weight, used_kits):
    if weight < 500:  # 중량이 500 이하라면 탐색 중지
        return 0

    if day == N:  # N일 동안 모든 운동 키트를 사용했으면 1 반환
        return 1

    count = 0
    for i in range(N):
        if not used_kits[i]:  # 아직 사용하지 않은 운동 키트 선택
            used_kits[i] = True
            count += backtrack(day + 1, weight + muscle_kits[i] - K, used_kits)  # 다음 상태로 이동
            used_kits[i] = False  # backtracking

    return count

# 아직 사용되지 않은 운동 키트를 False로 초기화
used_kits = [False] * N

print(backtrack(0, 500, used_kits))