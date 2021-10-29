import sys
sys.stdin = open('input.txt')

N = int(input())

score_board = []

for i in range(N):
    temp = list(input().split())
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    temp[3] = int(temp[3])
    score_board.append(temp)
score_board.sort()
first_sort = []
i = 0
while True:

