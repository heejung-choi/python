# 1. 리스트 (list)
my_list1 =[10,'문자열', True]
print(my_list1)
print(type(my_list1))
print(my_list1[0])

#2. 튜블(tuple)
# 튜플은 수정 불가능(불변, immutable)하고, 읽을 수 밖에 없다.
# 직접 사용하기 보다는 파이썬 내부에서 사용하고 있다.
my_tuple1 =(1,2)
print(my_tuple1)
print(type(my_tuple1))

# 어떻게 파이썬 내부에서 사용하고 있을까?
my_tuple2 = 1,2
print(my_tuple2)
print(type(my_tuple2))

x, y =1, 2
print(x)
print(y)
#tuple 읽기 전용 변수를 넣어줄때에는 내부적으로  tuple로 정해준다. 값이 변하지 않는다.

x,y=y,x
print(x)
print(y)
# 하나의 요소로 구성된 튜플은 값 뒤에 쉼표를 붙여서 만든다.

#3. range()
# range는 숫자의 시퀀스를 나타내기 위해 사용
print(type(range(1)))
print(range(10))
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#a=[]
#b=list()