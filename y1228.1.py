yy = ['chen','yu','you','sun']
print (yy,end = "")
print ("Here is a sorted list",end = "")
print (sorted(yy),end = "")
print (yy,end = "")
yy.reverse()
print (yy,end = "")
#print (len(yy),end = "")
for yy1 in yy:
  print ("\t" + yy1.upper() + " this is a thrick",end = "")