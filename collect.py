import numpy as np
import os, sys
sys.path.append(os.path.abspath(os.getcwd()))
from find import subset

'''
in:

katalogi - lista katalogow do odwiedzenia
path - sciezka do foldera z baza danych
feature_name - nazwa cechy
out:
whole_mfcc - cechy (x)
label_vector - odpowiedzi (y)

'''

def collectData(katalogi, path, feature_name):

	
	whole_feature = [] #np.empty([len(katalogi) * ilosc_elementow_zbioru, 52])
	whole_delta_mfcc = [] #np.empty([len(katalogi)*ilosc_elementow_zbioru, 52])
	#label_vector = np.empty([len(katalogi)*ilosc_elementow_zbioru, 1])
	label_vector = []
	labels = {'english':1, 'french': 2, 'german': 3, 'italian':4, 'polish':5, 'spanish': 6}



	for j, katalog in enumerate(katalogi):


		current_dir = path+'\\'+katalog
		#print('wejscie do katalogu: ' +  katalog)
		pliki = os.listdir(current_dir)
		os.chdir(current_dir)
		
		label = katalog.split('-')[0]   #czyli y dla maszyny
		
		pliki = [x for x in pliki if not '.flac' in x] #pliki ktore nie sa flac czyli te z danymi
		
		#list_delta_mfcc = [x for x in pliki if 'delta' in x] #rozdzielenie plikow
		#list_mfcc = list(set(pliki) - set(list_delta_mfcc))
		
		list = [x for x in pliki if feature_name in x]
		
		
		'''
		for i, file in enumerate(list_delta_mfcc):
			data_delta_mfcc = np.load(file)
			whole_delta_mfcc[i,:] = data_delta_mfcc
		'''	
		
		for i, file in enumerate(list):
			data = np.load(file)
			whole_feature.append(data)
			#data = np.array(data)
			#whole_feature = whole_feature + data
			
		
		for i in range(len(list)):
			label_vector.append(labels[label])
			#label_vector = label_vector + labels[label]
			
		whole = []
		whole.append(whole_feature)
		whole.append(label_vector)
	
	return whole_feature, label_vector, whole

	
#-------------------f()
path = 'D:\Dropbox\praca magisterska\languages'


#data_train = subset(['english', 'female'], path)
katalogi_train = subset([ 'female', 'train'], path)
#k = collectData(data_train, path, 'mfcc')









































	