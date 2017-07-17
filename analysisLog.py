import os
au=[]
#name
author=os.popen('''git log -3 --pretty="%an" ''')
au=author.read().splitlines()
print au
f=file("log.txt","w")
f.write("author name is:\n")
for a in au:
	f.write(a+"\n")
#email	
email=os.popen('''git log -3 --pretty="%ae" ''')
em=email.read().splitlines()	
f.write("\nemail is:\n")
for a in em:
	f.write(a+"\n")	
#commit
commit=os.popen('''git log -3 --pretty="%H" ''')	
co=commit.read().splitlines()
f.write("\ncommit is:\n")
for a in co:
	f.write(a+"\n")	
#time
changeTime=os.popen('''git log -3 --pretty="%ad" ''')
ti=changeTime.read().splitlines()
f.write("\nchange time is:\n")
for a in ti:
	f.write(a+'\n')	
#description
description=os.popen('''git log -3 --pretty="%s" ''')
de=description.read().splitlines()
f.write("\ndescription is:\n")
for a in de:
	f.write(a+'\n')	
f.close()