import sys
import heapq

n = int(sys.stdin.readline().rstrip())

subways = list(map(int, sys.stdin.readline().rstrip().split()))

total = sum(subways)

dists_init = {}

for s, s_len in enumerate(subways):
    for i in range(s_len):
        dists_init[(s + 1, i + 1)] = float("inf")

subways = [0] + subways

m = int(sys.stdin.readline().rstrip())

transfers = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]

transfers_edges = {(t[0], t[1]): (t[2], t[3]) for t in transfers}
transfers_edges.update({(t[2], t[3]): (t[0], t[1]) for t in transfers})

k = int(sys.stdin.readline().rstrip())

requests = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(k)]


def dijkstra(u, transfer_weight):
    dists = dists_init.copy()
    dists[u] = 0
    pq = [(u, 0)]

    while pq:
        curr_node, curr_dist = heapq.heappop(pq)

        if curr_dist > dists[curr_node]:
            continue

        if curr_node[1] == 1:
            dist = curr_dist + 1
            adj = (curr_node[0], curr_node[1] + 1)

            print(adj)

            if dist < dists[adj]:
                dists[adj] = dist
                heapq.heappush(pq, (adj, dist))

        elif curr_node[1] == subways[curr_node[0]]:
            dist = curr_dist + 1
            adj = (curr_node[0], curr_node[1] - 1)

            if dist < dists[adj]:
                dists[adj] = dist
                heapq.heappush(pq, (adj, dist))
        else:
            dist1 = curr_dist + 1
            adj1 = (curr_node[0], curr_node[1] - 1)

            if dist1 < dists[adj1]:
                dists[adj1] = dist1
                heapq.heappush(pq, (adj1, dist1))

            dist2 = curr_dist + 1
            adj2 = (curr_node[0], curr_node[1] + 1)

            if dist2 < dists[adj2]:
                dists[adj2] = dist2
                heapq.heappush(pq, (adj2, dist2))

        if curr_node in transfers_edges:
            dist = curr_dist + transfer_weight
            adj = transfers_edges[curr_node]

            if dist < dists[adj]:
                dists[adj] = dist
                heapq.heappush(pq, (adj, dist))

    return dists


for r in requests:
    print(dijkstra((r[1], r[2]), r[0])[(r[3], r[4])])
