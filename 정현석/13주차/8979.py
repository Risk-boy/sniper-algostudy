import sys

[n, k] = list(map(int, sys.stdin.readline().rstrip().split()))
countries = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
countries = {c[0]: c[1:4]  for c in countries}

k = countries[k]

countries = sorted(countries.values(), reverse=True)

print(countries.index(k)+1)