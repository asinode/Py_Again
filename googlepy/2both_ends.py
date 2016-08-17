#!/home/as/anaconda2/bin/python

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
    # +++your code here+++
    s = "LinuxLove"
    s2 = s[:1] + s[-1:]
    print s2
    return

# Execute this from CLI using the below command example:
# python -c 'from donuts import donuts; print donuts(15)'
