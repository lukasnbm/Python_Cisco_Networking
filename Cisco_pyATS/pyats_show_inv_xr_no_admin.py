from genie.testbed import load
from unicon.eal.dialogs import Statement, Dialog
import pandas as pd
from nested_lookup import nested_lookup
import datetime
currentDT = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

print("\nCREATE EXCEL FOR SHOW INVENTORY - XR NO ADMIN")
print("=============================================")
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
	p1 = dev.parse('show inventory')
		
	NAME  = list(p1['module_name'].keys())
	DESCR = nested_lookup('descr',p1)
	SN    = nested_lookup('sn',p1)
	PID   = nested_lookup('pid',p1)
	VID   = nested_lookup('vid',p1)

	ALL_DICT = {'NAME' : NAME,'DESCR' : DESCR,'SN' : SN,'PID' : PID,'VID' : VID}

	df = pd.DataFrame.from_dict(ALL_DICT, orient='columns')
	df.to_csv(str(currentDT) + '_' + 'show_inv_'+ nodes + '.csv')

dev.disconnect()