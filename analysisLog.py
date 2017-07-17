import os
f=file("log.txt","w")
#name
try:
	author=os.popen('git log -3 --pretty=%an ')	
	au=author.read().splitlines()	
	if len(au)!=0:
		print au	
		f.write("author name is:\n")
		for a in au:
			f.write(a+"\n")
	else:
		print "error:can not get name"
except:
		print "error:can not get name"
#email	
try:
	email=os.popen('''git log -3 --pretty="%ae" ''')
	em=email.read().splitlines()
	if len(em)!=0:
		print em
		f.write("\nemail is:\n")
		for a in em:
			f.write(a+"\n")
	else:
		print "error:can not get email "		
except:
	print "can not get email"
#commit
try:
	commit=os.popen('''git log -3 --pretty="%H" ''')	
	co=commit.read().splitlines()
	if len(co)!=0:
		print co
		f.write("\ncommit is:\n")
		for a in co:
			f.write(a+"\n")
	else:
		print "error:can not get commit number"	
except:
	print "error:can not get commit number"
#time
try:
	changeTime=os.popen('''git log -3 --pretty="%ad" ''')
	ti=changeTime.read().splitlines()
<<<<<<< HEAD
	if len(ti)!=0:
		print ti
		f.write("\nchange time is:\n")
		for a in ti:
			f.write(a+'\n')	
	else:
		print "error:can not get time"
except:
	print "error:can not get time"	
#description
try:
	description=os.popen('''git log -3 --pretty="%s" ''')
	de=description.read().splitlines()
	if len(de)!=0:
		print de
		f.write("\ndescription is:\n")
		for a in de:
			f.write(a+'\n')
	else:
		print "error:can not get commit description"
except:
	print "error:can not get commit description"			
finally:
	f.close()