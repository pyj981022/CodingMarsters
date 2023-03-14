""" 세아는 영어를 너무 좋아한 나머지 자기만의 영어사전을 만들려고 합니다. 
머릿속에 떠오른 영어단어를 다음과 같은 기준에 따라 정리하려고 합니다.
우선, 길이가 짧은 단어부터 순서대로 나열합니다. 
만약 단어의 길이가 같다면 사전순대로 정리합니다. 
세아가 사전을 만드는 프로그램을 작성해주세요.
"""
# import sys

# n = int(input())

# li = [input() for _ in range(n)]

# li.sort(key=len)

# for i in li:
#     print(i)

import sys
word=set()
for i in range(int(input())) :
  word.add(sys.stdin.readline().rstrip())
word=list(word)
word.sort()
word.sort(key=lambda x:len(x))
print("\n".join(word))

"""참고 URL
- https://pika-chu.tistory.com/334
"""