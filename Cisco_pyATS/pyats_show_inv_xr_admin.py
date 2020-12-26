from genie.testbed import load
from unicon.eal.dialogs import Statement, Dialog
import pandas as pd
import datetime
import re
currentDT = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

print("\nCREATE EXCEL FOR SHOW INVENTORY - XR ADMIN")
print("==========================================")
print("Enter the hostname (followed by enter): ")
rtr_list = []
while True:
    hostname = input()
    if hostname:
        rtr_list.append(hostname)
    else:
        break

for rtr in rtr_list:
	nodes = rtr 
	tb = load('Operation_List_Master.yaml')
	dev = tb.devices[nodes]
	d = Dialog([Statement(pattern=r'Permission denied',action=None,args=None,loop_continue=True,continue_timer=False)])
	dev.connect(connect_reply=d)
	p0 = dev.admin_execute('show inventory')
	P0=re.split('\r\n|NAME:|, DESCR:|PID:|, VID:|, SN:',p0)
	del P0[0]
	P1 = (list(filter(None,P0)))
	
	NAME  = []
	DESCR = []
	SN    = []
	PID   = []
	VID   = []
	
	for a in range(0, len(P1), 5):
		NAME.append(P1[a])
		
	for a in range(1, len(P1), 5):
		DESCR.append(P1[a])
	
	for a in range(4, len(P1), 5):
		SN.append(P1[a])
		
	for a in range(2, len(P1), 5):
		PID.append(P1[a])
	
	for a in range(3, len(P1), 5):
		VID.append(P1[a])
		
	ALL_DICT = {'NAME' : NAME,'DESCR' : DESCR,'SN' : SN,'PID' : PID,'VID' : VID}
	
	df = pd.DataFrame.from_dict(ALL_DICT, orient='columns')
	df.to_csv(str(currentDT) + '_' + 'show_inv_admin_'+ nodes + '.csv')

dev.disconnect()