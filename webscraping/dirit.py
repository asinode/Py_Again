#!/home/asinode/anaconda2/envs/scraping1/bin/python
#!/usr/bin/python3

# Thanks to https://automatetheboringstuff.com/chapter11/
# dirit.py - Launches a map in the browser with the directions from an address
# to a given address.

import webbrowser, sys

fromadd = input("Enter the FROM address: ")
toadd = input("Enter the TO address: ")

webbrowser.open('http://www.google.com/maps/dir/' + fromadd + '/' + toadd)
