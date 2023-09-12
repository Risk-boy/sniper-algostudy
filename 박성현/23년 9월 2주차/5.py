N,K = map(int,input().split())
N += 1
N_list = list(str(N))
cur_idx = -1
max_idx = len(N_list)
while True:
    if N_list.count('5') >= K:
        break
    while N_list[cur_idx] == '5' and abs(cur_idx) < max_idx:
        cur_idx -= 1
    
    cur_value = int(''.join(N_list))
    cur_value = cur_value + 10**(abs(cur_idx)-1)
    N_list = list(str(cur_value))
    max_idx = len(N_list)
 
 
 
print(''.join(N_list))