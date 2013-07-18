'''
	Day06 
'''
'''
	mvc ch7
'''
import pickle

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

#define class AthleteList 
class AthleteList(list):
	def __init__(self, a_name, a_bday = None, a_times = []):
		list.__init__([])
		self.m_Name = a_name
		self.m_BDay = a_bday
		self.extend(a_times)

	def top3times(self):
		return (sorted(set([sanitize(each) for each in self]))[0:3])


#define function read file
#return object of AthleteList
def readFile(filename):
	try:
		with open(filename) as InputFile:
			list = InputFile.readline().strip().split(',')
			return (AthleteList(list.pop(0), list.pop(0), list))
	except IOError as err:
		print('IOError : ' + str(err))
		return (None)
#end def

#define function
def storePickle(filelist):
	all_athletes = {}
	for each in filelist:
		ath = readFile(each)
		all_athletes[ath.m_Name] = ath
	try:
		with open('athletes.pickle', 'wb') as athf:
			pickle.dump(all_athletes, athf)
	except PickleError as PklErr:
		print("PklErr : " + str(PklErr))
	return (all_athletes)


#define function
def loadPickle():
	all_athletes = {}
	try:
		with open('athletes.pickle', 'rb') as athf:
			all_athletes = pickle.load(athf)
	except IOError as IOErr:
		print("IOErr : " + str(IOErr))
	return (all_athletes)