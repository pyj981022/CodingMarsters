"""초등학교 2학년인 또리는 요즘 머릿속으로 하는 숫자놀이에 푹 빠져있습니다. 또리는 자연수 N이 주어졌을 때 N의 자릿수를 뒤집은 숫자와 각 자릿수의 합을 생각합니다. 이런 또리를 좋아하는 친구 빅은 또리와 놀고 싶었습니다. 하지만 빅은 계산을 잘하지 못합니다.

계산을 잘 하지 못하는 빅을 도와 자연수 N이 주어졌을 때 N의 자릿수를 뒤집은 숫자와 각 자릿수의 합을 각각 출력하는 프로그램을 작성해주세요. 이때 뒤집은 숫자가 0으로 시작하는 경우, 0을 생략하고 출력합니다.

예를 들어 N = 200일 때, 자릿수를 뒤집은 숫자는 002이며, 각 자릿수의 합은 2입니다. 따라서 2와 2를 줄로 구분하여 출력합니다.
"""
    
a = int(input())
sum_a = 0
# b = (a // 100) + (((a % 100) // 10) * 10) + ((a % 10) * 100)

# reverse
print(int(str(a)[::-1]))

# sum
while a>0:
    digit = a % 10
    sum_a = sum_a + digit
    a = a // 10
print(sum_a)

"""참고 방법 
1) reverse https://artra.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5%EB%90%9C-%EC%A0%95%EC%88%98-%EC%88%AB%EC%9E%90-%EB%92%A4%EC%A7%91%EA%B8%B0
2) sum https://logdeveloper.github.io/python/python-concept-chapter10/"""    