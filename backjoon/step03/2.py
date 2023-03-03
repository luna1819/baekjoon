# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

T = int(input())
list = []

for i in range(T):
    A , B = map(int, input().split( ))
    list.append(A+B)

for i in range(len(list)):
    print(list[i])