#MassBypassShortlink
#!/usr/bin/env python3
import json
import time
import os
import requests
from colorama import Fore, Back, Style
import base64
import pyfiglet

hijau = Fore.GREEN
merah = Fore.RED
cyan = Fore.CYAN
tai = Fore.YELLOW
biru = Fore.BLUE

def clear_window():
	linux = "clear"
	windows ="cls"
	os.system([linux,windows][os.name == "nt"])
clear_window()

def banner():
	logo = pyfiglet.figlet_format("URLSkip")
	print(logo)
	print(cyan+"      [!] Mass Bypass Shortlink ")
	print(Style.RESET_ALL)
	print(tai+"      [!] By : Wan5550")
	print(Style.RESET_ALL)
	print(biru+"      [!] Thanks For My Friend")
	print(Style.RESET_ALL)
	print("_____________________________________")
banner()

print("\n")
input_list = input("[!] List Site Shortlink > ")
print("\n")
open_list = open(input_list,"r").read().splitlines()

for enco in open_list:
    ba64 = base64.b64encode(bytes(enco,encoding='utf8')).decode("utf-8")
    api = "https://lp.nrmn.top/api/bypass?url="
    req = requests.get(api+str(ba64)).text
    try:
        print(hijau+f"URL : {str(enco)} > {json.loads(req)['url']}")
    except:
    	print(merah+f"URL : {str(enco)} > Error No Supported")
    
print(Style.RESET_ALL)
