"""평행 세계의 대한민국에서는 주민등록증에 영문이름이 같이 기재되어 있습니다. 
그래서 주민등록증을 발급받을 때 주민등록증 발급신청서에 자신이 사용할 영문이름도 같이 작성한다고 합니다. 
이때, 발급받으려는 사람의 영문이름의 길이가 20자를 넘으면 특별신청을 해야 합니다.
주민등록증을 발급받으려는 사람의 영문이름이 주어졌을 때, 특별신청을 해야하는지 판단하는 프로그램을 작성해주세요.
"""

import sys

from string import ascii_lowercase

alphabet_list = list(ascii_lowercase) 


a = sys.stdin.readline()

if len(a) < 20:
    print('-1')
    
else: 
    print('0')