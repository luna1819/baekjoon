import random
import sys

def compare():











  #오름차순
  array = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

  for j in range(len(array)):
    k = len(array)-j
    for i in range(1, k):
      if array[i-1] < array[i]:
        array[i], array[i-1] = array[i-1], array[i]
        # temp = array[i-1]
        # array[i-1] = array[i]
        # array[i] = temp
  print(array)

  # 문자열 오름차순
  # num_str = "1567920"
  # num_list = list(num_str)
  #
  # for j in range(len(num_list)):
  #   k = len(num_list)-j
  #   for i in range(1, k):
  #     if num_list[i-1] < num_list[i]:
  #         num_list[i], num_list[i-1] = num_list[i-1], num_list[i]
  #
  # num_str = ''.join(num_list)
  #
  # print(num_str)


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    compare()
# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
