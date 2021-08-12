#1 ~ target-1 수까지 모든 금액을 만들 수 있다고 가정
#

# 동전의 갯수
N = int(input())

# 동전
coins = list(map(int, input().split()))
def solution(coins) :
    # 오름차순으로 정렬`
    coins.sort()

    #target num
    target = 1
    
    for coin in coins:
        if target < coin:
            break
        target += coin
    return target

print(solution(coins))