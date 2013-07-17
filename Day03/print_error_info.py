'''
	Day03 practise
'''
'''
	print error info
'''

try:
	data = open('missing.txt')
	print(data.readline())
except IOError as err:
	#define a error name 'err' for IOError

	#str() function convert any object that meets the condition to string 
	print('file error :' + str(err))
finally:
	#locals() BIF return a set of all variable in current field
	if 'data' in locals():
		data.close()