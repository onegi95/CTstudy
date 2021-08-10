a = input()

def solution(s):
    cnt = 0
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            cnt += 1
    
# 010과 같은 경우 01일때 cnt + 1, 10일때 + 1이 되므로 이 방식은 두배씩 그
# 개수가 늘어나기 때문에 2로 나누어준 몫 부분을 가져와야 한다.    
    return (cnt+1)//2

print(solution(a))