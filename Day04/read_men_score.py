'''
	Day04 
'''
'''
	read file
'''

JamesScore = []
SarahScore = []
JulieScore = []
MikeyScore = []

try:
	with open('james.txt') as James_file:
		JamesScore = James_file.readline().strip().split(',')
	with open('sarah.txt') as Sarah_file:
		SarahScore = Sarah_file.readline().strip().split(',')
	with open('julie.txt') as Julie_file:
		JulieScore = Julie_file.readline().strip().split(',')
	with open('mikey.txt') as Mikey_file:
		MikeyScore = Mikey_file.readline().strip().split(',')
except IOError as err:
	print('IOError :' + str(err))

print(JamesScore)
print(SarahScore)
print(JulieScore)
print(MikeyScore)