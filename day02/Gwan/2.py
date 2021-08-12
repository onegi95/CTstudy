s = input()
#첫 번쨰 문자를 숫자로 변경하여 대입 첫번째 문자부터 비교해서 진행
result = int(s[0])

for i in range(1, len(s)):
    # 두 번째 문자부터 int로 정수로 가져온다
    num = int(s[i])
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)