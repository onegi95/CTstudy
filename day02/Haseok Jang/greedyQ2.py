#문자열 받아오기
string = input()

def solution(string):
    #숫자인 리스트로 문자열 변환하기
    num_list = []
    for char in string :
        num_list.append(int(char))

    for idx in range(1,len(num_list)):
        #곱한 값과 다한 값
        multiple = num_list[idx-1] * num_list[idx]
        plus = num_list[idx-1] + num_list[idx]
        
        #비교하여 누적
        num_list[idx] = multiple if multiple > plus else plus
    #마지막 값 출력
    return(num_list[-1])
    
print(solution(string))