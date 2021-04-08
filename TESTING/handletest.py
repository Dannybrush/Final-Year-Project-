from win32 import win32gui

class windowgrabber:
    def __init__(self):
       
 
    def getactivewindow(self):
        w=win32gui
        self.window = w.GetWindowText (w.GetForegroundWindow())
        print(self.window)

