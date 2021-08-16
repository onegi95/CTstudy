
N_list = list(map(int, input()))

if len(N_list)%2 == 0:
    n = len(N_list)//2
    sum_front = sum(N_list[0:n])
    sum_back = sum(N_list[n:])

    if sum_front == sum_back:
        print("LUCKY")

    else:
        print("READY")












