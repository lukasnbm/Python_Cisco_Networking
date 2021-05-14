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
# REV 06 		 : 2021-04-29 / Tarakan

###################################--EBR HOST LIST--#####################################################
#																							            #
#Region 05 = ["ebr-slo.1","ebr-slo.2","ebr-smr.1","ebr-smr.2"]	                                        #
#Region 06 = ["ebr-gayungan.1","ebr-gayungan.2","ebr-hrm.1-new","ebr-hrm.2-new"]	                    #
#Region 07 = ["ebr-dps.1","ebr-dps.2","ebr-sgr.1","ebr-sgr.2"]                    	                    #
#Region 08 = ["ebr-bjb.1","ebr-bjb.2","ebr-bpp.1","ebr-bpp.2","ebr-ptk.1","ebr-ptk.2"]	                #
#Region 09 = ["ebr-sud.1-new","ebr-sud.2-new","ebr-upd.1-new","ebr-upd.2-new","ebr-mdo.1","ebr-mdo.2"]  #
#Region 11 = ["ebr-jpr.1","ebr-jpr.2","ebr-sor.1","ebr-sor.2"]  									    #
#                                                                                                       #
#                                                                                                       #
#########################################################################################################


import json

with open('E:\NetAuto_Script\Python_script\Ping_Test_EBR\KUARO_PARAMETER.json', 'r') as f:
    ebr_dict = json.load(f)

for ebr in ebr_dict:
	ossera_var = (ebr["OSSERA_VAR"]) 
	device_access_var = (ebr["DEVICE_ACCESS_VAR"])
	host_gate = (ebr["HOST_GATE"])
	host_gi_switch = (ebr["HOST_GI_SWITCH"])  
	dest_add = (ebr["DEST_ADD"])
	command_var = (ebr["COMMAND_VAR"]) 

# NOTES: 
# 1 = Ping Test  
# 2 = Route Check
# 3 = Traceroute Numeric 
# 4 = Command_VAR_XR
# 5 = Command_VAR_NXOS
# 6 = Ping Test source Lo0
# 99= EXIT   

def core_function_xr_nxos(script_type_var): 
	cmd = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (ossera_var[1], ossera_var[2], ossera_var[0])		
	if script_type_var in ("1", "2", "3", "6"):
		for host_name in host_gate:
			for ip_destination in dest_add:
				NewTab = crt.Session.ConnectInTab(cmd)
				NewTab.Screen.Synchronous = True
				NewTab.Caption = host_name
				NewTab.Screen.WaitForString("$")
				NewTab.Screen.Send("ssh " + device_access_var[0] + "@" + host_name + chr(13))
				NewTab.Screen.WaitForString("Password:")
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
				if script_type_var == "6": 
					NewTab.Screen.Send("ping " + ip_destination +" count " + Ping_Repeat + " source loopback 0" + chr(13))
					NewTab.Screen.WaitForString("abort.")
	if script_type_var == "4":
		for host_name in host_gate:
			NewTab = crt.Session.ConnectInTab(cmd)
			NewTab.Screen.Synchronous = True
			NewTab.Caption = host_name
			NewTab.Screen.WaitForString("$")
			NewTab.Screen.Send("ssh " + device_access_var[0] + "@" + host_name + chr(13))
			NewTab.Screen.WaitForString("Password:")
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
			NewTab.Screen.Send("ssh " + device_access_var[0] + "@" + host_name_gi + chr(13))
			NewTab.Screen.WaitForString("word:")
			NewTab.Screen.Send(device_access_var[1] + chr(13))
			NewTab.Screen.WaitForString("#")
			NewTab.Screen.Send("ter len 0" + chr(13))
			NewTab.Screen.WaitForString("#")
			for command_name in command_var:
				NewTab.Screen.Send(command_name + chr(13))
				NewTab.Screen.WaitForString("#")


i = 0
while i < 1: 
	Script_Type = crt.Dialog.Prompt ("Choose the NUMBER for Script Type: \n 1 = Ping Test \n 2 = Route Check \n 3 = Traceroute Numeric \n 4 = Command_VAR_XR \n 5 = Command_VAR_NXOS \n 6 = Ping Test source Lo0 \n 99 = EXIT ")
	if Script_Type in ("1", "6"):
		Ping_Repeat = crt.Dialog.Prompt ("Please Input the number of repeat for ping: ")
		core_function_xr_nxos(Script_Type)
		break
	if Script_Type == "99" :
		break
	if not Script_Type in ("1", "2", "3", "4", "5", "6"):
		continue
	else:
		core_function_xr_nxos(Script_Type)
		break