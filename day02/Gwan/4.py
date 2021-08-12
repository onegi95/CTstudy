n = int(input())
coin = list(map(int, input().split()))
coin.sort()
# 오름차순으로 정렬해서 작은 동전부터 차례대로 추가하면서 만들 수 없는 금액 탐색
# 1, 1, 2라면 1~4 최소 5
# 1, 1, 2, 2 라면 1~4인거는 만들 수 있고 2를 추가해서 만들어지는 6 최소 7
# 1, 1, 2, 6 이되면 1~4되고 7~10이 되버리면서 (5, 6 스킵) => 5
# 즉 이전에 있던 target 보다 큰 수가 다음에 오게 되면 target이 최소 수
money = 1
for i in coin:
    # 주어지는 수가 target보다 크면 뿌수고 money 출력
    if money < i:
        break
    # 주어지는 수가 target보다 작을땐 더해서 만들 수 있는 최소 수를 만들어줌
    money += i
print(money)