import os
import json
import pickle
import sys
import platform
from pprint import pprint
import csv


class A(object):

    host = sys.platform

    # Make a Dictionary
    sys_info = {
        "Platform": platform.system(),
        "Platform Release": platform.release(),
        "Platform Version": platform.version(),
        "Platform Architecture": platform.architecture(),
        "Machine Type": platform.machine(),
        "Platform Node": platform.node(),
        "Platform Information": platform.platform(),
        "ALL": platform.uname(),
        #"HostName": socket.gethostname(),
        #"Host IP_Address": socket.gethostbyname(socket.gethostname()),
        "CPU": platform.processor(),
        "Python Build": platform.python_build(),
        "Python Compiler": platform.python_compiler(),
        "Python Version": platform.python_version(),
        "Windows Platform": platform.win32_ver()
        #  "OS": os.uname() # os.uname() ONLY SUPPORTED ON LINUX
    }

    def dictPickle(self):
        print("\ndictPickle: ")


    def dictJSON(self):
        print("\ndictJSON: ")

    def printdict(self):
        print("\nprintdict: ")
        print(self.sys_info)


    def iterateDict(self):
        print("\niteratedict: ")
        for item in self.sys_info:
            print(item)


    def iterateitemsDict(self):
        print("\niterateitemsdict: ")
        for item in self.sys_info.items():
            print(item)

    def txtPrint(self):
        print("\niterative KV : ")
        for k, v in self.sys_info.items():
            print(str(k) + ' >>> ' + str(v) + '')

    def prettyprintdict(self):
        print("\npretty print: ")
        pprint(self.sys_info)

    def txtwrite(self):
        print("\ntxtwrite: ")
        with open('./logs/txtprint.txt', 'w+') as f:
            for k, v in self.sys_info.items():
                f.write(str(k) + ' >>> ' + str(v) + '\n')

    def csvprint(self):
        print("\ncsvwrite: ")
        w = csv.writer(open('./logs/csvprint.csv', 'w+'))
        for k, v in self.sys_info.items():
            w.writerow([k, v])

    def printfile(self):
        print("\nprint to file: ")
        with open('./logs/printfile.txt', 'w') as f:
            print(self.sys_info, file=f)

    def writelines(self):
        print("\nwritelines: ")
        with open('./logs/writelines.txt', 'w') as f:
            for line in self.sys_info:
                f.writelines(str(line))

    def jsonwrite(self):
        print("\nJSONWrite : ")
        with open('./logs/jsonwrite.json', 'w') as f:
            f.write(json.dumps(self.sys_info))

    def picklewrite(self):
        print("\nPICKLE WRITE: ")
        with open('./logs/picklewrite.pickle', 'wb') as f:
            pickle.dump(self.sys_info, f)

    def jsonread(self):
        print("\nJSON Read: ")
        with open('./logs/jsonwrite.json', 'rb') as jsond:
            self.newjsondict = json.load(jsond)
        pprint(self.newjsondict)

    def pklread(self):
        print("\nPICKLE read: ")
        with open('./logs/picklewrite.pickle', 'rb') as pkld:
            self.newpickledict = pickle.load(pkld)
        pprint(self.newpickledict)

    def consoleandfile(self):
        print("\ncnfwrite: ")
        with open('./logs/cnf.txt', 'w+') as f:
            for k, v in self.sys_info.items():
                f.write(str(k) + ' >>> ' + str(v) + '\n')
                print(str(k) + ' >>> ' + str(v) + '')


input()
# A.dictPickle(A)
# A.dictJSON(A)
# A.printdict(A)
# A.iterateDict(A)
# A.iterateitemsDict(A)
# A.txtPrint(A)
# A.prettyprintdict(A)
# A.txtwrite(A)
# A.csvprint(A)
# A.printfile(A)
# A.writelines(A)
# A.jsonwrite(A)
# A.picklewrite(A)
# #A.pklread(A)
# A.jsonread(A)
# A.consoleandfile(A)

input()
pprint(A.sys_info)
#print(A.sys_info.encode())
pprint(str(A.sys_info))
print(str(A.sys_info).encode())
b = (str(A.sys_info).encode())
print()
