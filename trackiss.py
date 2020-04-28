import requests
from termcolor import cprint
from pprint import pprint
from pyfiglet import figlet_format
cprint(figlet_format("\t      TRACKISS",font="standard"),"red",attrs=["bold"])
a=requests.get("https://api.wheretheiss.at/v1/satellites/25544")
j=a.json()
print("\033[31;1m[*]Exact and Current Data of ISS !!! ")
print("\033[33;1m")
pprint(j)

