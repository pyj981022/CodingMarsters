"""아스키(ASCII, American Standard Code for Information Interchange)는 문자 인코딩의 한 종류입니다. 
아스키에서 128개의 문자는 각각 0 이상 128 미만의 정수에 대응됩니다.
10진수 정수 A를 입력받고, 아스키 표에 따라 정수 A를 문자로 변환하여 출력하는 프로그램을 작성해주세요."""

import sys

a = int(sys.stdin.readline())

print(chr(a))