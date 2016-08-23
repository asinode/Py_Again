import ConfigParser, os, time, getpass

def get_dump():
    print "What is the username:"
    user = raw_input()

    print "Enter the password (Don't worry, it is not visible!):"
    password = getpass.getpass()

    print "Enter hostname:"
    host = raw_input()

    print "Enter the name of the DB you would like take a dump of:"
    database = raw_input()


    now_time = time.ctime()
    filestamp = time.strftime('%Y-%m-%d-%I:%M')
    os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > %s.gz" % (user,password,host,database,database+"_"+filestamp))

    print "\n-- Here is your dumpfile "+database+"_"+filestamp+".gz created on "+now_time+"--"

if __name__=="__main__":
    get_dump()
