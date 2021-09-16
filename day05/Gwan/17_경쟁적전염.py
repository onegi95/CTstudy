import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
virus_map = [list(map(int, input().split())) for _ in range(n)] # 전체 맵 정보 담는 리스트
virus =[] # 바이러스 정보를 담는 리스트

for y in range(n):
    for x in range(n):
        if virus_map[y][x] != 0:
            # 바이러스 번호, y위치, x위치, 시간 을 입력받는다.
            virus.append((virus_map[y][x], y, x, 0))
print(virus)
# 초와, x, y 좌표를 받아온다.
sec, X, Y = map(int, input().split())

# 상 하 좌 우 방향벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 정렬 안해주면 오류발생
virus.sort()
# queue에 virus 정보를 넣는다.
q = deque(virus)
print(virus)
# queue가 빌때까지!
while q:
    # 들어있는 정보를 받아와서
    print(q)
    virus, y, x, time = q.popleft()
    if time == sec:
        break
        # 4방향으로 순회해서
    for i in range(4):
        my = y + dy[i]
        mx = x + dx[i]
        # 나아갈 수 있다면 그곳으로 바이러스 전파
        if 0 <= my < n and 0 <= mx < n:
            if virus_map[my][mx] == 0:
                virus_map[my][mx] = virus
                # 전파하고 바이러스 정보를 다시 q에 담는다
                q.append((virus, my, mx, time+1))

print(virus_map[X-1][Y-1])