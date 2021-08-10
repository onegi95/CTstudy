n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
arr.sort(reverse = True)

while m != 0:
    result += arr[0]*k
    m-=k
    result += arr[1]
    m -= 1

print(result)