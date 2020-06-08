guess_count = 1		#A Guessing Game
guess_limit = 3
secret_number = 5
while guess_count <= guess_limit:
	guess = int(input('Guess: '))
	guess_count += 1
	if guess == 5:
		print('You won')
		break
	
else:	#this else belongs to while loop, not to the if loop above
	print('Sorry you failed ')
#unlike other languages , In python we also have an else condition for while loop,this else will run only after when the while loop is terminated internally(by itself) not by the break statement entered by the coder. 
	

