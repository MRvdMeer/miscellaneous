# This program will (attempt to) solve the assignment 'k-romeincalc' 
# from the VU course 'Inleiding Programmeren'.
# It will translate Roman numerals to Arabic (standard) numbers and back, 
# and be able to perform simple calculations on the Roman numerals (+, -, *, /)
# when running, the user can input three possible inputs to the console, 
# a Roman symbol followed by an operator followed by a second Roman symbol,
# just an operator and a Roman symbol, in which case the calculator takes the previous
# output and performs the operation on that, or a period (.) which ends the program.
# I'm currently still working on error handling in certain situations, although
# the program is already working.

import math

letter_values = {
	# Contains the default values for each of the Roman symbols.

	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000
}

special_combos = {
	# Contains the values for special combinations of Roman symbols.
	
	'IV': 4,
	'IX': 9,
	'XL': 40,
	'XC': 90,
	'CD': 400,
	'CM': 900	
}


# NOTE: Each type of special_combo (I-, X-, C-) can only appear ONCE. 

operators = ['+', '-', '*', '/']



def RomanToNumber(roman):
	# This function has been tested and works correctly except for proper error handling.

	# Translates a Roman numeral into a standard number. 
	# If the Roman numeral is not well-defined, this function gives an error message.
	
	input_number = roman.upper()
	position = 0
	result = 0
	length = len(input_number)
	base_10_characters = {'M': 0, 'C': 0, 'X': 0, 'I': 0}
	non_base_10_characters = ['D', 'L', 'V']
	still_allowed_characters = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
	
	while position < length:
		# check if next two characters are a special combination
		# if so, add their value correctly and skip 2 steps forward.
		# otherwise take just the single character and add its value
		# and skip a single step forward.
		
		if input_number[position] in still_allowed_characters:
			letter = input_number[position]
			index = still_allowed_characters.index(letter)
			if input_number[position:position+2] in special_combos:
				# print("Special Combo Activated!")
				s = input_number[position:position+2]
				still_allowed_characters = still_allowed_characters[index+1:]
				# print("Still allowed:", still_allowed_characters)
				result += special_combos[s]
				position += 2
			elif input_number[position] in letter_values:
				if letter in base_10_characters:
					base_10_characters[letter] += 1
					if base_10_characters[letter] >= 3:
						still_allowed_characters = still_allowed_characters[index+1:]
						# print("Still allowed:", still_allowed_characters)
				elif letter in non_base_10_characters:
					still_allowed_characters = still_allowed_characters[index+1:]
					# print("Still allowed:", still_allowed_characters)
				result += letter_values[input_number[position]]
				position = position + 1
		elif input_number[position] in letter_values:
			print("Invalid Input - : Roman number %s not well-defined." % roman)
			return
		else:
			print("Invalid Input - %s not a Roman character." % input_number[position])
			return
	return result
	




def NumberToRoman(number): 
	# This function has been tested and works correctly. The only thing that needs to be 
	# improved is the error handling for invalid inputs.
	
	# Translates a standard number into a Roman numeral.
	# For now, the upper limit of 3999 is given.
	# As there was no zero in the Roman Empire, zero returns a blank (empty) string
	# and negative numbers give an error message.
	
	values_to_check = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	letter_values = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
	result = ""
	input_number = number
	if not isinstance(number, int):
		# number should be an integer
		print("Invalid input - input number should be an integer")
		return
	elif number == 0:
		return ""
	elif number < 0:
		print("Input number is negative")
		return
	elif number >= 4000:
		print("Input number is too large - overflow")
		return
	else:
		for i in range(len(values_to_check)):
			while input_number >= values_to_check[i]:
				result = result + letter_values[i]
				input_number = input_number - values_to_check[i]
	return result





def RunCalc(roman1, operator, roman2):
	# This function has been tested and works properly.

	# reads input, a string which should contains exactly one operator and
	# two Roman numerals. Then performs the required calculation.
	
	print(roman1, operator, roman2)
	
	number1 = RomanToNumber(roman1)
	number2 = RomanToNumber(roman2)
	
	if operator == '+':
		return NumberToRoman(number1 + number2)
	elif operator == '-':
		return NumberToRoman(number1 - number2)
	elif operator == '*':
		return NumberToRoman(number1 * number2)
	elif operator == '/':
		return NumberToRoman(math.floor(number1 / number2))
	else:
		print("Operator not recognized")
		return
	


def Calculator():
	# Starts the calculator. Acceptable inputs are:
	# Two Roman numerals with an operator in between,
	# A single Roman numeral,
	# a period (.) - this stops the calculator.
	position = 0
	input_for_calculator = ""
	previous_output = ""
	roman1 = ""
	roman2 = ""
	operator = ""
	while True:
		# Run through the input and determine the position of the first operator.
		# Everything before the operator becomes the first Roman numeral.
		# Everything after becomes the second. If the operator is at the beginning
		# then the previous output becomes the first Roman numeral.
		
		input_for_calculator = input(">")
		if input_for_calculator == '.':
			print("Calculator ended.")
			break
			
		for character in input_for_calculator:
			if character in operators:
				operator = character
				position = input_for_calculator.index(operator)
				break
		
		if position == 0:
			roman1 = previous_output
		else:
			roman1 = input_for_calculator[:position]
		roman2 = input_for_calculator[position+1:]
		
		previous_output = RunCalc(roman1, operator, roman2)
		print("-----")
		print(previous_output)
	

Calculator()
