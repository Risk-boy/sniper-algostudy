import sys

def find_k(n, k):
    sieve = list(range(2, n+1))

    count = 0

    while sieve:
        first = sieve.pop(0)
        count += 1
        
        if count == k:
            return first
        
        first_multiple = first*2
        
        while first_multiple <= n:
            if first_multiple in sieve:
                sieve.remove(first_multiple)
                count += 1
                
                if count == k:
                    return first_multiple
            
            first_multiple += first
            
print(find_k(*map(int, sys.stdin.readline().rstrip().split())))