# Learning Python
# Date: 14 Sep 2016
#====================

# Start Here!

# lets try a simple function
# indentation matters a lot in python. we dont use braces to define a loop or a function etc. its all in indentation

def add_numbers(x,y):
  sum_num = x + y
  return sum_num

  # are you seeing this now?
  # yeah....pls continue...sorry!
# x and y are the args to the function. and returning sum

# this is how we call a function:
# as the function returns some value, we need to capture it
a = 10
b = 15
my_sum = add_numbers(a,b)
print (my_sum)

# try to run this
# yes, got the result 25.
# so, arthamainda? Sure, done!

def largest(x,y):
    if x > y:
        print x
    elif x == y:
        print "Both numbers are equal!"
    else:
        print y

largest(34, 98)
# if they are equal? :P
# case, if they are equal the print msg gets ed,o otherwise a value is returned. we can make it uniform. return badulu prints pettochu
# Actually, what is the difference btwn them, print and return?
# print -e msg whatever then and there. nothing would be returned from the functino.on. if we say return, we need to capture that whwith the function call
# akkada print no need....OK!

def for_loop():
    for i in range(10):
        print i

for_loop()

# Done!?
# functions ni vadalaraa? :D
# ante......em ledu
# while loop??
# theliyatle .... scratching my head! Never done before!


def while_loop():
    while i<11:
        print i
        i = i + 1

while_loop()
# i ni define and declare cheyaledu ga, direct ga print i antunnaam
# what if its a user defined array? not just 0 to 10

#array = # while i in array: is this okay? this would become a infinite loop. Oh!
# But we normally do not declare anything in python right? Sorry you were saying something! Yeah, we need to define first! But....while chaala siraaku too muc
# :D :D :D

# EASY. lets see!
# pop ani oka function nerchukundaam.. pop removes an element from a list

arr = range(10)
while (arr):
    print arr.pop(0)

# try.....give me one sec pls

# OK .... what about this while loop?

i = 0
while i <= len(arr):
    print arr[i]
    i = i + 1

# Nope .... same problem....i is not defined. I don't understand this while thing.
# oops, yeah. okay now?
# Learning Python
# Date: 14 Sep 2016
#====================

# Start Here!

# lets try a simple function
# indentation matters a lot in python. we dont use braces to define a loop or a function etc. its all in indentation

def add_numbers(x,y):
  sum_num = x + y
  return sum_num

  # are you seeing this now?
  # yeah....pls continue...sorry!
# x and y are the args to the function. and returning sum

# this is how we call a function:
# as the function returns some value, we need to capture it
a = 10
b = 15
my_sum = add_numbers(a,b)
print (my_sum)

# try to run this
# yes, got the result 25.
# so, arthamainda? Sure, done!

def largest(x,y):
    if x > y:
        print x
    elif x == y:
        print "Both numbers are equal!"
    else:
        print y

largest(34, 98)
# if they are equal? :P
# case, if they are equal the print msg gets ed,o otherwise a value is returned. we can make it uniform. return badulu prints pettochu
# Actually, what is the difference btwn them, print and return?
# print -e msg whatever then and there. nothing would be returned from the functino.on. if we say return, we need to capture that whwith the function call
# akkada print no need....OK!

def for_loop():
    for i in range(10):
        print i

for_loop()

# Done!?
# functions ni vadalaraa? :D
# ante......em ledu
# while loop??
# theliyatle .... scratching my head! Never done before!


def while_loop():
    while i<11:
        print i
        i = i + 1

while_loop()
# i ni define and declare cheyaledu ga, direct ga print i antunnaam
# what if its a user defined array? not just 0 to 10

#array = # while i in array: is this okay? this would become a infinite loop. Oh!
# But we normally do not declare anything in python right? Sorry you were saying something! Yeah, we need to define first! But....while chaala siraaku too muc
# :D :D :D

# EASY. lets see!
# pop ani oka function nerchukundaam.. pop removes an element from a list

arr = range(10)
while (arr):
    print arr.pop(0)

# try.....give me one sec pls

# OK .... what about this while loop?

i = 0
while i <= len(arr):
    print arr[i]
    i = i + 1

# Nope .... same problem....i is not defined. I don't understand this while thing.
# oops, yeah. okay now?
# Learning Python
# Date: 14 Sep 2016
#====================

# Start Here!

# lets try a simple function
# indentation matters a lot in python. we dont use braces to define a loop or a function etc. its all in indentation

def add_numbers(x,y):
  sum_num = x + y
  return sum_num

  # are you seeing this now?
  # yeah....pls continue...sorry!
# x and y are the args to the function. and returning sum

# this is how we call a function:
# as the function returns some value, we need to capture it
a = 10
b = 15
my_sum = add_numbers(a,b)
print (my_sum)

# try to run this
# yes, got the result 25.
# so, arthamainda? Sure, done!

def largest(x,y):
    if x > y:
        print x
    elif x == y:
        print "Both numbers are equal!"
    else:
        print y

largest(34, 98)
# if they are equal? :P
# case, if they are equal the print msg gets ed,o otherwise a value is returned. we can make it uniform. return badulu prints pettochu
# Actually, what is the difference btwn them, print and return?
# print -e msg whatever then and there. nothing would be returned from the functino.on. if we say return, we need to capture that whwith the function call
# akkada print no need....OK!

def for_loop():
    for i in range(10):
        print i

for_loop()

# Done!?
# functions ni vadalaraa? :D
# ante......em ledu
# while loop??
# theliyatle .... scratching my head! Never done before!


def while_loop():
    while i<11:
        print i
        i = i + 1

while_loop()
# i ni define and declare cheyaledu ga, direct ga print i antunnaam
# what if its a user defined array? not just 0 to 10

#array = # while i in array: is this okay? this would become a infinite loop. Oh!
# But we normally do not declare anything in python right? Sorry you were saying something! Yeah, we need to define first! But....while chaala siraaku too muc
# :D :D :D

# EASY. lets see!
# pop ani oka function nerchukundaam.. pop removes an element from a list

arr = range(10)
while (arr):
    print arr.pop(0)

# try.....give me one sec pls

# OK .... what about this while loop?

arr = range(10)
i = 0
while i <= len(arr):
    print arr[i]
    i = i + 1

# Nope .... same problem....i is not defined. I don't understand this while thing.
# oops, yeah. okay now?

# Now with the above changes, it gives the output but also throws an error

"""
Traceback (most recent call last):
  File "<string>", line 268, in <module>
IndexError: list index out of range
[Finished in 0.07s]
"""
