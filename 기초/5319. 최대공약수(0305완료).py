"""최대공약수란 어떤 두 개 이상의 자연수들이 있을 때, 두 수의 공통된 약수 중 가장 큰 수를 말합니다. 
서로 다른 두 자연수 N, M이 주어졌을 때, 두 수의 최대공약수를 출력하는 프로그램을 작성해주세요
"""
import sys

a, b = input().split()

a = int(a)
b = int(b)

for i in range(1, a + 1):
  if (a % i == 0) & (b% i == 0):
    gcd = i 
  
print(gcd)

"""참고 URL
1) 최대공약수
- https://creatorjo.tistory.com/129

2) 2개의 값 입력 받기
- https://uhhyunjoo.tistory.com/20


"""