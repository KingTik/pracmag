import numpy as np
import os, sys
sys.path.append(os.path.abspath(os.getcwd()))
from find import subset
from collect import collectData




def conc_data(in_data1, in_data2):
	
	data1 = np.array(in_data1[0])
	label1 = np.array(in_data1[1])

	


	data2 = np.array(in_data2[0])
	label2 = np.array(in_data2[1])

	sum_data=[]
	#sum_label=[]



	for i in range(len(data1)):
		
		sum_data.append(np.append(data1[i], data2[i]))
		
	#um_label.append(np.append(label1, label2))
	
	whole = []
	whole.append(sum_data)
	whole.append(label1)
	
	return sum_data, label1, whole



def conc_data_multiple(*args):

	
	
	if len(args) > 2:
		d1, l1, whole = conc_data(args[0], args[1])
		
		for i in range(len(args)-2):
		
			d1, l1, whole = conc_data(whole, args[i+2])
	else:
	
		d1, l1, whole = conc_data(args[0], args[1])
	
	return d1, l1, whole
	
	
'''
path = 'D:\Dropbox\praca magisterska\languages'
katalogi_train = subset(['test'], path)
data1, label1, w1 = collectData(10, katalogi_train, path, 'mfcc')

data2, label2, w2 = collectData(10, katalogi_train, path, 'sc')


'''











