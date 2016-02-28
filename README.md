My first python script that uses the netatmo-api-python library to
visualize the current co2 level using a netatmo weather station, a  raspberry pi and some ws281x pixel strips.

The script authenticates using OAUTH2 using the netatmo-api-python(https://github.com/philippelt/netatmo-api-python), then pulls the current value from the netatmp api (http://dev.netatmo.com),
converts the current co2 level to a color
(code inspired by http://stackoverflow.com/questions/20792445/calculate-rgb-value-for-a-range-of-values-to-create-heat-map)
and uses some ws2812 pixel strips (see https://learn.adafruit.com/neopixels-on-raspberry-pi/overview for info and wiring) 
to constantly visualize the current level.

If you want to use it, do the following:
1) Get a raspberry pi
   I use the version 2 model b and you also need a Netatmo weather station

2) Get some ws281x pixels
   Mine are http://www.watterott.com/de/WS2812-Stick-10x-RGB-LED
   But others should work as well, like https://www.adafruit.com/products/1426

3) Wire everything up
   You can find some help here: https://learn.adafruit.com/neopixels-on-raspberry-pi/wiring

4) Get the netatmo-api-python 
   from  https://github.com/philippelt/netatmo-api-python

5) Get an Netatmo account and register your application
   http://dev.netatmo.com/dev/createapp

6) Enter your credentials in the netatmo-api-python library
   Simply edit lnetatmo.py, set _CLIENT_ID, _CLIENT_ID_SECRET, _USERNAME and _PASSWORD

7) Maybe you want to modify the colors that display the Co2 values
   then you need to modify CO2_COLOR_GREEN, _YELLOW and _RED in the co2Warner.py

8) Start the script and enjoy
   You may want to launch it at startup of your pi


Please contact me in case you find something that needs to be correct.



