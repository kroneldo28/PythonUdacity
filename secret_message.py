# This is a program that take a folder containing a series a photos of letters and arrange it to show a message

import os 

file_list = os.listdir("./prank")
print(file_list)
cwd = os.getcwd()
print cwd

os.chdir("./prank")
for file_name in file_list:
	os.rename(file_name,file_name.translate(None,"0123456789"))

os.chdir(cwd)
