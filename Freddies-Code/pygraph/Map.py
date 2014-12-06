import Image

def map_facts():
	global map_centre
	map_centre = map.size[0]/2,map.size[1]/2
	print ('The map\'s centre is at ' + str(map_centre) + '.')

def pixel_eval(pixel):
	print(map.getpixel(pixel))
	print(map.getdata(pixel))

def startup():
	global map
	map = Image.open('map.png')
	#map.show()
	map_facts()
	pixel_eval(map_centre)
	pixel_eval(0,0)

startup()
