""" 1부터 N까지의 숫자 중에서 5의 배수의 개수를 출력하는 프로그램을 작성해주세요 """
N = int(input())
cnt = 0

for i in range(1, N+1):
    if i % 5 == 0:
        cnt+=1
print(cnt)