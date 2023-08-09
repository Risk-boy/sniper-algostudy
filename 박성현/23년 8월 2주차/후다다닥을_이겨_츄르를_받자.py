import heapq
import sys
def input():
    return sys.stdin.readline().rstrip() 
INF = int(10e9)

# 기본 노드 만들어주기
node = int(input())
graph = [[] for _ in range(node+1)]
num_of_station = list(map(int, input().split()))
for ind, num in enumerate(num_of_station):
    for _ in range(1,num+2):
        graph[ind+1].append([])



for i in range(1,len(graph)):
    N = len(graph[i])
    for j in range(1,N+1):
        if 2<=j<=N-1:
            graph[i][j].append([(i, j-1), (1, False)])
            graph[i][j-1].append([(i, j), (1, False)])
    

num_of_transfer = int(input())
for _ in range(num_of_transfer):
    lane1, station1, lane2, station2 = map(int,input().split())
    graph[lane1][station1].append([(lane2, station2), (0,True)])
    graph[lane2][station2].append([(lane1, station1), (0,True)])


def dijkstra(transfer_time:int, start:tuple):
    # 거리 계산할 distance 만들어주기
    distance = [[] for _ in range(node+1)]
    for ind, num in enumerate(num_of_station):
        for _ in range(1,num+2):
            distance[ind+1].append(INF)

    q = []
    heapq.heappush(q, (0,start)) # start는 (1,3) = 1호선의 3번역 형식
    distance[start[0]][start[1]] = 0
    while q:
        # print(f'This is q: {q}----------')
        dist, now = heapq.heappop(q)
        # print('This is now:', dist,now)
        if distance[now[0]][now[1]] < dist:
            continue
        for i in graph[now[0]][now[1]]:
            if i[1][1] == False:
                cost = dist + i[1][0]
                if cost < distance[i[0][0]][i[0][1]]:
                    # print(f'I will update {i[0]}')
                    distance[i[0][0]][i[0][1]] = cost
                    heapq.heappush(q,(cost,(i[0][0],i[0][1])))
            else: # 즉 환승 가능하면
                # print(f'I will update {i[0]}')
                cost = dist + i[1][0] + transfer_time
                if cost < distance[i[0][0]][i[0][1]]:
                    distance[i[0][0]][i[0][1]] = cost
                    heapq.heappush(q,(cost,(i[0][0],i[0][1])))
    return distance

test_num = int(input())
for _ in range(test_num):
    data = list(map(int, input().split()))
    transfer_time, *lane_data = data
    start = tuple(lane_data[:2])
    target = tuple(lane_data[2:])
    # print(f'This is Transfer_time:{transfer_time}')
    distance = dijkstra(transfer_time, start)
    # print(distance)
    print(distance[target[0]][target[1]])






