import librosa
import sys, os, re
import numpy as np
sys.path.append(os.path.abspath(os.getcwd())) # <-sciezka do find.py
from find import subset
from pauzy import get_pauses_stats

path = 'D:\Dropbox\praca magisterska\languages'
katalogi = subset([], path)

def make_stats(in_array):
	return [np.average(in_array), np.min(in_array), np.max(in_array), np.std(in_array), np.cov(in_array), np.median(in_array), np.var(in_array), np.mean(in_array)]
	
	
	
def poly_stats(mat_in):
	
	ret_arr = []
	
	for p in mat_in:
		#ret_arr.append(make_stats(p))
		ret_arr = ret_arr+make_stats(p)

	return ret_arr
	
	
def mfcc_array( y, sr, mfcc_number ):

	#y, sr = librosa.load(file)
	mel = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=mfcc_number) 

	ret_array = []

	for m in mel:
		ret_array = ret_array + make_stats(m)
		

		
	ret_array = np.array(ret_array)
	return ret_array

def delta_mfcc_array( y, sr, mfcc_number):

	#y, sr = librosa.load(file)
	mel = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=mfcc_number) 
	delta_mel = librosa.feature.delta(mel)
	ret_array = []

	for m in delta_mel:
		ret_array = ret_array + make_stats(m)
		

		
	ret_array = np.array(ret_array)
	return ret_array	

for katalog in katalogi:

	current_dir = path+'\\'+katalog
	print('wejscie do katalogu: ' +  katalog)
	pliki = os.listdir(current_dir)
	os.chdir(current_dir)
	
	#regex = re.compile('*.flac')
	pliki = [x for x in pliki if '.flac' in x] #odfiltrowanie tylko plikow typu .flac
	
	for fileName in pliki:
		#fileName = '01.flac'
		print(fileName)
		y, sr = librosa.load(fileName)

		print('processing file: ' + fileName)




		
			#DELTA MFCC
		newFileName = fileName.split('.')[0]
		np.save(newFileName+'_delta', delta_mfcc_array(y, sr, 13) )
		


	
		
	### MFCC + delta MFCC ###


		#mfcc_number = 13		#ilosc mfcc
		#subfeature_number = 4	#ilosc cech wyciagnietych z mfcc (srednia, std, itp...)

		#funkcja mfcc sama dzieli sygnał na ramki 
		#mel = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=mfcc_number) 	#MFCC
		#delta_mel = librosa.feature.delta(mel)

		
		#MFCC
		newFileName = fileName.split('.')[0]
		np.save(newFileName+'_mfcc', mfcc_array(y, sr, 13) )
		
	
		
	

			### RMS + ZERO CROSS ###
		rms = librosa.feature.rmse(y=y)
		zcr = librosa.feature.zero_crossing_rate(y=y)
		zcr_matrix = make_stats(zcr)#[np.average(zcr), np.min(zcr), np.max(zcr), np.std(zcr)]
		rms_matrix = make_stats(rms)#[np.average(rms), np.min(rms), np.max(rms), np.std(rms)]
		
		newFileName = fileName.split('.')[0]
		np.save(newFileName+'_rms', rms_matrix)
		np.save(newFileName+'_zcr', zcr_matrix)
		
				### PAUSE TIME RATE###
		pause_matrix = get_pauses_stats(y)
		
		newFileName = fileName.split('.')[0]
		np.save(newFileName+'_pause', pause_matrix)	


		### ZERO CROSSING RATE###
		zcr = librosa.feature.zero_crossing_rate(y=y)
		
		zcr_matrix =make_stats(zcr) #[np.average(zcr), np.min(zcr), np.max(zcr), np.std(zcr)]
		
		newFileName = fileName.split('.')[0]
		np.save(newFileName+'_zcr', zcr_matrix)		
		

			### SPECTRAL CENTROID ###
		# (2584x1)
		sc = librosa.feature.spectral_centroid(y=y)
		
		sc_matrix = make_stats(sc)#[np.average(sc), np.min(sc), np.max(sc), np.std(sc)]
		
		newFileName = fileName.split('.')[0]
		np.save(newFileName+'_sc', sc_matrix)	
		
		### POLY ###	
		S = np.abs(librosa.stft(y))
		line = librosa.feature.poly_features(S=S, sr=sr)

		quad = librosa.feature.poly_features(S=S, order=2)


		line_matrix  = poly_stats(line)
		quad_matrix  = poly_stats(quad)
		
		np.save(newFileName+'_polyline', line_matrix)	
		np.save(newFileName+'_polyquad', quad_matrix)	
		
		### tonal centroid features ###
		
		tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
		tonnetz_matrix  = poly_stats(tonnetz)
		np.save(newFileName+'_tonnetz', tonnetz_matrix)	
		
'''	
		### RMS ###
		# (2584x1)
		rms = librosa.feature.rmse(y=y)
		
		rms_matrix = make_stats(rms)#[np.average(rms), np.min(rms), np.max(rms), np.std(rms)]
		
		newFileName = fileName.split('.')[0]
		np.save(newFileName+'_rms', rms_matrix)
	
		
	
		### MFCC i delta MFCC ###


		mfcc_number = 13		#ilosc mfcc
		subfeature_number = 4	#ilosc cech wyciagnietych z mfcc (srednia, std, itp...)

		#funkcja mfcc sama dzieli sygnał na ramki 
		mel = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=mfcc_number) 	#MFCC
		delta_mel = librosa.feature.delta(mel)



		subfeature_mfcc_matrix = np.empty(subfeature_number * mfcc_number)
		subfeature_delta_mfcc_matrix  = np.empty(subfeature_number * mfcc_number)
		#subfeature_delta_mfcc_matrix = np.zeros([subfeature_number, mfcc_number])

		for i in range(0, mfcc_number):

			slice = mel[i,:]
			frame_avg = np.average(slice)
			frame_min = np.amin(slice)
			frame_max = np.amax(slice)
			frame_std = np.std(slice)
			subfeature_mfcc_matrix[i*subfeature_number:i*subfeature_number+4] = [frame_avg, frame_max, frame_min, frame_std]
			###delta
			delta_slice = delta_mel[i,:]
			frame_avg = np.average(delta_slice)
			frame_min = np.amin(delta_slice)
			frame_max = np.amax(delta_slice)
			frame_std = np.std(delta_slice)
			subfeature_delta_mfcc_matrix[i*subfeature_number:i*subfeature_number+4] = [frame_avg, frame_max, frame_min, frame_std]
			#subfeature_delta_mfcc_matrix[:,i] = [frame_avg, frame_max, frame_min, frame_std]	
			
					newFileName = fileName.split('.')[0]
		newFileNameDelta = fileName.split('.')[0]


		np.save(newFileName+'_mfcc', subfeature_mfcc_matrix)
		np.save(newFileName+'_delta', subfeature_delta_mfcc_matrix)

	
	
			'''
			
			
		



			
		
			
			
			
			
			
			
			
			
			
			
