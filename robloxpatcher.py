#!/usr/bin/env python3
modules = ["requests", "json", "os", "base64", "tkinter"]
version = "1.0.0"

def exitFunc():
	input("> Press enter to exit <")
	exit()

for module in modules:
	try:
		print("Importing "+module+"...")
		exec("import "+module)
		print("Imported "+module+"!")
	except:
		print("Please install the \""+module+"\" module.")
		exitFunc()

url = 'https://api.github.com/repos/TJ20201/RobloxPatcher/contents/meta.json'
req = requests.get(url)
content = ''
if req.status_code == requests.codes.ok:
	req = req.json()
	content = base64.b64decode(req['content'])
if content = '':
	print("The content of the meta.json can not be found. Do you have an accessible internet connection?")
	exitFunc()
jcont = json.loads(content)
lts_version = jcont["rp_ver"]
if lts_version != version:
	print(f"A (possibly newer) stable version of the Roblox Patcher tool is available. (Latest stable version {lts_version} is available whilst you are on version {version}.)")
else:
	try:
		print("------")
		# Changable types: sound
		drt = input("Input the path to your local Roblox installation without a trailing slash. (folder that contains RobloxBetaLauncher.exe) >> ")
		typ = input("Specify what you would like to change to an older version. (sound) >> ")
		name = jcont["name"]
		# TYPE: SOUND
		if typ == 'sound':
			name = name["sound"]
			tub = input("Specify which sound you would like to change. (death) >>")
			# SUBTYPE: DEATH
			if tub == 'death':
				name = name["death"]
				tfn = input('Specify which sound would you like the DEATH SOUND to be. DO NOT INCLUDE /old OR /new[n] (oof/old | augh/new1) >> ')
				# SET DEATH TO OOF
				if tfn == "oof":
					target = drt+f"/content/sounds/{name}"
		exitFunc()
