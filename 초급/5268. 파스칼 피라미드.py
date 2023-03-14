"""
파스칼 피라미드는 파스칼의 삼각형을 3차원으로 확장한 개념으로 정수가 나열된 사면체의 모양을 하고 있습니다. 
논의를 간단하게 하기 위해 밑면이 직각이등변삼각형인 삼각뿔 모양이라고 가정하겠습니다. 파스칼 피라미드를 만드는 방법은 다음과 같습니다.
1. 먼저 삼각뿔 맨꼭대기(1층)에 1행 1열에 1을 써넣습니다. 
2. 그 아래층의 i행 j열에는 바로 윗층 i행 j열, i-1행 j열, i행 j-1열의 요소들을 더한 값을 써넣습니다. 
만약 윗층에 해당 요소가 없다면 0으로 간주합니다. 
파스칼 피라미드의 각 층을 분리해서 4층까지 표현하면 다음과 같습니다. 
<1층>
1
<2층>

1 1

1
<3층>

1 2 1

2 2

1
<4층>

1 3 3 1

3 6 3

3 3

1
정수 n이 입력될 때, 파스칼 피라미드 n층을 출력하는 프로그램을 작성해주세요.
"""

import sys

cycle = int(sys.stdin.readline())

numbers = [] # 출력 용 저장 리스트
temp = [] # 계산용 임시 리스트

for i in range(cycle): # 반복문
    numbers.append(1) # 첫부분 1 입력
    temp.append(1) # 계산용도 동일하게 적용
    if i < 2: 
        pass # 2가 넘어갈 될 때까지 무시
    else:
        for j in range(1, len(numbers)-1): # 계산
            temp[j] = numbers[j-1]+numbers[j]
    for j in range(len(numbers)): # 계산 완료된 코드를 다시 저장
        numbers[j]=temp[j]
        print(str(numbers[j]) + " ", end="") # 한줄로 출력

        
    print("") # 줄 띄우기
    
# import sys

# a = int(sys.stdin.readline())

# for i in range(a):
#     print('*'*(a-i))