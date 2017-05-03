import os, re


'''
in:
subset - [jezyk, plec, cel] (order is important)
path - sciezka do katalogu z samplami
out:
lista nazw folderow
'''
def subset(subset, path):
	
	dir_list = os.listdir(path)
	ret_table = []
	lacznik = '(.*)'
	#lacznik = '-'
	pattern = lacznik.join(subset)
	
	pattern = lacznik+pattern+lacznik
	
	
	for folder in dir_list:
		if re.match(pattern, folder):
			ret_table.insert(-1, folder)
			
	if 'docs' in ret_table:
		ret_table.remove('docs')
		
	return ret_table
	
			


