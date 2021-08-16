n = int(input())
coin = list(map(int, input().split()))
coin.sort()

money = 1
for i in coin:
    if money < i:
        break
    money += i
print(money)