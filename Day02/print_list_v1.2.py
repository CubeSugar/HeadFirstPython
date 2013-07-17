"""Day 2 practise"""
"""
	this is a function, 
	the function print each item of the list
	besides, it also print every level indent

	v1.1.0
"""

def print_list(the_list, level = 0):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_list(each_item， level + 1)
		else:
			for tab_stop in range(level):
				print("\t", end='')
			print(each_item)

"""
	this is a function, 
	the function print each item of the list
	besides, it also print every level indent

	v1.2.0
"""

def print_list2(the_list, indent = False, level = 0):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_list2(each_item, indent, level + 1)
		else:
			if indent:
				for tab_stop in range(level):
					print("\t", end = '')
			print(each_item)

