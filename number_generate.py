def written_form(num):
	try:
		my_num = str(num)
		# high_numbers = ['', ' mille ', ' millions','milliards','billions']
		high_numbers = ['billions','milliards','millions','mille','']

		num_list = []
		length = len( my_num)
		pad =  -length % 3 + length
		my_num = my_num.zfill(pad)
		for i in range(0,len(my_num),3):
			num_list.append(my_num[i:i+3])
		
		value = ''
		# print(num_list)
		# print(len(num_list))
		for n, i in enumerate(num_list):
			temp_value = find_base_number(i).strip()
			unit = high_numbers[-len(num_list)+n ] 
			if temp_value == 'un':
				unit = unit.replace('s','')
			temp_value = temp_value + ' ' + unit 
			# print(temp_value)
			value += temp_value + ' '
			if value.strip() =='':
				value ='zero'
		return value.strip()

	except IndexError:

		return ''



def find_base_number(num):

	"""
	takes 3 digit number and gives the written form
	"""	
	entiers = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']
	dizaines = ['onze','douze','treize','quatorze','quinze','seize','dix-sept','dix-huit','dix-neuf']
	tens = ['vingt','trente','quarante','cinquante','soixante','soixante-dix','quatre-vingts','quatre-vingt-dix']

	base_numbers = entiers+ ['dix'] +dizaines

	for number in tens:
		base_numbers += [number]

		if 'vingts' in number:
			number = number.replace('vingts','vingt')

		if 'dix' in number:
			use_list = dizaines
			number =number[:-4]
		else:
			use_list = entiers
		temp_list = [number + ' et ' +x if x=='un' else number +'-'+x for x in use_list]
		base_numbers += temp_list
	# two special cases:
	special_case = {'soixante-onze': 'soixante-et-onze','quatre-vingt et un': 'quatre-vingt-un'}
	base_numbers = list(map(special_case.get,base_numbers,base_numbers))

	num = str(num)
	hundreds = ''
	if len(num) == 3 and num[0] !='0':
		base = int(num[1:])
		base = 'cents' if base == 0 else 'cent'
		hundreds = find_base_number(num[0])
		hundreds = 'cent ' if hundreds == 'un' else hundreds + f' {base} ' 
		num = num[1:]
	num = int(num)
	return hundreds if num == 0  else hundreds +  base_numbers[num-1]

if __name__ == '__main__':
	try:
		answer = int (input('Enter number:  ',))
		print (written_form(answer))
	except ValueError:
		print('please enter a valid number')