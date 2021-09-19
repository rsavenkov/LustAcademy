import sys
from copy import copy
from PIL  import Image

list_im = [

'door_hotel_dale_mainstreet',
'door_shop_dale_mainstreet',
'door_spa_dale_mainstreet',
'sign_shop_dale_mainstreet',
'sign_spa_dale_mainstreet',
]

# creates a new empty image, RGB mode, and size 444 by 95


im = Image.open(list_im[0]+'_1.png')

for i in list_im[1:]:
	x = Image.open(i+'_1.png')
	im.paste(copy(x), (0,0), copy(x))


im.save('test.png')

