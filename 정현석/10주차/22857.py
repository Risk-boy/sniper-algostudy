import sys

[n, k] = list(map(int, sys.stdin.readline().rstrip().split()))
seq = list(map(lambda x: int(x) % 2 == 0, sys.stdin.readline().rstrip().split()))

curr_k = 0
while seq:
    if not seq[0]:
        seq.pop(0)
        n -= 1
    else:
        break

curr_max = 0
while seq:
    if seq[0]:
        seq.pop(0)
        curr_max += 1
        n -= 1
    else:
        break

max_subseq = curr_max
k_list = [curr_max]

i = 0
while i < n:
    if not seq[i]:
        odd_len = 0
        while i < n and not seq[i]:
            i += 1
            odd_len += 1
        
        k_list.append(odd_len)
        
        curr_k += odd_len
        
        while curr_k > k:
            curr_max -= k_list.pop(0)
            curr_k -= k_list.pop(0)
    else:
        even_len = 0
        while i < n and seq[i]:
            i += 1
            even_len += 1
        k_list.append(even_len)
        curr_max += even_len
        
        if curr_max > max_subseq:
            max_subseq = curr_max

print(max_subseq)