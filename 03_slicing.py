# slicing
sample_list = list(range(0,31))
print(sample_list)
print(sample_list[1:3])
# [|1,2,3,4]
# | 슬라이싱의 시작부분 (공간을 자른다.)
print(sample_list[10:-1]) 
# 끝에만 제외해서 하고 싶다면
print(sample_list[0:len(sample_list) :3])
#print(sample_list[0:31:3]) 동일
print (sample_list[::3])
print(sample_list[::-1]) 
# 뒤에서 부터 역순으로 
print(sample_list[1:1]) 
# 아무것도 안뜬다.