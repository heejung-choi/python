# while 문은 조건식이 True인 경우 반복적으로 코드를 실행
# 조건식이 False 일때까지 실행
# 그래서 종료 조건을 반드시 설정해줘야 한다.

n = 0

while n < 3:
    print(n)
    n = n + 1

a = ''

while a != '안녕':
    print('안녕이라고 할 때 까지 물어볼거야.....')
    a = input('말해봐 : ')