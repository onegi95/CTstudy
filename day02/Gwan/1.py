# 모험가 길드
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
cnt = 0
for i in range(len(arr)):
    val = arr[i]
    cnt += 1
    if val == cnt:
        result += 1
        cnt = 0
print(result)