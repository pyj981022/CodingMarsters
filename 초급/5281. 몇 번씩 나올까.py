""" 1부터 N까지의 숫자를 일렬로 늘어놓았을 때, 0부터 9까지의 숫자가 각각 몇 번씩 나오는지 알아내는 프로그램을 작성해주세요."""

a = int(input())

result=[0]*10
for i in range(a):
    x=str(i)
    for j in x:
        result[int(j)]+=1
print(result)