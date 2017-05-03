import librosa
import matplotlib.pyplot as plt
import numpy as np
from math import pow



def words_count(indexes):

	word_cnt = 1
	for i in range(len(indexes)-1):
		if indexes[i+1]== indexes[i]+1:

			pass
		else:
			word_cnt = word_cnt+1
	
	return word_cnt
		

def get_pauses(indexes):
	# start - poczatek nowego slowe; end - koniec poprzedniego slowa
	pauses=[]
	
	end = indexes[0]
	
	for i in range(len(indexes)-1):
		if indexes[i+1]== indexes[i]+1:
			end = indexes[i+1]
		else:
			start = indexes[i+1]
			pauses.append(start-end)
			end = start
			
	return pauses



def get_pauses_stats(y):
	#wyliczenie energii
	frames = librosa.util.frame(y)
	frames = np.transpose(frames)
	energy = []
	for frame in frames:
		
		sum=0
		for sample in frame:
			sum = sum + sample**2

		energy.append(sum)

		

	threshold = 0.10 * np.max(energy)  # prog

	x=[]
	#y=[]
	for index, i in enumerate(energy):
		if i > threshold:
	#		y.append(i)
			x.append(index)
			
	
	pauses = get_pauses(x)
	stat_array = [np.average(pauses), np.amin(pauses), np.amax(pauses), np.std(pauses)]
	
	
	return stat_array		
	return 

	
	
#y, sr = librosa.load('01.flac') #zaladowanie pliku
#print(get_pauses_stats(y))

'''			
print(words_count(x))
print(get_pauses(x))


plt.subplot(211)
plt.plot(y)
print(x)
plt.subplot(212)
plt.plot(energy)
plt.plot([threshold]*len(energy), 'r')
plt.plot(x,y,'g*')

plt.show()
'''