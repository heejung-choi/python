# 1. set 
# 대중적으로 많이 쓰지는 않는다.
set_a = {1,2,3}
set_b = {3,6,9}

print(set_a - set_b) #차집합
print(set_a | set_b) #합집합
print(set_a & set_b) #교집합

set_c = set() #set는 빈괄호로 만들지 못한다. dictionary와 겹치기 때문 이렇게 만들어줘야 한다.

# set_c= {1,1,1} => 1 중복을 제거하기 때문에 어차피 1이다.

# 2. dictionary
dict_a= {}
print(type(dict_a))
dict_b= dict() #이것보다는 {}이것이 메모리 사용을 줄여준다.
# dict_a= {1:1, 2:2, 3:3, 1:4}  #키는 겹치면 안된다. 겹칠 경우 나중에 선언된 키로 설정된다.
# print(dict_a) #{1: 4, 2: 2, 3: 3}

phone_book = {
    '서울' : '02',
    '경기' : '031'
}
print(phone_book['서울'])

#dir() # 특정 객체가 가지고 있는 리스트들을 나열해 준다
print(dir(dict))

print(phone_book.values()) # 값들만 출력할 수 있다.
#print(phone_book.get('서울'))
#print(phone_book.__str__)
#print(help(dict))

