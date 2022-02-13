import random

liste=['A', 'T', 'G', 'C']
for i in range(0, 5):
	print(str(random.choices(liste, k=random.randint(2,4))))