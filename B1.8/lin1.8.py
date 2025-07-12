print("Loading LinPy\n")
print("Loading module os...")
import os
print("Loaded module os                                (100%)")
print("Loading hashlib ...")
import hashlib
print("Loaded hashlib                                  (100%)")
print("Loading json ...")
import json
print("Loaded json                                     (100%)")
print("Loading module shutil")
import shutil
print("Loaded module shutil                            (100%)")
print("Loading module time...")
import time
print("Loaded module time                              (100%)")
print("Loading module datetime...")
import datetime
print("Loaded module datetime                          (100%)")
print("Importing module random")
import random
print("Imported module random                          (100%)")
print("Loading module threading...")
import threading
print("Loaded threading                                (100%)")
print("Loading module sys...")
import sys
print("Loaded module sys                               (100%)")
print("Loading module socket...")
import socket
print("Loaded module socket                            (100%)")
print("Loading module webbrowser...")
import webbrowser
print("Loaded module webbrowser                        (100%)")
print("Loading nmap...")
import nmap
print("Loaded nmap                                     (100%)")
print("Importing encrytion and decryption tools")
import base64
from cryptography.fernet import Fernet, InvalidToken
print("Imported encryption and decryption tools        (100%)")
print("Importing pinging feature")
from ping3 import ping, verbose_ping
print("Imported pinging features                       (100%)")
print("Loading logo")
logo = """
      /\  /\                                     
      ||__||                                     
      |    |                                     
      | || |                                     
╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗
█                                               █       Socials:
█  _     _       ______   __   ___  ____        █       https://www.tiktok.com/@an0nsn1pr
█ | |   (_)_ __ |  _ \ \ / /  / _ \/ ___|       █       https://www.youtube.com/@An0nySn1pr
█ | |   | | '_ \| |_) \ V /  | | | \___ \       █       https://x.com/AnOnSn1pr
█ | |___| | | | |  __/ | |   | |_| |___) |      █       
█ |_____|_|_| |_|_|    |_|    \___/|____/       █       Join the LinPY Community on Discord:
█                                               █       https://discord.gg/nYBvazmP
█   /\_/\  (0>                                  █
█  ( o.o ) //\             Made by an0nsn1pr :D █       E-mail me: 
█   > - <  V_/_                                 █       an0nsn1pr@gmail.com
╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝
"""
print("Loaded logo                                     (100%)")
print("Importing text editor(made with ChatGPT)")
import curses

#Not very proud of this lol
def nano_editor(stdscr, editfilename):
    curses.curs_set(1)
    stdscr.keypad(True)

    if os.path.exists(editfilename):
        with open(editfilename, "r") as f:
            lines = f.read().splitlines()
    else:

        raise FileNotFoundError(f"{editfilename} does not exist")
        
    y, x = 0, 0 

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Press Ctrl+X to exit")
        stdscr.addstr(1, 0, "Press Ctrl+O to save")
        stdscr.addstr(2, 0, "Press Ctrl+K to delete current line")
        stdscr.addstr(4, 0, "-" * 40)
        for idx, line in enumerate(lines):
            stdscr.addstr(idx + 5, 0, line)

        stdscr.move(y + 5, x) 
        stdscr.refresh()

        key = stdscr.getch()

        if key == 24:
            break
        elif key == 15:  
            with open(editfilename, "w") as f:
                f.write("\n".join(lines))
            stdscr.addstr(len(lines) + 6, 0, f"Saved to {editfilename}. Press any key.")
            stdscr.getch()
        elif key == 11:
            if lines:
                lines.pop(y)
                if y >= len(lines):
                    y = max(0, len(lines) - 1)
                if not lines:
                    lines.append("")
        elif key == curses.KEY_ENTER or key == 10 or key == 13:
            current = lines[y]
            lines[y] = current[:x]
            lines.insert(y + 1, current[x:])
            y += 1
            x = 0
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            if x > 0:
                lines[y] = lines[y][:x - 1] + lines[y][x:]
                x -= 1
            elif y > 0:
                x = len(lines[y - 1])
                lines[y - 1] += lines[y]
                lines.pop(y)
                y -= 1
        elif key == curses.KEY_UP:
            y = max(0, y - 1)
            x = min(x, len(lines[y]))
        elif key == curses.KEY_DOWN:
            y = min(len(lines) - 1, y + 1)
            x = min(x, len(lines[y]))
        elif key == curses.KEY_LEFT:
            x = max(0, x - 1)
        elif key == curses.KEY_RIGHT:
            x = min(len(lines[y]), x + 1)
        elif 32 <= key <= 126:
            while y >= len(lines):
                lines.append("")

            lines[y] = lines[y][:x] + chr(key) + lines[y][x:]
            x += 1

print("Loaded text editor")
print("Getting current directory...")
filename = "lin.py"
try:
    currentdir = "root"
    linpypath = os.getcwd()
    rootfolder = "rfolderb18"
    filesystempath = linpypath+'\\'+rootfolder

    if not os.path.exists(filesystempath):
        os.system("cls")
        print("Looks like the LinPY filesystem inst installed")
        print("Dont worry i got you ;)")
        time.sleep(2)
        os.system("cls")
        print(logo+"\n")
        print("Making the ROOT folder")
        os.mkdir(rootfolder)
        print("Made the ROOT folder")
        print("Changing directory to the new ROOT folder")
        os.chdir(filesystempath)
        print("Making the main JSON file")
        sj = {
            "setupcheck":False,
            "username": " ",
            "passw": " ",
            "version": "Beta 1.8"
        }
        with open("setup.json", "w") as f:
            json.dump(sj, f, indent=4)
        print("Made the main file")
        print("Making the ROOT JSON file")
        with open("root.json", "w") as f:
            json.dump({"name": " ", "dirlist":[], "filelist": []}, f, indent=4)
        print("Made the ROOT file")
        print("Making the directory JSON files")

        dirdfl = {
            "name": " ",
            "use": False,
            "filelist": []
            }
        
        print("     Making dir 1")
        with open("dir1.json", "w") as f:
            json.dump(dirdfl, f, indent=4)
        print("     Made dir 1")

        print("     Making dir 2")
        with open("dir2.json", "w") as f:
            json.dump(dirdfl, f, indent=4)
        print("     Made dir 2")

        print("     Making dir 3")
        with open("dir3.json", "w") as f:
            json.dump(dirdfl, f, indent=4)
        print("     Made dir 3")

        print("     Making dir 4")
        with open("dir4.json", "w") as f:
            json.dump(dirdfl, f, indent=4)
        print("     Made dir 4")

        print("     Making dir 5")
        with open("dir5.json", "w") as f:
            json.dump(dirdfl, f, indent=4)
        print("     Made dir 5")

        print("     Making dir 6")
        with open("dir6.json", "w") as f:
            json.dump(dirdfl, f, indent=4)
        print("     Made dir 6")

        print("     Making dir 7")
        with open("dir7.json", "w") as f:
            json.dump(dirdfl, f, indent=4)
        print("     Made dir 7")

        print("     Making dir 8")
        with open("dir8.json", "w") as f:
            json.dump(dirdfl, f, indent=4)
        print("     Made dir 8")

        print("     Making dir 9")
        with open("dir9.json", "w") as f:
            json.dump(dirdfl, f, indent=4)
        print("     Made dir 9")

        print("     Making dir 10")
        with open("dir10.json", "w") as f:
            json.dump(dirdfl, f, indent=4)
        print("     Made dir 10")
        print("Finished with the directories, be wise you have only 10 at the moment")

        
        print("Making deafult commands JSON file")
        deafultcmd = {
                "help": "help",
                "changepsw": "changepsw",
                "changeuser" : "changeuser",
                "delacc": "delacc",
                "reset": "reset",
                "print": "print",
                "hexample": "hexample",
                "ls": "ls",
                "lsall": "lsall",
                "cd": "cd",
                "cd ..": "cd ..",
                "pwd": "pwd",
                "mkdir": "mkdir",
                "whoami": "whoami",
                "rmdir": "rmdir",
                "rm": "rm",
                "mkfile": "mkfile",
                "encrypt":"encrypt",
                "decrypt":"decrypt",
                "ping":"ping",
                "nano":"nano"   ,
                "time":"time",
                "clear":"clear",
                "nmap":"nmap",
                "credits":"credits",
                "quit":"quit",
                "restart":"restart"
        }

        with open("deafultcommands.json", "w") as f:
            json.dump(deafultcmd, f, indent=4)

        with open("commands.json", "w") as f:
            json.dump(deafultcmd, f, indent=4)
        print("Made deafult commands JSON file")
        print("Press ENTER if you are not a nerd")
        input()
        os.system("cls")
        print(logo)
        print("\nRestarting in 2 seconds")
        time.sleep(2)
        os.system("cls")
        os.system("python " + filename)
    
    else:
        print("Changing current directory to ROOT")
        os.chdir(filesystempath)
        print("Changed directory                               (100%)")

except Exception as e:
    print("Looks like LinPY filesystem isnt installed")
    print("Error: ", e)

print("Loading files and folders...")

with open("setup.json", "r") as f:
    setup = json.load(f)
with open("dir1.json", "r") as f:
    dir1 = json.load(f)
with open("dir2.json", "r") as f:
    dir2 = json.load(f)
with open("dir3.json", "r") as f:
    dir3 = json.load(f)
with open("dir4.json", "r") as f:
    dir4 = json.load(f)
with open("dir5.json", "r") as f:
    dir5 = json.load(f)
with open("dir6.json", "r") as f:
    dir6 = json.load(f)
with open("dir7.json", "r") as f:
    dir7 = json.load(f)
with open("dir8.json", "r") as f:
    dir8 = json.load(f)
with open("dir9.json", "r") as f:
    dir9 = json.load(f)
with open("dir10.json", "r") as f:
    dir10 = json.load(f)
with open("root.json", "r") as f:
    root = json.load(f)
with open("commands.json", "r") as f:
    commands= json.load(f)
with open("deafultcommands.json", "r") as f:
    d_commands = json.load(f)

print("Loaded files and folder                         (100%)")
print("Loading credentials...")

starttime = datetime.datetime.now()

user = setup["username"]
version = setup["version"]

print("Loaded credentials                              (100%)")
print("Loading Commands")
helpcmd = commands["help"]
changepsw =commands["changepsw"]
changeuser=commands["changeuser"]
delacc    =commands["delacc"]
reset = commands["reset"]
printcmd =commands["print"]
hexample=  commands["hexample"]
ls = commands["ls"]
lsall=    commands["lsall"]
cd  =      commands["cd"]
cd_back =    commands["cd .."]
pwd    =  commands["pwd"]
mkdircmd   =  commands["mkdir"]
whoami   = commands["whoami"]
rmdir     =commands["rmdir"]
rm        =commands["rm"]
mkfile   =commands["mkfile"]
encrypt   =commands["encrypt"]
decrypt = commands["decrypt"]
pingcmd     =commands["ping"]
nano     =commands["nano"]
timecmd =commands["time"]
clear    =commands["clear"]
nmapcmd   =commands["nmap"]
credits   =commands["credits"]
quit      =commands["quit"]
restart =commands["restart"]

print("\nCommands: \n\n" + helpcmd)
print(changepsw)
print(changeuser)
print(delacc)
print(reset)
print(printcmd)
print(hexample)
print(ls)
print(lsall)
print(cd)
print(cd_back)
print(pwd)
print(mkdircmd)
print(whoami)
print(rmdir)
print(rm)
print(mkfile)
print(encrypt)
print(decrypt)
print(pingcmd)
print(nano)
print(timecmd)
print(clear)
print(nmapcmd)
print(credits)
print(quit)
print(restart + "\n")

print("Loaded commands                                 (100%)")
print("Loaded everything                               (100%)...\n\n")

print("Loaded LinPy OS")
input("Press ENTER to continue or view what LinPY loaded\n")
os.system("cls")
print("Welcome to LinPy OS\n")
print(f"Time of launch:  {starttime}")
print(f"Version {version}\n")
print(logo+"\n")

if setup["setupcheck"] == False:
    print("LINPY OS SETUP: \n")
    n=1
    while n>0:
        user = input("What would you like your USERNAME to be?\n   $ ")
        password = input("What would you like your PASSWORD to be?\n   $ ")
        confirm = input(f"Are you sure you want your username to be \"{user}\" and your password to be \"{password}\" ? [y/n]")

        p = hashlib.new("SHA256")
        p.update(password.encode())
        if confirm== "y":
            setup["username"] = user
            setup["passw"] = p.hexdigest()
            setup["setupcheck"] = True
            n = 0
            print(f"\nWelcome to LinPy {user}! Press ENTER to go on with your OS!!!")
            input()
            with open("setup.json", "w") as f:
                json.dump(setup, f, indent=4)

        elif confirm== "n":
            print("Okay, set your new USERNAME and PASSWORD below:")
        else:
            print("NOT AN OPTION! Please answer the confirmation question with a y for yes, and n for no.")
else:
    print(f"Welcome back {setup['username']}!\n")
    i = 1
    wrong = 0
    while i > 0:
        passlogin = input("Password:  ").strip().encode()
        passlogin_hash = hashlib.sha256(passlogin).hexdigest()
        if setup["passw"] == passlogin_hash:
            print("You are logged in!")
            input()
            break
        else:
            print("WRONG PASSWORD\n")
            wrong += 1
            if wrong==5:
                print("You must wait 2 mintes before you can try again!")
                time.sleep(120)
                wrong=0

cmd_list = (f"""
{helpcmd}      -       tells you the avalibile commands and their porpuse
{changepsw} -       lets you change the psw
{changeuser}-       lets you change your username
{delacc}    -       deletes your credentials
{reset}     -       deletes your entire folder system
{printcmd}     -       prints the folowing text
{hexample}  -       shows you commands and the format the they are used
{ls}        -       lists the files and the directories on the current directory
{lsall}     -       lists all the the files and directories on the machine
{cd}        -       changes the directory
{pwd}       -       prints the current directory
{mkdircmd}     -       makes a new directory
{whoami}    -       tells the username 
{rmdir}     -       deletes folder
{rm}        -       deletes the file
{mkfile}    -       makes a file inside of the current working directory
{encrypt}   -       encrypts a file with a password of your chosing plus double hashing
{decrypt}   -       decrypts a file with the password you used before
{pingcmd}      -       check to see if an IP or domain is up
{nano}      -       edit a file
{timecmd}      -       prints current time and date
{clear}     -       clears screen
{nmapcmd}      -       port scanner
{credits}   -       gives the credits to the people who made some tools in this app
{quit}      -       shuts down LinPY
{restart}   -       restarts LinPY, its not usefull but good to have
                """)

cmdhelp_list = (f"""
{help}      -       {help}
{printcmd}     -       {printcmd} [whatever text you want]
{changepsw} -       {changepsw}
{changeuser}-       {changeuser}
{delacc}    -       {delacc}
{reset}     -       {reset}
{hexample}  -       {hexample}
{ls}        -       {ls}
{lsall}     -       {lsall}
{cd}        -       {cd} [number assinged to directory/..]
{pwd}       -       {pwd}
{mkdircmd}     -       {mkdircmd} [slot 1-20] [name of the directory]
{whoami}    -       {whoami}
{rmdir}     -       {rmdir} [1-20]
{rm}        -       {rm} [filename]
{mkfile}    -       {mkfile} [name] [extension]
{encrypt}   -       {encrypt} [filename.extension]
{decrypt}   -       {decrypt} [filename.extension]
{nano}      -       {nano} [filename.extension]
{pingcmd}      -       {pingcmd} [IP or Domain] [optional: a number that will ping the IP x4]
{timecmd}      -       {timecmd}
{clear}     -       {clear} [optional: -nologo]
{nmapcmd}      -       {nmapcmd}
{credits}   -       {credits} [optional: name of the tool]
{quit}      -       {quit}
{restart}   -       {restart}
""")

nmap_help = ("""
Avalibile commands:

help
exit
scan
""")

chatcmd = ("""
Avalibile commands:
           
help
startchat
exit
""")

while True:
    try:
        cp = filesystempath 
        cp2 = cp + "\\"
        currentpath = os.getcwd()
        
        names = [dir1["name"], dir2["name"], dir3["name"], dir4["name"],
                dir5["name"], dir6["name"], dir7["name"], dir8["name"],
                dir9["name"], dir10["name"]]

        valid_paths = [cp] + [cp2 + name for name in names]

        if currentpath not in valid_paths:
            os.chdir(cp)

        cmd = input(f"{user}@{currentdir} >>> ")
        
        command = cmd.split()

        if not cmd:
            continue

        if cmd == helpcmd:
            print(cmd_list)
        elif cmd == hexample:
            print(cmdhelp_list)

        elif cmd == quit:
            os.system("cls")
            print(logo)
            print("Shutting down LinPy.....")
            print("Bye bye, cya next time :D (if there is a next time)")
            time.sleep(2)
            os.system("cls")
            break

        elif command[0] == restart:
            os.system("cls")
            print(logo)
            print("Restarting in a sec")
            time.sleep(2)
            if currentdir == "root":
                os.chdir("..")
                os.system("cls")
                os.system("python lin.py")
                break
            else:
                os.chdir("..")
                os.chdir("..")
                os.system("cls")
                os.system("python lin.py")
                break
        
        elif command[0] == "reset":
            print("WARNING: the ROOT folder will be reinstalled but if you need any file back, its in the bin :)")
            print("Type \"Confirm\" to delete, type \"n\"to quit")
            confirm_reset = input(">>> ")
            if confirm_reset == "n":
                print("Okay not deleting your files")
            elif confirm_reset == "Confirm":
                print("Confirm with your password")
                confirm_reset_psw = input(">>> ")
                crp_hex = hashlib.sha256(confirm_reset_psw.encode()).hexdigest()
                if crp_hex == setup["passw"]:
                    os.system("cls")
                    print(logo)
                    print("Reseting everything")
                    os.chdir("..")
                    shutil.rmtree(filesystempath)
                    print("Removed the filesystem")
                    print("Start LinPY again for a new filesystem :)")
                    time.sleep(2)
                    os.system("cls")
                    break

                else:
                    print("Looks like your system is safe, because you didnt type the correct password LOL")
        elif command[0] == printcmd:
            print(" ".join(command[1:]))

        elif command[0] == mkdircmd:
            if len(command) < 3:
                print("Opss not enough arguments!")
                continue
            if currentdir != "root":
                print("Unable to make folder because our filesystem allows only 10 subfolders inside the ROOT folder")
                continue
            print("Making directory")
            name = command[2]
            ename = ("(1)" + name)
            if command[1] == "1":
                ename = ("(1)" + name)
                if name==dir2["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir3["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir4["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir5["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir6["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir7["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir8["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir9["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir10["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif dir1["use"] == True:
                    print("Unable to make this folder because slot is already used")
                else:
                    dir1["name"] = name
                    dir1["use"] = True
                    os.mkdir(name)
                    with open("dir1.json", "w") as f:
                        json.dump(dir1, f, indent=4)
                    if ename not in root["dirlist"]:
                        root["dirlist"].append(ename)
                    with open("root.json", "w") as f:
                        json.dump(root, f, indent=4)
                    os.chdir(filesystempath + '\\' + name)
                    currentdir = {name} 
                    cjsonfile = open("data.json", "w")
                    with cjsonfile as f:
                        json.dump({"name": name, "filelist":[]}, f, indent=4)
                    os.chdir("..")
                    currentdir = "root"
            elif command[1] == "2":
                ename = ("(2)" + name)
                if name==dir1["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir3["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir4["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir5["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir6["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir7["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir8["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir9["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir10["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif dir2["use"] == True:
                    print("Unable to make this folder because slot is already used")
                else:
                    dir2["name"] = name
                    dir2["use"] = True
                    os.mkdir(name)
                    with open("dir2.json", "w") as f:
                        json.dump(dir2, f, indent=4)
                    if ename not in root["dirlist"]:
                        root["dirlist"].append(ename)
                    with open("root.json", "w") as f:
                        json.dump(root, f, indent=4)
                    os.chdir(filesystempath + '\\' + name)
                    currentdir = {name} 
                    cjsonfile = open("data.json", "w")
                    with cjsonfile as f:
                        json.dump({"name": name, "filelist":[]}, f, indent=4)
                    os.chdir("..")
                    currentdir = "root"
            elif command[1] == "3":
                ename = ("(3)" + name)
                if name==dir2["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir1["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir4["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir5["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir6["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir7["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir8["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir9["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir10["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif dir3["use"] == True:
                    print("Unable to make this folder because slot is already used")
                else:
                    dir3["name"] = name
                    dir3["use"] = True
                    os.mkdir(name)
                    with open("dir3.json", "w") as f:
                        json.dump(dir3, f, indent=4)
                    if ename not in root["dirlist"]:
                        root["dirlist"].append(ename)
                    with open("root.json", "w") as f:
                        json.dump(root, f, indent=4)
                    os.chdir(filesystempath + '\\' + name)
                    currentdir = {name} 
                    cjsonfile = open("data.json", "w")
                    with cjsonfile as f:
                        json.dump({"name": name, "filelist":[]}, f, indent=4)
                    os.chdir("..")
                    currentdir = "root"
            elif command[1] == "4":
                ename = ("(4)" + name)
                if name==dir2["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir3["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir1["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir5["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir6["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir7["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir8["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir9["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir10["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif dir4["use"] == True:
                    print("Unable to make this folder because slot is already used")
                else:
                    dir4["name"] = name
                    dir4["use"] = True
                    os.mkdir(name)
                    with open("dir4.json", "w") as f:
                        json.dump(dir4, f, indent=4)
                    if ename not in root["dirlist"]:
                        root["dirlist"].append(ename)
                    with open("root.json", "w") as f:
                        json.dump(root, f, indent=4)
                    os.chdir(filesystempath + '\\' + name)
                    currentdir = {name} 
                    cjsonfile = open("data.json", "w")
                    with cjsonfile as f:
                        json.dump({"name": name, "filelist":[]}, f, indent=4)
                    os.chdir("..")
                    currentdir = "root"
            elif command[1] == "5":
                ename = ("(5)" + name)
                if name==dir2["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir3["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir4["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir1["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir6["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir7["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir8["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir9["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir10["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif dir5["use"] == True:
                    print("Unable to make this folder because slot is already used")
                else:
                    dir5["name"] = name
                    dir5["use"] = True
                    os.mkdir(name)
                    with open("dir5.json", "w") as f:
                        json.dump(dir5, f, indent=4)
                    if ename not in root["dirlist"]:
                        root["dirlist"].append(ename)
                    with open("root.json", "w") as f:
                        json.dump(root, f, indent=4)
                    os.chdir(filesystempath + '\\' + name)
                    currentdir = {name} 
                    cjsonfile = open("data.json", "w")
                    with cjsonfile as f:
                        json.dump({"name": name, "filelist":[]}, f, indent=4)
                    os.chdir("..")
                    currentdir = "root"
            elif command[1] == "6":
                ename = ("(6)" + name)
                if name==dir2["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir3["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir4["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir5["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir1["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir7["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir8["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir9["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir10["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif dir6["use"] == True:
                    print("Unable to make this folder because slot is already used")
                else:
                    dir6["name"] = name
                    dir6["use"] = True
                    os.mkdir(name)
                    with open("dir6.json", "w") as f:
                        json.dump(dir6, f, indent=4)
                    if ename not in root["dirlist"]:
                        root["dirlist"].append(ename)
                    with open("root.json", "w") as f:
                        json.dump(root, f, indent=4)
                    os.chdir(filesystempath + '\\' + name)
                    currentdir = {name} 
                    cjsonfile = open("data.json", "w")
                    with cjsonfile as f:
                        json.dump({"name": name, "filelist":[]}, f, indent=4)
                    os.chdir("..")
                    currentdir = "root"
            elif command[1] == "7":
                ename = ("(7)" + name)
                if name==dir2["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir3["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir4["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir5["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir6["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir1["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir8["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir9["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir10["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif dir7["use"] == True:
                    print("Unable to make this folder because slot is already used")
                else:
                    dir7["name"] = name
                    dir7["use"] = True
                    os.mkdir(name)
                    with open("dir7.json", "w") as f:
                        json.dump(dir7, f, indent=4)
                    if ename not in root["dirlist"]:
                        root["dirlist"].append(ename)
                    with open("root.json", "w") as f:
                        json.dump(root, f, indent=4)
                    os.chdir(filesystempath + '\\' + name)
                    currentdir = {name} 
                    cjsonfile = open("data.json", "w")
                    with cjsonfile as f:
                        json.dump({"name": name, "filelist":[]}, f, indent=4)
                    os.chdir("..")
                    currentdir = "root"
            elif command[1] == "8":
                ename = ("(8)" + name)
                if name==dir2["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir3["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir4["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir5["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir6["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir7["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir1["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir9["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir10["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif dir8["use"] == True:
                    print("Unable to make this folder because slot is already used")
                else:
                    dir8["name"] = name
                    dir8["use"] = True
                    os.mkdir(name)
                    with open("dir8.json", "w") as f:
                        json.dump(dir8, f, indent=4)
                    if ename not in root["dirlist"]:
                        root["dirlist"].append(ename)
                    with open("root.json", "w") as f:
                        json.dump(root, f, indent=4)
                    os.chdir(filesystempath + '\\' + name)
                    currentdir = {name} 
                    cjsonfile = open("data.json", "w")
                    with cjsonfile as f:
                        json.dump({"name": name, "filelist":[]}, f, indent=4)
                    os.chdir("..")
                    currentdir = "root"
            elif command[1] == "9":
                ename = ("(9)" + name)
                if name==dir2["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir3["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir4["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir5["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir6["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir7["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir8["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir1["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir10["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif dir9["use"] == True:
                    print("Unable to make this folder because slot is already used")
                else:
                    dir9["name"] = name
                    dir9["use"] = True
                    os.mkdir(name)
                    with open("dir9.json", "w") as f:
                        json.dump(dir9, f, indent=4)
                    if ename not in root["dirlist"]:
                        root["dirlist"].append(ename)
                    with open("root.json", "w") as f:
                        json.dump(root, f, indent=4)
                    os.chdir(filesystempath + '\\' + name)
                    currentdir = {name} 
                    cjsonfile = open("data.json", "w")
                    with cjsonfile as f:
                        json.dump({"name": name, "filelist":[]}, f, indent=4)
                    os.chdir("..")
                    currentdir = "root"
            elif command[1] == "10":
                ename = ("(10)" + name)
                if name==dir2["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir3["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir4["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir5["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir6["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir7["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir8["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir9["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif name==dir1["name"]:
                    print("Unable to make folder because a folder with this name already exists")
                elif dir10["use"] == True:
                    print("Unable to make this folder because slot is already used")
                else:
                    dir10["name"] = name
                    dir10["use"] = True
                    os.mkdir(name)
                    with open("dir10.json", "w") as f:
                        json.dump(dir10, f, indent=4)
                    if ename not in root["dirlist"]:
                        root["dirlist"].append(ename)
                    with open("root.json", "w") as f:
                        json.dump(root, f, indent=4)
                    os.chdir(filesystempath + '\\' + name)
                    currentdir = {name} 
                    cjsonfile = open("data.json", "w")
                    with cjsonfile as f:
                        json.dump({"name": name, "filelist":[]}, f, indent=4)
                    os.chdir("..")
                    currentdir = "root"
            else:
                print("There are no more slots due to the filesystem (sorry)")
        
        elif command[0] == cd:
            if len(command) < 2:
                print("Not enoght arguments silly :D")
                continue
            if currentdir == "root":
                
                if command[1] == "1":
                    if dir1["use"] == False:
                        print("Folder doesnt exist (yet)")
                    else:
                        os.chdir(filesystempath + "\\" +dir1["name"])
                        currentdir = dir1["name"]

                elif command[1] == "2":
                    if dir2["use"] == False:
                        print("Folder doesnt exist (yet)")
                    else:
                        os.chdir(filesystempath + "\\" + dir2["name"])
                        currentdir = dir2["name"]

                elif command[1] == "3":
                    if dir3["use"] == False:
                        print("Folder doesnt exist (yet)")
                    else:
                        os.chdir(filesystempath+ "\\" + dir3["name"])
                        currentdir = dir3["name"]

                elif command[1] == "4":
                    if dir4["use"] == False:
                        print("Folder doesnt exist (yet)")
                    else:
                        os.chdir(filesystempath+ "\\" + dir4["name"])
                        currentdir = dir4["name"]

                elif command[1] == "5":
                    if dir5["use"] == False:
                        print("Folder doesnt exist (yet)")
                    else:
                        os.chdir(filesystempath+ "\\" + dir5["name"])
                        currentdir = dir5["name"]

                elif command[1] == "6":
                    if dir6["use"] == False:
                        print("Folder doesnt exist (yet)")
                    else:
                        os.chdir(filesystempath+ "\\" + dir6["name"])
                        currentdir = dir6["name"]

                elif command[1] == "7":
                    if dir7["use"] == False:
                        print("Folder doesnt exist (yet)")
                    else:
                        os.chdir(filesystempath+ "\\" + dir7["name"])
                        currentdir = dir7["name"]

                elif command[1] == "8":
                    if dir8["use"] == False:
                        print("Folder doesnt exist (yet)")
                    else:
                        os.chdir(filesystempath+ "\\" + dir8["name"])
                        currentdir = dir8["name"]

                elif command[1] == "9":
                    if dir9["use"] == False:
                        print("Folder doesnt exist (yet)")
                    else:
                        os.chdir(filesystempath+ "\\" + dir9["name"])
                        currentdir = dir9["name"]

                elif command[1] == "10":
                    if dir10["use"] == False:
                        print("Folder doesnt exist (yet)")
                    else:
                        os.chdir(filesystempath+ "\\" + dir10["name"])    
                        currentdir = dir10["name"]
                
                else:
                    print("Not an avalibile folder!")
            if command[1] == "..":
                os.chdir("..")
                currentdir = "root"

        elif command[0] == pwd:
            print(currentdir)
            print(os.getcwd())

        elif command[0] == whoami:
            print(setup["username"])
        
        elif command[0] == rmdir:
            if len(command) < 2:    
                print("Forgot the directory!")
                continue
            if currentdir != "root":
                os.chdir("..")
                currentdir = "root"
            
            if command[1] == "1":
                    namebd = dir1["name"]
                    delname = ("(1)"+dir1["name"])
                    shutil.rmtree(dir1["name"])
                    dir1["name"] = " "
                    dir1["use"] = False
                    with open("dir1.json", "w") as f:
                            json.dump(dir1, f, indent=4)
                    if delname in root["dirlist"]:
                        root["dirlist"].remove(delname)
                    with open("root.json", "w") as f:
                            json.dump(root, f, indent=4)  
                    print(f"Deleted folder \"{namebd}\"")

            elif command[1] == "2":
                    delname = ("(2)"+dir2["name"])
                    delname1 = (dir2["name"])
                    shutil.rmtree(filesystempath + '\\' + delname1)
                    dir2["name"] = " "
                    dir2["use"] = False
                    with open("dir2.json", "w") as f:
                            json.dump(dir2, f, indent=4)
                    if delname in root["dirlist"]:
                        root["dirlist"].remove(delname)
                    with open("root.json", "w") as f:
                            json.dump(root, f, indent=4)
                    print(f"Deleted folder \"{delname1}\"")

            elif command[1] == "3":
                    namebd = dir3["name"]
                    delname = ("(3)"+dir3["name"])
                    shutil.rmtree(dir3["name"])
                    dir3["name"] = " "
                    dir3["use"] = False
                    with open("dir3.json", "w") as f:
                            json.dump(dir3, f, indent=4)
                    if delname in root["dirlist"]:
                        root["dirlist"].remove(delname)
                    with open("root.json", "w") as f:
                            json.dump(root, f, indent=4)
                    print(f"Deleted folder \"{namebd}\"")

            elif command[1] == "4":
                    namebd = dir4["name"]
                    delname = ("(4)"+dir4["name"])
                    shutil.rmtree(dir4["name"])
                    dir4["name"] = " "
                    dir4["use"] = False
                    with open("dir4.json", "w") as f:
                            json.dump(dir4, f, indent=4)
                    if delname in root["dirlist"]:
                        root["dirlist"].remove(delname)
                    with open("root.json", "w") as f:
                            json.dump(root, f, indent=4)
                    print(f"Deleted folder \"{namebd}\"")

            elif command[1] == "5":
                    namebd = dir5["name"]
                    delname = ("(5)"+dir5["name"])
                    shutil.rmtree(dir5["name"])
                    dir5["name"] = " "
                    dir5["use"] = False
                    with open("dir5.json", "w") as f:
                            json.dump(dir5, f, indent=4)
                    if delname in root["dirlist"]:
                        root["dirlist"].remove(delname)
                    with open("root.json", "w") as f:
                            json.dump(root, f, indent=4)
                    print(f"Deleted folder \"{namebd}\"")

            elif command[1] == "6":
                    namebd = dir6["name"]
                    delname = ("(6)"+dir6["name"])
                    shutil.rmtree(dir6["name"])
                    dir6["name"] = " "
                    dir6["use"] = False
                    with open("dir6.json", "w") as f:
                            json.dump(dir6, f, indent=4)
                    if delname in root["dirlist"]:
                        root["dirlist"].remove(delname)
                    with open("root.json", "w") as f:
                            json.dump(root, f, indent=4)
                    print(f"Deleted folder \"{namebd}\"")

            elif command[1] == "7":
                    namebd = dir7["name"]
                    delname = ("(7)"+dir7["name"])
                    shutil.rmtree(dir7["name"])
                    dir7["name"] = " "
                    dir7["use"] = False
                    with open("dir7.json", "w") as f:
                            json.dump(dir7, f, indent=4)
                    if delname in root["dirlist"]:
                        root["dirlist"].remove(delname)
                    with open("root.json", "w") as f:
                            json.dump(root, f, indent=4)
                    print(f"Deleted folder \"{namebd}\"")

            elif command[1] == "8":
                    namebd = dir8["name"]
                    delname = ("(8)"+dir8["name"])
                    shutil.rmtree(dir8["name"])
                    dir8["name"] = " "
                    dir8["use"] = False
                    with open("dir8.json", "w") as f:
                            json.dump(dir8, f, indent=4)
                    if delname in root["dirlist"]:
                        root["dirlist"].remove(delname)
                    with open("root.json", "w") as f:
                            json.dump(root, f, indent=4)
                    print(f"Deleted folder \"{namebd}\"")

            elif command[1] == "9":
                    namebd = dir9["name"]
                    delname = ("(9)"+dir9["name"])
                    shutil.rmtree(dir9["name"])
                    dir9["name"] = " "
                    dir9["use"] = False
                    with open("dir9.json", "w") as f:
                            json.dump(dir9, f, indent=4)
                    if delname in root["dirlist"]:
                        root["dirlist"].remove(delname)
                    with open("root.json", "w") as f:
                            json.dump(root, f, indent=4)
                    print(f"Deleted folder \"{namebd}\"")

            elif command[1] == "10":
                    namebd = dir10["name"]
                    delname = ("(10)"+dir10["name"])
                    shutil.rmtree(dir10["name"])
                    dir10["name"] = " "
                    dir10["use"] = False
                    with open("dir10.json", "w") as f:
                            json.dump(dir10, f, indent=4)
                    if delname in root["dirlist"]:
                        root["dirlist"].remove(delname)
                    with open("root.json", "w") as f:
                            json.dump(root, f, indent=4)
                    print(f"Deleted folder \"{namebd}\"")

            else:
                print("Not a correct way to use rmdir")
        
        elif command[0] == ls:
            if currentdir == "root":
                print(f"Directories: ", " ".join(root["dirlist"]))
                print(f"Files      : ", " ".join(root["filelist"]))

            else:
                with open("data.json", "r") as f:
                    data = json.load(f)
                print(f"Files      : ", " ".join(data["filelist"]))

        
        elif command[0] == lsall:
            print(f"ROOT DIRECTORIES: ", " ".join(root["dirlist"]))
            print(f"ROOT Files      : ", " ".join(root["filelist"]))
        
        elif command[0] == mkfile:
            if len(command)<3:
                print("Wrong way to use \"mkfile\". Type hexample for an example :)")
                continue
            name = command[1]
            tof = command[2]
            total = name + "." + tof
            if currentdir == "root":
                if total in root["filelist"]:
                    print("File with that name already exists! Try making another one")
                    continue
            else:
                with open("data.json", "r") as f:
                    data = json.load(f)
                if total in data["filelist"]:
                    print("File with that name already exists! Try making another one")
                    continue
            
            with open(f"{name}.{tof}", "w") as f:
                f.write("...")
            if currentdir == "root":
                root["filelist"].append(f"{name}.{tof}")
                with open("root.json", "w") as f:
                    json.dump(root, f, indent=4)
            else:
                with open("data.json", "r") as f:
                    data = json.load(f)
                data["filelist"].append(f"{name}.{tof}")
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
            print("Created new file!")
                

        elif command[0] == rm:
            if len(command)<2:
                print("Opss! Not enough arguments")
                continue

            rmfilename = command[1]

            if currentdir == "root":
                    if os.path.exists(rmfilename):
                        if rmfilename in root["filelist"]:
                            root["filelist"].remove(rmfilename)
                            os.remove(rmfilename)
                            with open("root.json", "w") as f:
                                json.dump(root, f, indent=4)
                            print("File deleted.")
                        else:
                            print("Opps! File doesn't exist, or at least not in this folder :/")
                    else:
                        print("Opps! File does not exist on disk.")
            else:
                    if os.path.exists(rmfilename):
                        if rmfilename in data["filelist"]:
                            data["filelist"].remove(rmfilename)
                            os.remove(rmfilename)
                            with open("data.json", "w") as f:
                                json.dump(data, f, indent=4)
                            print("File deleted.")
                        else:
                            print("Opps! File doesn't exist, or at least not in this folder :/")
                    else:
                        print("Opps! File does not exist or atleats on this folder :(")

        elif command[0] == timecmd:
            time_rn = datetime.datetime.now()
            print(f"Date and time:      {time_rn}")
            continue
        
        elif command[0] == changepsw:

            currentpasshex = hashlib.new("SHA256")
            newpswhex = hashlib.new("SHA256")

            currentpsw = input("Whats your current password >>> ")
            newpsw = input("New password                >>> ")
            confirmpsw = input("Confirm password            >>> ")

            currentpasshex.update(currentpsw.encode())
            newpswhex.update(newpsw.encode())

            if currentpasshex.hexdigest() == setup["passw"]:
                if newpsw == confirmpsw:
                    setup["passw"] = newpswhex.hexdigest()

                    with open("setup.json", "w") as f:
                        json.dump(setup, f, indent=4)
                    print("Changed password")
            else:
                print("WRONG PASSWORD! UNABLE TO CHANGE IT")
        
        elif command[0] == nano:
            if len(command) < 2:
                print("Wrong format silly!")
                continue
            editfilename = command[1]
            if editfilename == "setup.json":
                print("NOT ALLOWING THIS BECAUSE IT CAN BREAK YOUR SYSTEM")
            elif not os.path.exists(editfilename):
                print("File doesnt exist")
                continue
            else:
                curses.wrapper(nano_editor, editfilename)

        
        elif command[0] == changeuser:
            changeuserhex = hashlib.new("SHA256")

            newusername = input("New username      >>> ")
            confirmpsw = input("Confirm password  >>> ")
            changeuserhex.update(confirmpsw.encode())

            if changeuserhex.hexdigest() == setup["passw"]:
                setup["username"] = newusername
                with open("setup.json", "w") as f:
                        json.dump(setup, f, indent=4)
                user = newusername
                print("Username changed! ")

            else:
                print("Couldnt change username because you put the wrong password")
        
        elif command[0] == delacc:
            cnf = input("Are you sure you want to delete your acc? (y/n) >>> ")
            if cnf == "n":
                print("Aborting...")
                continue
            elif cnf == "y":
                delacchex = hashlib.new("SHA256")
                confirmpsw = input("Confirm with your password >>> ")
                delacchex.update(confirmpsw.encode())
                if delacchex.hexdigest() == setup["passw"]:
                    setup["setupcheck"] = False
                    setup["username"] = ""
                    setup["passw"] = ""
                    with open("setup.json", "w") as f:
                        json.dump(setup, f, indent=4)
                    print("Account has been deleted")
                    print("Shutting down LinPy...")
                    break
            else:
                print("Not an option!")

        elif command[0] == encrypt:
            if len(command) < 2:
                print("Wrong format :/ silly")
                continue
            encryption_filename = command[1]
            print("Are you sure you want to procced with this? If you forget your password, this file could be gone for a long time...")
            print("Type \"Confirm\" for confirmation, type \"Nevermind\" to exit")
            while True:
                confirm_encryption = input(">>> ")
                if confirm_encryption.lower() == "confirm":
                    print("Encrypting File, be carefull. No turning back unless you shut down LinPY")
                    encryption_psw = input("Password for this file >>> ").encode()

                    first_layer_of_encryption = hashlib.sha256(encryption_psw).digest()
                    second_layer_of_encryption = hashlib.sha256(first_layer_of_encryption).digest()
                    fernet_key = base64.urlsafe_b64encode(second_layer_of_encryption)
                    fernet = Fernet(fernet_key)
                    try:
                        with open(f"{encryption_filename}", "rb") as f:
                            ftbe = f.read()
                            enc_data = fernet.encrypt(ftbe)
                            with open(f"{encryption_filename}", "wb") as f:
                                f.write(enc_data)
                            print("File encrypted, dont forget your psw :)")
                            break
                    except Exception as e:
                        print(f"File \"{encryption_filename}\" doesnt seem to be avalibile in this folder, opss")
                        break


                elif confirm_encryption.lower() == "nevermind":
                    print("Phew, you could have lost a file XD")
                    break
                else:
                    print("Wrong answer, son")
                    break



        elif command[0] == decrypt:
            if len(command)<2:
                print("Wrong format pal")
                continue
            decryption_filename = command[1]
            dec_psw = input("Decryption psw >>> ").encode()
            first_layer_of_decryption = hashlib.sha256(dec_psw).digest()
            second_layer_of_decryption = hashlib.sha256(first_layer_of_decryption).digest()
            fernet_key = base64.urlsafe_b64encode(second_layer_of_decryption)
            fernet = Fernet(fernet_key)
            try:
                with open(f"{decryption_filename}", "rb") as f:
                    data = f.read()
                try:
                    decrypted_data = fernet.decrypt(data)

                    with open(f"{decryption_filename}", "wb") as f:
                        f.write(decrypted_data)

                    print("File decrypted successfully.\n")
                    
                    
                except InvalidToken:
                    print("Wrong Password or maybe (just maybe) the file corrupted")
                    continue
            
            except Exception as e:
                print(f"File {decryption_filename} doesnt seem to exist")
                continue

        elif command[0] == pingcmd:
            
            
            def ping_IP():
                
                total_number_of_pings = 1
                if len(command)<2:
                    print("Do you want to ping something or not?")
                    return
                if len(command) == 2:
                    ip = command[1]
                    delay = ping(int(ip))
                    if delay == False or None:
                        print(f"Couldnt ping IP {ip} try again now or later")
                        return
                    else:
                        print(f"IP: {ip} pinged successfully in {delay} seconds")
                        verbose_ping(ip)
                        print("Congrats, you are now MR Robot :D")         
                        return
                elif len(command) == 3:
                    
                    ip = command[1]
                    number_of_ping = command[2]
                    delay = ping(ip)
                    if delay == False or None:
                        print(f"Couldnt ping IP {ip} try again now or later")
                        return
                    else:
                        print(f"IP: {ip} pinged successfully in {delay} seconds")
                        

                        while True>0:
                            for i in range(int(number_of_ping)):
                                verbose_ping(ip)
                            p_total = int(command[2]) * 4
                            print(f"Pinged {ip} a total of {p_total} times if you need to know, nerd")
                            return
                        return
            ping_IP()  

        elif command[0] == clear:
            if len(command) == 1:
                os.system("cls")
                print(logo)
            elif len(command) >1:
                if command[1] == "-nologo":
                    os.system("cls")
        
        elif command[0] == "changecommand":
            if len(command)<3:
                print("Youre not worthy of changing a command  >:(")
                continue
            cmd_to_change = command[1]
            new_cmd = command[2]
            confirmpsw_cmd = input("Password >>> ")
            if confirmpsw_cmd == setup["passw"]:
                commands[cmd_to_change] = new_cmd
                with open("commands.json", "r") as f:
                    json.dump(commands, f, index=4)

        elif command[0] == "cat":
            cat1 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠛⠛⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⠿⢷⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠈⠿⠿⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣿⠃⠀⠀⠙⠿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡿⠋⠉⠀⠀⠀⠀⠀⠀⠙⠻⢷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠋⠀⠀⠀⠀⠀⣤⣀⠀⠀⠀⠀⠀⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠁⠀⠀⠀⠀⣠⡾⠉⠻⠶⠞⠿⣦⠀⠀⠈⢿⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⢀⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⢷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⠀⠀⠀⠀⠀⣰⠟⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⣶⠶⠾⠋⠉⠛⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⠀⠀⠄⠀⠀⠀⠹⣧⠀⠀⠀⠛⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣿⠇⠀⠀⠀⠀⢰⡿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠳⠶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⠀⠀⠀⠀⠀⣸⡟⠀⠀⠂⠀⡁⠠⠀⠐⠀⠀⠀⠘⣷⡀⠀⠀⠈⢿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⠀⠀⠀⠀⠀⢸⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠉⠙⠻⢶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⠀⠀⢠⣿⠀⢀⠐⠠⠁⡀⠂⡁⠐⠈⡐⠀⠀⠈⢿⡄⠀⠀⠀⠻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⡇⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⡐⠀⢀⠂⠁⡀⠡⠈⠄⠡⢀⠈⠙⠻⢶⣄⡀⠀⠀⠀⠀⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⣼⡇⠀⠄⡈⠐⠠⢀⠡⢀⠁⢂⠐⠈⡀⠂⠈⢿⣄⠀⠀⠀⠙⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠰⣿⡁⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠁⠀⡐⠀⠄⠂⠄⠡⠈⠄⠃⡄⠊⢄⠡⢂⠉⠻⣦⣄⠀⠀⠀⠀⠀⠀⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀⠀⠀⣿⠄⠈⠄⠠⢁⠂⠄⠂⠄⡈⠄⡈⠐⡀⢁⠂⡀⢿⡄⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠈⢀⠐⠀⠌⠠⠁⠌⡀⠃⠌⢂⠄⠡⢂⠐⢂⠡⠂⠄⠛⢷⣄⠀⠀⠀⠀⠀⠀⠙⣿⣄⣠⣠⣤⣤⣤⣴⣤⣤⣿⣥⣤⠀⠀⠀⠀⠀⣿⠟⠛⣷⠀⠂⠌⠠⢁⠂⡐⠠⢀⠡⠀⢂⠠⢀⠐⢻⡄⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⡟⠀⠀⠀⠀⠀⠀⣿⠄⠀⠂⠈⠀⠠⠀⠌⡀⠡⢈⠐⠠⢉⠰⠈⡄⠡⢂⠉⢄⠂⠡⠌⣰⣦⣽⣧⡀⠀⠀⠀⠀⠀⠀⠻⠛⠉⠉⠉⠉⠈⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣌⣠⢁⠂⡐⠠⢁⠂⠄⡁⠂⠄⢂⠈⠈⣷⠀⠀⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⡏⠀⠀⠀⠀⠀⠀⣻⡆⠀⠐⢀⠡⠐⠈⠠⢀⠁⠂⠌⡁⢂⠆⡑⠠⢁⠂⠌⣀⠊⡐⢤⣹⣧⡄⠉⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠳⠤⠁⠂⠈⡐⠠⠁⠌⡐⢈⠐⣸⣇⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡇⠀⠀⠀⠀⠀⠀⢸⣇⠀⠂⠠⢀⠂⢁⠂⠄⡈⡐⠠⠘⡀⠆⢌⡁⠎⡀⠃⠄⣡⣠⣿⢧⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢬⣐⠠⢈⠐⡀⣿⡀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡇⠀⠀⠀⠀⠀⠀⢸⡷⠀⢈⠐⡀⠌⠠⢈⠐⠠⠄⠡⡁⠒⡈⠤⠐⣠⣤⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠷⣦⣒⡶⢿⡅⠀⠀⠀⠀⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡇⠀⠀⠀⠀⠀⠀⠐⣿⡀⢂⠐⠠⢈⠐⠠⠌⢂⠌⠡⠐⠡⠐⠀⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠇⠈⠀⠀⠀⠀⠀⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢻⡇⠠⢈⠐⠤⢈⠂⠌⠄⡘⢠⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣧⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠘⣷⣠⣥⣌⠐⢂⠡⠈⣐⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢾⣇⠀⠀⠀⠀⠀⠀⠀⠀⢻⡏⠀⢻⣆⡀⢂⣵⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢻⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢈⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢾⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠙⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣷⣾⣷⣿⣾⣷⣶⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⠋⠉⢿⣿⣿⣿⢿⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⣶⣾⣧⣼⣿⡟⣯⣿⣯⣿⣮⣽⣿⣛⡇⠀⠀⠀⠀⠀⠀⠀⢿⣆⠀⠀⠀⠀
⠀⠀⠀⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⢿⣟⣿⡿⣿⣿⡏⣿⡙⣻⣦⣠⣼⣿⣿⣾⣿⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⡿⣿⢿⠿⠿⠿⠿⠿⠿⠿⣿⢿⣿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀
⠀⠀⠀⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡟⠛⢻⣿⡿⢿⣻⣿⣟⣿⣿⣿⣷⣿⣿⣿⡿⢿⠿⠷⠿⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠷⣦⡀
⠀⠀⢠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⢿⣿⣷⣶⡿⡿⠿⠟⠛⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⢀⠐⠠⠀⢂⡄⠠⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇
⠀⢀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠫⠉⠁⡀⠀⠄⢀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⣧⠀⡐⠨⣷⠀⠡⠈⢿⡀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠁
⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠐⠠⠁⡀⣰⠈⠠⠈⠄⣢⠌⠐⡀⢦⡄⠀⠀⠀⣀⣠⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⣀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡐⠠⠁⠠⠈⠄⡁⠂⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣿⠀
⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⡁⠄⡁⠂⢄⡿⢁⠂⡡⠘⠟⡀⠂⠄⡙⠃⢀⣾⠾⢿⣯⡙⣿⡿⠿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠚⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠂⠁⠂⠡⠐⠠⠁⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢿⣏⠀
⢻⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⡐⠠⢁⠂⡐⢀⠂⠡⢈⠐⠠⢁⠂⡐⠈⣾⡏⠀⣦⠉⣙⢢⡁⠏⢹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠁⠐⠀⠠⣵⡾⢿⣟⡻⣿⣶⣄⠀⠀⠀⠀⠀⠀⣼⡟⠀
⠀⠙⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⡁⠂⡐⢀⠂⠌⡐⠠⢈⠐⠠⠐⠀⠰⣿⡅⠀⠈⠲⣌⢡⠚⣱⠂⠻⠟⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣿⣄⠨⡝⠡⠏⢩⢿⣇⠀⠀⠀⣠⣾⠟⠀⠀
⠀⠀⢰⣿⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⠀⠄⠈⠄⠠⠁⠂⠈⢀⠀⠁⢰⣿⠀⠀⠀⠹⡄⢧⢋⡔⠧⠀⠀⣻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⣾⡟⠉⠛⠁⢀⡤⠲⢄⡘⣿⡄⢀⣴⡟⠁⠀⠀⠀
⠀⠀⠀⠙⢻⣶⣦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠐⠀⠁⠀⠀⢀⣾⠃⠀⠀⠀⠀⠙⠒⠮⠘⠁⠀⠀⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠃⠀⠀⠀⢘⣆⢣⢚⡤⢸⣷⡾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠰⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡿⠋⠁⠀⠀⠀⠀⠀⠊⠓⠎⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣼⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⣤⡀⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⢷⣶⣤⣤⣀⣀⣀⡀⢀⢀⣰⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣤⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠛⢻⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


"""
            
            cat2 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢶⡶⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠋⣱⠋⠀⠘⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢶⡶⢶⣤⣀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠋⢁⡼⠁⠀⠀⠀⢻⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠈⠓⢄⠉⠻⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠟⠀⢠⠎⠀⠀⠀⠀⠀⠸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠙⢦⠀⠈⠛⢷⣤⡀⠀⣀⣠⣤⣴⡶⠶⠶⠶⠶⣶⣟⣁⠀⣠⠋⠀⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠑⢤⡀⢀⡨⠟⠛⠉⠉⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠉⠙⠲⢄⡀⠀⠀⠀⠀⠀⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⢀⡤⠟⠁⠀⠀⠀⠀⠀⠀⠀⡟⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠹⡀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠈⢣⡀⣾⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⢀⡜⠁⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⡼⠀⠀⠳⡄⠀⢀⡴⠚⠉⠉⠉⠉⠓⢤⠀⠀⢹⣇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣀⡼⠀⠀⢠⠔⠋⠉⠀⢉⣙⠶⣄⣰⠃⠀⠀⠀⠙⣴⣿⠟⢿⣿⣷⣦⠀⠀⠀⢳⠀⠀⢿⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠃⠀⢰⠋⠀⠀⣠⣾⣿⡏⠉⢻⡻⡄⠀⠀⠀⢠⠋⣷⣄⣤⣿⣿⣿⣧⠀⠀⢸⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣟⠀⠀⠀⣿⣿⣿⣷⣶⣾⡇⠹⡄⠀⠀⢼⠀⢻⡟⠛⠛⠋⣀⠇⠀⢀⡼⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠸⡄⠀⠀⠻⣈⠉⠉⢁⡽⠃⢰⠇⠀⠀⠈⠣⣄⠉⠓⠒⠊⢁⣠⣴⣊⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠙⠦⣄⣀⠈⠉⢋⣉⡠⠔⠋⠀⠙⠟⠁⠀⠀⠉⠉⢉⠉⠉⠁⠀⠊⠉⠑⠒⣾⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⢀⣠⠴⠊⠉⠉⠉⠉⢠⡀⠀⠀⠀⣠⠟⢤⣀⡀⢀⡰⠋⠀⠀⠀⠀⣌⠉⠉⣹⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣉⣠⠤⠖⠀⠀⠀⠀⠀⠙⠲⠶⠊⠁⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⢀⠈⠉⣷⠿⢴⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣄⣀⠴⠃⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣽⠾⣅⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠙⢦⣴⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠚⠁⣿⠀⠀⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠃⢀⡴⠋⠀⡽⠓⠲⠤⠤⠤⠤⠤⠤⠤⠤⠤⠔⠚⠋⠁⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⣀⠔⠁⠀⠰⡆⠀⠀⠀⠀⠀⠀⠈⠙⠒⡖⠚⠉⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣴⡟⠀⠀⠀⠀⢀⡠⠞⠁⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀
⠀⠀⢀⣠⡶⠛⠉⢰⡧⠤⠴⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀
⠀⣰⠟⠉⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀
⣼⠏⠀⠀⠀⢠⡴⠶⣇⠀⠀⠀⠀⠀⠀⠀⣀⡤⠤⠤⠤⣀⢳⡀⣀⡤⠤⠤⠤⣄⡀⡇⣀⡤⠤⠤⠤⣄⣀⡿⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⢺⣀⢀⠘⣆⡀⣀⣀⣀⣠⡋⠁⢠⠀⢀⡀⠀⢹⡟⠁⠀⡄⠀⡀⠀⠙⡏⠁⢠⡀⠀⣀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀
⢻⡆⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠑⣼⣀⣸⣀⣀⣸⣇⣀⣀⣇⣀⣇⣀⣀⣇⣀⣘⣇⣀⣇⣀⣀⣼⠃⠀⠀⠀⠀⠀⠀
⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠻⢶⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""         
            cat3 = """
⠀⡿⢘⠀⠀⢠⠆⠀⠀⠀⡰⠬⢉⣽⣿⣿⡿⠟⠋⠁⠀⢿⣞⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢀⡟⡌⠀⠀⢐⠌⠀⠀⠄⡡⠃⠞⠛⠉⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣤⡇⡆⠁⠀⢘⡎⢤⠀⠀⠁⠀⠀⠀⠀⠀⠂⠠⠄⠂⢀⢹⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢸⡇⠅⠂⠀⡸⡜⢢⠅⠀⣀⡀⡀⠤⢶⣺⣿⡒⢄⠀⢭⣘⡻⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢾⡀⠁⠆⠀⢱⡎⢁⣶⣿⣿⠁⣸⡇⢸⣇⣿⣷⢸⣆⠀⣿⡿⣆⠹⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢺⢸⠀⠀⠀⢎⣴⣾⠿⠟⠿⣷⣿⣫⣾⣿⣿⣿⡎⣿⠿⠟⠉⠚⠻⣮⡙⣿⣿⣿⣿⣿⣿⣿⣿
⣻⢨⠐⠀⣠⣾⠿⠉⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣷⣅⠀⠀⠀⠀⠀⢩⣙⠚⣿⣿⣿⣿⣿⣿⣿
⣽⠰⠀⠈⠁⣠⣶⡀⠀⠀⠀⢀⢀⣾⣿⣿⣿⡿⣿⣿⣤⣤⣀⣀⣤⣾⠿⠇⠈⢿⣿⣿⣿⣿⣿
⣿⠆⠀⠀⡀⠙⠉⢀⢽⣿⣿⣿⣿⡿⢏⠿⡿⡭⢭⠻⣿⣿⣿⣿⣿⣷⣾⠐⡆⠈⢿⡿⠿⠿⠟
⢻⡃⠀⣀⣠⡄⠀⣈⣺⣿⢿⣿⣿⣿⣦⣀⠓⠃⣠⣾⣿⣛⣿⣟⣿⣿⠷⢿⣿⣇⢠⣤⣴⣶⣾
⠀⠀⢐⣾⠗⠈⠁⠤⣾⣷⣿⣾⣿⣿⣿⣿⡅⢌⣿⣿⣿⣿⣷⣿⣿⣽⣏⡀⠀⠉⣘⣚⡉⣩⣾
⠀⠄⠀⣀⠄⡠⣴⣾⣿⣿⣿⣿⣿⣷⣶⣤⣴⣦⣬⣴⣿⣿⣿⣿⣿⣿⣿⣶⣵⣈⢟⡟⣱⣿⣿
⠀⠂⠈⣡⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⡿⢗⣵⣿⣿⣿
⠀⠀⢱⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣾⣿⣿⣿⣿⣿
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢻⣿⣿⣿⣿⣷
⡀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⢿⣿⣿⣿⣿
⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠮⠹⠜⣯⣛
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠉
"""     
            cat4 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣶⣶⣴⣦⣄⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⣿⣿⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⠁⠀⠀⠀
⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀
⠈⢻⣿⣿⣶⣦⣤⣀⣴⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀
⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣟⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⢻⣿⣿⣟⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣮⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀
⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⠀⠀⠀⠀⠉⠛⠿⢿⡿⠿⠟⠉⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⢻⣿⣿⣿⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣷⣆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿⠿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⠟⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠉⠛⠻⠿⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⠟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

""" 
            cat5 = """
⠀⠀⠀⠀⠀⠀⣠⣶⠶⠶⠶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠶⠶⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⠀⠉⠛⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠋⠁⠀⠀⠀⠀⠉⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⡿⠀⠀⠀⣴⠟⠛⠻⣦⡀⠀⠀⠀⠀⠙⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⢀⣴⠾⠿⢷⣄⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⣼⠏⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⣙⣷⡶⠶⠶⢶⡶⠶⠶⠶⠶⠶⢶⣤⣴⠟⠁⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⢻⡆⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⢀⣿⠀⠀⠀⠀⠀⢀⣿⣀⡤⠖⠚⠉⠁⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⠀⠀⢸⡏⠀⠀⣀⣤⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣦⣄⠀⠀⠀⠀⣿⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⠀⠀⠸⢿⣶⢿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣦⣄⣀⣿⡇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠋⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣇⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢨⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀
⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛
⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢓⣴⣾⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡏⠀⠈⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠋⠀⠈⢻⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⡄⠀⠀⠀⠀⢀⡀⢸⣿⣿⣿⣷⣤⣴⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣦⣀⣠⣾⣿⣿⣿⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣤⣾⡷⠿⠖⠀⡰⠋⠀⠈⣿⣿⠟⢿⣿⣿⣿⡿⠁⠀⠀⠀⢠⣦⡄⠀⠀⠀⠀⠘⣿⣿⣿⣿⡿⢿⣿⡿⠀⠈⠉⠒⠤⣀⡀⢀⣠⣤⣀⡀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠉⠈⢿⣄⣀⠀⢱⡀⠀⠀⠘⢿⣷⣿⣿⣿⡿⠁⠀⠀⠻⣦⣴⢿⣦⣴⠗⠀⠀⠀⠙⢿⣿⣿⣷⣾⠟⠁⠀⠀⠀⢸⠀⠀⠉⠉⡉⠉⠙⢻⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣼⠿⣿⡀⠀⠉⠁⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠳⢄⣀⡠⠞⠀⠀⠀⠈⠛⢷⣶⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠛⠁⠀⠘⠻⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠻⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣄⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⠶⣦⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣴⠾⠛⠋⠁⠀⠈⠻⣧⡀⠀⠀⠀⠀⠀⣰⡟⠉⠀⠀⠙⢿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠉⠉⠉⠛⠛⠛⠛⠷⠶⠶⠶⠶⠶⠶⠶⠶⠶⠞⠛⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠘⣧
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⢀⣿⠁⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢀⣼⠿⠶⠶⠶⢶⣤⠀⣾⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠟⠁⠀⠀⠀⠀⠀⠹⣿⡏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⢀⣾⠟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⣴⡾⠟⠛⠻⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⡿⠁⠀⠀⠀⢀⣠⣶⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⣿⣦⣤⡴⠶⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠳⠶⠾⠛⠷⣦⣤⣤⣤⡶⠿⣷⣦⣤⣤⣤⣤⣤⣤⣤⣤⡶⠶⠞⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
            cat6 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢚⠝⠉⣧⠀
⠀⠀⠀⠀⠀⠀⡞⠛⢝⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⢠⠂⠀⠀⢸⠀
⠀⠀⠀⠀⠀⠀⡇⠀⠀⠑⢄⠉⠳⢤⡤⠴⠖⡖⠒⠒⠚⠥⢴⡁⠀⠀⠀⠀⡇
⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⢀⡽⠊⠁⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠑⢄⠀⢰⠀
⠀⠀⠀⠀⠀⠀⠸⡄⠀⡠⠃⠀⠀⠀⠀⠀⢠⠀⢃⠀⢀⠤⠐⠂⠤⡀⠑⡎⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣴⠁⡠⠂⠉⣨⡵⣦⡆⠀⠀⢳⡟⢻⣷⣦⠀⠰⠀⢹⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⡇⠀⣾⣿⣧⣼⠑⠀⠀⡇⢿⠛⠛⡹⠀⡰⠀⢸⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠱⣀⠙⠠⠤⢊⠔⠠⠤⠈⠂⠬⠥⠐⠚⠀⠤⣼⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠤⠒⠉⠉⠉⢄⠀⡠⠒⠤⠀⠜⠁⠀⠠⠉⣩⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢎⡁⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡶⣏⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⡩⠚⡤⢀⣀⣀⣀⣀⣀⡠⠤⠐⠊⠁⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠊⠀⠀⠀⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀
⠀⠀⠀⠀⢀⡎⠀⠀⠀⡠⠊⠀⠘⠀⠀⠀⠀⠈⢹⠉⠁⠀⠀⠀⢸⠀⠀⠀⠀
⠀⢀⡴⠚⠉⠇⠐⠒⠁⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀
⣰⠋⠀⢀⠤⡆⠀⠀⠀⢀⡀⠀⢀⣰⢀⡀⠀⠀⡀⣀⡀⠀⢀⣰⠃⠀⠀⠀⠀
⣿⠀⠀⠐⠤⠴⠤⠤⠤⠯⣰⠀⡄⠘⡃⠠⠀⡄⠸⠁⢠⠀⠀⠙⡆⠀⠀⠀⠀
⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⣸⠛⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀
⠀⠀⠉⠁⠒⠒⠒⠒⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
            cat7 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⠿⠿⠿⣿⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⢋⡀⠀⠀⠀⠀⠀⠉⠛⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠏⠐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡿⠿⠛⠛⠙⠋⠛⠿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠀⠀⣰⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡏⠀⠀⣼⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⠟⠁⠀⠀⠀⣠⣴⠶⠾⣿⡄⠀⠀⠀⠀⠘⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀⣼⡿⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠟⠁⠀⠀⢀⣴⡿⠋⠁⠀⠀⠘⣿⡄⠀⠀⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢸⣿⡇⠀⢸⣿⠃⠀⠀⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⣄⣠⣤⣠⣴⣴⣶⣶⣶⣶⣦⣶⣤⣀⣄⣀⡀⣀⣾⡿⠃⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠛⠛⠷⠤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠀⠀⣿⡇⠀⠀⠀⠈⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡶⠿⠿⠛⠉⠉⠉⠉⠉⠉⠈⠁⠉⠉⠉⠉⠉⠉⠛⣿⣿⠋⠀⠀⠀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠆⠀⠀⠀⠀⠀⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⡟⠋⡀⠄⡁⢂⠐⠠⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⡇⠀⢸⣿⠀⠀⠀⠀⠀⢼⣿⠆⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠃⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⡃⠀⠀⠀⠀⠀⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣧⠐⢀⠂⡐⠠⠈⠄⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠃⠀⣿⠏⠀⠀⠀⠀⣸⣾⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠟⠃⠀⠀⣰⣿⠃⠀⠀⠀⠀⢀⠀⡀⢀⢠⣤⣼⣾⣿⠁⠀⠀⠀⠀⠀⠸⣿⡆⠀⣠⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⡄⠂⣄⢡⣈⣔⠂⠀⠀⠀⠀⠀⠐
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠀⢸⣿⠁⠀⠀⠀⣰⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠀⠀⢠⣰⣭⣿⣷⣷⣾⣮⣭⣉⢹⡿⠀⠀⠀⠀⠀⠀⠀⣿⣷⣿⣟⢫⣉⠙⠻⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⠿⠟⠛⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡇⠀⣼⡇⠀⠀⢀⣰⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣼⣿⠟⠉⠉⠈⠉⠉⠛⠿⣿⣷⣄⠀⠀⠀⠀⢠⣤⣿⣿⠷⣉⠖⡠⢍⠢⡙⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⡟⠁⠀⣿⠃⠀⢠⣼⡿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡏⠀⣴⣶⠧⡙⢌⡑⠢⢌⠹⠿⣷⣤⠀⢀⣾⣿⣿⢏⠳⡈⢆⡑⠎⡔⡡⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣾⡇⠀⢘⡿⠀⣠⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢸⣿⡇⢀⣿⡏⠰⡁⠆⡌⠱⡈⢆⡱⢙⣿⣿⡿⠿⠿⣿⣿⣡⣜⣢⣜⠨⡔⣱⣯⣿⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⣼⡟⣿⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢸⣿⡇⠸⣿⡃⠱⣈⠖⡨⠑⡌⣆⣶⣧⣼⣿⡇⢒⡰⠼⣿⣿⡛⣿⣿⢇⠲⡰⢷⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠠⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢸⣿⠀⢸⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⣿⣿⠀⢻⠅⢳⡐⢎⠰⢩⣾⣿⠫⣝⠻⣿⣿⡰⢠⠃⣿⣿⣿⡿⢋⠄⡣⠜⣱⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⣾⣿⠂⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣧⡘⢌⠒⣌⠢⡉⢆⠻⣿⣷⣮⣷⣿⣿⣗⢢⢹⣾⣿⢅⠢⢅⢚⣴⡍⣼⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡟⢠⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⣻⢦⡍⢄⠣⡑⢌⢢⠑⡬⢉⡕⣸⣿⣿⣾⣿⣿⡣⢎⡱⣈⢚⣿⣸⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⣼⣿⢁⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⡷⣌⢻⣧⠌⢢⠑⡌⢢⢉⠖⡡⢒⣽⣿⠋⠁⢸⣿⣷⡍⢶⣡⢺⣾⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠏⣹⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⣎⠽⣿⡈⢆⠱⣈⠒⣌⢢⣱⣿⣿⠃⠀⠀⢸⣿⠻⣿⣶⣽⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠋⠁⠀⠈⢿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠁⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡼⣿⡔⡌⢒⠤⡩⢐⣮⣿⡿⠁⠀⠀⠀⣼⣿⠀⠈⠙⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣦⠀⠀⠀⠀⠀⠀⢸⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣷⣝⡧⣙⢆⡿⣴⣿⡿⠏⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⣠⣿⠏⠀⠀⠀⠀⠀⠀⢻⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⠿⢷⣿⡾⠿⠛⠉⠀⠀⠀⠀⠀⠠⠁⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⢀⠀⠀⢀⣰⡿⠋⠀⠀⠀⠀⠀⠀⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡧⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⢸⣿⠄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⢽⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⡁⠀⠀⠀⠀⠀⣠⣾⣿⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⠀⠀⠁⠀⠀⠀⠀⣸⣿⣿⡟⠛⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣠⣶⣶⣴⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⡿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⣻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣟⠀⠀⠹⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⡿⠿⠛⠉⠁⠉⠉⠙⢿⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣿⡇⠀⢠⣤⣄⣀⠀⠀⣻⣿⣿⣿⣿⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡀⠀⢐⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⣿⣇⠀⠈⠛⢿⣿⡇⢾⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣶⡀⠀⢀⣆⠀⠀⢸⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣾⣿⠛⠃⠀⠀⠹⣿⣿⣽⣿⡿⠁⠀⠀⠀⠀⠰⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⢾⣿⣿⣿⣿⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⣼⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⠿⣷⣤⣄⣀⡀⠉⠛⠉⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠻⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣠⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⡿⠿⠿⠶⢿⣶⣷⣤⣤⣄⣀⡀⠀⠀⠀⠀⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣆⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣤⣭⣙⣻⡿⢿⣷⣶⣶⣤⣤⣄⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⠟⠋⠁⠀⠀⠀⠀⠙⢿⣿⣿⣶⠀⠀⠀⢀⣀⣤⣶⣾⠟⠛⠛⢿⣷⣦⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⠿⣷⣶⣤⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⢡⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⠿⠟⠛⠛⠛⠛⠛⠛⠛⠻⠿⢿⣷⣤⣈⠉⣻⣿⠛⠻⠷⡶⣶⣤⣀⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠐⠂⠀⠀⠀⠒⠀⢀⣂⣀⣀⠀⣀⣀⣠⣼⣿⣿⣶⣶⠾⠟⠛⠋⠁⠀⠀⠀⠀⠈⠈⠻⣿⣦⡀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠉⠉⣰⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠻⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠻⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣮⡿⠾⠖⢦⣦⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠁⠀⣼⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣴⣶⣶⡿⠛⠋⠉⠁⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⣼⣿⠃⠀⠀⠀⠀⠀⠐⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⡿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠹⣿⣷⣼⣦⠖⠁⠀⠀⠲⣼⣿⠇⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣾⠿⠟⠛⠉⠁⠀⠀⠀⠀⣠⡴⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⢤⡀⠀⠀⠀⠀⢾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠘⢿⡄⠀⠀⠀⠀⠀⠀⢠⣴⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡖⠀⠀⠀⠀⠀⠀⠀⠘⠉⢻⣿⣇⠀⠀⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⢀⣿⠏⠀⠀⢰⣿⡿⢿⣶⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡿⢻⠋⠉⠁⠀⠀⠀⠀⠀⠀⠴⡶⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠐⠢⢄⠀⠀⠀⠀⠀⠉⠂⣀⠀⠀⢸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣧⠀⠀⢀⣀⣠⣾⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠻⣿⡄⠀⢀⣼⣿⠋⠀⠀⠀⠀⠀⠀⣴⡿⠋⠀⠀⠀⣾⣿⠀⠀⠙⠻⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣶⣶⣦⣤⣀⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠂⠀⠀⠀⠀⠀⠀⠀⢰⡼⣿⣷⡀⠀⠀⠀⠀⠀⠀⣧⣿⣿⣶⡿⠿⠛⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⢀⣴⡾⠏⠀⠀⠀⠀⣰⣿⡇⠀⠀⠀⠀⠈⠻⣿⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣈⣯⣵⣿⡿⠛⡉⢉⠛⠻⠿⣿⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠂⣤⡤⠖⠀⠀⠀⠀⠙⠿⣷⣦⣀⠀⠀⣂⣴⣿⡿⠛⢃⣠⣰⡤⢻⣿⣀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⡆⠀⠀⠀⠀⠤⠴⠖⠛⠁⠀⠀⠀⠀⠀⣰⣿⡟⢁⠀⠀⠀⠀⠀⠀⠈⠻⣷⡄⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣤⣶⣾⠿⠟⠛⠉⢀⠠⠁⡐⠀⢎⠰⡀⢀⠀⡉⠛⠛⠿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠙⠀⠀⠀⠀⠀⠀⢀⣠⣽⣿⣿⠿⠿⠿⠛⠿⠿⠿⠇⠉⠉⠀⠙⣿⣿⡇⢠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣀⠀⠀⠀⠀⠀⢀⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣿⡟⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠀
⠀⠀⠀⣾⣿⠟⠙⠰⠓⢾⣶⢾⣶⣤⣶⣤⣥⣀⡂⠙⠲⠖⢊⠅⠌⡐⢠⠛⠿⣷⣄⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⢀⣠⣴⣾⠿⠛⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⣾⣯⣄⣄⣄⣤⣤⣤⣤⣶⣾⡿⠿⣿⣷⣦⡀⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⡿⠃⣄⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡆⠀⠀
⠀⠀⠀⣿⣯⠀⠄⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠿⠿⢷⣾⣤⣌⡐⠈⠄⠃⠌⢉⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⡿⠟⠏⠄⠂⠞⠻⠛⠿⠿⠷⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠿⢻⣟⢛⣋⡉⢁⠀⣀⢠⣄⠛⢻⣿⣦⡀⢼⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠛⣿⣿⣶⣤⣤⣤⣤⣴⣶⣾⡿⠛⠉⡀⢔⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣷⠀⠀
⠀⠀⠐⣿⢿⣶⣦⣶⣄⠐⠠⠐⠂⠄⢠⠀⡀⠀⠀⢀⣀⡀⠉⠻⠿⣷⣮⣔⡈⠠⢀⠘⢻⣷⡀⠀⠀⢀⣴⣾⡿⢛⠡⠌⢀⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠈⠉⠛⠿⣷⣦⣄⡀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⣠⠟⠉⠀⠀⣈⣼⣿⣿⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡔⠁⠀⠸⣿⣏⠉⠋⠙⠻⠻⢋⠀⡀⣴⣾⣿⠿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀
⠀⠀⢰⣿⡆⢤⣌⣽⣧⡀⠐⠈⠌⡐⢀⠂⠥⠀⠀⠘⠻⠿⢷⣶⣤⣄⡉⠛⠿⣷⣄⡂⠄⢻⡗⢀⣴⣿⠛⡁⢆⣡⣾⡾⠿⠛⠛⠛⠛⠛⠛⠿⠷⣶⣦⣄⣀⠀⠀⠀⠉⠛⠿⣦⣄⡀⠀⠁⠀⣀⠀⠀⠀⠀⢀⠀⠈⠀⠀⣀⣴⡾⠟⠋⠁⢙⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡿⠁⠀⠀⠀⢹⣿⣆⣄⣠⣷⣶⡿⠿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠀⠀
⣶⣤⣾⣿⡄⠀⠈⢹⣏⡁⣠⠀⠀⠀⠀⠀⠀⠀⠐⠈⠷⢶⣤⣤⣉⠛⠿⣷⣦⣍⠻⣿⣦⡀⣷⣿⠟⣠⣶⣿⠿⢋⣁⣤⣤⣤⣤⣤⣤⣦⣤⣤⣤⣄⣀⣉⠛⠿⢷⣶⣤⣀⠀⠀⠛⢿⣦⣄⠀⠀⠀⠀⠀⠂⠀⠀⣠⣴⣾⠟⠋⠀⠀⠀⢤⣿⣿⠏⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⠾⠛⠁⠀⠀⠀⠀⢠⣾⣿⢫⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣾⣿⠇⠀⠀
⢸⣿⣿⣿⣿⣶⣜⣆⣛⡁⠙⡆⠀⢄⠀⠂⠀⡁⡄⢀⠀⡀⠈⠉⠻⢿⣶⣄⣉⠻⢷⣌⣙⣿⣿⡏⡴⠟⢋⣴⠾⠟⠛⠉⠉⠁⡀⠀⠀⡀⠈⠉⠉⠉⠛⠻⠿⣶⣤⡈⠙⠻⢿⣦⣄⡀⠈⠻⢷⣄⠀⠀⠀⣠⣴⡿⠟⠉⠀⠀⠀⢀⣠⣶⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠉⠁⠀⠀⠀⠀⠀⢀⣤⣿⣿⢏⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣵⣿⣿⠀⠀⠀
⠈⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣷⣶⣶⣶⣿⣿⣯⣛⠿⣿⣎⠈⠈⠉⠃⠀⠀⠀⠈⠈⠴⡾⠟⠛⠉⠋⠁⠉⠁⠉⠉⠓⠚⠶⣤⣤⣀⡀⠙⠋⠀⠀⠀⠈⠛⠿⣷⣦⣈⡹⢿⣷⡿⠟⠁⠀⠀⠀⣀⣤⣾⡿⠟⣏⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣤⣤⣴⣶⣶⣿⠿⠿⣛⣴⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠛⠛⠻⠿⣿⣿⣿⠿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣉⠓⡀⠀⠀⢀⠠⠐⠀⠈⠀⠀⠀⢀⣲⣴⣼⣶⣷⣮⣶⣤⣺⣴⡄⠂⢹⠿⠻⣶⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠂⠀⠀⠀⠀⣀⣴⣿⠿⢛⣥⡤⢾⣿⢛⣿⣿⣦⣯⣴⣤⣦⣤⣴⣶⣿⣿⠿⠿⠟⠛⠛⠉⠉⠉⠀⣄⣺⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⡿⠛⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣾⣯⣬⡛⠉⡏⢿⣿⠻⢿⣿⣿⣿⣿⣷⣦⣤⣤⣤⣤⣤⣄⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣂⠐⠄⢢⡔⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⠟⠋⢠⡶⠋⢃⣰⣭⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠀⢀⠀⡀⢀⠠⢠⣤⣶⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣶⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⣷⣯⣄⣀⠠⠸⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠉⠉⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣶⣤⣀⡄⢀⠀⠠⠐⢀⣦⣀⣀⡠⠰⠉⠂⣁⣼⣿⣿⣿⣿⣿⣿⣿⡟⠋⠑⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣤⣴⣾⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⣿⣷⣦⣽⣟⣿⡟⠛⠛⠛⠿⠿⠿⠿⠿⠿⢿⡋⠀⡄⠀⠄⠂⢀⠀⡀⠀⡀⠄⠀⠉⠙⠻⠿⣿⣿⣿⣿⣿⣷⣶⣥⣄⡀⠈⠁⠁⣀⣡⣶⣿⣿⣿⣿⣿⣿⡿⢿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣶⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⣿⣿⣦⣤⣀⣁⡈⠁⠈⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠁⠀⠠⠈⠀⠄⢀⣄⠀⣨⠝⠻⢿⣿⣿⣿⣿⣿⣿⣶⣷⣿⣿⣿⣿⣿⣿⠿⠯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣀⣤⣴⣷⡿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⠿⠿⣿⣶⣶⣤⣄⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠦⠀⠉⠛⠿⠿⣿⣿⣿⣿⣿⠿⠛⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⣤⣤⣤⣶⣾⡿⠿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠿⠿⣷⣶⣶⣶⣦⣦⣤⣤⣀⣀⣀⣀⣀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣠⣤⣤⣴⣶⣶⣾⠶⠿⠿⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠛⠛⠻⠿⠿⠿⠿⢿⡿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣾⣾⣷⣾⣿⣿⢿⠿⠿⠿⠿⠿⠟⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

            cat8 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠟⣫⡿⠉⢻⣇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠟⢁⡴⠋⠀⠀⠈⢿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠷⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠋⠁⣠⠞⠁⠀⠀⠀⠀⢸⣷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⠀⠉⠳⢤⡉⠙⠻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠏⠁⠀⣰⠃⠀⠀⠀⠀⠀⠀⠈⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠙⠶⣄⠀⠉⠻⢷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣾⠟⠁⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠉⠛⢿⣶⣀⣤⣶⠶⠿⠟⠛⣿⠉⠉⠉⠉⠉⠙⠛⠳⠶⠦⣤⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⣀⡴⠿⠉⠉⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠲⢤⣀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⢀⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡴⠀⠀⠀⠀⠀⠀⣠⡾⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⢸⡟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠹⣆⠀⠀⠀⠀⠀⣠⡴⠶⠖⠶⠶⢦⣀⠀⠀⠀⠹⣦⡿⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣧⠀⠀⢠⡟⠀⠀⠀⠀⢀⣀⣠⠤⢤⣀⣀⠀⠀⠀⢀⡟⠀⠀⠀⠙⣦⠀⠀⣴⣟⣁⣀⣀⡀⠀⠀⠀⠈⠳⣆⠀⠀⠸⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⣄⡿⠀⠀⠀⣠⠶⠋⠁⠀⠀⢀⣀⣉⡳⢦⣀⣾⠀⠀⠀⠀⠀⠘⢷⡾⡿⠚⠻⣿⣿⣿⣶⡄⠀⠀⠀⠸⡆⠀⠀⢹⣇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⠁⠀⠀⣴⠋⠀⠀⠀⣠⣾⣿⣿⠋⠉⠳⣝⢧⡀⠀⠀⠀⠀⠀⡾⢻⣧⣀⣀⣿⣿⣿⣿⣿⡄⠀⠀⠀⡇⠀⠀⠸⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⢰⠇⠀⠀⠀⢰⣿⣿⣿⣿⣄⣀⣴⣿⠈⢷⠀⠀⠀⠀⣸⡃⠸⣿⣿⢿⣿⣿⠟⠉⣿⠁⠀⠀⢠⡇⠀⠀⠀⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠘⣇⠀⠀⠀⢸⣿⠿⢿⣿⣿⠿⠿⣿⠀⠈⡇⠀⠀⠀⠙⣇⠀⠙⢧⣀⣀⣀⣠⠶⠃⠀⠀⣠⠟⠁⠀⠀⠀⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠻⣄⠀⠀⠀⠻⣤⣀⣀⣀⣠⡶⠋⢀⣼⠃⣀⣀⣀⡀⠙⠶⢤⣀⣈⣉⣉⣁⣀⣤⠶⠾⢥⣀⣀⡀⠀⢠⣿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠉⠳⢤⣀⣀⠀⠉⠉⣉⣁⣠⠶⠚⠁⠀⠈⠙⡏⠁⠀⠀⠀⠈⠉⠉⡉⠉⠁⠀⠀⠀⠁⠀⠉⠉⠙⣻⡏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⢀⣀⠶⠛⠉⠉⠉⠉⠉⢉⡀⠀⠀⠀⠀⠀⣠⢿⣄⠀⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⡈⠉⠉⠉⢹⡿⠓⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⠴⠞⠋⠁⣀⡀⠀⠀⠀⠀⠀⠈⠳⣄⣀⣀⣠⠞⠁⠀⠈⠙⠲⠶⠖⠋⠀⠀⠀⠀⠀⠀⠈⠓⠶⢤⣰⣿⣃⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⡶⠚⠋⠉⢀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢤⣀⣴⡟⠉⠙⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣠⠶⠋⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⡿⠳⣦⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠙⠷⣄⣶⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠶⠛⠉⣿⠀⠀⠀⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⢀⡶⠋⠉⢳⠶⠦⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡤⠴⠶⠒⠉⠉⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠐⠋⠀⠀⢀⡿⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠟⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠰⠶⠦⢤⣤⠤⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⣰⠞⠁⠀⠀⠀⠉⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠿⡿⠀⠀⠀⠀⠀⣀⡤⠶⠋⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣴⡿⠛⠉⠀⢰⡧⠤⠶⠶⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣾⠟⠉⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣰⡿⠃⠀⠀⠀⠀⠀⣀⣘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⣀⡀⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠁⠀⠀⠀⠀⢰⡟⠉⠉⢹⡄⠀⠀⠀⠀⠀⠀⠀⣀⡴⠚⠋⠉⠉⠉⠙⠶⣄⣷⣠⠶⠚⠉⠉⠉⠉⠙⠶⣤⣧⡴⠞⠋⠉⠉⠉⠙⠲⢦⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠀⠀⠀⠀⠀⠸⣇⣀⣀⣀⣻⣄⣀⣀⣀⣀⣀⣰⣏⡀⠀⣴⠀⠀⣤⠀⠀⠈⣿⠁⠀⠀⣶⠀⠀⣤⠀⠀⠈⡿⠀⠀⢰⡀⠀⢠⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⡆⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢷⣼⠀⠀⣿⠀⠀⠀⣿⡀⠀⠀⢹⠀⠀⣿⠀⠀⠀⣷⠀⠀⢸⡇⠀⢸⠀⠀⠀⣸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠻⣷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠉⠻⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""     
            cat9 = """
⢠⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⡀⢻⣄⠀⠀⠀⠀⠀⠀⢀⣴⣿⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠙⠻⣇⠈⢹⣧⣄⣀⣀⣀⣴⣾⠿⠿⠿⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠚⣿⣿⣶⣿⣿⣿⣿⢿⢿⢿⣿⣥⣿⣥⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⢿⣿⣷⣸⣼⠈⣰⣾⣿⣷⣿⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢿⡟⣷⣿⣽⣿⣿⣿⣿⣿⣯⣼⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢈⣿⣽⡿⣟⣠⢿⡈⣿⣭⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣯⡃⠨⢄⣀⢁⠈⠙⣾⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⠋⠛⢦⣤⣠⣴⣾⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡟⣣⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣷⣿⢿⣿⣿⣿⡿⠿⡮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⣿⣷⣿⣿⣿⣿⣻⣥⡼⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⣿⣿⣿⣿⣿⣯⣿⣷⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢹⣿⣿⣿⣿⣯⣿⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣿⣟⢿⣿⡔⣟⣭⣿⣿⣿⢿⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣿⣾⣏⢿⢝⡶⡞⢻⣍⣲⣿⢿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣮⢐⠃⠂⣽⣿⢿⡿⣿⠿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⡼⣿⣿⣿⡍⢰⣾⣿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡯⢽⡿⢿⣴⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠁⣿⠿⠚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⣸⠏⡀⢰⡏⠈⢿⣿⣿⢿⣿⡿⡃⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣻⣧⣴⢷⡿⠀⠀⠘⢿⣿⣾⠟⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠿⢶⣿⣿⠁⣀⣀⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢷⣶⣤⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣤⣿⣿⣿⣿⢿⢿⡇⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀
⠀⠀⠀⠠⠿⢿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠈⠻⠿⠿⠿⠿⠿⠿⠟⠛⠛⠛⠛⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣿⣿⣿⣿⣿⣷⣼
⠀⠀⠀⠀⠀⡀⡀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡙⠻⣿⣿⣿


"""

            cat10 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠖⠶⠦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⢀⠀⠈⠉⠓⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⢠⡏⠙⠲⢤⡀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⠛⠋⢹⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⣸⠁⠀⠀⠀⠈⠳⣄⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠴⠚⠋⢀⣀⣀⡄⠀⠀⢳
⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⢸⠀⢀⡇⠀⠀⠀⠀⡀⠀⢈⡳⠄⠀⣀⣹⣄⣀⠤⣤⣤⣤⢤⣀⣀⣀⡀⣀⠴⠟⠉⢀⣠⠶⠊⠉⠁⠀⣇⠀⠀⢸
⠀⠀⢀⣴⣿⣿⣿⡇⠀⠀⠀⠀⠀⣼⠀⢸⡇⠀⠀⢀⣤⠿⠖⠋⠀⠀⠈⠉⠁⢸⡇⠀⢸⣿⣿⠀⠀⢿⡉⠉⠳⢦⣀⣴⠋⠀⠀⠀⠀⠀⠀⢹⠀⠀⢸
⠀⢠⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⢸⠀⠘⠓⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠃⠀⢸⣿⣿⠀⠀⢸⣧⠀⠀⠀⠀⠈⠳⢤⣆⠀⠀⠀⠀⣸⠀⠀⢸
⢠⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⢸⣿⣿⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⡀⡇⠀⠀⢸
⣼⠉⠉⢻⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢸⣿⣿⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⢀⢸
⡟⠒⠶⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⣿⣿⣿⡀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⡟
⣇⠀⠉⢻⣿⡀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⣿⣿⣿⡇⠀⢀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃
⣟⠛⠛⠛⢿⣿⣄⠀⠀⠀⠀⠀⠀⣼⢀⣀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠈⣿⣆⠀⠸⣿⠋⠀⢀⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
⠹⣆⠀⠀⠠⠟⣿⣷⣄⠀⠀⠀⠀⡟⠀⢿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠘⠿⠷⠀⠀⠀⠐⠿⠟⠁⠀⢀⣀⣤⣶⣶⣤⣄⡀⠀⠀⠀⠀⢀⡇⠀
⠀⠙⢦⣤⠶⠚⠉⠻⣯⣳⡀⠀⠀⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⡁⢈⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⠿⣿⣿⣷⣄⣀⣠⣼⡇⠀
⠀⠀⠀⠙⢦⡀⣠⡤⠞⢣⣧⠀⠀⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⢿⣿⣿⣿⣿⣧⣀⣼⣿⣿⣿⡿⠛⢹⠃⠀
⠀⠀⠀⠀⠀⠙⣦⠤⠴⣿⣿⠀⠀⣷⢀⣼⡟⣇⠹⣿⣿⢾⣻⣿⣿⣿⠏⣸⣻⠀⠀⠀⠀⠀⠀⠀⠀⣸⢹⠸⣿⣿⣿⣿⣿⣿⣿⣿⢟⣿⡇⠀⡞⠀⠀
⠀⠀⠀⠀⠀⠀⢻⠴⠶⣿⡏⠀⠀⢿⡾⠁⢳⡘⢧⡉⠛⠿⠿⠿⠟⠉⣠⢟⡟⠀⠀⢀⣀⣀⣀⠀⠀⣧⢸⡀⠻⣿⣿⣯⣿⣿⣿⡟⣿⣿⢁⣸⡇⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣤⣤⣿⡇⠀⠀⠸⡆⠀⠀⠑⢤⠉⠓⠒⠠⠤⠖⢚⣩⠞⠀⠠⡤⣼⣶⢞⣋⣀⠀⠹⣆⠳⣄⠈⠙⠛⠛⠛⣉⠔⣹⠃⣼⡽⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣀⣤⠼⢿⡄⠀⠀⢻⡄⠀⠀⠀⠉⠛⠒⠚⠛⠛⠋⠀⠀⠀⠀⠘⠻⣿⡷⠞⠋⠀⠀⠘⠳⣤⡉⠛⠛⠛⠋⣠⠴⠃⠀⢻⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡧⠤⠴⠚⠛⢦⣀⠀⠻⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠉⠁⠀⠀⢠⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢳⡄⠀⠀⠀⠀⠉⠙⠶⢬⣝⣳⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⢀⡀⠈⠀⢸⣿⠄⠈⣏⢩⡓⠒⠒⠲⠦⠤⠤⣤⣤⣤⣤⣄⣀⣀⣀⡀⠀⠀⠀⠀⢀⣀⡤⠞⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⣾⣷⣿⡇⠀⠀⠀⠘⠀⠀⠈⠀⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡏⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣸⣁⣀⠀⠉⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡏⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⢀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡏⣿⣶⣦⣄⣀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⡼⠃⢀⣨⡽⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠈⠹⣤⣀⣀⡼⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢀⣼⠃⠐⠛⠁⠀⣨⣷⡖⠢⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠈⠙⠓⠒⠶⢤⣿⣁⣀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⣸⡠⠶⠋⠈⠙⠲⢄⠀⠀⠀⠀⢙⣆⢼⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⢸⡇⠈⢻⣉⠒⠺⣧⣴⠶⠶⠒⠒⠶⢤⡏⠀⠀⠀⠀⠀⠀⠈⠙⣆⠀⣴⢋⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⣠⣤⠘⢳⡐⠒⣮⢷⠀⣯⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⡟⠀⠀⢹⡄⢹⣤⡼⠟⠁⢸⡄⠀⡖⠛⠛⢛⡋⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⠤⠧⠤⠤⠾⠖⠁⠀⠀⠀⠀⠈⣇⠀⣿⠀⠀⠀⣷⠀⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠳⠛⠶⠤⠴⠗⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
            cat = [cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10]
            cat_choice = random.choice(cat)
            print(cat_choice)
    #still in dev
        elif command[0] == nmapcmd:
            print("Ohh scary XD")
            print("\nYou are inside nmap program, type help if you need help")
            while True:
                nmcmd = input(f"{user}@nmap >>> ")
                if nmcmd == "help":
                    print(nmap_help)
                elif nmcmd == "exit":
                    print("Exiting NMap\n")
                    break
                elif nmcmd == "scan":
                    ip = input("IP address           >>> ")
                    if not ip:
                        print("You are missing the key ingridient")
                        continue
                    starting_port = input("Port range start     >>> ")
                    if not starting_port:
                        starting_port = 1
                    finishing_port = input("Finishing port       >>> ")
                    if not finishing_port:
                        finishing_port = 1000
                    sS = input("Stealth scan (y/n)   >>> ")
                    if not sS:
                        sS = "n"
                    print(f"\nHost       >>> {ip}")
                    print(f"Port range >>> {starting_port} - {finishing_port}\n")

                else:
                    ("Not a recognised command")
    #still in dev

        #testing
        elif command[0] == "printhex":
            print(setup["passw"])
        #testing

        else:
            print("Unknown command :/")
        
    except Exception as e:
        print("An error occurred:")
        print(f"{type(e).__name__}: {e}")
        input("\nPress ENTER to continue :)")