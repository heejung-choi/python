import random

numbers = [1,2,3,4,5]

result = random.choice(numbers)

print(result)

pick = random.choice(range(10))

print(pick)

n = random.sample(range(20), 3)

print(n)

print(dir(random))