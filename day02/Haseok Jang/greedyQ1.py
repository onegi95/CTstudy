# 모험가 길드 문제 공포도가 X인 모험가는 반드시 인원이 X이상인 그륩에 들어가야한다.

# 모험가의 수
players = int(input())
# 모험가들의 공포도 List
stats = list(map(int,input().split()))

def solution(players, stat):
    # 만들어지는 그룹 수
    groups = 0
    # 모험가들을 공포도가 낮은 순으로 정렬
    stats.sort()
    # 그룹멤버 수
    cnt=0
    for i in range(len(stats)):
        # 그룹멤버 한명씩 추출
        cnt +=1

        # 그룹멤버의 공포도
        member = stats.pop(0)
        if member == cnt :
            groups += 1
            cnt = 0

    return groups

print(solution(players, stats))      