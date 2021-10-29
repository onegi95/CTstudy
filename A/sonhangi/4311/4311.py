import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, O, M = map(int,input().split()) # 사용 가능한 숫자 갯수, 연산자 갯수, 최대 연산 횟수

    num_list = [0]*10

    # 사용 가능한 숫자를 받아온다
    temp = list(map(int, input().split()))
    for i in range(len(temp)):
        num_list[temp[i]] = 1

    # 사용 가능한 연산자를 받아온다
    cal_list = [0]*5
    temp2 = list(map(int, input().split()))
    for i in range(len(temp2)):
        cal_list[temp2[i]] = 1

    # 타겟 넘버를 받아온다
    target = int(input())

    #--------------- 입력 끝 -------------------#


    print(temp2)
    print(num_list,cal_list,target)


