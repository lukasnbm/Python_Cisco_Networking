# $language = "python"
# $interface = "1.0"

# Author : Lukas Marbun - IP RAN

EVE_IP = "192.168.233.47"
port = [
"32769",
"32770",
"32771",
"32772",
"32773",
#"32774",
#"32775",
#"32776",
#"32777",
#"32778",
#"32779",
#"32780",
]

Script_Type = "1"

if Script_Type == "1":
	for ports in port:
		cmd = "/TELNET %s %s" % (EVE_IP,ports)
		NewTab = crt.Session.ConnectInTab(cmd)
		NewTab.Screen.Synchronous = True