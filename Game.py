import random
import os

while True:
	print("-----Gambling  game----- \n")
	input("Press ENTER to roll")

	random_num1 = random.randint(1, 9)
	random_num2 = random.randint(1, 9)
	
	os.system('clear')
	print(f"[{random_num1}] [{random_num2}]")

	if random_num1 == random_num2:
		os.system('clear')
		print(f"[{random_num1}] [{random_num2}]")
		print("you win! The numbers were the same.")
		continue
