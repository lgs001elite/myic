import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import csv


ic_num = 15
sub_range1 = [25, 100]
sub_range2 = [25, 500]
sub_range3 = [100, 500]
sub_range4 = [100, 1000]
sub_range5 = [500, 1000]
energy_set1 = []
energy_set2 = []
energy_set3 = []
energy_set4 = []
energy_set5 = []
energy_range_set = [sub_range1, sub_range2, sub_range3, sub_range4, sub_range5]
energy_con_set   = [energy_set1, energy_set2, energy_set3, energy_set4, energy_set5]


csv_writerKarios = open('Karios-datasets.txt', mode='w')
csv_writerOrigin = open('Origin-datasets.txt', mode='w')
csv_writerFind   = open('Find-datasets.txt', mode='w')
kariosSet = []
originSet = []
findSet   = []



# Generate a random charging time
def randomCharging(startNum, endNum):
    return rd.randint(startNum, endNum)

# geometric ranom generator
def geoGenerator(lam):
    rNumber = np.random.geometric(p=lam, size=1)
    return int(rNumber)


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



# Function entry for Find
def find(energySet1, energySet2):
    global csv_writerFind
    global findSet
    senderIndex   = 0
    receiverIndex = 0
    senderCharge   =  energySet1[senderIndex]   
    receiverCharge =  energySet2[receiverIndex] 
    senderIndex   = senderIndex + 1
    receiverIndex = receiverIndex + 1  
    waitingTimeS = senderCharge + 1 + \
            geoGenerator(returnParameter(senderCharge))
            #rd.randint(0, energySet1[0])    
    waitingTimeR = receiverCharge + 1 + \
            geoGenerator(returnParameter(receiverCharge))
            #rd.randint(0, energySet2[0])
    stopSignal = 1
    while (stopSignal != 0):
        if (waitingTimeS > waitingTimeR):
            while (waitingTimeS > waitingTimeR):
                receiverCharge =   energySet2[receiverIndex]
                receiverIndex = receiverIndex + 1
                delay = geoGenerator(returnParameter(receiverCharge))
                waitingTimeR = receiverCharge + 1 + delay+ waitingTimeR
        elif (waitingTimeS < waitingTimeR):
            while (waitingTimeS < waitingTimeR):
                senderCharge =  energySet1[senderIndex]
                senderIndex = senderIndex + 1
                delay = geoGenerator(returnParameter(senderCharge))
                waitingTimeS = senderCharge + 1 + delay + waitingTimeS
        else :
            stopSignal = 0  
            findSet.append(waitingTimeS)
            csv_writerFind.write(str(waitingTimeS)+"\n")

# Function entry for Karios
def karios(energySet1, energySet2):
    global csv_writerKarios
    global kariosSet
    senderIndex    = 0
    receiverIndex  = 0
    # for sender node
    subAlignTime_sender = energySet1[senderIndex] + 1 + rd.randint(0, energySet1[senderIndex]) 
    senderIndex  = senderIndex + 1
    draft_time   = subAlignTime_sender % ic_num
    delayNum = 0
    while (draft_time != delayNum):
        delayNum =  delayNum + 1
        nodeCharge = energySet1[senderIndex]
        senderIndex = senderIndex + 1
        subAlignTime_sender = subAlignTime_sender + nodeCharge + 1
        delay_time   = ic_num - subAlignTime_sender%ic_num
        subAlignTime_sender = subAlignTime_sender + delay_time
    sumSender_pre = subAlignTime_sender
    # for receiver node
    subAlignTime_receiver = energySet2[receiverIndex] + 1 + rd.randint(0, energySet2[receiverIndex]) 
    receiverIndex  = receiverIndex + 1
    draft_time   = subAlignTime_receiver % ic_num
    delayNum = 0
    while (draft_time != delayNum):
        delayNum =  delayNum + 1
        nodeCharge = energySet2[receiverIndex]
        receiverIndex = receiverIndex + 1
        subAlignTime_receiver = subAlignTime_receiver + nodeCharge + 1
        delay_time   = ic_num - subAlignTime_receiver%ic_num
        subAlignTime_receiver = subAlignTime_receiver + delay_time
    sumReceiver_pre = subAlignTime_receiver

    # print("alignment with icc")
    # print("senderSum_pre:"+ str(sumSender_pre))
    # print("receiverSum_pre:"+str(sumReceiver_pre))


    # updating times in the first time
    senderCharge  = energySet1[senderIndex] 
    receiverCharge = energySet2[receiverIndex]
    sumSender   = ic_num - (senderCharge + 1)%ic_num + senderCharge + 1
    sumReceiver = ic_num - (receiverCharge + 1)%ic_num + receiverCharge + 1
    receiverIndex = receiverIndex + 1
    senderIndex   = senderIndex + 1
    pre_sumSender   = 0
    pre_sumReceiver = 0
    # record work timr in the first time
    pre_receiver_work_time = 0
    pre_sender_work_time   = 0
    # print("first attempting to discovry with baseCyle")
    # print("senderSum:"+ str(sumSender))
    # print("receiverSum:"+str(sumReceiver))
    baseCharge = 0
    baseCycle_sender   = 0
    baseCycle_receiver = 0
    if (sumReceiver > sumSender):
        while(sumReceiver > sumSender):
            if (receiverCharge > senderCharge):
                baseCharge = rd.randint(senderCharge, receiverCharge)
            else:
                baseCharge = rd.randint(receiverCharge, senderCharge)
            # print("pre sender's charging:"+str(senderCharge))
            # print("pre_receiver's Charging:"+ str(receiverCharge))
            senderCharge  = energySet1[senderIndex]
            # print("sender's charging:"+str(senderCharge))
            senderIndex   = senderIndex + 1
            pre_sender_work_time   = sumSender
            sumSender = sumSender + ic_num - (senderCharge + 1) % ic_num + (senderCharge + 1)
        if (sumSender != sumReceiver):
            pre_sumReceiver = sumReceiver 
            baseCycle_receiver =  ic_num - (baseCharge + 1) % ic_num + baseCharge + 1
            sumReceiver = sumReceiver + baseCycle_receiver - receiverCharge%baseCycle_receiver + receiverCharge
    else:
        while(sumReceiver < sumSender):
            if (receiverCharge > senderCharge):
                baseCharge = rd.randint(senderCharge, receiverCharge)
            else:
                baseCharge = rd.randint(receiverCharge, senderCharge)
            # print("pre-receiver's charging:"+str(receiverCharge))
            # print("pre_sender's charging:"+str(senderCharge))
            receiverCharge  = energySet2[receiverIndex] 
            # print("receiver's charging:"+str(receiverCharge))
            receiverIndex   = receiverIndex + 1
            pre_receiver_work_time = sumReceiver
            sumReceiver = sumReceiver + ic_num - (receiverCharge + 1) % ic_num + (receiverCharge + 1) 
        if (sumSender != sumReceiver):
            pre_sumSender = sumSender
            baseCycle_sender =  ic_num - (baseCharge + 1) % ic_num + baseCharge + 1
            sumSender   = sumSender + baseCycle_sender - senderCharge%baseCycle_sender + senderCharge
    # print("baseCycle_sender:"+str(baseCycle_sender))
    # print("baseCycle_receiver:"+str(baseCycle_receiver))
    # print("pre_senderSum:"+ str(pre_sumSender))
    # print("pre_receiverSum:"+str(pre_sumReceiver))
    # print("next_senderSum:"+ str(sumSender))
    # print("next_receiverSum:"+str(sumReceiver))
    #discovery assist
    # print("the following steps for discovery")
    while (sumSender != sumReceiver):
        if (sumSender > sumReceiver):
            while(sumSender > sumReceiver):
                if (receiverCharge > senderCharge):
                    baseCharge = rd.randint(senderCharge, receiverCharge)
                else:
                    baseCharge = rd.randint(receiverCharge, senderCharge)
                
                # print("pre-receiver's charging:"+str(receiverCharge))
                # print("pre-sender's charging:"+str(senderCharge))
                baseCycle_receiver =  ic_num - (baseCharge + 1) % ic_num + baseCharge + 1
                receiverCharge  = energySet2[receiverIndex]
                receiverIndex   = receiverIndex + 1
                pre_receiver_work_time = sumReceiver
                sumReceiver = sumReceiver + baseCycle_receiver - receiverCharge%baseCycle_receiver + receiverCharge
                # print("baseCharge:"+str(baseCharge))
                # print("baseCycle_receiver:"+str(baseCycle_receiver))
                # print("receiver's charging:"+str(receiverCharge))
                # print("pre_receiver_work_time:"+str(pre_receiver_work_time))
            # if ((sumReceiver > pre_sender_work_time) and (baseCycle_sender != 0)):
            #     receiverCharge_temp  = energySet2[receiverIndex]
            #     sumReceiver_temp = sumReceiver + receiverCharge_temp + 1 + (sumReceiver - pre_sender_work_time)
            #     sumReceiver_temp = sumReceiver_temp + baseCycle_sender - sumReceiver_temp%baseCycle_sender
            #     if (sumReceiver_temp == sumSender):
            #         print("sumReceiver_temp:"+ str(sumReceiver_temp))
            #         print("sumSender:"+str(sumSender))
            #         print("baseCharge:"+str(baseCharge))
            #         print("pre_senderSum:"+ str(pre_sumSender))
            #         print("pre_receiverSum:"+str(pre_sumReceiver))
            #         print("receiver's charging:"+str(receiverCharge))
            #         print("pre_receiver_work_time:"+str(pre_receiver_work_time))
            #         sumReceiver = sumSender
            #         break
            
        if (sumReceiver > sumSender):
            while(sumReceiver > sumSender):
                if (receiverCharge > senderCharge):
                    baseCharge = rd.randint(senderCharge, receiverCharge)
                else:
                    baseCharge = rd.randint(receiverCharge, senderCharge)
                # print("pre-receiver's charging:"+str(receiverCharge))
                # print("pre-sender's charging:"+str(senderCharge))
                baseCycle_sender  =  ic_num - (baseCharge + 1) % ic_num + baseCharge + 1
                senderCharge  = energySet1[senderIndex]
                senderIndex   = senderIndex + 1
                pre_sender_work_time   = sumSender
                sumSender = sumSender + baseCycle_sender - senderCharge%baseCycle_sender + senderCharge
                # print("sender's charging:"+str(senderCharge))
                # print("baseCycle_sender:"+str(baseCycle_sender))
                # print("sender's charging:"+str(senderCharge))
                # print("pre_sender_work_time:"+ str(pre_sender_work_time))
            # if ((sumSender > pre_receiver_work_time) and (baseCycle_receiver != 0)):
            #     senderCharge_temp  = energySet1[senderIndex]
            #     sumSender_temp = sumSender + senderCharge_temp + 1 + (sumSender - pre_receiver_work_time)
            #     sumSender_temp = sumSender_temp + baseCycle_receiver - sumSender_temp%baseCycle_receiver
            #     if (sumSender_temp == sumReceiver):
            #         print("sumSender_temp:"+ str(sumSender_temp))
            #         print("sumReceiver:"+str(sumReceiver))
            #         print("sender's charging:"+str(senderCharge))
            #         print("pre_senderSum:"+ str(pre_sumSender))
            #         print("pre_receiverSum:"+str(pre_sumReceiver))
            #         print("sender's charging:"+str(senderCharge))
            #         print("pre_sender_work_time:"+ str(pre_sender_work_time))
            #         sumSender = sumReceiver
            #         break
        # print("next_senderSum:"+ str(sumSender))
        # print("next_receiverSum:"+str(sumReceiver))
    # print("sum_time:" + str(sumSender + sumSender_pre))
    csv_writerKarios.write(str(sumSender + sumSender_pre)+"\n")
    kariosSet.append(sumSender + sumSender_pre)

# Function entry for original
def origin(energySet1, energySet2):
    global csv_writerOrigin
    global originSet
    senderIndex    = 0
    receiverIndex  = 0
    # for sender node
    subAlignTime_sender = energySet1[senderIndex] + 1 + rd.randint(0, energySet1[senderIndex]) 
    senderIndex  = senderIndex + 1
    draft_time   = subAlignTime_sender % ic_num
    delayNum = 0
    while (draft_time != delayNum):
        delayNum =  delayNum + 1
        nodeCharge = energySet1[senderIndex]
        senderIndex = senderIndex + 1
        subAlignTime_sender = subAlignTime_sender + nodeCharge + 1
        delay_time   = ic_num - subAlignTime_sender%ic_num
        subAlignTime_sender = subAlignTime_sender + delay_time
    sumSender_pre = subAlignTime_sender
    # for receiver node
    subAlignTime_receiver = energySet2[receiverIndex] + 1 + rd.randint(0, energySet2[receiverIndex]) 
    receiverIndex  = receiverIndex + 1
    draft_time   = subAlignTime_receiver % ic_num
    delayNum = 0
    while (draft_time != delayNum):
        delayNum =  delayNum + 1
        nodeCharge = energySet2[receiverIndex]
        receiverIndex = receiverIndex + 1
        subAlignTime_receiver = subAlignTime_receiver + nodeCharge + 1
        delay_time   = ic_num - subAlignTime_receiver%ic_num
        subAlignTime_receiver = subAlignTime_receiver + delay_time
    sumReceiver_pre = subAlignTime_receiver


    senderCharge  = energySet1[senderIndex] 
    receiverCharge = energySet2[receiverIndex]
    sumSender   = ic_num - (senderCharge + 1)%ic_num + senderCharge + 1
    sumReceiver = ic_num - (receiverCharge + 1)%ic_num + receiverCharge + 1
    receiverIndex = receiverIndex + 1
    senderIndex   = senderIndex + 1
    print("***************************Starting****************************")
    print("senderSum:" + str(sumSender))
    print("senderCharge:"+str(senderCharge))
    print("receiverSum:"+str(sumReceiver))
    print("receiveCharge:"+str(receiverCharge))
    #discovery assist
    while (sumSender != sumReceiver):
        if (sumSender > sumReceiver):
            receiverCharge   = energySet2[receiverIndex]
            receiverIndex    = receiverIndex + 1
            sumReceiver   = sumReceiver + ic_num - (receiverCharge + 1)%ic_num + receiverCharge + 1
        if (sumSender < sumReceiver):
            senderCharge   = energySet1[senderIndex]
            senderIndex = senderIndex + 1
            sumSender     = sumSender + ic_num - (senderCharge + 1)%ic_num + senderCharge + 1
        print("senderSum:" + str(sumSender))
        print("senderCharge:"+str(senderCharge))
        print("receiverSum:"+str(sumReceiver))
        print("receiveCharge:"+str(receiverCharge))
    csv_writerOrigin.write(str(sumSender + sumSender_pre)+"\n")
    originSet.append(sumSender + sumSender_pre)



if __name__ == "__main__":
    for k in range(1000):
        # collect energy conditions
        index = 0
        for e_con in energy_range_set:
            for i in range(100000):
                energy_con_set[index].append(randomCharging(e_con[0], e_con[1]))
        # print(energy_con_set[index])
            index = index + 1
        # distribute energy conditions to IC nodes
        energy_dis = []
        for i in range(ic_num):
            energy_dis.append(rd.randint(0, len(energy_con_set) - 1))
        # Find
        for i in range(ic_num):
            for j in range(i + 1, ic_num):
                find(energy_con_set[energy_dis[i]], energy_con_set[energy_dis[j]])
        # Karios
        for i in range(ic_num):
            for j in range(i + 1, ic_num):
                karios(energy_con_set[energy_dis[i]], energy_con_set[energy_dis[j]])
        #     break
        # break

        #Origin
        for i in range(ic_num):
            for j in range(i + 1, ic_num):
                origin(energy_con_set[energy_dis[i]], energy_con_set[energy_dis[j]])

    findSet_sorted = np.sort(findSet)
    kariosSet_sorted = np.sort(kariosSet)
    originSet_sorted = np.sort(originSet)
    print(np.mean(findSet))
    print(np.mean(kariosSet))
    print(np.mean(originSet_sorted))

    cdf_find = np.arange(1, len(findSet_sorted) + 1) / len(findSet_sorted)
    cdf_karios = np.arange(1, len(kariosSet_sorted) + 1) / len(kariosSet_sorted)
    cdf_origin = np.arange(1, len(originSet_sorted) + 1) / len(originSet_sorted)

    plt.figure()
    plt.plot(findSet_sorted, cdf_find, label="Find")
    plt.plot(kariosSet_sorted, cdf_karios, label="Karios")
    plt.plot(originSet_sorted, cdf_karios, label="Origin")
    plt.legend()
    plt.grid()
    plt.savefig("cdf_discovery_xxx" +".pdf", format="pdf", bbox_inches="tight")
    plt.show()

    


























