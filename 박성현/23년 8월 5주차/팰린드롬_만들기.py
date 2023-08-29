import sys 
def input():
    return sys.stdin.readline().rstrip()

def make_shortest_palindrome(s):
    def is_palindrome(subs):
        return subs == subs[::-1]

    length = len(s)
    for i in range(length):
        if is_palindrome(s[i:]):
            return length + i
    return 2 * length - 1

s = input().strip()
print(make_shortest_palindrome(s))
