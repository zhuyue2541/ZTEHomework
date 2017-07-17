import os
au=[]
#a=os.system("git log -3 >>a.txt")
author=os.popen('''git log -3 --pretty="%an" ''')
au=author.read().splitlines()
print au
f=file("log.txt","w")
f.write("author name is:\n")
for a in au:
	f.write(a+"\n")
f.close()