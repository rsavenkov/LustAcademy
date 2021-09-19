q_to_p = {
'Victoria': {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 7: 7, 8: 8, 9: 9, 10: 10}, 
'Sabrina':  {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}, 
'Haley':    {2: 1, 1: 2, 3: 3, 6: 4, 7: 5, 10: 6, 11: 7, 12: 8}, 
'Samantha': {1: 2, 2: 3, 3: 4, 4: 5, 6: 5}, 
'Audrey':   {1: 1, 3: 2, 4: 3}, 
'Lily':     {2: 3, 1: 2, 3: 4, 4: 5, 5: 6, 6: 7}, 
'Naomi':    {2: 3, 1: 2, 3: 4, 5: 5, 6: 6, 8: 7}, 
'Amelie':   {1: 1, 2: 2}, 
'Molly':    {1: 1, 2: 2}, 
'Elijah':   {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}, 
'Jacob':    {1: 1, 2: 2}
}

import os
from subprocess import Popen
from openpyxl   import load_workbook
i = 0
def find(what):
	where   = 'D:/Илья/renpy-7.4.6-sdk/LA/game'
	sublime = 'D:/Илья/sublime/sublime_text.exe' 
	for root, dirs, files in os.walk(where):
	    for file in files:
	        #print(root)
	        if file.endswith('rpy') and 'tl\\' not in root:
	            f  = open(root + '/' + file, encoding='utf-8')
	            file_name = 'None'
	            try:
	                for line in f.readlines():
	                    if what.upper() in line.upper():

	                        #print(line)
	                        i += 1
	                        if file_name == 'None':
	                            Popen([sublime, (root + '/' + file)])
	                            print(root + '/' + file)
	                            
	                        file_name = file
	            
	            except:
	                pass
	            f.close()
wb = load_workbook('Активности (1) (1).xlsx')

sheet = wb['QLogs']
rtrns = []

b_table = ['Victoria_1_1', 'Victoria_1', 'Victoria_2', 'Victoria_3', 'Victoria_4', 'Victoria_5', 'Victoria_7', 'Victoria_8', 'Victoria_9', 'Victoria_10', 
'Sabrina_1_1', 'Sabrina_1', 'Sabrina_2', 'Sabrina_3', 'Sabrina_4', 'Sabrina_5', 
'Haley_2_1', 'Haley_1', 'Haley_3', 'Haley_6', 'Haley_7', 'Haley_10', 'Haley_11', 'Haley_12', 
'Samantha_1', 'Samantha_2', 'Samantha_3', 'Samantha_4', 'Samantha_6', 
'Audrey_1_1\nAudrey_2_1', 'Audrey_3', 'Audrey_4', 
'Lily_2_1\nLily_3_1', 'Lily_1', 'Lily_2', 'Lily_3', 'Lily_4', 'Lily_5', 'Lily_6', 
'Naomi_2_1\nNaomi_3_1', 'Naomi_1', 'Naomi_2', 'Naomi_3', 'Naomi_5', 'Naomi_6', 'Naomi_8', 
'Amelie_1', 'Amelie_2', 
'Molly_1', 'Molly_2', 
'Elijah_1', 'Elijah_2', 'Elijah_3', 'Elijah_4', 'Elijah_5', 
'Jacob_1', 'Jacob_2']



find('Victoria_1_label')
# for i in range(2, 300):

#     b = sheet['B'+str(i)]
#     c = sheet['C'+str(i)]
#     #try:
#     if b.value is not None:
#         if '_' in b.value:
#             x = b.value
#             #print(x)
#             #x = b.value.split('_')[0]
#             if x not in rtrns:
#                 rtrns.append(x)
#             #rtrns[x].update({int(b.value.split('_')[1]):int(c.value)})
#             #print()

# print(rtrns)

# 	#find()




#$ p_up('Victoria', 2)
'''
Victoria_1
Victoria_2
Victoria_3
Victoria_4
Victoria_5
Victoria_7
'''


'''
Sabrina_1
Sabrina_2
Sabrina_3
Sabrina_4
'''

'''
Haley_1
Haley_3
Haley_6
Haley_7
'''

'''
Samantha_1
Samantha_2
Samantha_3
Samantha_4
Samantha_6
'''

'''
Audrey_3
Audrey_4
'''


'''
Lily_1
Lily_2
Lily_3
Lily_4
Lily_5
'''

'''
Naomi_1
Naomi_2
Naomi_3
Naomi_5
Naomi_6
'''

'''
Amelie_1
Amelie_2
'''

'''
Molly_1
Molly_2
'''

'''
Elijah_1
Elijah_2
Elijah_3
'''

'''
Jacob_1
Jacob_2
'''