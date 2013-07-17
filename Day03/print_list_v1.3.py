"""
	this is a function, 
	the function :
	*print each item of the list
	*print every level indent
	*print to specify output 

	v1.3.0
"""
import sys

def print_list(the_list, indent = False, level = 0, output = sys.stdout):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_list(each_item, indent, level + 1, file = output)
		else:
			if indent:
				for tab_stop in range(level):
					print("\t", end = '', file = output)
			print(each_item, file = output)