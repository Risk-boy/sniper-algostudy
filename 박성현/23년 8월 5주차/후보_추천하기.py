import sys
from collections import Counter

def input():
    return sys.stdin.readline().rstrip()

N = int(input()) # 사진틀 수
M = int(input()) # 전체 추천 횟수
recommendations = list(map(int, input().split())) #투표 현황 
candidates = []
INF = int(10e9)

def find_candidate_to_remove(candidates):
    min_recommendations = INF
    oldest_idx = 0

    for idx, candidate in enumerate(candidates):
        if candidate['recommendations'] < min_recommendations:
            min_recommendations = candidate['recommendations']
            oldest_idx = idx
        elif candidate['recommendations'] == min_recommendations:
            if candidate['time'] < candidates[oldest_idx]['time']:
                oldest_idx = idx

    return oldest_idx, min_recommendations

for idx, student_id in enumerate(recommendations):
    found = False # 이미 후보로 있는지 확인하는 플래스
    for candidate in candidates:
        if candidate['id'] == student_id:
            candidate['recommendations'] += 1
            found = True
            break
    if not found:
        if len(candidates) < N : # 사진틀에 여유가 있으면
            candidates.append({'id': student_id,'recommendations':1,'time':idx})
        else:
            remove_idx, min_recommendations = find_candidate_to_remove(candidates)
            candidates.pop(remove_idx)
            candidates.append({'id': student_id,'recommendations':1,'time':idx})

candidates.sort(key=lambda x: (x['id']))
print(' '.join([str(candidate['id']) for candidate in candidates]))

        

            