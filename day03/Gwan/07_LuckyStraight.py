import sys
sys.stdin = open('07_input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = input()
    n = len(numbers)//2
    a = numbers[0:n]
    b = numbers[n:]
    x = 0
    y = 0
    for i in a:
        x += int(i)
    for i in b:
        y += int(i)

    if x == y:
        print('Lucky')
    else:
        print('Ready')

T = int(input())

for tc in range(1, T+1):
    numbers = input()
    n = len(numbers)//2
    a = 0
    b = 0
    for i in numbers[0:n]:
        a += int(i)
    for i in numbers[n:]:
        b += int(i)
    if a == b:
        print('Lucky')
    else:
        print('Ready')    