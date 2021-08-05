n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
 
arr.sort(reverse=True)
n1 = arr[0]
n2 = arr[1]
 
i = m // (k+1)
mod = m % (k+1)
result = n1 * i * k + n2 * i
 
if mod != 0:
    result += mod * n1
    
print(result)