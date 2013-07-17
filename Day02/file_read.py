'''
	Day 2 practise
'''

'''
	file io practise
	read file and print the file as the same format
'''

import os

os.getcwd()

os.chdir('../Documents/ProgrammingExercise/Python/Day02/FileIOTest')

if os.path.exists('file_io_test.txt'):
#try:
	file = open('file_io_test.txt')

	for each_line in file:
		if not each_line.find('.') == -1:
		#try:
			(surface, meaning) = each_line.split('.', 1)
			print(surface)
			print(meaning)
		#except: '''ValueError'''
			#pass
	file.close()
else:
#except: '''IOError'''
	print('no such file')