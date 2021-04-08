
class tester:
    def __init__(self):
        self.switcher = {
            1: self.p,
            2: self.a,
            3: self.b,
            "Test": self.indexchange,
        }

    def p(self):
        print("p")

    def a(self):
        print("a")

    def b(self):
        print("b")

    def indexchange(self):
        print("I'm a genius")


test = tester()
func = test.switcher.get(3)
func()
try:
    func = test.switcher.get(4)
    func()
except TypeError:
    print("This operation does not exist. ")
except Exception as e:
    print("Even I don't know how you got this error - so I'll lock the pc. ")
    func = test.switcher.get(1)
    func()
#
# FinalSwitcher = {
#     1: self.sendHostInfo,
#     2: self.txtmsg,
#     3: self.filesend,
#     4: self.runprocess,
#     5: self.runrun,
#     6: self.enableTN,
#     7: self.playchess,
#     8: self.playstarwars,
#     9: self.weather,
#     10: self.locksystem,
#     11: self.shutdown,
#     12: self.shutdownmessage,
#     13: self.restart,
#     14: self.fakeshell,
#     15: self.endless
# }

#
# FinalSwitcher = {
#     "-Host": self.sendHostInfo,
#     "-Msg": self.txtmsg,
#     "-Fsend": self.filesend,
#     "-RP": self.runprocess,
#     "-RR": self.runrun,
#     "-Telnet": self.enableTN,
#     "-Chess": self.playchess,
#     "-EpIV": self.playstarwars,
#     "-Weather": self.weather,
#     "-lock": self.locksystem,
#     "-shutdown": self.shutdown,
#     "-shutdownM": self.shutdownmessage,
#     "-restart": self.restart,
#     "-shell": self.fakeshell,
#     "-loop": self.endless
# }