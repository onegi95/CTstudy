N = int(input())
# 처음 가장 원 숫자인 100이 들어와야 하기 때문이다.

# 최종 결과값
real_result = []
# 왜 범위를 이렇게 지정했냐?
# n의 반보다 적은 경우는 무조건 4번째에서 음수가 나오기 때문!!
for i in range(N // 2, N+1):
    # result와 n은 원래 값으로 초기화시켜준다.
    result = [N]
    n = N
    # 바로 2번째 값을 넣어준다.
    result.append(i)

    # 2번째 숫자까지 들어오게 되었을 때 while문을 돌려 다 채워준다.
    while n >= 0:
        n = result[-2] - result[-1]
        # n이 음수면 바로 break 아니면 그 값을 result에 채워준다.
        if n < 0:
            break
        result.append(n)

    real_result.append(result)
print(real_result)
length = []
for i in real_result:
    length.append(len(i))

max_length = max(length)
max_idx = length.index(max_length)
print(max_length)
print(*real_result[max_idx])

