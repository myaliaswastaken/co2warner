Simple python script that uses the netatmo-api-python library to
visualize the current co2 level using a raspberry pi and some 
ws2812 pixel strips in colors from green to red.

The script pulls the current value from the netatmp api (http://dev.netatmo.com),
converts the current co2 level to a color
(code inspired by http://stackoverflow.com/questions/20792445/calculate-rgb-value-for-a-range-of-values-to-create-heat-map)
and uses some ws2812 pixel strips (see https://learn.adafruit.com/neopixels-on-raspberry-pi/overview for info and wiring) 
to constantly visualize the current level.



