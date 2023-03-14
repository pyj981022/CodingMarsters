""" 정수 A와 B가 입력될 때 A개의 원소에서 B개의 원소를 뽑는 조합에 대한 총 경우의 수를 출력하는 프로그램을 작성해주세요."""

from sys import stdin

import operator as op
from functools import reduce

n, r= map(int, stdin.readline().split())

def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

print(nCr(n, r))

"""참고 URL
1. 조합 코드
-https://brownbears.tistory.com/459 
"""