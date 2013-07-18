'''
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

class Athlete:
	def __init__(self, a_name, a_bday = None, a_times = []):
		self.m_Name = a_name
		self.m_bday = a_bday
		self.m_times = a_times

	def add_time(self, a_time = None):
		self.m_times.append(a_time)

	def add_times(self, a_times = []):
		self.m_times.extend(a_times)

	def top3times(self):
		return (sorted(set([sanitize(each) for each in self.m_times]))[0:3])


