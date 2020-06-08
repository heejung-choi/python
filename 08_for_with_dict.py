classroom = {
    'teacher' : 'kim',
    'student1' : 'hong',
    'student2' : 'choi'
}

for member in classroom:
    print(member)
# 딕셔너리를 for문으로 돌리면 key 값만 나온다.
print("----------------------")

for member in classroom:
    print(classroom[member])
print("----------------------")
# 이렇게 뽑아도 되지만, 다르게 접근한다.

# dict.values 를 사용한다.
for member in classroom.keys():
    print(member)
# key
print("----------------------")

for member in classroom.values():
    print(member)
print("----------------------")

for key, value in classroom.items():
    print(key, value)