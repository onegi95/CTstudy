import sys
sys.stdin = open('input.txt')

N = int(input())
data = list(map(int, input().split()))
result = -1

for i in range(N):
    if i == data[i]:
        result = i
        break
print(result)