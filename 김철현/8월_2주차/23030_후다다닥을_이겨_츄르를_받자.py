import sys, heapq
input = sys.stdin.readline 


def dijkstra(s1, s2, t):
    q = []
    heapq.heappush(q, (0, s1, s2))
    distance[s1][s2] = 0
    while q:
        dist, cur, cur_sub = heapq.heappop(q)
        
        if distance[cur][cur_sub] < dist:
            continue
        for nxt in [cur_sub - 1, cur_sub + 1]:
            if  0 <= nxt < stations_num[cur]:
                cost = dist + 1
                if cost < distance[cur][nxt]:
                    distance[cur][nxt] = cost
                    heapq.heappush(q, (cost, cur, nxt))
        if hwan[cur][cur_sub] != 0:
            h, h_sub = hwan[cur][cur_sub][0], hwan[cur][cur_sub][1]
            if distance[h][h_sub] > dist + t:
                distance[h][h_sub] = dist + t
                heapq.heappush(q, (dist + t, h, h_sub))
    return


INF = int(1e9)
n = int(input())    # 노선 개수  
stations_num = list(map(int, input().split()))  # 노선별 역 개수
m = int(input())    # 환승역 개수

distance = [[[INF, False] for _ in range(50)] for _ in range(n)]


hwan = [[0] * 50 for _ in range(n)]
for _ in range(m):
    p1, p2, q1, q2 = map(int, input().split())
    hwan[p1 - 1][p2 - 1] = [q1 - 1, q2 - 1]
    hwan[q1 - 1][q2 - 1] = [p1 - 1, p2 - 1]


K = int(input())
for _ in range(K):
    t, u1, u2, v1, v2 = map(int, input().split())
    
    distance = [[INF for _ in range(50)] for _ in range(n)]
    dijkstra(u1 - 1, u2 - 1, t)
    print(distance[v1 - 1][v2 - 1])