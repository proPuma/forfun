import os, sys
def clearscreen():
    if sys.platform == "linux2":
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
        
clearscreen()
banner = """\033[1;31m 
    __________  ____  ________  ___   __
   / ____/ __ \/ __ \/ ____/ / / / | / /
  / /_  / / / / /_/ / /_  / / / /  |/ / 
 / __/ / /_/ / _, _/ __/ / /_/ / /|  /  
/_/    \____/_/ |_/_/    \____/_/ |_/   
                                        
""""""\033[1;32mcreated by @noname_pxpxpx"""
print(banner)
