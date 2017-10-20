confile=open('running-config.cfg','r')
newconfile=open('newfile.cfg','w')
for line in confile:
   newconfile.write(line.replace('172','192'))

