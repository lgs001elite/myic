import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logging
import os
import csv
from math import gcd

from tqdm import tqdm

threshold = 300000000


# geometric ranom generator
def geoGenerator(lam):
    rNumber = np.random.geometric(p=lam, size=1)
    return int(rNumber[0])


def uniform_integer_random(min_val, max_val):
    # Generate a random integer in the specified range
    return np.random.randint(min_val, max_val + 1)




    
# This function is for varying charging situation
def returnParameter_1_500(chargingTime):
    signalTag = 0
    with open("opt_scale_1_500.csv", 'r') as opt_scale:
        lines = csv.reader(opt_scale)
        countNum = 0
        for row in lines:
            if (countNum == 0):
                countNum = countNum + 1
                continue
            countNum = countNum + 1
            if (chargingTime >= int(row[0])):
                return float(row[1])
                break
    ranLoc = uniform_integer_random(1, countNum -1)
    countNum = 0
    df = pd.read_csv('opt_scale_1_500.csv')
    varlen = len(df['x_opt'])
    locRand = uniform_integer_random(0, varlen -1)
    # print(df['x_opt'][locRand])
    return float(df['x_opt'][locRand])


def returnParameter_501_1000(chargingTime):
    signalTag = 0
    with open("opt_scale_501_1000.csv", 'r') as opt_scale:
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








set_501 = []
set_1 = []


set_1_csv = open("set_1_20.csv", 'w')
set_501_csv = open("set_501_20.csv", 'w')
print("set_1")
for i in range(20):
    sum1 = uniform_integer_random(501, 1000)
    sum2 = uniform_integer_random(501, 1000)
    chr1 = uniform_integer_random(501, 1000)
    chr2 = uniform_integer_random(501, 1000)
    while (sum1 != sum2):
        sum1 = sum1 + geoGenerator(returnParameter_1_500(chr1))
        sum2 = sum2 + geoGenerator(returnParameter_1_500(chr2))
        if (threshold < sum1):
            break
    print("set_1_csv_success:"+ str(i))
    set_1_csv.write(str(sum1)+"\n")
    set_1.append(sum1)
    print("chr1:"+ str(chr1)+"; chr2:" + str(chr2))
    
    sum1 = uniform_integer_random(501, 1000)
    sum2 = uniform_integer_random(501, 1000)
    while (sum1 != sum2):
        sum1 = sum1 + geoGenerator(returnParameter_501_1000(chr1))
        sum2 = sum2 + geoGenerator(returnParameter_501_1000(chr2))
        if (threshold < sum1):
            break
    print("set_501_csv_success:"+ str(i))
    set_501_csv.write(str(sum1)+"\n")
    set_501.append(sum1)
    print("chr1:"+ str(chr1)+"; chr2:" + str(chr2))
set_1_csv.close()
set_501_csv.close()



# set_501_csv = open("set_501_20.csv", 'w')
# print("set_501")
# for i in range(20):
#     sum1 = uniform_integer_random(501, 1000)
#     sum2 = uniform_integer_random(501, 1000)
#     chr1 = uniform_integer_random(501, 1000)
#     chr2 = uniform_integer_random(501, 1000)
#     while (sum1 != sum2):
#         sum1 = sum1 + geoGenerator(returnParameter_501_1000(chr1))
#         sum2 = sum2 + geoGenerator(returnParameter_501_1000(chr2))
#         if (threshold < sum1):
#             break
#     print("set_501_csv_success:"+ str(i))
#     set_501_csv.write(str(sum1)+"\n")
#     set_501.append(sum1)
#     print("chr1:"+ str(chr1)+"; chr2:" + str(chr2))
# set_501_csv.close()




fig = plt.figure(constrained_layout=True, figsize=(5, 5))   


set_1_sorted = np.sort(set_1)
cdf_set_1 = np.arange(1, len(set_1_sorted) + 1) / len(set_1_sorted)
plt.plot(set_1_sorted, cdf_set_1, label="[1,500]]")
  
set_501_sorted = np.sort(set_501)
cdf_set_501 = np.arange(1, len(set_501_sorted) + 1) / len(set_501_sorted)
plt.plot(set_501_sorted, cdf_set_501, label="[500, 1000]")


plt.savefig("find_parameters_syn_performance.pdf", format='pdf')
plt.show()











# delay_range = [1,
# 4,
# 5,
# 2,
# 3,
# 2,
# 2,
# 1,
# 2,
# 16,
# 19,
# 3,
# 3,
# 8,
# 3,
# 4,
# 2,
# 2,
# 2,
# 4,
# 5,
# 5,
# 9,
# 11,
# 2,
# 8,
# 4,
# 16,
# 12,
# 1,
# 3,
# 15,
# 6,
# 4,
# 1,
# 10,
# 1,
# 9,
# 16,
# 5,
# 9,
# 4,
# 2,
# 1,
# 5,
# 23,
# 7,
# 2,
# 6,
# 24,
# 6,
# 8,
# 2,
# 4,
# 14,
# 18,
# 6,
# 2,
# 1,
# 8,
# 10,
# 5,
# 3,
# 2,
# 1,
# 8,
# 9,
# 22,
# 15,
# 2,
# 1,
# 1,
# 13,
# 6,
# 57,
# 22,
# 6,
# 1,
# 2,
# 7,
# 4,
# 7,
# 15,
# 7,
# 3,
# 11,
# 3,
# 1,
# 12,
# 2,
# 11,
# 6,
# 1,
# 5,
# 3,
# 19,
# 8,
# 3,
# 6,
# 19,
# 9,
# 5,
# 15,
# 1]   
# print(len(delay_range))       
            



