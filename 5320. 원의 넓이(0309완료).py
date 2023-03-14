""" 영태는 학교에서 원의 반지름과 원의 넓이의 관계에 대해 배웠습니다. 
잘 알려진 바와 같이, 원의 넓이는 반지름 × 반지름 × 원주율과 같습니다. 
영태는 아직 초등학생이기 때문에 원주율(PI)의 값은 소수점 두 자리까지, 즉 3.14로 합니다. 
원의 반지름이 주어지면 원의 넓이를 출력하는 프로그램을 작성해주세요"""

r = int(input())
result = r*r*3.14

if result == int(result):
    print(int(result))
else:
    print(result)

""" 참고 URL
1) 원의 넓이
- https://codethem.tistory.com/137
- https://hello-ming.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%98%EC%A7%80%EB%A6%84%EC%9D%98-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0%EB%A5%BC-%EB%B0%9B%EA%B3%A0-%EC%9B%90%EC%9D%98-%EB%A9%B4%EC%A0%81%EA%B3%BC-%EB%91%98%EB%A0%88-%EA%B5%AC%ED%95%98%EA%B8%B0

2) 소숫점 버리기
- https://aplab.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%86%8C%EC%88%98%EC%A0%90-%EC%B6%9C%EB%A0%A5