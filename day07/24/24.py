import sys
sys.stdin = open('input.txt')

N = int(input())

house = list(map(int,input().split()))
house.sort()
center = N//2 -1
print(house[center])
center_val = house[center]
min_val = 99999999999
min_place = 99999999999
if N == 1:
    print(0)
elif N == 2:
    print(abs[house[0] - house[1]])
else:
    for val in [house[center],house[center + 1], house[center -1], house[center - 2]]:
        temp = 0
        for i in range(N):
            if house[i] - val < 0:
                temp += (val - house[i])
            else:
                temp += house[i] - val
        if min_val >= temp and min_place > val:
            min_val = temp
            min_place = val

    print(min_place)

