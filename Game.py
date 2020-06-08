import random
sample_space = ['Rock', 'Paper', 'Scissor']
win = {'r' : 'Scissor', 'p': 'Rock', 's' : 'Paper'}
map = {'p':'Paper','r':'Rock','s':'Scissor'}
point,count = 0, 0
num = int(input('Enter Number of Turns ::  '))
while count < num:
    print('''
r : Rock
p : Paper
s : Scissor
    
q : quit
''')
    choice = input("Enter Choice :: ")
    comp = random.choice(sample_space)
    count+=1
    if choice == 'q':
        break
    if comp == map[choice]:
        print('Same choice')
        count-=1
    elif win[choice] == comp:
        point+=1
        print(f"Your choice {map[choice]} and computer choosed {comp} ---- 1 point")
    elif win[choice] != comp:
        print(f"Your choice {map[choice]} and computer choosed {comp} ---- 0 point")

print(f'Total Points :: {point} / {num}')
if point > num/2 :
    print("WINNERR WINNERR")
else:
    print('LOSERRRRRR')





