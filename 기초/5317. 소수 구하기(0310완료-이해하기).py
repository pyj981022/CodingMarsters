""" 소수 정리'란 어떤 자연수 이하의 소수가 몇 개나 있는지 그 값을 어림할 수 있는 정리입니다.
이 정리가 맞는지 의구심이 들은 진수는 직접 확인해 보기로 했습니다. 
한참을 계산하던 진수는 소수의 개수를 헤아리는데 몹시 많은 시간일 든다는 걸 깨닫고 여러분들께 도움을 구했습니다. 
진수를 위해 자연수 N 이하의 소수 개수를 출력하는 프로그램을 작성해주세요.
이때 소수란 양의 약수가 자기 자신과 1만 존재하는 수를 말합니다. 
또한 어떤 정수 A가 어떤 정수 B의 약수라는 것은 B를 A로 나누었을 때 나누어 떨어짐을 의미합니다.
"""

import sys

a = int(input())

def prime(n):
    count = n-1
    for i in range(2,n+1):
        for x in range(2,i):
            if i % x == 0:
                count -= 1
                break
    return count

print(prime(a))

"""참고 URL
1) 소수의 개수 구하기
- https://codingdojang.com/scode/503?orderby=time&langby=python
"""