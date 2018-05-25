# This is a program that wait 10 seconds then open a web page

import time
import webbrowser

breaks = 3
while breaks > 0:
	time.sleep(10)
	webbrowser.open("https://kkakko.com")
	breaks = breaks -1
