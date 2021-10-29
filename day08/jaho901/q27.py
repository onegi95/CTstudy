import sys
sys.stdin = open('q27.txt')

N, X = map(int, input().split())
data = list(map(int, input().split()))
result = 0

for i in data:
    if i == X:
        result += 1

if result == 0:
    print(-1)
else:
    print(result)