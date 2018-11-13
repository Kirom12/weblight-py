import unicornhat as uh

uh.set_layout(uh.PHAT)
uh.brightness(0.8)

def setlight(r, g, b):
	for x in range(8):
		for y in range(4):
			uh.set_pixel(x, y, r, g, b)
	uh.show()