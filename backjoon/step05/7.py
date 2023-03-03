# 알파벳 대소문자로 된 단어가 주어지면,
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

S = list(input().lower())
answer = dict()
for i in S:
    if i not in answer.keys():
        answer[i] = 1
    else:
        answer[i] += 1
tmp = [i for i, j in answer.items() if max(answer.values()) == j]
if len(tmp) > 1:
    print("?")
else:
    upper_char: str = max(answer, key=answer.get)
    print(upper_char.upper())