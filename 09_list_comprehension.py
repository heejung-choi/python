my_list = []

for x in range(10):
    my_list.append(x ** 2)
print(my_list)

# my_newlist = my list.append(x ** 2) for x in range(10) 
# 위의 코드를 한줄로 나타내면 이렇게 되는데 아래와 같이 생략해준다.
# for 문을 단순히 한줄로 줄인 것이 아니다.
# 시퀀스의 요소를 전부 또는 일부를 처리하고, 그결과를 리스트로 돌려주는 간결한 방법

my_newlist = [x ** 2 for x in range(10)]
my_newlist2 = list(x ** 2 for x in range(10))
print(my_newlist)
print(my_newlist2)
print("------------------------------------")

# if문이 있을 때에는 어떻게 줄일까?
# list comprehension with if statements
numbers = list(range(10,100,10))
print(numbers)

my_numbers_1 = []
for number in numbers:
    if number % 4 == 0:
        my_numbers_1.append(number)

my_numbers_1 = [number for number in numbers if number % 4 == 0]
print(my_numbers_1)
#append 되어지는 값은 for문 왼쪽에 오른쪽에는 조건을 준다.

my_numbers_2 = []
for number in numbers:
    if number > 50:
        my_numbers_2.append(number + 7)
    else:
        my_numbers_2.append(number + 5)

my_numbers_2 = [number + 7 if number >= 50 else number + 5 for number in numbers]
print(my_numbers_2)
print("------------------------------------")
# 조건 표현식
# true_value <if> 조건식 <else> false_value

gugu = []
for a in range(2, 10):
    for b in range(1, 10):
        gugu.append(a * b)
print(gugu)
print("------------------------------------")
# 안의 for문이 9번 돌아야 밖의 for문이 돌게 된다.

gugu2 = [a * b for a in range(2, 10) for b in range(1, 10)]
print(gugu2)