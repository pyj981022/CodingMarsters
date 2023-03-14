"""철수는 건강을 위해 팔굽혀펴기를 시작했습니다. 
매일 아침 팔굽혀펴기를 하고, 그날 팔굽혀펴기를 몇 회 했는지 노트에 정확하게 기록해두었습니다.
N일이 지나고 노트를 봤을 때, 노트에는 N개의 양의 정수가 쓰여있었습니다. 
철수가 N일 동안 팔굽혀펴기를 총 몇 회 했는지 구하는 프로그램을 작성해주세요
"""

import sys

list1 = []

a = int(sys.stdin.readline())

for i in range(a):
    b = int(sys.stdin.readline())
    list1.append(b)
    
print(sum(list1))

""" 참고 URL
1) 입력값 반복
- https://dojang.io/mod/page/view.php?id=1272
"""