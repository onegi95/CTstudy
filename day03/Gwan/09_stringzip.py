def solution(string):
    answer = 10000
    if len(string) == 1:
        return 1
    # if string == 'aabbaccc'
    # 문자열의 절반으로 확인하는게 max
    for i in range(1, len(string)//2+1):
        # 빈 문자열에 최종 값을 넣어준다.
        result = ''
        # 겹치는 문자열 앞에 넣어줄 숫자
        cnt = 1
        # 기준으로 삼을 문자열 초기화
        slice_string = string[:i]
        # i번째부터 i길이 마다 찾아야 하므로 range범위 설정
        for j in range(i, len(string)+i, i):
            # 만약 기준으로 삼을 문자열과 탐색 문자열이 같으면
            if slice_string == string[j:j+i]:
                # 1개씩 더해서 몇개인지 세어준다
                cnt += 1
            # 만약 같지 않을때 
            else:
                # cnt가 1이라면 빈 문자열 result에 기준 값 넣어준다
                if cnt == 1:
                    result += slice_string
                # 1이 아닐 때는 cnt값과 기준 값을 붙여서 문자열에 넣어준다
                else:
                    result += str(cnt) + slice_string
                slice_string = string[j:j+i]
                cnt = 1
        # 기존에 설정했던 답이랑 길이랑         
        answer = min(answer, len(result))
    return answer
# 테스트 케이스 1개 나가는데 뭘까