from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
# 노드 관계를 나타내줄 배열
arr = [[] for _ in range(n+1)]
# 거리를 나타내줄 배열
distance = [0] * (n+1)
# 방문 여부를 표시해줄 배열
visited = [False] * (n+1)

# 노드간의 관계 표시 1번부터
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

def bfs(start):
    # 최종 결과를 담아줄 빈 배열
    answer = []
    # 시작 부분 부터 큐에 담는다.
    q = deque([start])
    # 해당 노드에 방문표시를 한다
    visited[start] = True
    # 출발점은 거리가 0이므로 0에서 시작
    distance[start] = 0
    # queue가 빌 때까지 진행한다.
    while q:
        # 현재노드를 now라는 변수에 담아주고
        now = q.popleft()
        # 현재노드과 연결된 노드를 차례대로 확인한다.
        for next in arr[now]:
            # 만약 방문 안했다면
            if not visited[next]:
                # 방문표시하고 그 노드를 queue에 넣어주고 
                # 다음 노드까지 가는 거리는 그 현재노드까지 간거리 + 1
                visited[next] = True
                q.append(next)
                distance[next] = distance[now] + 1
                # 만약 그 노드 까지 가는 거리가 k라면 조건을 만족하므로 answer에 넣어준다.
                if distance[next] == k:
                    answer.append(next)
    # 만약 거리를 만족하는게 없다면 -1 출력
    if len(answer) == 0:
        print(-1)
    # 그렇지 않다면 만족하는 모든 수 출력
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')
# 시작노드 x로부터 bfs 함수 호출 시작
bfs(x)