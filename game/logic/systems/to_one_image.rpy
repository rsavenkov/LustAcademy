# import sys
# from copy import copy
# from PIL  import Image

# list_im = [

# 'door_hotel_dale_mainstreet',
# 'door_shop_dale_mainstreet',
# 'door_spa_dale_mainstreet',
# 'sign_shop_dale_mainstreet',
# 'sign_spa_dale_mainstreet',
# ]

# for j in ('1', '2', '3', '4'):
# 	im = Image.open(list_im[0]+'_'+j+'.png')
# 	for i in list_im[1:]:
# 		x = Image.open(i+'_'+j+'.png')
# 		im.paste(copy(x), (0,0), copy(x))


# 	im.save('dale_mainstreet_'+str(j)+'.png')

