# 모험가 길드
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
cnt = 0
# 모험가 파티원 수 만큼  돈다
for i in range(len(arr)):
    # 공포도를 넣는다
    val = arr[i]
    cnt += 1
    # 공포도가 모험가 수랑 같으면 result 하나 늘리고 새로운 그룹ㄱㄱ
    if val == cnt:
        result += 1
        cnt = 0
print(result)