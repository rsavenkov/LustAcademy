import os

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
    	if 'webm' in file:
    		print('image sc i_'+file[:-5] + '= Movie(play="images/video/'+file+'", loop = True)')
    		#print(file[:-5])