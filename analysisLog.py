import os
f=file("log.txt","w")
#name
try:
	author=os.popen('''git log -3 --pretty="%an" ''')
	au=author.read().splitlines()
	print au
	f.write("author name is:\n")
	for a in au:
		f.write(a+"\n")
except:
		print "can not get name"
#email	
try:
	email=os.popen('''git log -3 --pretty="%ae" ''')
	em=email.read().splitlines()
	print em
	f.write("\nemail is:\n")
	for a in em:
		f.write(a+"\n")	
except:
		print "can not get email"		
#commit
try:
	commit=os.popen('''git log -3 --pretty="%H" ''')	
	co=commit.read().splitlines()
	print co
	f.write("\ncommit is:\n")
	for a in co:
		f.write(a+"\n")	
except:
		print "can not get commit number"			
#time
try:
	changeTime=os.popen('''git log -3 --pretty="%ad" ''')
	ti=changeTime.read().splitlines()
	print ti
	f.write("\nchange time is:\n")
	for a in ti:
		f.write(a+'\n')	
except:
		print "can not get time"		
#description
try:
	description=os.popen('''git log -3 --pretty="%s" ''')
	de=description.read().splitlines()
	print de
	f.write("\ndescription is:\n")
	for a in de:
		f.write(a+'\n')	
except:
		print "can not get description"	
finally:		
	f.close()