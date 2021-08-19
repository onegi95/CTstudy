import sys
sys.stdin = open('상하좌우.txt')

n = int(input())
move = input().split()
x, y = 1, 1

for i in range(len(move)):
    if move[i] == 'L':
        if x > 1:
            x -= 1

    if move[i] == 'R':
        if x < n:
            x += 1

    if move[i] == 'D':
        if y < n:
            y += 1

    if move[i] == 'U':
        if y > 1:
            y -= 1

print(y, x)

n = int(input())
move = input().split()
x, y = 1, 1

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in move:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)