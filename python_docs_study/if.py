x = int(input("숫자를 입력하세요:"))

if x < 0:
    x = 0
    print('x가 0보다 작아 0으로 변환합니다.')
elif x == 0:
    print('x는 0입니다.')
elif x == 1:
    print('x는 1입니다.')
else:
    print('x는 0보다 큽니다.')