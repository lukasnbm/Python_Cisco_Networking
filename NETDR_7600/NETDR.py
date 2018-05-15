from collections import Counter
txtfile   = open('C:\Python27\Scripts\NETDR 7600\STORM_ORI.txt','r') 


linelist  = []
linelist2 = []
linelist3 = []
linelist4 = []
linelist5 = []

'''
# Jika mau mencari src_vlan gunakan script yg di komen ini 
i = 0
for line in txtfile:
    linelist.append(line.rstrip("\n"))
    if "src_vlan" in linelist[i]: 
	    linelist2.insert(i,linelist[i])
    i = i+1

	
linelist3 = [w.split(': ', 1)[1] for w in linelist2]	
linelist5 = [t.split(', ', 1)[0] for t in linelist3]	
result = Counter(linelist5)
'''

i = 0
for line in txtfile:
    linelist.append(line.rstrip("\n"))
    if "interface" in linelist[i]: 
	    linelist2.insert(i,linelist[i])
    i = i+1

	
linelist3 = [w.split(', ', 1)[0] for w in linelist2]	
result = Counter(linelist3)



print ("\n")
print ("NETDR_RESULT_L3")
print ("===============\n")
for key,val in result.most_common():
    print key," = ", val

print ("\n\n\n\n\n")


#######################################
#######################################	

txtfile.seek(0) 
linelist  = []	
linelist2 = []

i = 0
for line in txtfile:
    linelist.append(line.rstrip("\n"))
    if "srcmac" in linelist[i]: 
	    linelist2.insert(i,linelist[i])
    i = i+1


linelist4 = [p.split(', ', 2)[1] for p in linelist2]	
result1 = Counter(linelist4)


print ("NETDR_RESULT_L2")
print ("===============\n")
for key,val in result1.most_common():
    print key," = ", val
	
raw_input()	

	



