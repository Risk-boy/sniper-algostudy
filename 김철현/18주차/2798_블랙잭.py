import sys
input = sys.stdin.readline 


n, m = map(int, input().split())
nums = list(map(int, input().split()))

max_sum = 0

for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            sum = nums[i] + nums[j] + nums[k]

            if sum <= m and sum > max_sum:
                max_sum = sum

print(max_sum)