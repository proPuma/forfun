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
 _______   _____   ______   _______  _______  _     _  ______
(_______) / ___ \ (_____ \ (_______)(_______)| |   | ||  ___ \
 _____   | |   | | _____) ) _____    _____   | |   | || |   | |       |  ___)  | |   | |(_____ ( |  ___)  |  ___)  | |   | || |   | |
| |      | |___| |      | || |_____ | |      | |___| || |   | |
|_|       \_____/       |_||_______)|_|       \______||_|   |_|""""""\033[1;32mcreated by @noname_pxpxpx"""
print(banner)