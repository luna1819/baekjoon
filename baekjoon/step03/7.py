# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys

N = int(sys.stdin.readline())
for x in range(N):
    A, B = map(int, sys.stdin.readline().split( ))
    print("Case #"+str(x+1)+":", str(A+B))