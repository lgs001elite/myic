
from __future__ import print_function
import argparse
import subprocess
import sys
import os
import os.path
import functools
import fnmatch

#.............................................................
class CmdExecutor(object):
    def run(self, cmd):
        print (' '.join(cmd))
        result = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log = result.communicate()[0].decode("ascii")
        while (result.returncode == None):
            log += result.communicate()[0].decode("ascii")
            continue
        print(log)

#.............................................................
class ProgramDevice(object):
    cmd = CmdExecutor()

    def ninjaProgram(self):
        print("Ninja programming")
        log = cmd.run(['ninja', 'beaconing_nrf52840_xxAA_s140_7.2.0'])
        print(log)
        log = cmd.run(['ninja', 'flash_beaconing_nrf52840_xxAA_s140_7.2.0'])
        print(log)

    def nrfErase(self, device_id):
        print("Erase device", device_id)
        log = cmd.run(['nrfjprog', '--eraseall', "-s", device_id])
        print(log)

    def nrfReset(self, device_id):
        print("Resetting device", device_id)
        log = cmd.run(['nrfjprog', '--reset', "-s", device_id])
        print(log)

#..............................................................
class errorList(object):
    def __init__(self):
        self.error_lst = []
    
    def addErrors(self, ec):
        for e in ec:
            self.error_lst.append(e)
    
    def getErrors(self):
        return self.error_lst

#..............................................................

def printBoards(devices):
    for i in range(len(devices)):
        print(str(i) + " : " + devices[i])

def get_board_index(msg, devs):
    printBoards(devs)
    while(1):
        try:
            if (sys.version_info[0] == 0):
                getinput = raw_input
            else:
                getinput = input

            lst_range = list(range(len(devs)))
            inp = getinput('\n' + msg + str(lst_range) + ' [Enter `s`: To skip] ')

            if ((len(inp) > 1) or (len(inp) == 0)):
                raise ValueError
            
            inp = str(inp.lower())
            
            if (not ((inp == 's') or (inp in map(str, lst_range)))):
                raise ValueError
            elif (inp == 's'):
                print("Warning: Skipping this firmware")
                return 0
            
            num = int(inp)
        except ValueError:
            print ("Error: Please enter valid input")
            continue
        
        return (devs[num])

#......................................................................
def find_file(path, filename_filter):
    flist = []
    for base, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, filename_filter):
            flist.append(os.path.join(base, filename))


#......................................................................
cwd = os.getcwd()
print("Current directory: " + cwd)

parser = argparse.ArgumentParser(description="Mesh communication - Firmware flashing script")
parser.add_argument('-s', '--sinkNode', default=0x01, help="Provide the sink node device ID")
parser.add_argument('-c', '--commonNode', default=0x02, help="Provide the common node device ID, start from 2")
args = parser.parse_args()

sink_loaded = False
common_loaded = False
ec = 0
eList = errorList()
server_devices = []

#...................................................................... Filter nRF52 boards
cmd = CmdExecutor()
log = cmd.run(['nrfjprog', '-i'])
devices = log

# Action: Program Software and firmware
"""
for d in devices:
    if (d == str(args.sinkNode)):
        sink_loaded = True
    elif (d == str(args.commonNode)):
        common_loaded = Tru
"""


