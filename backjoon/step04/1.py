# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

import sys

N = int(sys.stdin.readline())
while True:
    arr = list(map(int, sys.stdin.readline().split( )))
    if len(arr) == N:
        break

arr_num = []
V = int(sys.stdin.readline())
for i in range(N):
    if arr[i] == V:
        arr_num.append(V)

print(len(arr_num))