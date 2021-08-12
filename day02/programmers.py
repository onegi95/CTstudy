def solution(n, lost, reserve):
    # n : 전체 학생
    answer = n-len(lost)
    lost.sort()
    reserve.sort()
    for i in lost:
        if i in reserve:
            reserve.pop(reserve.index(i))
            answer += 1
        elif i-1 in reserve and i-1 not in lost:
            reserve.pop(reserve.index(i-1))
            answer += 1

        elif i+1 in reserve and i+1 not in lost:
            reserve.pop(reserve.index(i+1))
            answer += 1
    
    return answer