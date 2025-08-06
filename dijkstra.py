# 1. 경로 탐색 및 최적화 (Path Planning)
# 문제 예시
#
# 도시 내 차량이 목적지까지 이동해야 한다.
# 도로는 그래프로 주어지며, 각 간선은 시간 가중치를 가지고 있다.
# 특정 노드는 사고나 공사로 인해 통행이 불가능할 수 있다.
#
# 출발지에서 목적지까지 가장 빠른 경로를 구하라.
#
# 입력: 노드 수, 간선 정보(시간), 폐쇄된 노드
#
# 출력: 최단 경로 및 소요 시간
#
# 관련 기술: 다익스트라, A* 알고리즘

import heapq
from collections import defaultdict


def shortest_path(edges, blocked_nodes, num_nodes, start, end):
    # 1. 인접 리스트 생성(양방향 그래프)
    graph = defaultdict(list)
    # print(graph)
    for u, v, time in edges:
        # print(u, v, time)
        if u not in blocked_nodes and v not in blocked_nodes:
            # print(u, v)
            graph[u].append((v, time))
            graph[v].append((u, time))

    # 2. 초기 설정
    # dist[node]는 시작점에서 해당 노드까지의 현재까지 알려진 최단 시간을 의미
    # -> 처음에는 아무것도 모르니까 모든 노드까지의 거리를 무한대로 놓고 시작
    # 이후 다익스트라가 더 짧은 경로를 찾으면 해당 값을 갱신

    # dist = {}
    # for node in range(num_nodes):
    #     if node not in blocked_nodes:
    #         dist[node] = float("inf")

    # print(dist)

    # 딕셔너리 컴프리헨션 사용
    dist = {
        node: float("inf") for node in range(num_nodes) if node not in blocked_nodes
    }

    prev = {}  # 경로 추적용
    # 출발점은 자기 자신까지의 거리가 0이니까,
    # 여기는 예외적으로 0으로 초기화
    dist[start] = 0
    heap = [(0, start)]  # (거리, 노드)

    # 3. 다익스트라 알고리즘
    while heap:
        # print(heap)
        # heapq 모듈을 사용하면 거리(=우선순위)가 낮은 항목이 먼저 꺼내짐
        cur_dist, u = heapq.heappop(heap)
        # print(cur_dist, u)
        if u == end:
            break
        if cur_dist > dist[u]:
            continue

        """
        u: 지금 처리 중인 노드
        v: u의 이웃 노드
        weight: u->v로 이동하는 데 걸리는 시간
        dist[u]: 시작점에서 현재 노드 u까지의 최단 거리
        dist[v]: 시작점에서 v까지 현재까지 알려진 최단 거리
        
        지금 알고 있는 v까지 가는 거리(dist[v])보다,
        u를 거쳐서 가는 새 경로(dist[u]+weight)가 더 짧으면,
        그걸로 업데이트 하겠다.
        """

        for v, weight in graph[u]:
            # print(graph[u])
            # print(dist[u], dist[v], weight) # 0, inf, 4
            # print(dist[u] + weight)
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                # print(dist[v])
                # 경로 추적용으로, v까지 가는 최단 경로 직전 노드가 u라는 걸 저장하는 부분
                # 나중에 출발지부터 도착지까지 경로를 역추적할 때 사용
                prev[v] = u
                # 우선순위 큐에 (새 거리, 노드 v)를 추가
                # 나중에 v가 가장 가까운 노드로 다시 탐색 대상에 들어감
                heapq.heappush(heap, (dist[v], v))

    #     print(heap)
    # print(prev)

    # 4. 경로 재구성
    if end not in dist or dist[end] == float("inf"):
        return None, float("inf")  # 경로 없음

    path = []
    node = end

    while node != start:
        # print(node)
        path.append(node)
        # print(path)
        node = prev[node]
        # print(node)
    path.append(start)
    # print(path)
    path.reverse()
    # print(path)
    # print(dist)
    return path, dist[end]


if __name__ == "__main__":
    num_nodes = 6
    edges = [
        # (u, v, w)
        (0, 1, 4),  # 0번 노드에서 1번 노드까지 가는 데 4초 걸림
        (0, 2, 2),
        (1, 2, 1),
        (1, 3, 5),  # 1번 -> 3번 : 5초
        (2, 3, 8),
        (2, 4, 10),
        (3, 4, 2),
        (3, 5, 6),
        (4, 5, 2),
    ]
    blocked_nodes = {3}  # 사고로 통과 불가능한 노드
    start = 0
    end = 5

    path, total_time = shortest_path(edges, blocked_nodes, num_nodes, start, end)
    print("최단 경로:", path)
    print("총 소요 시간:", total_time)
