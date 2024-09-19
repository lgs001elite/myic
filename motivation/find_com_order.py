import numpy as np
import logging
import os
import csv
from math import gcd

from tqdm import tqdm

from concurrent.futures import ThreadPoolExecutor


time_threshold = 300000000   # it stands for one hour if one slot stands for 1ms

time_counter1 = 0
syn_counter1= 0
time_counter2 = 0
syn_counter2 = 0
repeation_number = 15

class Vars:
    STATIC_TRACE = 0
    COMPLEX_TRACE = 1
    STAIRS_TRACE = 2
    CARS_TRACE = 3
    JOGGING_TRACE = 4
    OFFICE_TRACE = 5
    WASHER_TRACE = 6

scenarios = [ "STATIC_TRACE",  "COMPLEX_TRACE", "STAIRS_TRACE", "CARS_TRACE", 
             "JOGGING_TRACE", "OFFICE_TRACE", "WASHER_TRACE"]


class synSchemes:
    find = 0
    flync_find = 1
    pulsar = 2
    free_beacon = 3

globalLoc = 0
icSet1 = []

icSet2 = []

icSet3 = []

icSet4 = []



carSet    = []
carSetLen = 0
carSetIndex = 0
stairSet  = []
stairSetLen = 0
stairSetIndex = 0
joggingSet= []
joggingSetLen = 0
joggingSetIndex = 0
officeSet = []
officeSetLen = 0
officeSetIndex = 0
washerSet = []
washerSetLen = 0
washerSetIndex = 0
realSet = []
realSetLen = []


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def min_co_prime(n):
    if n == 2:
        return 1
    i = 2 # co-prime number is greater than 1
    while True:
        if gcd(n,i) == 1:
            return i
        i += 1




def readCSV(filename):
    array = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            int_row = [int(item) for item in row]
            array.append(int_row)
    return array

def crossMixed(targetList, subList):
    global washerSet
    global joggingSet
    global carSet
    global officeSet
    global stairSet
    tempTargetList = []
    lenTarget  = len(targetList)
    lenSubList = len(subList)
    index2 = 0
    for index1 in range(lenSubList):
        tempTargetList.append(subList[index1][0])
        if (index1 < lenTarget):
            tempTargetList.append(targetList[index2])
            index2: int = index1 + 1
    for index3 in range(index2, lenTarget):
        tempTargetList.append(targetList[index3])
    return  tempTargetList


def mergeSets(nameSet, num):
    global washerSet
    global joggingSet
    global carSet
    global officeSet
    global stairSet
    for index in range(num):
        tempList = readCSV("../chargingsets/"+nameSet+"_"+str(index)+"th.csv")
        if nameSet == "cars":
            carSet = crossMixed(carSet, tempList)
        if nameSet == "jogging":
            joggingSet = crossMixed(joggingSet, tempList)
        if nameSet == "office":
            officeSet = crossMixed(officeSet, tempList)
        if nameSet == "stairs":
            stairSet = crossMixed(stairSet, tempList)
        if nameSet == "washer":
            washerSet = crossMixed(washerSet, tempList)
        
# including [] edges
def uniform_integer_random(min_val, max_val):
    # Generate a random integer in the specified range
    return np.random.randint(min_val, max_val + 1)



# geometric ranom generator
def geoGenerator(lam):
    rNumber = np.random.geometric(p=lam, size=1)
    return int(rNumber[0])

# This function is for varying charging situation
def returnParameter(chargingTime):
    signalTag = 0
    with open("opt_scale.csv", 'r') as opt_scale:
        lines = csv.reader(opt_scale)
        countNum = 0
        for row in lines:
            if (countNum == 0):
                countNum = countNum + 1
                continue
            countNum = countNum + 1
            if (chargingTime >= int(row[0])):
                signalTag = 1
                return float(row[1])
                break
        if (signalTag == 0):
            return 0.8358041858099494
        
def energy_model(scenario, nodeId, disScheme):
    global icSet1
    global icSet2
    global stairSetIndex
    global carSetIndex
    global joggingSetIndex
    global officeSetIndex
    global washerSetIndex
    global realSet
    if scenario == Vars.STATIC_TRACE:
        return 100
    elif scenario == Vars.COMPLEX_TRACE:
        return uniform_integer_random(100, 501)
    elif (scenario >= Vars.STAIRS_TRACE) and (scenario <= Vars.WASHER_TRACE):
        # clarify datasets for each discovery method
        icSet = []
        if disScheme == 0:
            icSet =  icSet1
        if disScheme == 1:
            icSet =  icSet2
    
        index = icSet[nodeId].currentTraceIndex
        # print(nodeId)
        if index < realSetLen[1]:
            index = index + 1
            icSet[nodeId].currentTraceIndex = index
            return realSet[1][index - 1]
        else:
            index = uniform_integer_random(0,  realSetLen[1] - 2)
            index = index + 1
            icSet[nodeId].currentTraceIndex = index
            return realSet[1][index - 1]  


class ic:
    def __init__(self):
        self.icId = 0
        self.pairId = 0
        self.cycleHis = 0
        self.timeSet = []
        self.distributionSize = 0
        self.indicateSize = 0
        self.locOnCycle = 0
        self.currentLoc = 0
        self.attemptNum = 0
        self.collisionNum = 0
        self.currentTraceIndex = 0
        self.disTime = 0
        self.synTime = 0
        self.free_beaconColCounter = 0
        self.distributed = False
        self.timeout = False


def updatingRandomSyntime(icID, icSet, synScheme, scenario):
    global icSet1
    global icSet2
    icCharge = energy_model(scenario, icID, synScheme)
    dutyCycle = icCharge + 1
    ic_indication_cycle = icSet[icID].indicateSize
    delay: int = geoGenerator(returnParameter(icCharge))
    icSet[icID].synTime = icSet[icID].synTime + dutyCycle + delay


def updatingCoorAssiSyntime(icID, icSet, synScheme, scenario):
    global icSet3
    global icSet4
    receiverCharge = energy_model(scenario, icID, synScheme)
    dutyCycle = receiverCharge + 1
    ic_distribution_cycle = icSet[icID].distributionSize
    if (synScheme == synSchemes.free_beacon):
        bias = dutyCycle%ic_distribution_cycle
        if bias != 0:
            bias = ic_distribution_cycle - bias
        icSet[icID].synTime = icSet[icID].synTime + bias + dutyCycle
        if (icSet[icID].free_beaconColCounter < ic_distribution_cycle):
            icSet[icID].free_beaconColCounter = icSet[icID].free_beaconColCounter + 1
        else:
            icSet[icID].synTime = icSet[icID].synTime + ic_distribution_cycle * uniform_integer_random(0, 1)
    else:
        bias = dutyCycle%ic_distribution_cycle
        if bias != 0:
            bias = ic_distribution_cycle - bias
        icSet[icID].synTime = icSet[icID].synTime + bias +  dutyCycle + ic_distribution_cycle * uniform_integer_random(0, 1)


def updatingCoorAssiDistime(icID, icSet, synScheme, scenario):
    global icSet3
    global icSet4
    receiverCharge = energy_model(scenario, icID, synScheme)
    dutyCycle = receiverCharge + 1
    ic_distribution_cycle = icSet[icID].distributionSize
    if (synScheme == synSchemes.free_beacon):
        bias = dutyCycle%ic_distribution_cycle
        if bias != 0:
            bias = ic_distribution_cycle - bias
        icSet[icID].disTime = icSet[icID].disTime + bias + dutyCycle
        if (icSet[icID].free_beaconColCounter < ic_distribution_cycle):
            icSet[icID].free_beaconColCounter = icSet[icID].free_beaconColCounter + 1
        else:
            icSet[icID].disTime = icSet[icID].disTime + ic_distribution_cycle * uniform_integer_random(0, 1)
    else:
        bias = dutyCycle%ic_distribution_cycle
        if bias != 0:
            bias = ic_distribution_cycle - bias
        icSet[icID].disTime = icSet[icID].disTime + bias +  dutyCycle + ic_distribution_cycle * uniform_integer_random(0, 1) + 1

def collisionCheckOnSyn(nodeNums, icSet, index1, index2, synScheme, scenario):
    global icSet1
    global icSet2
    for index in range(nodeNums):
        if index == index1:
            continue
        if index == index2:
            continue
        ic_syn_time = icSet[index1].synTime
        while (icSet[index].synTime == ic_syn_time):
            icSet[index1].collisionNum = icSet[index1].collisionNum + 1
            icSet[index2].collisionNum = icSet[index2].collisionNum + 1
            return True
    return False



def collisionCheckOnSyn_find_order(nodeNums, icSet, synScheme, scenario):
    global icSet2
    global syn_counter2
    invalid_num = 0
    while(1):
        for index in range(nodeNums):
            updatingRandomSyntime(index, icSet, synScheme, scenario)
            if ((icSet[index].synTime > time_threshold) and (icSet[index].timeout == False)):
                    invalid_num = invalid_num + 1
                    icSet[index].timeout = True
        for index in  range(nodeNums):
            tTime = icSet[index].synTime
            for index2 in range(nodeNums):
                if (index2 == index):
                    continue
                while(icSet[index2].synTime < tTime):
                    updatingRandomSyntime(index2, icSet, synScheme, scenario)
            repNum = 0
            for index2 in range(nodeNums):
                if (index == index2):
                    continue
                if tTime == icSet[index2].synTime:
                    repNum = repNum + 1
            if repNum == 1:
                syn_counter2 = syn_counter2 + 1 
                print("success2!")
        if (invalid_num == nodeNums):
            print("finish")
            break



def pairCoordinatorFunction(scenario, senderId, receiverId, synScheme, icSet, nodeNums):
    global icSet3
    global icSet4
    sender = icSet[senderId]
    receiver = icSet[receiverId]
    while (True):
        if (sender.synTime > time_threshold):
            receiver.timeSet.append(receiver.synTime)
            sender.timeSet.append(sender.synTime)
            break
        if (sender.synTime > receiver.synTime):
            updatingCoorAssiSyntime(receiverId, icSet, synScheme, scenario)
        elif (sender.synTime < receiver.synTime):
            updatingCoorAssiSyntime(senderId, icSet, synScheme, scenario)      
        else:
            if(collisionCheckOnSyn(nodeNums, icSet, senderId, receiverId, synScheme, scenario) == False):
                receiver.timeSet.append(receiver.synTime)
                sender.timeSet.append(sender.synTime)
                break
            else:
                updatingCoorAssiSyntime(senderId, icSet, synScheme, scenario)
                updatingCoorAssiSyntime(receiverId, icSet, synScheme, scenario)
                continue


def pairRandomFunction(scenario, synScheme, icSet, nodeNums):
    global icSet1
    global syn_counter1
    invalid_num = 0
    while(1):
        i = 0
        j = 0
        while i < nodeNums:
            j = i + 1
            updatingRandomSyntime(i, icSet, synScheme, scenario)
            updatingRandomSyntime(j, icSet, synScheme, scenario)
            #print(icSet[i].synTime)
            #print(icSet[j].synTime)
            #print("**********")
            if ((icSet[i].synTime > time_threshold) and (icSet[i].timeout == False)):
                invalid_num = invalid_num + 1
                #print("increase 2:" + str(invalid_num))
                icSet[i].timeout = True
            if ((icSet[j].synTime > time_threshold) and (icSet[j].timeout == False)):
                invalid_num = invalid_num + 1
                #print("increase 2:" + str(invalid_num))
                icSet[j].timeout = True
            
            big_chr = 0
            anchor = 0
            anchor2 = 0
            if (icSet[i].synTime > icSet[j].synTime):
                big_chr = icSet[i].synTime
                anchor = i
                anchor2 = j
            else:
                big_chr = icSet[j].synTime
                anchor = j
                anchor2 = i
        
            for index in range(nodeNums):
                if (index == anchor):
                    continue
                while(icSet[index].synTime < big_chr):
                    updatingRandomSyntime(index, icSet, synScheme, scenario)
        
            repNum = 0
            for index2 in range(nodeNums):
                if (anchor == index2):
                    continue
                if icSet[anchor].synTime == icSet[index2].synTime:
                    repNum = repNum + 1
            if (repNum == 1):
                if icSet[anchor2].synTime == icSet[anchor].synTime:
                    syn_counter1 = syn_counter1 + 1 
                    print("success1!")
            i = i + 2
        if (invalid_num == nodeNums):
            print("finish")
            break
  
        
        
        


def InitailPairs(icSet, scheme, index, distribution_cycle, scenario):
    global icSet3
    global icSet4
    tchTime = energy_model(scenario, index + 1, scheme)
    dutyCycle = tchTime + 1 + uniform_integer_random(0, tchTime)
    delayTime = (dutyCycle % distribution_cycle)
    if delayTime != 0:
        delayTime = distribution_cycle - delayTime
    icSet[index + 1].synTime = icSet[index + 1].currentLoc + dutyCycle + delayTime
                
    tchTime = energy_model(scenario, index, scheme)
    dutyCycle = tchTime + 1 + uniform_integer_random(0,tchTime)
    delayTime = (dutyCycle % distribution_cycle)
    if delayTime != 0:
        delayTime = distribution_cycle - delayTime
    icSet[index].synTime = icSet[index].currentLoc  + dutyCycle + delayTime

    icSet[index].currentTraceIndex = uniform_integer_random(0, repeation_number)
    icSet[index + 1].currentTraceIndex = uniform_integer_random(0, repeation_number)

    icSet[index].currentTraceIndex = uniform_integer_random(0, repeation_number)
    icSet[index + 1].currentTraceIndex = uniform_integer_random(0, repeation_number)
    icSet[index + 1].free_beaconColCounter = 0
    icSet[index].free_beaconColCounter = 0


def collisionCheckOnDis(idNum, nodeNums, icSet, synScheme, scenario):
    global icSet3
    global icSet4
    ic_syn_time = icSet[idNum].disTime
    for index in range(nodeNums):
        if index != idNum:
            c_ic_syn_time = icSet[index].disTime
            while (c_ic_syn_time < ic_syn_time):             
                # calculate the current loc on the coordinator
                ic_cycle_distribution = icSet[index].distributionSize  
                updatingCoorAssiDistime(index, icSet, synScheme, scenario)
                icSet[index].locOnCycle = icSet[index].disTime % ic_cycle_distribution
                c_ic_syn_time = icSet[index].disTime # update the c_ic_syn_time
            if (c_ic_syn_time == ic_syn_time):
               icSet[idNum].collisionNum = icSet[idNum].collisionNum + 1
               icSet[index].collisionNum = icSet[idNum].collisionNum + 1
               return True
    return False



def distributePairs(nodeNums, icSet, distribution_cycle, scheme):
    global icSet3
    global icSet4
    for index1 in range(0, nodeNums, 2):
        index2 =index1 + 1
        # compute the bias
        bias1 = icSet[index1].locOnCycle
        bias2 = icSet[index2].locOnCycle
        bias = 0
        if (bias2 >= bias1):
            bias = bias2 - bias1
        else:
            bias = distribution_cycle - bias1 + bias2
        icSet[index1].synTime = bias1 + bias
        icSet[index2].synTime = bias2
        # updating and recording nodes' location
        icSet[index1].currentLoc = bias2
        icSet[index2].currentLoc = bias2



def recursiveIni(nodeNums, distribution_cycle, indicator_cycle, scenario,  synScheme, icSet):
    global globalLoc
    global icSet1
    global icSet2
    nodeIndex = 0
    while (nodeIndex < nodeNums):
        newIC = ic()
        newIC.icId = nodeIndex
        newIC.distributionSize = distribution_cycle
        newIC.indicateSize = indicator_cycle
        newIC.cycleHis  = 1
        newIC.currentTraceIndex = uniform_integer_random(0,  realSetLen[1] - 1)
        newIC.attemptNum = 0
        newIC.locOnCycle = 0
        newIC.currentLoc = 0
        newIC.distributed = False
        newIC.free_beaconColCounter = 0
        newIC.timeout = False
        icSet.append(newIC)
        nodeIndex = nodeIndex + 1
    # for non-coordinator
    nodeIndex = 0
    while (nodeIndex < nodeNums):
        icNode = icSet[nodeIndex]
        tchTime = energy_model(scenario, nodeIndex, synScheme)
        icNode.synTime = uniform_integer_random(0, tchTime) 
        nodeIndex = nodeIndex + 1
   


# Function entry for Pulsar
def Pulsar(distribution_cycle, indicator_cycle, scenario, nodeNums, icSet):
    global icSet3
    # Initialize
    global globalLoc
    globalLoc = 0
    recursiveIni(nodeNums, distribution_cycle, indicator_cycle, scenario, synSchemes.pulsar, icSet)
    # distribute pairs
    distributePairs(nodeNums, icSet, distribution_cycle, synSchemes.pulsar)
    for index in range(0, nodeNums, 2):
        senderId   = icSet[index].icId
        receiverId = icSet[index + 1].icId
        if (receiverId > senderId):
            i = 0
            while i < repeation_number:
                i += 1
                #print("Pulsar"+str(i))
                pairCoordinatorFunction(scenario, senderId, receiverId, synSchemes.pulsar, icSet, nodeNums)
                InitailPairs(icSet, synSchemes.pulsar, senderId, distribution_cycle, scenario)
    #print("Pulsar finished")
                
# Function entry for Free_beacon
def Free_beacon(distribution_cycle, indicator_cycle, scenario, nodeNums, icSet):
    global icSet4
    # Initialize
    global globalLoc
    globalLoc = 0
    recursiveIni(nodeNums, distribution_cycle, indicator_cycle, scenario, synSchemes.free_beacon, icSet)
    # distribute pairs
    distributePairs(nodeNums, icSet, distribution_cycle, synSchemes.free_beacon)
    for index in range(0, nodeNums, 2):
        senderId = icSet[index].icId
        receiverId = icSet[index + 1].icId
        i = 0
        while i < repeation_number:
            i += 1
            #print("Free_beacon"+str(i))
            pairCoordinatorFunction(scenario, senderId, receiverId, synSchemes.free_beacon, icSet, nodeNums)
            InitailPairs(icSet, synSchemes.free_beacon, senderId, distribution_cycle, scenario)
    #print("Free_beacon finished")


# Function entry for Find
def Find(distribution_cycle, indicator_cycle, scenario, nodeNums, icSet):
    global icSet1
    global syn_counter1
    recursiveIni(nodeNums, distribution_cycle, indicator_cycle, scenario, synSchemes.find, icSet)
    pairRandomFunction(scenario, synSchemes.find, icSet, nodeNums)


# Function entry for Flync_Find
def Flync_Find(distribution_cycle, indicator_cycle, scenario, nodeNums, icSet):
    global icSet2
    global syn_counter2
    recursiveIni(nodeNums, distribution_cycle, indicator_cycle, scenario, synSchemes.flync_find, icSet)
    collisionCheckOnSyn_find_order(nodeNums, icSet,  synSchemes.flync_find, scenario)




    
    



if __name__ == "__main__":   
    mergeSets("washer", 5)
    mergeSets("stairs", 6)
    mergeSets("office", 5)
    mergeSets("jogging", 5)
    mergeSets("cars", 6)
    washerSetLen = len(washerSet)
    carSetLen = len(carSet)
    officeSetLen = len(officeSet)
    joggingSetLen = len(joggingSet)
    stairSetLen = len(stairSet)
    realSet = [stairSet, carSet, joggingSet, officeSet, washerSet]
    realSetLen.append(stairSetLen)
    realSetLen.append(carSetLen)
    realSetLen.append(joggingSetLen)
    realSetLen.append(officeSetLen)
    realSetLen.append(washerSetLen)
    
    icNums = 100
    syn_counter1 = 0
    syn_counter2 = 0
    results_set1 = []
    results_set2 = []
    set1_csv = open("set1_100.csv", 'w')
    set2_csv = open("set2_100.csv", 'w')
    for i in range(10):
        icSet1 = []
        icSet2 = []
        Find(0, 0,  Vars.CARS_TRACE, icNums, icSet1)
        Flync_Find(0, 0, Vars.CARS_TRACE, icNums, icSet2)
        print(syn_counter1)
        print(syn_counter2)
        results_set1.append(syn_counter1)
        results_set2.append(syn_counter2)
        set1_csv.write(str(syn_counter1) + "\n")
        set2_csv.write(str(syn_counter2) + "\n")
        syn_counter1 = 0
        syn_counter2 = 0
        print(str(i)+"******************")
    set1_csv.close()
    set2_csv.close()
    

        