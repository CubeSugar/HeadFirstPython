"""Day 1 practise"""
"""
	this is a function, 
	the function print each item of the list

	v1.0.0
"""

def print_list(the_list):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_list(each_item)
		else:
			print(each_item)


