from twython import Twython
from smbus import SMBus
import time

# Twitter authentication
APP_KEY='<API key>'
APP_SECRET='<API secret>'
OAUTH_TOKEN='<Access token>'
OAUTH_TOKEN_SECRET='<Access token secret>'

# Twython object
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# I2C globals
ADDR = 0x27
bus = SMBus(1)

# Special characters
deg = u'\N{DEGREE SIGN}'

# Main loop
while True:

	# Get the current system date and time
	datetime = time.strftime('%m/%d/%Y %H:%M:%S')

	# Read data from sensor
	bus.write_byte(ADDR, 0x00)
	ans = bus.read_i2c_block_data(ADDR, 0x00, 4)

	# Convert to human readable humidity
	humd = ((ans[0] & 0x3f) << 8) + ans[1]
	humd = humd * float('6.10e-3')
	humd = '{:.0f}'.format(humd)

	# Convert temperature to Celsius
	temp = (ans[2] << 8) + ans[3]
	temp = temp >> 2
	temp = (temp * float('1.007e-2')) - 40.0
	temp = '{:.1f}'.format(temp)

	# Print date, time, temperature, and humidity
	print datetime
	print 'Temperature: ' + str(temp) + deg + 'C'
	print 'Humidity: ' + str(humd) + '%'
	print ''

	# Post to Twitter!
	msg = 'Weatherbot here! It is ' + datetime + \
		'. The temperature is ' + str(temp) + \
		deg + 'C, and the humidity is ' + \
		str(humd) + '%.'
	twitter.update_status(status=msg)

	# Delay (in seconds) before next reading
	time.sleep(60)