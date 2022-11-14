import random
jackpot=random.randint(20,30)
guess=int(input("chal guess kar"))
counter=1
while guess != jackpot:
	if guess<jackpot:
	print("guess higher")
	else:
	print("guess lower")
	guess=int(input("chal guess kar"))
	counter +=1
print("Sahi jawab")
print("you took", counter, 'attempt')
