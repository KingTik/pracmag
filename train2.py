import numpy as np
import os, sys
sys.path.append(os.path.abspath(os.getcwd()))
from collect import collectData
from find import subset
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklej import conc_data_multiple

path = 'D:\Dropbox\praca magisterska\languages'



def print_shape(data, name="feature"):
	
	data1 = np.array(data[0])
	data2 = np.array(data[1])
	
	print("data "+ name+": " + str(data1.shape))
	print("label "+ name+": " + str(data2.shape))


katalogi_train = subset(['train'], path)
katalogi_test = subset(['test'], path)

### KATALOGI TRENINGOWE ###
mfcc_data_train, mfcc_label_train, whole_mfcc_train = collectData( katalogi_train, path, 'mfcc')
delta_mfcc_data_train, delta_mfcc_label_train, whole_delta_mfcc_train =collectData(katalogi_train, path, 'delta')
pause_data_train, pause_label_train, whole_pause_train = collectData(katalogi_train, path, 'pause')
rms_data_train, rms_label_train, whole_rms_train = collectData(katalogi_train, path, 'rms')
sc_data_train, sc_label_train, whole_sc_train = collectData(katalogi_train, path, 'sc')
#zrc_data_train, zrc_label_train, whole_zrc_train = collectData( katalogi_train, path, 'zrc')
# tonn_data_train, tonn_label_train, whole_tonn_train = collectData( katalogi_train, path, 'tonnentz')
line_data_train, line_label_train, whole_line_train = collectData(katalogi_train, path, 'polyline')
quad_data_train, quad_label_train, whole_quad_train = collectData( katalogi_train, path, 'polyquad')

### KATALOGI TESTOWE ###
mfcc_data_test, mfcc_label_test, whole_mfcc_test = collectData( katalogi_test, path, 'mfcc')
delta_mfcc_data_test, delta_mfcc_label_test, whole_delta_mfcc_test = collectData( katalogi_test, path, 'delta')
pause_data_test, pause_label_test, whole_pause_test = collectData( katalogi_test, path, 'pause')
rms_data_test, rms_label_test, whole_rms_test = collectData( katalogi_test, path, 'rms')
sc_data_test, sc_label_test, whole_sc_test = collectData(katalogi_test, path, 'sc')
#zrc_data_test, zrc_label_test, whole_zrc_test  = collectData( katalogi_test, path, 'zrc')
#tonn_data_test, tonn_label_test, whole_tonn_test = collectData( katalogi_test, path, 'tonnentz')
line_data_test, line_label_test, whole_line_test = collectData( katalogi_test, path, 'polyline')
quad_data_test, quad_label_test, whole_quad_test = collectData( katalogi_test, path, 'polyquad')

#wszystkie cechy

d1, l1, whole1 = conc_data_multiple(whole_mfcc_train, whole_delta_mfcc_train, whole_pause_train, whole_rms_train, whole_sc_train,  whole_line_train, whole_quad_train)
d2, l2, whole2 = conc_data_multiple(whole_mfcc_test, whole_delta_mfcc_test, whole_pause_test, whole_rms_test, whole_sc_test, whole_line_test, whole_quad_test)





'''
svm_m = svm.SVC()
svm_m.fit(d1, l1)

#t_w, t_l_vec = collectData(5, katalogi_test, path, name)
predictions = svm_m.predict(d2)
print("skutecznosc wszystkich cech na raz: "+str(accuracy_score(l2, predictions)))	#predictions

'''
































