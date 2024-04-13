import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import csv


cars_bonito_success_rate = [98.21, 97.81, 98.14, 97.48, 97.40, 97.70, 98.17, 97.84, 96.91, 97.91, 97.34, 96.30, 97.73, 97.21, 96.35]
cars_bonito_delay = [19.045, 21.984, 18.35, 21.605, 40.921, 22.787, 20.427, 21.791, 33.115, 28.748, 26.083, 36.429, 24.709, 41.330, 34.044] 
cars_kairos_success_rate_10 = [99.70, 99.38, 99.28, 99.44, 98.51, 99.30, 99.26, 99.33, 98.20, 99.07, 98.98, 97.82, 99.32, 98.33, 97.96]
cars_kairos_delay_10 = [13.754, 16.171, 14.15, 16.583, 22.025, 16.379, 15.033, 15.466, 21.674, 17.394, 18.213, 23.768, 17.587, 21.213, 22.231]
cars_kairos_success_rate_5 = [99.22, 98.84, 98.92, 99.16, 97.40, 99.09, 99.05, 98.92, 97.41, 98.84, 98.91, 97.39, 98.79, 97.59, 97.21]
cars_kairos_delay_5 = [12.108, 14.053, 12.203, 14.561, 17.332, 14.398, 12.715, 13.83, 17.552, 14.953, 16.175, 18.539,  14.883, 16.395, 18.535]
cars_kairos_success_rate_0_8 = [99.34, 99.25, 99.04, 99.44, 97.96, 99.09, 98.99, 99.19, 97.90, 98.99, 98.91, 97.71, 99.09, 97.68, 97.42]
cars_kairos_delay_0_8        = [12.322, 14.430, 12.608, 14.762, 19.690, 14.682, 13.474, 13.859, 19.454, 15.575, 6.267, 21.139, 15.810, 19.039, 19.704]
cars_kairos_success_rate_0_5 = [98.68, 98.70, 98.56, 99.09, 96.47, 98.46, 98.17, 98.58, 96.51, 98.07, 98.51, 96.63, 98.56, 97.03, 96.67]
cars_kairos_delay_0_5        = [10.015, 11.803, 10.107, 12.104, 15.902, 11.810, 11.173, 11.363, 16.143, 12.730, 13.295, 17.318, 13.022, 15.698, 16.240]
cars_kairos_success_rate_10_update = [99.16, 99.18, 98.92, 99.30, 97.59, 98.67, 98.58, 99.12, 97.60, 98.53, 98.75, 97.17, 98.71, 97.31, 96.89]
cars_kairos_delay_10_update        = [11.437, 13.749, 11.554, 13.744, 18.577, 13.263, 12.173, 12.828, 17.582, 13.896, 14.498, 18.931, 14.126, 17.180, 17.904]


jogging_bonito_success_rate = [99.65, 99.20, 99.61, 99.36, 99.66, 97.74, 99.73, 99.68, 99.58, 99.71]
jogging_bonito_delay = [3.613, 4.024, 3.597, 3.654, 2.910, 0.014, 2.014, 2.909, 3.149, 1.996] 
jogging_kairos_success_rate_10 = [99.58, 99.61, 99.58, 99.53, 99.66, 99.98, 99.75, 99.58, 99.51, 99.77]
jogging_kairos_delay_10 = [2.44, 3.119, 2.433, 2.531, 2.404, 0.018, 1.547, 2.369, 2.578, 1.531]
jogging_kairos_success_rate_5 = [99.58, 99.50, 99.51, 99.48, 99.34, 99.97, 99.69, 99.32, 99.30, 99.68]
jogging_kairos_delay_5 = [2.163, 2.804, 2.176, 2.227, 2.043, 0.017, 1.410, 2.023, 2.190, 1.383]
jogging_kairos_success_rate_0_8 = [99.40, 99.53, 99.37, 99.46, 99.46, 99.96, 99.68, 99.44, 99.30, 99.75]
jogging_kairos_delay_0_8        = [2.182, 2.775, 2.178, 2.268, 2.149, 0.016, 1.381, 2.107, 2.298, 1.369]
jogging_kairos_success_rate_0_5 = [98.82, 99.02, 98.87, 98.79, 98.83, 99.91, 99.44, 98.64, 98.60, 99.36]
jogging_kairos_delay_0_5        = [1.789, 2.277, 1.785, 1.872, 1.759, 0.013, 1,135, 1.721, 1.874, 1.122]
jogging_kairos_success_rate_10_update = [99.68, 99.67, 99.63, 99.56, 99.68, 99.98, 99.76, 99.60, 99.56, 99.77]
jogging_kairos_delay_10_update        = [2.570, 3.299, 2.562, 2.696, 2.581, 0.018, 1.640, 2.573, 2.811, 1.619]


office_bonito_success_rate = [98.76, 98.65, 97.38, 98.36, 99.11, 97.70, 98.64, 96.82, 97.81, 97.28]
office_bonito_delay = [0.316, 0.344, 0.325, 0.347, 0.374, 0.322, 0.338, 0.343, 0.365, 0.344] 
office_kairos_success_rate_10 = [98.95, 98.47, 99.32, 98.66, 98.39, 99.28, 98.74, 99.34, 98.38, 99.37]
office_kairos_delay_10 = [0.189, 0.284, 0.481, 0.329, 0.284, 0.479, 0.327, 0.481, 0.327, 0.481]
office_kairos_success_rate_5 = [98.90, 98.41, 99.24, 98.45, 98.39, 99.26, 98.65, 99.29, 98.27, 99.27]
office_kairos_delay_5 = [0.189, 0.282, 0.462, 0.322, 0.282, 0.460, 0.321, 0.462, 0.322, 0.464]
office_kairos_success_rate_0_8 = [98.92, 98.43, 98.72, 98.41, 98.34, 98.63, 98.42, 98.68, 98.33, 98.54]
office_kairos_delay_0_8        = [0.170, 0.256, 0.433, 0.296, 0.256, 0.431, 0.294, 0.433, 0.295, 0.433]
office_kairos_success_rate_0_5 = [98.90, 98.39, 98.42, 98.21, 98.31, 98.37, 98.26, 98.05, 98.28, 97.77]
office_kairos_delay_0_5        = [0.142, 0.213, 0.361, 0.246, 0.213, 0.359, 0.245, 0.361, 0.245, 0.361]
office_kairos_success_rate_10_update = [98.93, 98.44, 98.72, 98.41, 98.34, 98.63, 98.42, 98.68, 98.33, 98.56]
office_kairos_delay_10_update        = [0.170, 0.256, 0.433, 0.296, 0.256, 0.431, 0.295, 0.433, 0.295, 0.434]


stairs_bonito_success_rate = [99.13, 98.74, 98.63, 98.63, 98.35, 98.71, 98.55, 98.46, 98.37, 98.58, 98.57, 98.48, 98.57, 98.52, 98.49]
stairs_bonito_delay = [0.044, 0.045, 0.047, 0.047, 0.047, 0.045, 0.046, 0.046, 0.046, 0.047, 0.047, 0.047, 0.046, 0.047, 0.047] 
stairs_kairos_success_rate_10 = [99.99, 99.99, 99.99, 99.99, 99.99, 99.99, 99.98, 99.98, 99.99, 99.98, 99.98, 99.99, 99.99, 99.98, 99.99]
stairs_kairos_delay_10 = [0.085, 0.087, 0.087, 0.086, 0.086, 0.087, 0.085, 0.084, 0.085, 0.087, 0.087, 0.087, 0.085, 0.085, 0.085]
stairs_kairos_success_rate_5 = [99.99, 99.99, 99.99, 99.99, 99.99, 99.99, 99.98, 99.98, 99.99, 99.98, 99.98, 99.99, 99.99, 99.98, 99.99]
stairs_kairos_delay_5 = [0.085, 0.086, 0.086, 0.086, 0.086, 0.086, 0.085, 0.084, 0.085, 0.087, 0.087, 0.087, 0.085, 0.085, 0.085]
stairs_kairos_success_rate_0_8 = [99.99, 99.99, 99.99, 99.99, 99.99, 99.99, 99.98, 99.98, 99.98, 99.98, 99.98, 99.99, 99.98, 99.98, 99.98]
stairs_kairos_delay_0_8        = [0.077, 0.078, 0.078, 0.078, 0.078, 0.078, 0.076, 0.076, 0.077, 0.078, 0.078, 0.078, 0.077, 0.077, 0.077]
stairs_kairos_success_rate_0_5 = [99.98, 99.98, 99.98, 99.98, 99.98, 99.99, 99.97, 99.97, 99.97, 99.97, 99.97, 99.97, 99.98, 99.96, 99.97]
stairs_kairos_delay_0_5        = [0.064, 0.065, 0.065, 0.065, 0.065, 0.065, 0.064, 0.063, 0.064, 0.065, 0.065, 0.065, 0.064, 0.064, 0.064]
stairs_kairos_success_rate_10_update = [99.93, 99.93, 99.81, 99.83, 99.82, 99.96, 99.83, 99.84, 99.82, 99.82, 99.83, 99.82, 99.92, 99.89, 99.89]
stairs_kairos_delay_10_update        = [0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.044, 0.045, 0.046, 0.046, 0.046, 0.045, 0.045, 0.045]


washer_bonito_success_rate = [99.18, 97.26, 99.27, 99.46, 97.01, 99.03, 99.79, 97.01, 99.51, 99.47]
washer_bonito_delay = [0.388, 9.221, 0.170, 0.268, 9.160, 0.393, 0.915, 9.160, 28.364, 0.266] 
washer_kairos_success_rate_10 = [99.86, 99.72, 99.91, 99.87, 99.55, 99.91, 99.86, 99.55, 99.51, 99.9]
washer_kairos_delay_10 = [0.496, 2.113, 0.298, 0.298, 2.117, 0.495, 0.494, 2.116, 2.11, 0.293]
washer_kairos_success_rate_5 = [99.86, 99.72, 99.91, 99.87, 99.55, 99.91, 99.86, 99.55, 99.51, 99.90]
washer_kairos_delay_5 = [0.505, 2.113, 0.299, 0.299, 2.114, 0.494, 0.494, 2.114, 2.106, 0.300]
washer_kairos_success_rate_0_8 = [99.81, 99.53, 99.90, 99.87, 99.55, 99.89, 99.86, 99.55, 99.51, 99.90]
washer_kairos_delay_0_8        = [0.447, 1.899, 0.268, 0.268, 1.905, 0.446, 0.445, 1.904, 1.898, 0.264]
washer_kairos_success_rate_0_5 = [99.79, 99.43, 99.88, 99.87, 99.55, 99.86, 99.84, 99.55, 99.32, 99.88]
washer_kairos_delay_0_5        = [0.372, 1.582, 0.223, 0.223, 1.587, 0.371, 0.370, 1.586, 1.580, 0.219]
washer_kairos_success_rate_10_update = [99.69, 99.43, 99.82, 99.81, 99.37, 99.73, 99.81, 99.37, 99.32, 99.84]
washer_kairos_delay_10_update        = [0.275, 1.167, 0.165, 0.165, 1.167, 0.273, 0.272, 1.169, 1.164, 0.163]


cars_bonito_mean_success_rate = np.mean(cars_bonito_success_rate)
cars_bonito_mean_delay = np.mean(cars_bonito_delay)
cars_kairos_mean_success_rate = np.mean(cars_kairos_success_rate_10_update)
cars_karios_mean_delay = np.mean(cars_kairos_delay_10_update)
print("Cars scenarios (S=10)")
print("bonito mean success rate:"+ str(cars_bonito_mean_success_rate))
print("bonito mean delay:" + str(cars_bonito_mean_delay))
print("kairos mean success rate:" + str(cars_kairos_mean_success_rate) + ", improve:"+ str(cars_kairos_mean_success_rate  - cars_bonito_mean_success_rate))
print("kairos mean delay:" + str(cars_karios_mean_delay) + ", improve:"+ str(cars_bonito_mean_delay - cars_karios_mean_delay))
print("*******************************")
# print("Cars scenarios (S=5)")
# cars_kairos_mean_success_rate = np.mean(cars_kairos_success_rate_5)
# cars_karios_mean_delay = np.mean(cars_kairos_delay_5)
# print("kairos mean success rate:" + str(cars_kairos_mean_success_rate) + ", improve:"+ str((cars_kairos_mean_success_rate - cars_bonito_mean_success_rate)/cars_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(cars_karios_mean_delay) + ", improve:"+ str((cars_bonito_mean_delay - cars_karios_mean_delay)/cars_bonito_mean_delay * 100))
# print("*******************************")
# print("Cars scenarios (S=0.8)")
# cars_kairos_mean_success_rate = np.mean(cars_kairos_success_rate_0_8)
# cars_karios_mean_delay = np.mean(cars_kairos_delay_0_8)
# print("kairos mean success rate:" + str(cars_kairos_mean_success_rate) + ", improve:"+ str((cars_kairos_mean_success_rate - cars_bonito_mean_success_rate)/cars_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(cars_karios_mean_delay) + ", improve:"+ str((cars_bonito_mean_delay - cars_karios_mean_delay)/cars_bonito_mean_delay * 100))
# print("*******************************")
# print("Cars scenarios (S=0.5)")
# cars_kairos_mean_success_rate = np.mean(cars_kairos_success_rate_0_5)
# cars_karios_mean_delay = np.mean(cars_kairos_delay_0_5)
# print("kairos mean success rate:" + str(cars_kairos_mean_success_rate) + ", improve:"+ str((cars_kairos_mean_success_rate - cars_bonito_mean_success_rate)/cars_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(cars_karios_mean_delay) + ", improve:"+ str((cars_bonito_mean_delay - cars_karios_mean_delay)/cars_bonito_mean_delay * 100))
# print("*******************************")


jogging_bonito_mean_success_rate = np.mean(jogging_bonito_success_rate)
jogging_bonito_mean_delay = np.mean(jogging_bonito_delay)
jogging_kairos_mean_success_rate = np.mean(jogging_kairos_success_rate_10_update)
jogging_karios_mean_delay = np.mean(jogging_kairos_delay_10_update)
print("Jogging scenarios (S=10)")
print("bonito mean success rate:" + str(jogging_bonito_mean_success_rate))
print("bonito mean delay:" + str(jogging_bonito_mean_delay))
print("kairos mean success rate:" + str(jogging_kairos_mean_success_rate) + "\
    improve:"+ str(jogging_kairos_mean_success_rate - jogging_bonito_mean_success_rate ))
print("kairos mean delay:" + str(jogging_karios_mean_delay) + ", improve:"+ str(jogging_bonito_mean_delay - jogging_karios_mean_delay))
print("*******************************")
# print("Jogging scenarios (S=5)")
# jogging_kairos_mean_success_rate = np.mean(jogging_kairos_success_rate_5)
# jogging_karios_mean_delay = np.mean(jogging_kairos_delay_5)
# print("kairos mean success rate:" + str(jogging_kairos_mean_success_rate) + "\
#     improve:"+ str((jogging_kairos_mean_success_rate - jogging_bonito_mean_success_rate)/jogging_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(jogging_karios_mean_delay) + ", improve:"+ str((jogging_bonito_mean_delay - jogging_karios_mean_delay)/jogging_bonito_mean_delay * 100))
# print("*******************************")
# print("Jogging scenarios (S=0.8)")
# jogging_kairos_mean_success_rate = np.mean(jogging_kairos_success_rate_0_8)
# jogging_karios_mean_delay = np.mean(jogging_kairos_delay_0_8)
# print("kairos mean success rate:" + str(jogging_kairos_mean_success_rate) + "\
#     improve:"+ str((jogging_kairos_mean_success_rate - jogging_bonito_mean_success_rate)/jogging_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(jogging_karios_mean_delay) + ", improve:"+ str((jogging_bonito_mean_delay - jogging_karios_mean_delay)/jogging_bonito_mean_delay * 100))
# print("*******************************")
# print("Jogging scenarios (S=0.5)")
# jogging_kairos_mean_success_rate = np.mean(jogging_kairos_success_rate_0_5)
# jogging_karios_mean_delay = np.mean(jogging_kairos_delay_0_5)
# print("kairos mean success rate:" + str(jogging_kairos_mean_success_rate) + "\
#     improve:"+ str((jogging_kairos_mean_success_rate - jogging_bonito_mean_success_rate)/jogging_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(jogging_karios_mean_delay) + ", improve:"+ str((jogging_bonito_mean_delay - jogging_karios_mean_delay)/jogging_bonito_mean_delay * 100))
# print("*******************************")


office_bonito_mean_success_rate = np.mean(office_bonito_success_rate)
office_bonito_mean_delay = np.mean(office_bonito_delay)
office_kairos_mean_success_rate = np.mean(office_kairos_success_rate_10_update)
office_karios_mean_delay = np.mean(office_kairos_delay_10_update)
print("Office scenarios (S=10)")
print("bonito mean success rate:" + str(office_bonito_mean_success_rate))
print("bonito mean delay:" + str(office_bonito_mean_delay))
print("kairos mean success rate:" + str(office_kairos_mean_success_rate) + ", improve:" + \
    str(office_kairos_mean_success_rate - office_bonito_mean_success_rate))
print("kairos mean delay:" + str(office_karios_mean_delay) + ", improve:"+ str(office_bonito_mean_delay - office_karios_mean_delay))
print("*******************************")
# print("Office scenarios (S=5)")
# office_kairos_mean_success_rate = np.mean(office_kairos_success_rate_5)
# office_karios_mean_delay = np.mean(office_kairos_delay_5)
# print("kairos mean success rate:" + str(office_kairos_mean_success_rate) + ", improve:" + \
#     str((office_kairos_mean_success_rate - office_bonito_mean_success_rate)/office_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(office_karios_mean_delay) + ", improve:"+ str((office_bonito_mean_delay - office_karios_mean_delay)/office_bonito_mean_delay * 100))
# print("*******************************")
# print("Office scenarios (S=0.8)")
# office_kairos_mean_success_rate = np.mean(office_kairos_success_rate_0_8)
# office_karios_mean_delay = np.mean(office_kairos_delay_0_8)
# print("kairos mean success rate:" + str(office_kairos_mean_success_rate) + ", improve:" + \
#     str((office_kairos_mean_success_rate - office_bonito_mean_success_rate)/office_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(office_karios_mean_delay) + ", improve:"+ str((office_bonito_mean_delay - office_karios_mean_delay)/office_bonito_mean_delay * 100))
# print("*******************************")
# print("Office scenarios (S=0.5)")
# office_kairos_mean_success_rate = np.mean(office_kairos_success_rate_0_5)
# office_karios_mean_delay = np.mean(office_kairos_delay_0_5)
# print("kairos mean success rate:" + str(office_kairos_mean_success_rate) + ", improve:" + \
#     str((office_kairos_mean_success_rate - office_bonito_mean_success_rate)/office_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(office_karios_mean_delay) + ", improve:"+ str((office_bonito_mean_delay - office_karios_mean_delay)/office_bonito_mean_delay * 100))
# print("*******************************")


stairs_bonito_mean_success_rate = np.mean(stairs_bonito_success_rate)
stairs_bonito_mean_delay = np.mean(stairs_bonito_delay)
stairs_kairos_mean_success_rate = np.mean(stairs_kairos_success_rate_10_update)
stairs_karios_mean_delay = np.mean(stairs_kairos_delay_10_update)
print("Stairs scenarios (S=10)")
print("bonito mean success rate:"+ str(stairs_bonito_mean_success_rate))
print("bonito mean delay:" + str(stairs_bonito_mean_delay))
print("kairos mean success rate:" + str(stairs_kairos_mean_success_rate) + ", improve:"\
    + str(stairs_kairos_mean_success_rate - stairs_bonito_mean_success_rate))
print("kairos mean delay:" + str(stairs_karios_mean_delay) + ", improve:" + str(stairs_bonito_mean_delay - stairs_karios_mean_delay))
print("*******************************")
# print("Stairs scenarios (S=5)")
# stairs_kairos_mean_success_rate = np.mean(stairs_kairos_success_rate_5)
# stairs_karios_mean_delay = np.mean(stairs_kairos_delay_5)
# print("kairos mean success rate:" + str(stairs_kairos_mean_success_rate) + ", improve:"\
#     + str((stairs_kairos_mean_success_rate - stairs_bonito_mean_success_rate)/stairs_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(stairs_karios_mean_delay) + ", improve:" + str((stairs_bonito_mean_delay - stairs_karios_mean_delay)/stairs_bonito_mean_delay * 100))
# print("*******************************")
# print("Stairs scenarios (S=0.8)")
# stairs_kairos_mean_success_rate = np.mean(stairs_kairos_success_rate_0_8)
# stairs_karios_mean_delay = np.mean(stairs_kairos_delay_0_8)
# print("kairos mean success rate:" + str(stairs_kairos_mean_success_rate) + ", improve:"\
#     + str((stairs_kairos_mean_success_rate - stairs_bonito_mean_success_rate)/stairs_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(stairs_karios_mean_delay) + ", improve:" + str((stairs_bonito_mean_delay - stairs_karios_mean_delay)/stairs_bonito_mean_delay * 100))
# print("*******************************")
# print("Stairs scenarios (S=0.5)")
# stairs_kairos_mean_success_rate = np.mean(stairs_kairos_success_rate_0_5)
# stairs_karios_mean_delay = np.mean(stairs_kairos_delay_0_5)
# print("kairos mean success rate:" + str(stairs_kairos_mean_success_rate) + ", improve:"\
#     + str((stairs_kairos_mean_success_rate - stairs_bonito_mean_success_rate)/stairs_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(stairs_karios_mean_delay) + ", improve:" + str((stairs_bonito_mean_delay - stairs_karios_mean_delay)/stairs_bonito_mean_delay * 100))
# print("*******************************")


washer_bonito_mean_success_rate = np.mean(washer_bonito_success_rate)
washer_bonito_mean_delay = np.mean(washer_bonito_delay)
washer_kairos_mean_success_rate = np.mean(washer_kairos_success_rate_10_update)
washer_karios_mean_delay = np.mean(washer_kairos_delay_10_update)
print("Washer scenarios (S=10)")
print("bonito mean success rate:" + str(washer_bonito_mean_success_rate))
print("bonito mean delay:"+ str(washer_bonito_mean_delay))
print("kairos mean success rate:" + str(washer_kairos_mean_success_rate) + ", improve:"\
    + str(washer_kairos_mean_success_rate - washer_bonito_mean_success_rate))
print("kairos mean delay:" + str(washer_karios_mean_delay) + ", improve:"+ str(washer_bonito_mean_delay - washer_karios_mean_delay))
print("*******************************")



# print("Washer scenarios (S=5)")
# washer_kairos_mean_success_rate = np.mean(washer_kairos_success_rate_5)
# washer_karios_mean_delay = np.mean(washer_kairos_delay_5)
# print("kairos mean success rate:" + str(washer_kairos_mean_success_rate) + ", improve:"\
#     + str((washer_kairos_mean_success_rate - washer_bonito_mean_success_rate)/washer_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(washer_karios_mean_delay) + ", improve:"+ str((washer_bonito_mean_delay - washer_karios_mean_delay)/(washer_bonito_mean_delay * 100)))
# print("*******************************")
# print("Washer scenarios (S=0.8)")
# washer_kairos_mean_success_rate = np.mean(washer_kairos_success_rate_0_8)
# washer_karios_mean_delay = np.mean(washer_kairos_delay_0_8)
# print("kairos mean success rate:" + str(washer_kairos_mean_success_rate) + ", improve:"\
#     + str((washer_kairos_mean_success_rate - washer_bonito_mean_success_rate)/washer_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(washer_karios_mean_delay) + ", improve:"+ str((washer_bonito_mean_delay - washer_karios_mean_delay)/(washer_bonito_mean_delay * 100)))
# print("*******************************")
# print("Washer scenarios (S=0.5)")
# washer_kairos_mean_success_rate = np.mean(washer_kairos_success_rate_0_5)
# washer_karios_mean_delay = np.mean(washer_kairos_delay_0_5)
# print("kairos mean success rate:" + str(washer_kairos_mean_success_rate) + ", improve:"\
#     + str((washer_kairos_mean_success_rate - washer_bonito_mean_success_rate)/washer_bonito_mean_success_rate * 100))
# print("kairos mean delay:" + str(washer_karios_mean_delay) + ", improve:"+ str((washer_bonito_mean_delay - washer_karios_mean_delay)/(washer_bonito_mean_delay * 100)))
# print("*******************************")




