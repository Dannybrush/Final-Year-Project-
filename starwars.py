import os                                       # running commands                                # Socket Connection
import subprocess                               # Running commands
import sys                                      # System Information
import time                                     # Sleep

def playstarwars():
    msg = "telnet telehack.com "
    runrun(msg)
    msg2 = ".starwars"
    time.sleep(2)
    runrun(msg2)
    print("[+] Target is now Watching Star Wars Ep.IV: A New Hope")
    # Sw = subprocess.check_call("start /B start cmd.exe @cmd /c telnet towel.blinkenlights.nl ", shell=True)

def runrun(msg):
    obj = "failed"
    try:
        obj, _ = subprocess.run(msg, check=True, shell=True)
        # output = (obj.stdout.read() + obj.stderr.read()).decode("utf-8", errors="ignore")
    except Exception as e:
        print("This failed too (runrun) : " + str(e) + " + " + str(obj))

playstarwars()
input()
