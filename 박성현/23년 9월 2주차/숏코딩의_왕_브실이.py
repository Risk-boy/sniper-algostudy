import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 차이 수열 B 생성
B = [A[i+1] - A[i] for i in range(N-1)]
# print(B)
# print(sum(B))
# B 수열의 전체 합
total_happiness = sum(B)

max_happiness = total_happiness

# 누적 합 계산
prefix_sum = [0] * (N-1)
prefix_sum[0] = B[0]
for i in range(1, N-1):
    prefix_sum[i] = prefix_sum[i-1] + B[i]

C = [prefix_sum[0]]
for i in range(1, M):
    C.append(min(C[-1], prefix_sum[i]))

# 뒤에서의 누적 합 계산
suffix_sum = [0] * (N-1)
suffix_sum[-1] = B[-1]
for i in range(N-3, -1, -1):  # 뒤에서부터 진행
    suffix_sum[i] = suffix_sum[i+1] + B[i]

D = [suffix_sum[-1]]
for i in range(1, M):
    D.append(min(D[-1], suffix_sum[N-2-i]))


min_combined_value = float('inf')  # 최솟값을 저장하기 위한 변수, 초기값은 무한대로 설정

for i in range(M+1):  # 앞에서 0개를 선택하는 경우도 고려
    # C의 i번째 값과 D의 M-i번째 값을 합한다. 
    # i 혹은 M-i가 0일 때는 해당 리스트의 값을 더하지 않습니다.
    current_value = (C[i-1] if i > 0 else 0) + (D[M-i-1] if i < M else 0)
    # print(current_value)
    min_combined_value = min(min_combined_value, current_value)

if min_combined_value<0:
    print(total_happiness-min_combined_value)
else:
    print(total_happiness)


