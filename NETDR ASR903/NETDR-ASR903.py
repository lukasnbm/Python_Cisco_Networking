from collections import Counter
txtfile   = open('C:\Python27\Scripts\NETDR ASR903\STORM_ORI-ASR903.txt','r')


linelist  = []
linelist2 = []
linelist3 = []
linelist4 = []

i = 0
for line in txtfile:
    linelist.append(line.rstrip("\n"))
    if "l3id" in linelist[i]: 
	    linelist2.insert(i,linelist[i])
    i = i+1

	
linelist3 = [w.rsplit(' ', 1)[1] for w in linelist2]	
result = Counter(linelist3)

print ("\n")
print ("NETDR_RESULT_L3 - ASR903")
print ("========================\n")
for key,val in result.most_common():
    print "l3id", key," = ", val


raw_input()	

	



