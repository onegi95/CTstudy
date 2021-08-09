inp = input()

def solution(s):
    prev=''
    cnt= 0
    for i in s:
        if i!=prev:
            cnt+=1
            prev = i
    return (cnt)//2

print(solution(inp))    
