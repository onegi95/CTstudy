import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    home = []
    chicken = []
    # 집과 치킨집의 위치를 분리해서 기록해둔다(둘 좌표값 차이를 계산하기 위해)
    for y in range(n):
        for x in range(n):
            if city[y][x] == 1:
                home.append((y, x))
            elif city[y][x] == 2:
                chicken.append((y, x))
    # 현재 들어있는 좌표값
    # print(home)
    # print(chicken)
    # print()
    # 최종 값을 담을 ans 1000은 그냥 임의로 큰 값을 넣어서 min 값을 찾을 수 있게
    ans = 1000000
    # 백트래킹은 시간초과가 발생해서 combinations라는 내장 함수를 써야 한다.
    # combinations란?
    for i in combinations(chicken, m):
        # print(i)
        # print()
        # 임시로 값을 받아줄 변수
        tmp = 0
        for j in home:
            # print(j)
            min_v = 1000000
            for k in i:
                distance = abs(k[0] - j[0]) + abs(k[1] - j[1])
                min_v = min(min_v, distance)
            tmp += min_v
        # print()

        ans = min(ans, tmp)

    print(ans)