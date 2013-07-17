'''
'''

import pickle

surface = []

try:
	with open('surface.txt', 'rb') as sf_in:
		surface = pickle.load(sf_in)
except PickleError as PlkError:
	print("PickleError : " + str(PlkError))
except IOError as ioerr:
	print("IOError : " + str(ioerr))