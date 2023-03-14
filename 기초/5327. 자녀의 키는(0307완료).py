""" 아버지의 키와 어머니의 키를 알면 그 자녀의 키를 예측할 수 있는 방법이 있습니다. 

바로 아버지의 키와 어머니의 키의 평균이 그 자녀의 예상 키가 됩니다. 



아버지와 어머니의 키가 자연수로 각각 주어질 때 자녀의 예상 키를 출력하는 프로그램을 작성해주세요"""

import math

dad, mom= input().split()

dad = int(dad)
mom = int(mom)

child = math.trunc((dad+mom)/2)


print(child)
