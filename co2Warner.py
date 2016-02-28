import lnetatmo, time
from neopixel import *

DEBUG 		 = True	   		# If ture, some debug information will be logged out on the consle
LED_COUNT        = 30      		# Number of LED pixels.
LED_PIN          = 18      		# GPIO pin connected to the pixels (must support PWM!).
LED_BRIGHTNESS   = 128	   		# Brightness between 0 and 255
LED_FREQ_HZ      = 800000  		# LED signal frequency in hertz (usually 800khz)
LED_DMA          = 5       		# DMA channel to use for generating signal (try 5)
LED_INVERT       = False   		# True to invert the signal (when using NPN transistor level shift)
CO2_MIN	         = 0	   		# Min Co2 value, here the green value starts
CO2_MAX	         = 1500	   		# Max Co2 value, from here on the red color will be displayed
CO2_STEPS        = 10			# Steps for color display
CO2_COLOR_RED    = (128, 0, 0)		# Red color
CO2_COLOR_GREEN  = (0, 255, 0)		# Green color
CO2_COLOR_YELLOW = (255, 140, 0)	# Yellow color

# Calculates the color to diplay for current Co2 level
# See http://stackoverflow.com/questions/20792445/calculate-rgb-value-for-a-range-of-values-to-create-heat-map
def rgb(minval, maxval, val, colors):
    max_index = len(colors)-1
    v = float(val-minval) / float(maxval-minval) * max_index
    i1, i2 = int(v), min(int(v)+1, max_index)
    (r1, g1, b1), (r2, g2, b2) = colors[i1], colors[i2]
    f = v - i1
    return int(r1 + f*(r2-r1)), int(g1 + f*(g2-g1)), int(b1 + f*(b2-b1))


# Main loop
# Basically inspired by the strandtest example of the ws281x library
# https://github.com/jgarff/rpi_ws281x/blob/master/python/examples/strandtest.py
if __name__ == '__main__':

	# Waiting to make sure we have connectivity
	time.sleep(30)

        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        # Intialize the library (must be called once before other functions).
        strip.begin()

	authorization = lnetatmo.ClientAuth()

	while True:
		devList = lnetatmo.DeviceList(authorization)
		theData = devList.lastData()
		r, g, b = rgb(CO2_MIN, CO2_MAX, theData['internal']['CO2'], [CO2_COLOR_GREEN, CO2_COLOR_YELLOW, CO2_COLOR_RED])
                
		if DEBUG:
			print('----------------------')
			print(time.strftime("%d.%m.%Y: %H:%M"))
                        print('CO2 level: %s' % theData['internal']['CO2'])
                        print('Color: (%d, %d, %d)' % (r, g, b))


		for position in range(0, LED_COUNT):
			strip.setPixelColorRGB(position, r, g, b)
		strip.show()
		# Refresh value every minute
		time.sleep(60)
