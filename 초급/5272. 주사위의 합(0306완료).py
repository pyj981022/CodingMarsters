"""주사위 2개를 굴려 합이 N이 나오는 경우의 수를 구하는 프로그램을 작성해주세요. 
반드시 주사위 2개를 함께 굴리며, 예를 들어 N = 5일 때는 (1, 4), (2, 3), (3, 2), (4, 1)의 네 가지 경우의 수가 존재합니다.
"""
import sys

a = int(sys.stdin.readline())

for i in range(1, 7):
    for j in range(1, 7):
        if i + j == a:
            print(i, j)
            
            
""" 참고 URL
https://brightnightsky77.tistory.com/677
"""