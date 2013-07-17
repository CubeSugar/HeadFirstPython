'''
	Day 05  
'''
'''
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

SarahInfo = readFile(filename = 'sarah2.txt')

'''
#v1.0
(Sarah_Name, Sarah_BDay) = SarahInfo.pop(0), SarahInfo.pop(0)
print(Sarah_Name + "'s fastest times are: " + str(sorted(set([sanitize(each) for each in SarahInfo]))[0:3]))
'''

#v1.1
Sarah = {}
Sarah['Name'] = SarahInfo.pop(0)
Sarah['BDay'] = SarahInfo.pop(0)
Sarah['Scores'] = SarahInfo

print(Sarah['Name'] + "'s fastest times are : " + str(sorted(set(sanitize(each) for each in Sarah['Scores']))[0:3]))
