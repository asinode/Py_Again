#!/home/asinode/anaconda2/envs/scraping1/bin/python
#!/usr/bin/python3

# Thanks to https://automatetheboringstuff.com/chapter11/
# mapit.py - Launches a map in the browser using an address
# from the command line or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	# Get address from command line.
	address = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard.
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)

