configfile=open('running-config.cfg','r')
f=open('text.cfg','w')
list=[] 

for line in configfile:


  if 'access-list' in line:
    print(line)
    f.write(line)


configfile.close()
