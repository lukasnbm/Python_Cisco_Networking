# $language = "python"
# $interface = "1.0"

# This automatically generated script may need to be
# edited in order to work correctly.

# Author : Lukas Marbun - IP RAN
# Initial Date   : 2019-08-10 / Bontang
# REV 02 		 : 2019-09-02 / Sangatta
# REV 03 		 : 2019-11-19 / Tenggarong
# REV 04 		 : 2019-11-20 / KotaBangun
# REV 05 		 : 2020-02-04 / Kuaro
# REV 06 		 : 2020-02-09 / Tarakan

###################################-- NODES LIST--###########################################
#																							#
#SulawesiSelatan   = ["ebr-sud.1-new","ebr-sud.2-new","ebr-upd.1-new","ebr-upd.2-new"]  	#
#JawaTimur         = ["ebr-gayungan.1","ebr-gayungan.2","ebr-hrm.1-new","ebr-hrm.2-new"]	#
#Bali              = ["ebr-dps.1","ebr-dps.2"]                                          	#
#Papua             = ["10.113.176.13","10.115.171.21"]  									#
#KalimantanSelatan = ["ebr-bjb.1","ebr-bjb.2"]												#
#																							#
#EBR =  ["ebr-gayungan.1","ebr-gayungan.2","ebr-hrm.1-new","ebr-hrm.2-new",					#
#		"ebr-sud.1-new","ebr-sud.2-new","ebr-upd.1-new","ebr-upd.2-new",                    #
#		"ebr-dps.1","ebr-dps.2","10.113.176.13","10.115.171.21",                            #
#		"ebr-bjb.1","ebr-bjb.2"]                                                            #
#                                                                                           #
#GI-SWITCH = ["gi-switch-jpr-1","gi-switch-jpr-2","gi-switch-tmk-1","gi-switch-tmk-2",		#
#		"gi-switch-upd-1","gi-switch-upd-2","gi-switch-sud-1","gi-switch-sud-2",			#
#		"gi-switch-gyg-1","gi-switch-gyg-2","gi-switch-hrm-1","gi-switch-hrm-2"]            #
#																							#
#############################################################################################

import json

with open('C:\Python27\Scripts\EBR Ping Test\KUARO_TARAKAN_PARAMETER.json', 'r') as f:
    ebr_dict = json.load(f)

for ebr in ebr_dict:
	ossera_var = (ebr["OSSERA_VAR"]) 
	device_access_var = (ebr["DEVICE_ACCESS_VAR"])
	host_gate = (ebr["HOST_GATE"])
	host_gi_switch = (ebr["HOST_GI_SWITCH"])  
	dest_add = (ebr["DEST_ADD"])
	command_var = (ebr["COMMAND_VAR"]) 

# NOTES: 
# 1= Ping Test  
# 2= Route Check
# 3= Traceroute Numeric 
# 4= Command_VAR_XR
# 5= Command_VAR_NXOS

def core_function_xr_nxos(script_type_var): 
	cmd = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (ossera_var[1], ossera_var[2], ossera_var[0])		
	if script_type_var in ("1", "2", "3"):
		for host_name in host_gate:
			for ip_destination in dest_add:
				NewTab = crt.Session.ConnectInTab(cmd)
				NewTab.Screen.Synchronous = True
				NewTab.Caption = host_name
				NewTab.Screen.WaitForString("$")
				NewTab.Screen.Send("telnet " + host_name + chr(13))
				NewTab.Screen.WaitForString("ACS 5.8 username:")
				NewTab.Screen.Send(device_access_var[0]+ chr(13))
				NewTab.Screen.WaitForString("ACS 5.8 password:")
				NewTab.Screen.Send(device_access_var[1] + chr(13))
				NewTab.Screen.WaitForString("#")
				NewTab.Screen.Send("ter len 0" + chr(13))		
				NewTab.Screen.WaitForString("#")
				if script_type_var == "1": 
					NewTab.Screen.Send("ping " + ip_destination +" count " + Ping_Repeat + chr(13))	
					NewTab.Screen.WaitForString("abort.")
				if script_type_var == "2": 
					NewTab.Screen.Send("show route " + ip_destination + chr(13))
					NewTab.Screen.WaitForString("#")
				if script_type_var == "3": 
					NewTab.Screen.Send("traceroute " + ip_destination + " numeric "+ chr(13))
					NewTab.Screen.WaitForString("abort.")
	if script_type_var == "4":
		for host_name in host_gate:
			NewTab = crt.Session.ConnectInTab(cmd)
			NewTab.Screen.Synchronous = True
			NewTab.Caption = host_name
			NewTab.Screen.WaitForString("$")
			NewTab.Screen.Send("telnet " + host_name + chr(13))
			NewTab.Screen.WaitForString("ACS 5.8 username:")
			NewTab.Screen.Send(device_access_var[0]+ chr(13))
			NewTab.Screen.WaitForString("ACS 5.8 password:")
			NewTab.Screen.Send(device_access_var[1] + chr(13))
			NewTab.Screen.WaitForString("#")
			NewTab.Screen.Send("ter len 0" + chr(13))		
			NewTab.Screen.WaitForString("#")
			for command_name in command_var:
				NewTab.Screen.Send(command_name + chr(13))
				NewTab.Screen.WaitForString("#")
	if script_type_var == "5" :
		for host_name_gi in host_gi_switch:
			NewTab = crt.Session.ConnectInTab(cmd)
			NewTab.Screen.Synchronous = True
			NewTab.Caption = host_name_gi
			NewTab.Screen.WaitForString("$")		
			NewTab.Screen.Send("telnet " + host_name_gi + chr(13))
			NewTab.Screen.WaitForString("login:")
			NewTab.Screen.Send(device_access_var[0]+ chr(13))
			NewTab.Screen.WaitForString("Password:")
			NewTab.Screen.Send(device_access_var[1] + chr(13))
			NewTab.Screen.WaitForString("#")
			NewTab.Screen.Send("ter len 0" + chr(13))
			NewTab.Screen.WaitForString("#")
			for command_name in command_var:
				NewTab.Screen.Send(command_name + chr(13))
				NewTab.Screen.WaitForString("#")


i = 0
while i < 1: 
	Script_Type = crt.Dialog.Prompt ("Choose the NUMBER for Script Type: \n 1 = Ping Test \n 2 = Route Check \n 3 = Traceroute Numeric \n 4 = Command_VAR_XR \n 5 = Command_VAR_NXOS")
	if Script_Type == "1":
		Ping_Repeat = crt.Dialog.Prompt ("Please Input the number of repeat for ping: ")
		core_function_xr_nxos(Script_Type)
		break
	if not Script_Type in ("1", "2", "3", "4", "5"):
		continue
	else:
		core_function_xr_nxos(Script_Type)
		break
