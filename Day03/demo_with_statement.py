'''
	Day03 practise
'''
'''
	print error info

	use 'with' instead 'finally' to auto close file
'''

try:
	with open('missing.txt') as data:
		print(data.readline())
except IOError as err:
	#define a error name 'err' for IOError

	#str() function convert any object that meets the condition to string 
	print('file error :' + str(err))
