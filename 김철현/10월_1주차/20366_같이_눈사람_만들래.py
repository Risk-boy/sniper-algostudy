import sys
input = sys.stdin.readline 


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
min_diff = float("inf")
for i in range(N - 3):
    for j in range(i + 1, N - 2):
        for k in range(j + 1, N - 1):
            left = k + 1
            right = N - 1
            while left <= right:
                middle = (left + right) // 2
                
                diff = arr[i] + arr[middle] - arr[j] - arr[k]
                if diff == 0:
                    print(0)
                    exit()
                
                if diff > 0:
                    right = middle - 1
                else:
                    left = middle + 1

                if min_diff > abs(diff):
                    min_diff = abs(diff)
print(min_diff)