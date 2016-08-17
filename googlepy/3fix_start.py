#!/home/as/anaconda2/bin/python

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
    # +++your code here+++
    s = "LinuxLoveLawlessButLegal"
    for i in s:
        if i == s.lower()[0]:
            s2 = s.lower().replace(i,'*')    
    print s2.replace(s2[0],s[0])
    return

# Execute this from CLI using the below command example:
# python -c 'from donuts import donuts; print donuts(15)'
