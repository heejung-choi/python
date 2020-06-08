# for 문은 정해진 범위 내 시퀀스(문자열, 튜플 리스트 같은)나
# 다른 반복가능한 객체(iterable)의 요소들을 순차적으로 실행합니다.
# 반복 가능한 마지막 요소까지 돌게 된다.

#for target_list in expression_list:
#    pass

for num in [0, 1, 2, 3, 4]:
    print(num)

# 종료 조건이 필요 없는 이유는 정해진 대로만 돌기 때문이다.

for num in range(100):
    print(num)

result = []
# list 만들 때 list()는 권장하지 않는다.
for num in range(1, 31):
    if num % 2 == 0:
       result.append(num)
print(result)

lunch = ['짜장면', '초밥', '탕수육']
for index, menu in enumerate(lunch):
    print(index, menu)

# enumerate : 차례로 열거하다.
print(enumerate(lunch))
# <enumerate object at 0x000001BE5A703EF8>
print(type(enumerate(lunch)))
# <class 'enumerate'>
print(list(enumerate(lunch)))
# [(0, '짜장면'), (1, '초밥'), (2, '탕수육')]
# tuple을 내부적으로 사용한다.
print(type(list(enumerate(lunch))[0]))
# <class 'tuple'>