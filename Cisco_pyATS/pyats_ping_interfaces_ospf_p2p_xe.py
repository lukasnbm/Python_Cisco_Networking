from genie.testbed import load
from unicon.eal.dialogs import Statement, Dialog
from nested_lookup import get_all_keys,nested_lookup
import datetime
import re
import ipaddress
currentDT = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

print("\nPING ALL P2P WAN LINK INTERFACE - XE")
print("====================================")
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
	dev.log_file(filename='/mnt/c/NetAuto_pyats_ops/Ping_Result/' + str(currentDT) + '_PING_OSPF_INT_' + nodes +'.log')
	p1 = dev.parse('show ip ospf interface brief')
	
	#INTERFACES = get_all_keys(p1)
	#r = re.compile("Port-channel\d|TenGigabitEthernet\d+\/\d+\/\d+|GigabitEthernet\d+\/\d+\/\d+|BDI\d+")
	#INTERFACES_1 = list(filter(r.match,INTERFACES))
	#print(INTERFACES_1)
	
	IP_ADD = nested_lookup('ip_address',p1)
	rr = re.compile("(\d+\.\d+\.\d+\.\d+)\/30")
	IP_ADD_1 = list(filter(rr.match,IP_ADD))
	#print(IP_ADD_1)
	
	IP_DEST = []
	for ip in IP_ADD_1:
		net4 = ipaddress.ip_network(ip, strict=False)
		for x in net4.hosts():
			if(str(x) + '/30') != ip:
				IP_DEST.append(str(x))

	for ipdestination in IP_DEST:
		dev.execute('ping ' + ipdestination + ' repeat 100 tos 192', timeout=450)
	
dev.disconnect()