#FRED WATTS PYTHON ASSIGNMENT


##########################################################################
## Imports & Variables
##########################################################################

import math

loop_flag = 1


##########################################################################
## Functions
##########################################################################




def vector_len():

	while loop_flag == 1:
		print("\n### VECTOR LENGTH CALCULATOR ###\nType comma-seperated integers (ex: 1,2,5) or [E] to exit:")
		input_string = input()
		if input_string == "e" or input_string == "E":
			break
		else:
			input_list = input_string.split(",")
			int_list = []
			for i in input_list:
				try:
					x = int(i)
					int_list.insert(len(int_list),x) 	
				except ValueError:
					print(i,"is not an integer.")
			vlength = math.sqrt(sum(list(map(lambda x: x ** 2,int_list))))
			print("\nInput:",int_list)
			print("Vector Length:",vlength)


def vector_dot_prod():
	while loop_flag == 1:
		vec1_list = []
		vec2_list = []
		print("\n### VECTOR DOT PRODUCT CALCULATOR ###")
		for j in [1, 2]:
			print("Enter Vector",j,", Type comma-seperated integers (ex: 1,2,5)")
			input_string = input()
			input_list = input_string.split(",")
			int_list = []
			for i in input_list:
				try:
					x = int(i)
					if j == 1:
						vec1_list.insert(len(vec1_list),x)
					else:
						vec2_list.insert(len(vec2_list),x)
				except ValueError:
					print(i,"is not an integer.")
		if vec1_list == [] or vec2_list == []:
			print("\nVector 1:",vec1_list," Vector 2:",vec2_list,"\nOne or both vectors is empty. Try again.")
			continue
		elif len(vec1_list) != len(vec2_list):
			print("\nVector 1:",vec1_list," Vector 2:",vec2_list,"\nThe vectors are not the same length. Try again.")
			continue
		else:
			print("\nVector 1:",vec1_list," Vector 2:",vec2_list)
			vec_count = 0
			product_list = []
			while vec_count < len(vec1_list):
				product_list.insert(len(product_list),vec1_list[vec_count] * vec2_list[vec_count])
				vec_count += 1
			print("Vector Dot Product:",sum(product_list),'\n')
		end_code = input("Type [E] to exit to menu or another input to restart:  ")
		if end_code == "e" or end_code == "E":
			break


def assignments():
	print("\n### ASSIGNMENT Tests ###\n\n")
	print("-----------------------------------------\nAssignment #2 - Exercise #1: Vector Length\n-----------------------------------------")
	vlength = math.sqrt(sum(list(map(lambda x: x ** 2,[8,7,6]))))
	print("v = [8,7,6]\nlength(v) =",vlength,'\n')
	vlength = math.sqrt(sum(list(map(lambda x: x ** 2,[9,2,-3,8,-4]))))
	print("v = [9,2,-3,8,-4]\nlength(v) =",vlength)
	print("\n\n-----------------------------------------\nAssignment #2 - Exercise #2: Dot Product\n-----------------------------------------")
	vec_count = 0
	vec1_list = [8,7,6]
	vec2_list = [9,-4,3]
	product_list = []
	while vec_count < 3:
		product_list.insert(len(product_list),vec1_list[vec_count] * vec2_list[vec_count])
		vec_count += 1
	print("Vector 1:",vec1_list," Vector 2:",vec2_list)
	print("Vector Dot Product:",sum(product_list),'\n')



##########################################################################
## Main Method
##########################################################################

class CommandError(Exception):
    pass



while loop_flag == 1:

	print("\n\n### FRED WATTS PYTHON FUNCTIONS MENU ###\nChoose function: [A]ssignment Tests, [V]ector Length, Vector [D]ot Product, [E]xit")
	tool_choice = input("Type [A/V/D/E]:")
	if tool_choice == "v" or tool_choice == "V":
		vector_len()
	elif tool_choice == "a" or tool_choice == "A":
		assignments()
	elif tool_choice == "d" or tool_choice == "D":
		vector_dot_prod()
	elif tool_choice == "e" or tool_choice == "E":
		break
	else:
		print("\nInvalid entry! Try Again.")