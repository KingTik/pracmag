import numpy as np
import os, sys
sys.path.append(os.path.abspath(os.getcwd()))
from collect import collectData
from find import subset
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
import csv
from sklej import conc_data_multiple

	
path = 'D:\Dropbox\praca magisterska\languages'


katalogi_train = subset(['train'], path)
katalogi_test = subset(['test'], path)

feature_names = ['mfcc', 'delta', 'rms', 'sc', 'polyline', 'polyquad']


def train(data_train, data_test, features,  path='D:\Dropbox\praca magisterska\languages'):

	result = ''
	w2, l_vec2, whole_pause  = collectData( data_train, path, 'pause')
	t_w2, t_l_vec2, t_whole_pause  = collectData( data_test, path, 'pause')	
	
	
	for feature in features:

		tree_array = []
		bayes_array = []
		svm_array = []
		
		#get data
		#w, l_vec, _  = collectData( data_train, path, feature)
		#t_w, t_l_vec, _  = collectData( data_test, path, feature)
		
		w, l_vec, whole_feature  = collectData( data_train, path, feature)
		t_w, t_l_vec, t_whole_feature  = collectData( data_test, path, feature)	
		
		w, l_vec, _  = conc_data_multiple(whole_feature, whole_pause)
		t_w, t_l_vec, _  = conc_data_multiple(t_whole_feature,  t_whole_pause)
		
		#decision tree
		tree_m = tree.DecisionTreeClassifier()
		tree_m.fit(w, l_vec)

		
		predictions_tree = tree_m.predict(t_w)
		tree_array.append(accuracy_score(t_l_vec, predictions_tree))

		
		#bayes
		bayes_m = GaussianNB()
		bayes_m.fit(w, l_vec)
		predictions_bayes = bayes_m.predict(t_w)
		bayes_array.append(accuracy_score(t_l_vec, predictions_bayes))
		
		#svc
		svm_m = svm.SVC()
		svm_m.fit(w, l_vec)
		predictions_svc = svm_m.predict(t_w)
		svm_array.append(accuracy_score(t_l_vec, predictions_svc))
		
		
		
		
		result = result + str(feature) + '\n'
		result = result + 'bayes ' + str(bayes_array) + ' tree' + str(tree_array) + ' svc ' + str(svm_array) + '\n'
		
		
		
			
	return result	




#print(train(katalogi_train, katalogi_test, ['mfcc'], save_to_file=1))


# pelne katalogi
print('pelne katalogi \n')
print(train(katalogi_train, katalogi_test, feature_names))
print('\n')


#kobiety
print('kobiety \n')
katalogi_train = subset([ 'female', 'train'], path)
katalogi_test = subset(['female', 'test'], path)
print(train(katalogi_train, katalogi_test, feature_names))
print('\n')

#mezczyzni
print('mezczyzni \n')
katalogi_train = subset([ 'male', 'train'], path)
katalogi_test = subset(['male', 'test'], path)
print(train(katalogi_train, katalogi_test, feature_names))
print('\n')

















'''
os.chdir('D:\Dropbox\praca magisterska\librosa')

f = open('example.csv','w+')
f.write("mfcc,1234")
f.write("delta,4321")
f.close()



'''








