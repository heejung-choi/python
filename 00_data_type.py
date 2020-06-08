print('hello, world')

number =10
string = '문자열'
bools =True  # 앞글자가 대문자.
print(number, string, bools)

# 수치형 (int, float, complex)
a = 3
print(type(a)) # class 'int'라고 나온다.

# bool
print(type(False))# class 'bool'라고 나온다.

#0, 0.0, (), [], {}, '', None -> 얘네는 False

# 문자형
greeting =  'hi'
name = 'harry'
print(greeting, name)
print(type(name))

# 사용자가 기본적으로 입력하는 것은 string
# input으로 입력받는다. 숫자를 입력하더라도 string으로 받는다.
#age= input()
#print(type(age))
# """를 세번 감싸서 입력하면 개행문자 없이 여러줄을 입력할 수 있다.
print("""
개행문자 없이
여러 줄을
그대로 출력가능합니다.
""")

print(3 * 'hey' + 'yo!') # heyheyheyyo!

# string interpolation
name ='choi'
# 1. %-formatting
print('hello, %s' % name) #hello, choi
# 2. .format()
print('hello, {}'.format(name)) #hello, choi
# 3. f-string (Literal String Interpolation)
print(f'hello, {name}')

pi = 3.141592
print(f'원주율은 {pi:.4}, 반지름이 2일때 원의 넓이는 {pi*2*2}')
