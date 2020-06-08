# 논리 연산자
print('-----and-----')
print(True and True)
print(True and False)
print(False and False)
print('-----or-----')
print(True or True)
print(True or False)
print(False or False)
print('-----not-----')
print(not True)
print(not 0)

# 단축평가
# and 는 둘다 true여야 하는데...
print('-- 단축평가 --')
vowels = 'aeiou'
print(('a' and 'b') in vowels)#b가 있는가를 마지막으로 보고 끝내기 때문에 b가 없어서 F
print(('b' and 'a') in vowels)#a가 있는가를 마지막으로 보고 끝내기 때문에 a가 있어서 T
print('a' and 'b')
print('b' and 'a')

# and 는 둘다  True인 경우만 True이기 때문에
# 첫번째 값이 True라도 두번째 값을 확인해야 한다.
print(3 and 5) #5
print(3 and 0) #0 
print(0 and 3) #0 앞이 0이면 F라고 보기 때문에 뒤의 숫자를 보지 않는다.
print(0 and 0) #0


print(5 or 3) #5
print(3 or 0) #3
print(0 or 3) #3
print(0 or 0) #0