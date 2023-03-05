# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

import sys

N = int(sys.stdin.readline())
star = ""
blank = ""
num = 3

for i in range(N):
    if i == 0:
        star += '*'
        print(star.rjust(N))

    elif 0 < i < N:
        star += '*'
        print(star.rjust(N) + '*' * i)

for j in range(N - 1):
    blank += " "
    astar_num = (2 * N - num)
    astar = '*' * astar_num
    print(blank + (astar.rjust(N - num)))
    num += 2
