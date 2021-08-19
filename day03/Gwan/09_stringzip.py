def solution(string):
    answer = 10000
    for i in range(1, len(string)//2+1):
        result = ''
        cnt = 1
        slice_string = string[:i]
        for j in range(i, len(string)+i, i):
            if slice_string == string[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    result += slice_string
                else:
                    result += str(cnt) + slice_string
                slice_string = string[j:j+i]
                cnt = 1
        answer = min(answer, len(result))
    return answer
# 테스트 케이스 1개 나가는데 뭘까