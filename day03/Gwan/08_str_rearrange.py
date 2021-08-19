import sys
sys.stdin = open('08_input.txt')

T = int(input())

for tc in range(1, T+1):
    string = input()
    digit = []
    alpha = []
    for i in range(len(string)):
        if string[i].isalpha():
            alpha.append(string[i])
            continue
        else:
            digit.append(int(string[i]))

    alpha.sort()
    alpha.append(str(sum(digit)))

    print(''.join(alpha))
    