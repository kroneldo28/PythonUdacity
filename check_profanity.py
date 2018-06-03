import urllib

def read_text():
	quotes = open("./movie_quotes")
	contents_of_files = quotes.read()
	print(contents_of_files)
	quotes.close()
	check_profanity(contents_of_files)

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
	output = connection.read()
	#print(output)
	connection.close()
	if "true" in output:
		print("Profanity Alert")
	elif "false" in output:
		print("There are no curse words in the document")
	else:
		print("There's a problem scanning the document")

read_text()
