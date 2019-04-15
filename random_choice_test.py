import random

vals = ['13w4', '12421', '421421', 45252]

val = random.randint(1, 10)
val2 = random.choice(vals)
val3 = random.choices(vals, k=10)
#  weight=[] = 비율

print(val)
print(val2)
print(val3)
print(random.sample(vals, k=3))
