'''
	Day 2 practise
'''

'''
	file io practise
	read file and print the file by new format
'''

import os

os.getcwd()

os.chdir('../Day02/FileIOTest')

if os.path.exists('file_io_test.txt'):
#try:
	file = open('file_io_test.txt')

	sf = []
	mn = []

	for each_line in file:
		if not each_line.find('.') == -1:
		#try:
			(surface, meaning) = each_line.split('.', 1)
			#print(surface)
			sf.append(surface)
			#print(meaning)
			mn.append(meaning)
		#except: '''ValueError'''
			#pass
	file.close()

	print(sf)
	print(mn)

else:
#except: '''IOError'''
	print('no such file')