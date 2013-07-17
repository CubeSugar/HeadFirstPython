'''
'''
'''
select men top score
'''

#define function format time_string
def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins, secs) = time_string.split(splitter)

	return (mins + '.' + secs)
#end def

#define function read file
def readFile(filename):
	try:
		with open(filename) as InputFile:
			list = InputFile.readline().strip().split(',')
			return list
	except IOError as err:
		print('IOError : ' + str(err))
		return (None)
#end def

#read men score
JamesScore = []
SarahScore = []
JulieScore = []
MikeyScore = []

JamesScore = readFile(filename = 'james.txt')
SarahScore = readFile(filename = 'sarah.txt')
JulieScore = readFile(filename = 'julie.txt')
MikeyScore = readFile(filename = 'mikey.txt')

print(sorted(set([sanitize(each) for each in JamesScore]))[0:3])
print(sorted(set([sanitize(each) for each in SarahScore]))[0:3])
print(sorted(set([sanitize(each) for each in JulieScore]))[0:3])
print(sorted(set([sanitize(each) for each in MikeyScore]))[0:3])
