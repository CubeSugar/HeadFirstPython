'''
	Day03 practise
	write file 
'''
'''
	V1.1
	use try/except/finally
'''


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
	sf_out = open('surface.txt', 'w')
	mn_out = open('meaning.txt', 'w')

	print(surface, file = sf_out)
	print(meaning, file = mn_out)

except IOError:
	print('write file error')

finally:
	sf_out.close()
	mn_out.close()