import random

import requests #크롤링

#numbers = [1,2,3,4,5,6,7,... 45]

numbers = range(1, 45)

#print(list(numbers))

pick = random.sample(numbers, 6)

print(pick)

lotto_url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=914'

response = requests.get(lotto_url)

lotto_info = response.json()

print(lotto_info)

bonus_num = lotto_info['bnusNo']  # 대괄호로 접근   만약 키값을 bnusNoa 로 없는 걸 주면 key 값이 잘 못 되었다고 error 뜸

bonus_num = lotto_info.get('bnusNo')  # .get 으로 접근   , none(이라고 없는 값이라고 뜸)

print(bonus_num) 

#print(dir(response))

#print(response.content) # "" 로 나옴.

#print(response.json())  #json은 무조건 "" 써야 하는데, ' ' 로 나왔다는 것은 json이 아니라는 뜻

#print(type(response.json()))

winner = []

lotto_info.get('drwtNo1')

#winner.append(lotto_info.get('drwtNo1'))

#winner.append(lotto_info.get('drwtNo2'))

#winner.append(lotto_info.get('drwtNo3'))

#winner.append(lotto_info.get('drwtNo4'))

#winner.append(lotto_info.get('drwtNo5'))

#winner.append(lotto_info.get('drwtNo6'))

for i in range(1,7):

  winner.append(lotto_info.get(f'drwtNo{i}'))

print(winner)

#pick, winner 비교해서 pick이 몇등에 당첨되었는지 확인해보기.

match_num = set(pick) & set(winner) # 전체 숫자중 교집합으로 몇개가 맞는지를 확인해서 몇등인지를 파악할 수 있음.

print(len(match_num))