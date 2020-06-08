is_started = False
while True:
	command = input('> ').lower()
	if command == 'help':
		print("""
Start-To start the car
Stop-To stop the car'
quit-To exit
		""")
	elif command == 'start':
		if is_started:
			print('Car is already Started')
		else:
			is_started = True
			print('Car Started')

	elif command == 'stop':
		if not is_started:
			print('Car is already Stopped.')
		else:
			is_started = False 
			print('Car Stopped.')		


	elif command == 'quit':
		break
	else:
		print("I Don't Understand")
