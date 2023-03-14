"""
k-드라마, k-브랜드, k-콘텐츠 ... 가영이는 수많은 'k'에 질렸습니다.

문득 가영이는 자신이 지금까지 본 K가 얼마나 되는지 궁금해졌습니다.

이를 위해서 가영이는 자신이 봤던 문자열에서 알파벳만 남기고 전부 소문자로 고쳤습니다.

하지만 가영이는 이 문자열에서 'k'의 개수를 세는 것에서 막히고 말았습니다.

가영이는 이에 프로그래밍을 잘 알고 있는 여러분께 도와달라고 부탁했습니다.

가영이를 위해서 알파벳 소문자로만 이루어진 문자열이 하나 주어졌을 때 이 문자열에 포함된 소문자 'k'의 개수를 출력하는 프로그램을 작성해주세요
"""
from string import ascii_lowercase
N = input()
N = list(N.lower())
# print(N)

print(N.count('k'))

"""
참고 방법

리스트 요소 개수 구하기 1) https://velog.io/@g0garden/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%9A%94%EC%86%8C%EC%9D%98-%EA%B0%9C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0-len-count

입력값 소문자 변환 2) https://blockdmask.tistory.com/416

소문자 리스트 추출 3) https://angelplayer.tistory.com/193
"""
