import sys
sys.stdin = open('input.txt')

N, C = map(int, input().split())
data = []
for _ in range(N):
    a = int(input())
    data.append(a)
data = sorted(data)

s = 1
e = data[-1] - data[0]
result = 0

while s <= e:
    mid = (s + e)//2
    dist = data[0]
    cnt = 1

    for i in range(1, N):
        if data[i] >= dist + mid:
            dist = data[i]
            cnt += 1

    if cnt < C:
        e = mid - 1

    elif cnt >= C:
        s = mid + 1
        result = mid

print(result)
