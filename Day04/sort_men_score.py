'''
'''
'''
sort men score
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

#read men score
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

#====================================================================
#format score
'''
#v1.0
JamesScoreFormat = []
SarahScoreFormat = []
JulieScoreFormat = []
MikeyScoreFormat = []

for each in JamesScore:
	JamesScoreFormat.append(sanitize(each))
for each in SarahScore:
	SarahScoreFormat.append(sanitize(each))
for each in JulieScore:
	JulieScoreFormat.append(sanitize(each))
for each in MikeyScore:
	MikeyScoreFormat.append(sanitize(each))

print(sorted(JamesScoreFormat))
print(sorted(SarahScoreFormat))
print(sorted(JulieScoreFormat))
print(sorted(MikeyScoreFormat))
'''

#use list comprehension
'''
#v1.1.1
JamesScoreFormat = [sanitize(each) for each in JamesScore]
SarahScoreFormat = [sanitize(each) for each in SarahScore]
JulieScoreFormat = [sanitize(each) for each in JulieScore]
MikeyScoreFormat = [sanitize(each) for each in MikeyScore]

print(sorted(JamesScoreFormat))
print(sorted(SarahScoreFormat))
print(sorted(JulieScoreFormat))
print(sorted(MikeyScoreFormat))
'''
'''
#v1.1.2
print(sorted([sanitize(each) for each in JamesScore]))
print(sorted([sanitize(each) for each in SarahScore]))
print(sorted([sanitize(each) for each in JulieScore]))
print(sorted([sanitize(each) for each in MikeyScore]))
'''
#====================================================================

#====================================================================
#select top 3 score
#delete duplicate

#v1.0
JamesScoreFormat = [sanitize(each) for each in JamesScore]
SarahScoreFormat = [sanitize(each) for each in SarahScore]
JulieScoreFormat = [sanitize(each) for each in JulieScore]
MikeyScoreFormat = [sanitize(each) for each in MikeyScore]

JamesScoreUnique = []
SarahScoreUnique = []
JulieScoreUnique = []
MikeyScoreUnique = []

for each in JamesScoreFormat:
	if each not in JamesScoreUnique:
		JamesScoreUnique.append(each)
for each in SarahScoreFormat:
	if each not in SarahScoreUnique:
		SarahScoreUnique.append(each)
for each in JulieScoreFormat:
	if each not in JulieScoreUnique:
		JulieScoreUnique.append(each)
for each in MikeyScoreFormat:
	if each not in MikeyScoreUnique:
		MikeyScoreUnique.append(each)

print(JamesScoreUnique[0:3])
print(SarahScoreUnique[0:3])
print(JulieScoreUnique[0:3])
print(MikeyScoreUnique[0:3])

