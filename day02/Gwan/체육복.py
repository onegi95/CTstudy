def solution(n, lost, reserve): 
    reser_del = set(reserve)-set(lost) 
    lost_del = set(lost)-set(reserve) 
    for i in reser_del: 
        if i-1 in lost_del: 
            lost_del.remove(i-1) 
        elif i+1 in lost_del: 
            lost_del.remove(i+1) 
    return n-len(lost_del)


def solution(n, lost, reserve): 
    for res in reserve: 
        if res in lost: 
            lost.remove(res) 
            reserve.remove(res) 
    answer = n - len(lost) 
    for i in lost: 
        if i in reserve: 
            answer += 1 
            reserve.remove(i) 
            
        elif i - 1 in reserve: 
            answer += 1 
            reserve.remove(i - 1) 
        
        elif i + 1 in reserve: 
            answer += 1 
            reserve.remove(i + 1) 
    return answer


def solution(n, lost, reserve): 
    reserve_n = list(set(reserve) - set(lost)) 
    lost_n = list(set(lost) - set(reserve))

    answer = n - len(lost_n) 
    for i in lost_n: 
        if i - 1 in reserve_n: 
            answer += 1 
            reserve_n.remove(i - 1) 
        elif i + 1 in reserve_n: 
            answer += 1 
            reserve_n.remove(i + 1) 
    
    return answer
