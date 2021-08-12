# 볼링공 수 N 공의 최대 무게 M
N, M = tuple(map(int, input().split()))

# 볼링공 무게 리스트
ball_list = list(map(int, input().split()))

def solution(N, ball_list):
    # 선택지
    cnt=0

    # 검색을 위한 이중 for 문
    for i in range(N):
        for j in range(N):
            #조건
            if i != j and ball_list[i] != ball_list[j]:
                cnt += 1
    #중복된 경우 제외 
    return cnt//2
    
print(solution(N, ball_list))