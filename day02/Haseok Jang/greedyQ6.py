def solution(food_times, k):
    idx = 0
    for i in range(k):
        food_times[idx] -= 1
        idx+=1
        idx%=3
    total = 0
    for i in food_times:
        if i<0:
            total += i
    return(idx - total)%3+1

print(solution([3,1,2],5))