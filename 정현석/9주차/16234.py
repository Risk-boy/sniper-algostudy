import sys

[n, l, r] = list(map(int, sys.stdin.readline().rstrip().split()))

countries = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]

count = 0

while True:
    count += 1
    
    unions = []

    for i in range(n):
        for j in range(n-1):
            diff = abs(countries[i][j] - countries[i][j+1])
            if diff >= l and diff <= r:
                curr_union, next_union = None, None
                for u in unions:
                    if (i, j) in u:
                        curr_union = u
                    if (i, j+1) in u:
                        next_union = u
                if curr_union and next_union:
                    if curr_union != next_union:
                        unions.remove(curr_union)
                        unions.remove(next_union)
                        unions.append(curr_union | next_union)
                elif curr_union:
                    unions.remove(curr_union)
                    curr_union.add((i, j+1))
                    unions.append(curr_union)
                elif next_union:
                    unions.remove(next_union)
                    next_union.add((i, j))
                    unions.append(next_union)
                else:
                    unions.append({(i, j), (i, j+1)})           
                    
    for i in range(n):
        for j in range(n-1):
            diff = abs(countries[j][i] - countries[j+1][i])
            if diff >= l and diff <= r:
                curr_union, next_union = None, None
                for u in unions:
                    if (j, i) in u:
                        curr_union = u
                    if (j+1, i) in u:
                        next_union = u
                if curr_union and next_union:
                    if curr_union != next_union:
                        unions.remove(curr_union)
                        unions.remove(next_union)
                        unions.append(curr_union | next_union)
                elif curr_union:
                    unions.remove(curr_union)
                    curr_union.add((j+1, i))
                    unions.append(curr_union)
                elif next_union:
                    unions.remove(next_union)
                    next_union.add((j, i))
                    unions.append(next_union)
                else:
                    unions.append({(j, i), (j+1, i)})
    
    if not unions:
        count -= 1
        break
    
    for u in unions:
        total = 0
        for c in u:
            total += countries[c[0]][c[1]]
        new_pop = total // len(u)
        for c in u:
            countries[c[0]][c[1]] = new_pop
        
print(count)