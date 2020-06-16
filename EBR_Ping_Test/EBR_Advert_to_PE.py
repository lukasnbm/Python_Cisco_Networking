# $language = "python"
# $interface = "1.0"

# This automatically generated script may need to be
# edited in order to work correctly.

# Author : Lukas Marbun - IP RAN

###################################--EBR HOST LIST--#########################################
#																							#
#SulawesiSelatan   = ["ebr-sud.1-new","ebr-sud.2-new","ebr-upd.1-new","ebr-upd.2-new"]  	#
#JawaTimur         = ["ebr-gayungan.1","ebr-gayungan.2","ebr-hrm.1-new","ebr-hrm.2-new"]	#
#Bali              = ["ebr-dps.1","ebr-dps.2"]                                          	#
#Papua             = ["10.113.176.13","10.115.171.21"]  									#
#KalimantanSelatan = ["ebr-bjb.1","ebr-bjb.2"]												#
#																							#
#All =  ["ebr-gayungan.1","ebr-gayungan.2","ebr-hrm.1-new","ebr-hrm.2-new",					#
#		"ebr-sud.1-new","ebr-sud.2-new","ebr-upd.1-new","ebr-upd.2-new",                    #
#		"ebr-dps.1","ebr-dps.2","10.113.176.13","10.115.171.21",                            #
#		"ebr-bjb.1","ebr-bjb.2"]                                                            #
#############################################################################################

# // OSSERA Variables //
host = "10.175.1.151"
user = "vitogui"
passwd = "May20.com"

# // Device Access Variable //
User_Pass = ["ridafir","Tahunbaru#55"]

# NOTES: 
# 1 = EBR Reg 6  
# 2 = EBR Reg 7
# 3 = EBR Reg 8
# 4 = EBR Reg 9
# 5 = EBR Reg 11

Host_Reg6  = ["ebr-gayungan.1","ebr-gayungan.2","ebr-hrm.1-new","ebr-hrm.2-new"]
Host_Reg7  = ["ebr-dps.1","ebr-dps.2"]
Host_Reg8  = ["ebr-bjb.1","ebr-bjb.2"]
Host_Reg9  = ["ebr-sud.1-new","ebr-sud.2-new","ebr-upd.1-new","ebr-upd.2-new"]
Host_Reg11 = ["10.113.176.13","10.115.171.21"]

PE_Address_Reg6  = ["222.124.75.121","118.98.84.89","118.98.87.221","222.124.74.193"]
PE_Address_Reg7  = ["36.92.255.81","36.92.255.85"]
PE_Address_Reg8  = ["36.92.255.77","36.92.255.73"]
PE_Address_Reg9  = ["61.94.4.105","61.94.4.109","118.98.84.229","118.98.84.121"]
PE_Address_Reg11 = ["36.92.253.1","118.97.6.17"]

Script_Type = crt.Dialog.Prompt ("Pick number for advertisement from EBR to PE Router : \n 1 => EBR Reg 6 \n 2 => EBR Reg 7 \n 3 => EBR Reg 8 \n 4 => EBR Reg 9 \n 5 => EBR Reg 11")

if Script_Type == "1":
	for host_ebr,pe_add in zip(Host_Reg6,PE_Address_Reg6):
		cmd = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (user, passwd, host)
		NewTab = crt.Session.ConnectInTab(cmd)
		NewTab.Screen.Synchronous = True
		NewTab.Caption = host_ebr
		NewTab.Screen.WaitForString("$")
		NewTab.Screen.Send("telnet " + host_ebr + chr(13))
		NewTab.Screen.WaitForString("ACS 5.8 username:")
		NewTab.Screen.Send(User_Pass[0]+ chr(13))
		NewTab.Screen.WaitForString("ACS 5.8 password:")
		NewTab.Screen.Send(User_Pass[1] + chr(13))
		NewTab.Screen.WaitForString("#")
		NewTab.Screen.Send("ter len 0" + chr(13))		
		NewTab.Screen.WaitForString("#")
		NewTab.Screen.Send("show bgp neighbor " + pe_add + " advertised-routes" + chr(13))
		NewTab.Screen.WaitForString(" ")

if Script_Type == "2":
	for host_ebr,pe_add in zip(Host_Reg7,PE_Address_Reg7):
		cmd = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (user, passwd, host)
		NewTab = crt.Session.ConnectInTab(cmd)
		NewTab.Screen.Synchronous = True
		NewTab.Caption = host_ebr
		NewTab.Screen.WaitForString("$")
		NewTab.Screen.Send("telnet " + host_ebr + chr(13))
		NewTab.Screen.WaitForString("ACS 5.8 username:")
		NewTab.Screen.Send(User_Pass[0]+ chr(13))
		NewTab.Screen.WaitForString("ACS 5.8 password:")
		NewTab.Screen.Send(User_Pass[1] + chr(13))
		NewTab.Screen.WaitForString("#")
		NewTab.Screen.Send("ter len 0" + chr(13))		
		NewTab.Screen.WaitForString("#")
		NewTab.Screen.Send("show bgp neighbor " + pe_add + " advertised-routes" + chr(13))
		NewTab.Screen.WaitForString(" ")
		
if Script_Type == "3":
	for host_ebr,pe_add in zip(Host_Reg8,PE_Address_Reg8):
		cmd = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (user, passwd, host)
		NewTab = crt.Session.ConnectInTab(cmd)
		NewTab.Screen.Synchronous = True
		NewTab.Caption = host_ebr
		NewTab.Screen.WaitForString("$")
		NewTab.Screen.Send("telnet " + host_ebr + chr(13))
		NewTab.Screen.WaitForString("ACS 5.8 username:")
		NewTab.Screen.Send(User_Pass[0]+ chr(13))
		NewTab.Screen.WaitForString("ACS 5.8 password:")
		NewTab.Screen.Send(User_Pass[1] + chr(13))
		NewTab.Screen.WaitForString("#")
		NewTab.Screen.Send("ter len 0" + chr(13))		
		NewTab.Screen.WaitForString("#")
		NewTab.Screen.Send("show bgp neighbor " + pe_add + " advertised-routes" + chr(13))
		NewTab.Screen.WaitForString(" ")
		
if Script_Type == "4":
	for host_ebr,pe_add in zip(Host_Reg9,PE_Address_Reg9):
		cmd = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (user, passwd, host)
		NewTab = crt.Session.ConnectInTab(cmd)
		NewTab.Screen.Synchronous = True
		NewTab.Caption = host_ebr
		NewTab.Screen.WaitForString("$")
		NewTab.Screen.Send("telnet " + host_ebr + chr(13))
		NewTab.Screen.WaitForString("ACS 5.8 username:")
		NewTab.Screen.Send(User_Pass[0]+ chr(13))
		NewTab.Screen.WaitForString("ACS 5.8 password:")
		NewTab.Screen.Send(User_Pass[1] + chr(13))
		NewTab.Screen.WaitForString("#")
		NewTab.Screen.Send("ter len 0" + chr(13))		
		NewTab.Screen.WaitForString("#")
		NewTab.Screen.Send("show bgp neighbor " + pe_add + " advertised-routes" + chr(13))
		NewTab.Screen.WaitForString(" ")
		
if Script_Type == "5":
	for host_ebr,pe_add in zip(Host_Reg11,PE_Address_Reg11):
		cmd = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (user, passwd, host)
		NewTab = crt.Session.ConnectInTab(cmd)
		NewTab.Screen.Synchronous = True
		NewTab.Caption = host_ebr
		NewTab.Screen.WaitForString("$")
		NewTab.Screen.Send("telnet " + host_ebr + chr(13))
		NewTab.Screen.WaitForString("ACS 5.8 username:")
		NewTab.Screen.Send(User_Pass[0]+ chr(13))
		NewTab.Screen.WaitForString("ACS 5.8 password:")
		NewTab.Screen.Send(User_Pass[1] + chr(13))
		NewTab.Screen.WaitForString("#")
		NewTab.Screen.Send("ter len 0" + chr(13))		
		NewTab.Screen.WaitForString("#")
		NewTab.Screen.Send("show bgp neighbor " + pe_add + " advertised-routes" + chr(13))
		NewTab.Screen.WaitForString(" ")
