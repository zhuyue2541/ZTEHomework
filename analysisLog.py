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
f.close()