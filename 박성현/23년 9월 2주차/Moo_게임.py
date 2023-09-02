def find_moo(N, k, length):
    if k == 0:  # Base case
        return 'm' if N == 1 else 'o'
    
    prev_length = (length - k - 3) // 2  # Calculate length of S(k-1)
    
    if N <= prev_length:
        return find_moo(N, k-1, prev_length)
    elif N <= prev_length + k + 3:
        return 'm' if N == prev_length + 1 else 'o'
    else:
        return find_moo(N - prev_length - k - 3, k-1, prev_length)

# 시작
N = int(input())
length = 3
k = 0

# Find k and length of S(k) that includes N
while length < N:
    k += 1
    length = 2 * length + k + 3

# Find the N-th character
print(find_moo(N, k, length))