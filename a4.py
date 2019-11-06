#FRED WATTS PYTHON ASSIGNMENT

#Writes a function that computes the length of a vector.  


##########################################################################
## Imports & Variables
##########################################################################

import math

loop_flag = 1


##########################################################################
## Helper Functions
##########################################################################



def vector_len():

	while loop_flag == 1:
		print("\n# VECTOR LENGTH CALCULATOR #\nType comma-seperated integers (ex: 1,2,5) or [E] to exit:")
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





	'''
    # Execute dig request
    rep = subprocess.check_output(
        f"dig @8.8.8.8 {name}", stderr=subprocess.STDOUT, shell=True,
    ).decode("utf-8").strip()

    # Parse output
    record = re.compile("^" + re.escape(name) + r'\.\s+(\d+)\s+IN\s+A\s+([\d\.]+)$', re.I)

    for line in rep.split("\n"):
        match = record.match(line)
        if match is not None:
            return match.groups()[-1]

    raise ValueError("Type comma-seperated vector values up to eight.")
	'''



#	print(list(map(lambda x: x ** 2,int_list)))
#	print(sum(list(map(lambda x: x ** 2,int_list))))


##########################################################################
## Main Method
##########################################################################

class CommandError(Exception):
    pass



while loop_flag == 1:

	print("\n\n### FRED WATTS PYTHON ASSIGNMENT MENU ###\nChoose tool: [V]ector Length, [E]xit")
	tool_choice = input("Type [V/E]:")
	if tool_choice == "v" or tool_choice == "V":
		vector_len()
	elif tool_choice == "e" or tool_choice == "E":
		break
	else:
		print("\nInvalid entry! Try Again.")