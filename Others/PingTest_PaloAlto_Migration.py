# $language = "python"
# $interface = "1.0"

# // OSSERA Variables //
host = "10.175.1.151"
user = "vitogui"
passwd = "May20.com"


# // Script Variables //
SOURCE_NODE = ["sr-tbs.1-new","sr-tbs.2-new"]
VRF = "Gn"
DESTINATION = [
"221.132.214.145",
"221.132.214.152",
"114.126.38.145 ",
"114.126.38.152 ",
]

for source in SOURCE_NODE:
	for destination in DESTINATION:
		cmd = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (user, passwd, host)
		NewTab = crt.Session.ConnectInTab(cmd)
		NewTab.Screen.Synchronous = True
		NewTab.Caption = source
		NewTab.Screen.WaitForString("$")
		NewTab.Screen.Send("telnet " + source + chr(13))
		NewTab.Screen.WaitForString("ACS 5.8 username:")
		NewTab.Screen.Send(user + chr(13))
		NewTab.Screen.WaitForString("ACS 5.8 password:")
		NewTab.Screen.Send(passwd + chr(13))
		NewTab.Screen.WaitForString("#")
		NewTab.Screen.Send("ping vrf " + VRF + " " + destination + " interval 600 rep 80000 " + chr(13))
		#NewTab.Screen.Send("ping vrf " + VRF + " " + destination + " interval 600 rep 200 " + chr(13))
		NewTab.Screen.WaitForString("abort.")