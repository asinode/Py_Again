#!/home/as/anaconda2/bin/python

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'

def donuts(count):
    # +++your code here+++
    if count < 10:
        print "Number of donuts: %s" % (count)
    else:
        print "Number of donuts: MANY"
    return

# Execute this from CLI using the below command example:
# python -c 'from donuts import donuts; print donuts(15)'
