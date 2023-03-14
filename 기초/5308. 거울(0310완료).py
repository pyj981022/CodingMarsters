"""수연이네 반 칠판 앞에 누군가 마법의 거울을 놓았습니다. 
이 거울엔 칠판에 쓴 수가 모두 거꾸로 읽은 모습으로 보입니다. 
예를 들어 123은 321로 보이고, 724는 427로 보입니다. 
칠판에 서로 다른 세 자리 수가 두 개 쓰여졌을 때, 거울에 보이는 두 수 중 더 큰 수를 출력하는 프로그램을 작성해주세요."""
from sys import stdin

a, b= map(int, stdin.readline().split())

a = int(str(a)[::-1])
b = int(str(b)[::-1])

if a > b:
    print(a)
else:
    print(b)