import numpy as np
import logging
import os
import csv
from math import gcd

from tqdm import tqdm

from concurrent.futures import ThreadPoolExecutor


time_threshold = 3600000 # it stands for one hour if one slot stands for 1ms
repeation_number = 50

static_value = 0

class Vars:
    STATIC_TRACE = 0
    COMPLEX_TRACE = 1
    STAIRS_TRACE = 2
    CARS_TRACE = 3
    JOGGING_TRACE = 4
    OFFICE_TRACE = 5
    WASHER_TRACE = 6

# scenarios = [ "STATIC_TRACE",  "COMPLEX_TRACE", "STAIRS_TRACE", "CARS_TRACE", 
#              "JOGGING_TRACE", "OFFICE_TRACE", "WASHER_TRACE"]


scenarios = [ "STATIC_TRACE",  "STAIRS_TRACE"]


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
        tempList = readCSV("../../charging_traces/"+nameSet+"_"+str(index)+"th.csv")
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
    global icSet3
    global icSet4
    global stairSetIndex
    global carSetIndex
    global joggingSetIndex
    global officeSetIndex
    global washerSetIndex
    global realSet
    global static_value
    if scenario == Vars.STATIC_TRACE:
        return static_value
    elif scenario == Vars.COMPLEX_TRACE:
        return uniform_integer_random(100, 501)
    elif (scenario >= Vars.STAIRS_TRACE) and (scenario <= Vars.WASHER_TRACE):
        # clarify datasets for each discovery method
        icSet = []
        if disScheme == 0:
            icSet =  icSet1
        elif disScheme == 1:
            icSet =  icSet2
        elif disScheme == 2:
            icSet =  icSet3
        else:
            icSet =  icSet4
        realLoc = scenario - 2
        index = icSet[nodeId].currentTraceIndex
        #print(nodeId)
        if index < realSetLen[realLoc]:
            index = index + 1
            icSet[nodeId].currentTraceIndex = index
            return realSet[realLoc][index - 1]
        else:
            index = 0
            index = index + 1
            icSet[nodeId].currentTraceIndex = index
            return realSet[realLoc][index - 1]  


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


def updatingRandomSyntime(icID, icSet, synScheme, scenario):
    global icSet1
    global icSet2
    icCharge = energy_model(scenario, icID, synScheme)
    dutyCycle = icCharge + 1
    ic_indication_cycle = icSet[icID].indicateSize
    if synScheme == synSchemes.find:
        delay: int = geoGenerator(returnParameter(icCharge))
        icSet[icID].synTime = icSet[icID].synTime + dutyCycle + delay
    else:
        delay = geoGenerator(returnParameter(icCharge))
        icSet[icID].synTime = icSet[icID].synTime + dutyCycle + delay
        bias = icSet[icID].synTime%ic_indication_cycle
        if bias != 0:
            bias = ic_indication_cycle - bias
        icSet[icID].synTime = icSet[icID].synTime + bias


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
    global icSet3
    global icSet4
    for index in range(nodeNums):
        if index == index1:
            continue
        if index == index2:
            continue
        ic_syn_time = icSet[index1].synTime
        while (icSet[index].synTime < ic_syn_time):
            if synScheme == synSchemes.find:
                updatingRandomSyntime(index, icSet, synScheme, scenario)
            elif synScheme == synSchemes.flync_find:
                updatingRandomSyntime(index, icSet, synScheme, scenario)
            elif synScheme == synSchemes.pulsar:
                updatingCoorAssiSyntime(index, icSet, synScheme, scenario)  
            else:
                updatingCoorAssiSyntime(index, icSet, synScheme, scenario)  
        if (icSet[index1].synTime == icSet[index].synTime):
            icSet[index1].collisionNum = icSet[index1].collisionNum + 1
            icSet[index2].collisionNum = icSet[index2].collisionNum + 1
            return True
    return False

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
    global icSet2
    # check same syn time
    i = 0
    while i < nodeNums:
        j = i + 1

        while (icSet[i].synTime != icSet[j].synTime):
            if (icSet[i].synTime < icSet[j].synTime):
                updatingRandomSyntime(i, icSet, synScheme, scenario)
            else:
                updatingRandomSyntime(j, icSet, synScheme, scenario)
            
        if (icSet[i].synTime == icSet[j].synTime):
            if(collisionCheckOnSyn(nodeNums, icSet, i, j, synScheme, scenario) == False):
                icSet[i].timeSet.append(icSet[i].synTime)
                icSet[j].timeSet.append(icSet[j].synTime)
                i += 2
                continue
            if (icSet[i].synTime > time_threshold):
                icSet[i].timeSet.append(icSet[i].synTime)
                icSet[j].timeSet.append(icSet[j].synTime)
                i += 2
                continue
            # collision happens, advancing  i and j progress
            # updating i and j
            updatingRandomSyntime(i, icSet, synScheme, scenario)
            updatingRandomSyntime(j, icSet, synScheme, scenario)
            i -= 2 # keeping syn
        i += 2


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
    global icSet3
    global icSet4
    nodeIndex = 0
    while (nodeIndex < nodeNums):
        newIC = ic()
        newIC.icId = nodeIndex
        newIC.distributionSize = distribution_cycle
        newIC.indicateSize = indicator_cycle
        newIC.cycleHis  = 1
        newIC.currentTraceIndex = uniform_integer_random(0,  repeation_number)
        newIC.attemptNum = 0
        newIC.locOnCycle = 0
        newIC.currentLoc = 0
        newIC.distributed = False
        newIC.free_beaconColCounter = 0
        icSet.append(newIC)
        nodeIndex = nodeIndex + 1
    # for non-coordinator
    nodeIndex = 0
    while (nodeIndex < nodeNums):
        icNode = icSet[nodeIndex]
        tchTime = energy_model(scenario, nodeIndex, synScheme)
        if (synScheme == synSchemes.flync_find) or (synScheme == synSchemes.find):
            icNode.synTime = uniform_integer_random(0, tchTime) 
        else:
            icNode.disTime = uniform_integer_random(0, tchTime) 
        nodeIndex = nodeIndex + 1
    if (synScheme == synSchemes.flync_find) or (synScheme == synSchemes.find):
        return
    # IC nodes update their loc on the distributed cycle based on the coordinator schemes
    nodeIndex = 0
    while  (nodeIndex < nodeNums):
        icNode = icSet[nodeIndex]
        # print("scheme:" + str(synScheme))
        while (icNode.distributed == False):
            updatingCoorAssiDistime(nodeIndex, icSet, synScheme, scenario)
            ic_cycle_indicator = icNode.indicateSize
            ic_cycle_distribution = icNode.distributionSize
            # calculate the current loc on the coordinator
            icNode.locOnCycle = icNode.disTime % ic_cycle_distribution
            if synScheme == synSchemes.pulsar:
                if icNode.locOnCycle == 0:
                    # print("pulsar_ic_cycle_indicator:" + str(ic_cycle_indicator))
                    # print("pulsar_ic_cycle_distribution:" + str(ic_cycle_distribution))
                    if (collisionCheckOnDis(nodeIndex, nodeNums, icSet, synScheme, scenario) == False):
                        globalLoc = globalLoc + 1
                        icNode.locOnCycle = globalLoc
                        icNode.disTime = icNode.disTime + globalLoc
                        icNode.distributed = True
            else:
                bias_slots = icNode.disTime % ic_cycle_distribution
                free_beaconLoc = icNode.disTime % ic_cycle_indicator
                if (free_beaconLoc == 0):
                    # print("free_beacon_ic_cycle_indicator:" + str(ic_cycle_indicator))
                    # print("free_beacon_ic_cycle_distribution:" + str(ic_cycle_distribution))
                    if (collisionCheckOnDis(nodeIndex, nodeNums, icSet, synScheme, scenario) == False):
                        icNode.locOnCycle = globalLoc
                        bias4Loc = 0
                        if (globalLoc >= bias_slots):
                            bias4Loc = globalLoc - bias_slots
                        else:
                            bias4Loc = ic_cycle_distribution - bias_slots + globalLoc                  
                        icNode.disTime = icNode.disTime + bias4Loc
                        globalLoc = globalLoc + 1 # without cooridnator's location
                        icNode.distributed = True
                        icNode.free_beaconColCounter = 0
                    else:
                        icNode.free_beaconColCounter = icNode.free_beaconColCounter + 1
                else:
                    icNode.free_beaconColCounter = icNode.free_beaconColCounter + 1
        icNode.free_beaconColCounter = 0 # reset for syn
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
    recursiveIni(nodeNums, distribution_cycle, indicator_cycle, scenario, synSchemes.find, icSet)
    i = 0
    while i < repeation_number: 
        i += 1
        #print("Find"+str(i))
        pairRandomFunction(scenario, synSchemes.find, icSet, nodeNums)
        for index in range(nodeNums):
            tchTime = energy_model(scenario, index, synSchemes.find)
            icSet[index].synTime = uniform_integer_random(0, tchTime) 
            icSet[index].currentTraceIndex = uniform_integer_random(0, repeation_number)
    #print("Find finished")


# Function entry for Flync_Find
def Flync_Find(distribution_cycle, indicator_cycle, scenario, nodeNums, icSet):
    global icSet2
    recursiveIni(nodeNums, distribution_cycle, indicator_cycle, scenario, synSchemes.flync_find, icSet)
    i = 0
    while i < repeation_number:
        i += 1
        #print("Flync_Find"+str(i))
        pairRandomFunction(scenario, synSchemes.flync_find, icSet, nodeNums)
        for index in range(nodeNums):
            tchTime = energy_model(scenario, index, synSchemes.flync_find)
            icSet[index].synTime = uniform_integer_random(0, tchTime)
            icSet[index].currentTraceIndex = uniform_integer_random(0, repeation_number)
    #print("Flync_Find finished")


def statistics(logger, scenario, icNums, icSet1_1, icSet2_1, icSet3_1, icSet4_1, poweroffLabel):
    global icSet1
    global icSet2
    global icSet3
    global icSet4


    synListFind = []
    colListFind = []
    disListFind = []

    synListFlyncFind = []
    colListFlyncFind = []
    disListFlyncFind =[]

    synListPulsar = []
    colListPulsar = []
    disListPulsar = []

    synListFree_beacon = []
    colListFree_beacon = []
    disListFree_beacon = []

    synListSets = [synListFind, synListFlyncFind,  synListPulsar, synListFree_beacon]
    colListSets = [colListFind, colListFlyncFind,  colListPulsar, colListFree_beacon]
    disListSets = [disListFind, disListFlyncFind,  disListPulsar, disListFree_beacon]

    # find
    disFile_find = open(poweroffLabel +"find_dis_in_"+ str(static_value)+"_"+scenarios[scenario]+"_"+str(icNums)+".csv", 'w')
    synFile_find = open(poweroffLabel +"find_syn_in_"+ str(static_value)+"_"+scenarios[scenario]+"_"+str(icNums)+".csv", 'w')
    collisionFile_find = open(poweroffLabel +"find_collision_in_"+ str(static_value)+"_"+scenarios[scenario]+"_"+str(icNums)+".csv", 'w')
    # flync find
    disFile_flync = open(poweroffLabel +"flync_dis_in_"+ str(static_value)+"_"+scenarios[scenario]+"_"+str(icNums)+".csv", 'w')
    synFile_flync = open(poweroffLabel +"flync_syn_in_"+ str(static_value)+"_"+scenarios[scenario]+"_"+str(icNums)+".csv", 'w')
    collisionFile_flync = open(poweroffLabel +"flync_collision_in_"+ str(static_value)+"_"+scenarios[scenario]
                                       +"_"+str(icNums)+".csv", 'w')
    # pulsar
    disFile_pulsar = open(poweroffLabel +"pulsar_dis_in_"+ str(static_value)+"_"+scenarios[scenario]+"_"+str(icNums)+".csv", 'w')
    synFile_pulsar = open(poweroffLabel +"pulsar_syn_in_"+ str(static_value)+"_"+scenarios[scenario]+"_"+str(icNums)+".csv", 'w')
    collisionFile_pulsar = open(poweroffLabel +"pulsar_collision_in_"+ str(static_value)+"_"+scenarios[scenario]
                                        +"_"+str(icNums)+".csv", 'w')
    # free_beacon
    disFile_free_beacon = open(poweroffLabel +"free_beacon_dis_in_"+ str(static_value)+"_"+scenarios[scenario]+"_"+str(icNums)+".csv", 'w')
    synFile_free_beacon = open(poweroffLabel +"free_beacon_syn_in_"+ str(static_value)+"_"+scenarios[scenario]+"_"+str(icNums)+".csv", 'w')
    collisionFile_free_beacon = open(poweroffLabel +"free_beacon_collision_in_"+ str(static_value)+"_"+scenarios[scenario]
                                             +"_"+str(icNums)+".csv", 'w')
    # sets
    disFiles = [disFile_find, disFile_flync, disFile_pulsar, disFile_free_beacon]
    synFiles = [synFile_find, synFile_flync,  synFile_pulsar, synFile_free_beacon]
    collisionFiles = [collisionFile_find, collisionFile_flync, collisionFile_pulsar,collisionFile_free_beacon]

    for index in range(icNums):
        indexSet = 0
        for icNodes in [icSet4_1]:
            icNode = icNodes[index]
            for elements in icNode.timeSet:
                synListSets[indexSet].append(elements)
                synFiles[indexSet].write(str(elements)+"\n")
            colListSets[indexSet].append(icNode.collisionNum)
            disListSets[indexSet].append(icNode.disTime)
            disFiles[indexSet].write(str(icNode.disTime)+"\n")
            collisionFiles[indexSet].write(str(icNode.collisionNum)+"\n")
            indexSet: int = indexSet + 1
    # close io find
    disFile_find.close()
    synFile_find.close()
    collisionFile_find.close()
    # close io flync
    disFile_flync.close()
    synFile_flync.close()
    collisionFile_flync.close()
    # close io pulsar
    disFile_pulsar.close()
    synFile_pulsar.close()
    collisionFile_pulsar.close()
    # close io free_beacon
    disFile_free_beacon.close()
    synFile_free_beacon.close()
    collisionFile_free_beacon.close()
    logger.info("*******************" + scenarios[scenario]+ "*******************")
    # log data
    synSchemeNames = ["Free_beacon"]
    # for setIndex in range(4):
    logger.info(synSchemeNames[0] +"_averageSyn: " + str(np.average(synListSets[0])))
    logger.info(synSchemeNames[0] +"_averageDis: " + str(np.average(disListSets[0])))
    logger.info(synSchemeNames[0] +"_averageCollisionNum: " + str(np.average(colListSets[0])))
    logger.info(synSchemeNames[0] +"_sumCollisionNum: " + str(np.sum(colListSets[0])))
    # simple performance establishment
    # for setIndex in range(3):
    #     if np.average(synListSets[0]) != 0:
    #         logger.info(synSchemeNames[setIndex] +"_averageEnhancedSyn: " + str(np.average(synListSets[setIndex]) / np.average(synListSets[0])))
    #     else:
    #         logger.info(synSchemeNames[setIndex] +"_averageEnhancedSyn: " + str(np.average(synListSets[setIndex])))
    #     if np.average(disListSets[0]) != 0:
    #         logger.info(synSchemeNames[setIndex] +"_averageEnhancedDis: " + str(np.average(disListSets[setIndex]) / np.average(disListSets[0])))
    #     else:
    #         logger.info(synSchemeNames[setIndex] +"_averageEnhancedDis: " + str(np.average(disListSets[setIndex])))
    #     if np.average(colListSets[setIndex]) != 0:
    #         logger.info(synSchemeNames[setIndex] +"_averageEnhancedCollisionNum: " + str(np.average(colListSets[setIndex] / np.average(colListSets[setIndex]))))
    #     else:
    #         logger.info(synSchemeNames[setIndex] +"_averageEnhancedCollisionNum: " + str(np.average(colListSets[setIndex])))


    

def sub_subTask(scenario, fb_size, icNums, logger, poweroffLabel):
    global icSet1
    global icSet2
    global icSet3
    global icSet4
    icSet1 = []
    icSet2 = []
    icSet3 = []
    icSet4 = []
    pulsarDistributionCycle = icNums + 1
    # concurrent execution
    futuresMoreMoreTasks = []
    executorMoreMore = ThreadPoolExecutor(max_workers=4)
    # futuresMoreMoreTasks.append(executorMoreMore.submit(Find, 0, 0, scenario, icNums, icSet1))
    # futuresMoreMoreTasks.append(executorMoreMore.submit(Flync_Find, 0, 10, scenario, icNums, icSet2))
    # futuresMoreMoreTasks.append(executorMoreMore.submit(Pulsar, pulsarDistributionCycle, 0, scenario, icNums, icSet3))
    futuresMoreMoreTasks.append(executorMoreMore.submit(Free_beacon, fb_size, min_co_prime(fb_size), scenario, icNums, icSet4))
    # Wait for all futures to complete
    for fTask in futuresMoreMoreTasks:
        fTask.result()
    statistics(logger, scenario, icNums, icSet1, icSet2, icSet3, icSet4, poweroffLabel)


def subTask(fb_size, icNums,logger, poweroffLabel):
    # futuresMoreTasks = []
    # executorMore = ThreadPoolExecutor(max_workers=7)
    for scenario in  [0, 1]:
        sub_subTask(scenario, fb_size, icNums, logger, poweroffLabel)



if __name__ == "__main__":
    #mergeSets("washer", 5)
    #mergeSets("stairs", 6)
    #mergeSets("office", 5)
    #mergeSets("jogging", 5)
    #mergeSets("cars", 6)
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
    scalability_nodeset = [10, 16, 20, 24, 30, 36, 40, 48, 50]
    Free_beacon_size = 51
    lengthNodeSet = len(scalability_nodeset)
    poweroffLabel = "special_scalability_51_"
    print(poweroffLabel)
    
    # for all concurrent jobs
    for sV in [10, 50, 100, 200, 300, 500]:
        static_value = sV
        for i in range(lengthNodeSet):
            logfilename = poweroffLabel+str(scalability_nodeset[i]) +"_results_"+ str(sV)+"_"
            if os.path.exists(logfilename):
                os.remove(logfilename)
            logger = logging.getLogger(logfilename)
            logger.setLevel(logging.INFO)
            handler = logging.FileHandler(os.path.join("./", logfilename + ".log"))
            handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            subTask(Free_beacon_size, scalability_nodeset[i], logger, poweroffLabel)

