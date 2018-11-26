import unicornhat as uh

power = 1
color = {
	'r': 0,
	'g': 0,
	'b': 0
}

uh.set_layout(uh.PHAT)
uh.brightness(0.8)

def setlight(r, g, b):
	global color

	if not power:
		return False

	color['r'] = r
	color['g'] = g
	color['b'] = b

	for x in range(8):
		for y in range(4):
			uh.set_pixel(x, y, r, g, b)
	uh.show()

def turnOn():
	global power

	power = 1
	setlight(color['r'], color['g'], color['b'])

def turnOff():
	global power

	uh.off()
	uh.show()
	power = 0