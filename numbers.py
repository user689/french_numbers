import random
import os
from number_generate import written_form

def print_cadre(w,messages=[]):
	messages.insert(0,'')
	messages.append('')
	h= len(messages)
	print('*'*w)
	for i in range(h):
		print('*' +('{:^'+str(w-2)+'}').format(messages[i]) +'*')
	print('*'*w)

def validate(var, inp=[]) :
	for i in inp:
		if i.lower() in var.lower():
			return True
		else:
			return False

def help(mode):
	os.system('cls')
	if mode == 1:
		print_cadre(120,messages=['You have chosen mode 1: Counting ', 
			'You need to write in french the number that comes after my number',
			'The game has 5 levels',
			'',
			'Every successful answer provides 1 point',
			'Every Wrong answer deducts 2 points',
			'Get 10 points to advance to the next level',
			'',
			'type quit or exit whenever you want to exit.',
			'type help to get show this screen',
			'Press Enter to continue'
		])
		input()
	elif mode ==2:
		print_cadre(120,messages=['You have chosen mode 2: Addition ', 
			'You need to add two numbers and type the answer in french',
			'The game has 5 levels',
			'',
			'Every successful answer provides 1 point',
			'Every Wrong answer deducts 2 points',
			'Get 10 points to advance to the next level',
			'',
			'type quit or exit whenever you want to exit.',
			'type help to get show this screen',
			'Press Enter to continue'
		])
		input()
	else:
		pass

def base_game(points=0,level=1,max_level=7,max_points=10):
	os.system('cls')
	levels = [10**x for x in range(2,max_level)]
	number = random.randint(0,levels[level-1])
	if points ==max_points:
		points =0
		level +=1 
	elif points < 0:
		points = 0 
	if level == max_level-1:
		print_cadre(120,messages=[
			'Congratulations! You won the game!'
			])
		input()
		return -1,-1,-1,[]
	print_cadre(120, messages=[
		f' Points: {points}' + ' ' * 96 + f'level: {level}/5 '
	])
	return number, points, level,levels


def counting(points =0, level=1, max_level=7,max_points=10):
	help(1)

	while True:
		number, points, level, levels = base_game(points=points,level=level,max_level=max_level,max_points=max_points)
		if level < 0:
			break
		correct_answer = written_form(number+1)
		print('')
		print(f'Ce qui vient apres: {number}')
		answer=(input('> '))
		if validate(answer, [correct_answer]):
			# print('correct! Vous avez 1 point')
			points +=1 
		elif validate(answer,['quit','exit']):
			break
		elif validate(answer,['help']):
			help(1)
			continue

		else:
			print(f'Faux! la bonne reponse etait: {correct_answer}')
			points -=2
			input()

def addition(points=0,level=1,max_level=7,max_points=10):
	help(2) # todo: add help section 2

	while True:
		number, points, level, levels = base_game(points=points,level=level,max_level=max_level,max_points=max_points)
		if level <0: 
			break
		random_number = random.randint(0, [x for x in range(15,1000,20)][level -1])
		correct_answer = written_form(number + random_number)
		print('')
		print(f'que fait {number} et {random_number}?')
		answer=(input('> '))
		if validate(answer, [correct_answer]):
			# print('correct! Vous avez 1 point')
			points +=1 
		elif validate(answer,['quit','exit']):
			break
		elif validate(answer,['help']):
			help(1)
			continue

		else:
			print(f'Faux! la bonne reponse etait: {correct_answer}')
			points -=2
			input()




os.system('cls')
print_cadre(120,messages=[
	'Welcome to the french numbers game',
	'This game is intended for french number practice',
	'This game has several modes',
	'',
	'',
	'',
	'Select mode:                                    ',
	'',
	'1: counting up                                  ',
	'2: simple addition (2 numbers)                  '
	])
valid_choices = [x for x in range(3)]
choice =''
while choice not in map(str,valid_choices):
	choice = input('> ')



if choice == '1':
	counting()
elif choice =='2':
	addition()