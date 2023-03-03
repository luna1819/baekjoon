# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

T = int(input())
num = input()
arr = []

for i in range(T):
    arr.append(int(num[i]))
print(sum(arr))