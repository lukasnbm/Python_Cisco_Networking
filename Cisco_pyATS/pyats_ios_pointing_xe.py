from genie.testbed import load
from unicon.eal.dialogs import Statement, Dialog
from nested_lookup import get_all_keys,nested_lookup
import datetime
import re
currentDT = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

print("\nPOINT THE BOOTFLASH TO NEW IOS")
print("==============================")
print("\nEnter the hostname (followed by enter): ")
rtr_list = []
while True:
    hostname = input()
    if hostname:
        rtr_list.append(hostname)
    else:
        break

FINAL_STATUS = []

for rtr in rtr_list: 
	nodes = rtr
	tb = load('Operation_List_Master.yaml')
	dev = tb.devices[nodes]
	d = Dialog([Statement(pattern=r'Permission denied',action=None,args=None,loop_continue=True,continue_timer=False)])
	dev.connect(connect_reply=d)
	p1 = dev.parse('show running-config')
	p2 = dev.parse('dir bootflash:')
	
	SHOW_RUN = get_all_keys(p1)
	r = re.compile("boot ")
	SHOW_RUN_1 = list(filter(r.match,SHOW_RUN))
	
	DIR_BOOTFLASH = list(p2['dir']['bootflash:/']['files'].keys())
	rr = re.compile("asr\S+.16.12.04.SPA.bin")
	DIR_BOOTFLASH_1 = list(filter(rr.match,DIR_BOOTFLASH))
	
	CONFIGURE = []
	for IOS in SHOW_RUN_1:
		CONFIGURE.append('no ' + IOS)

	if not DIR_BOOTFLASH_1:
		#print("\nPLEASE UPLOAD NEW IOS TO THE BOOTFLASH: OF " + nodes + "\n")
		FINAL_STATUS.append('Please upload new IOS to the bootflash: of ' + nodes)
		continue
		
	CONFIGURE.append('boot system flash bootflash:' + DIR_BOOTFLASH_1[0])
	CONFIGURE.append(SHOW_RUN_1[0])
	
	if CONFIGURE[-1] == CONFIGURE[-2]:
		#print("\nNEW IOS HAS BEEN POINTED ON " + nodes + "\n")
		FINAL_STATUS.append('New IOS ALREADY pointed on ' + nodes)
		continue
	
	ONWARD = input("\n!!!! WARNING !!!!\nDo you really really want to configure " + nodes +" ? \n(Yes for YES, anything else for NO) " )
	if ONWARD == "Yes":
		dev.log_file(filename='/mnt/c/NetAuto_pyats_ops/' + str(currentDT) + '_IOSXE_REPOINTING_' + nodes +'.log')
		dev.configure(CONFIGURE)
		FINAL_STATUS.append('New IOS has JUST been pointed on ' + nodes)
	else:
		dev.disconnect()


print("\nFINAL REPORT")
print("=============")
print(*FINAL_STATUS, sep = "\n")

dev.disconnect()
