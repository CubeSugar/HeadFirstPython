'''
	Day03 practise
	write file 
'''
'''
	V1.3
	format output
'''

import sys
#============================================
#import function
#============================================
"""
	this is a function, 
	the function :
	*print each item of the list
	*print every level indent
	*print to specify output 

	v1.3.0
"""

def print_list(the_list, indent = False, level = 0, output = sys.stdout):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_list(each_item, indent, level + 1, file = output)
		else:
			if indent:
				for tab_stop in range(level):
					print("\t", end = '', file = output)
			print(each_item, file = output)


surface = []
meaning = []

try:
	data = open('file_io_test.txt')
	for each_line in data:
		try:
			(sf, mn) = each_line.split('.')
			surface.append(sf)
			meaning.append(mn)
		except ValueError:
			pass
	data.close()
except IOError:
	print('file doesn\'t exist !')


try:
	with open('surface.txt', 'w') as sf_out:
		print_list(surface, output = sf_out)
	with open('meaning.txt', 'w') as mn_out:
		print_list(meaning, output = mn_out)
except IOError as err:
	print('file error :' + str(err))
