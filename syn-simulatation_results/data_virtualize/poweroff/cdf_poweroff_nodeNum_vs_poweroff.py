import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import csv




syn_methods = ["Find", "Flync", "Pulsar", "Free_beacon"]
syn_methods_name = ["Find", "Flync_Find", "Pulsar", "FreeBeacon"]

node_sets = [2, 10, 50]
node_sets_name = ["2", "10", "50"]

poweroff_rate = ["1", "5", "10", "20", "30"]

energy_scenarios = ["Static_trace", "Complex_trace", "Cars_trace", "Jogging_trace", "Office_trace", "Stairs_trace", "Washer_trace"]
energy_scenarios_names = ["Static", "Random", "Cars trace", "Jogging trace", "Office trace", "Stairs trace", "Washer trace"]

title ="cdf_free_beacon_poweroff_num_poweroff"
colors = ['steelblue', 'darkorange', 'forestgreen', 'firebrick']

find_static_2_1        = []
flync_static_2_1       = []
pulsar_static_2_1      = []
free_beacon_static_2_1 = []

find_static_2_5        = []
flync_static_2_5       = []
pulsar_static_2_5      = []
free_beacon_static_2_5 = []

find_static_2_10        = []
flync_static_2_10       = []
pulsar_static_2_10      = []
free_beacon_static_2_10 = []

find_static_2_20        = []
flync_static_2_20       = []
pulsar_static_2_20      = []
free_beacon_static_2_20 = []

find_static_2_30        = []
flync_static_2_30       = []
pulsar_static_2_30      = []
free_beacon_static_2_30 = []


find_static_10_1        = []
flync_static_10_1       = []
pulsar_static_10_1      = []
free_beacon_static_10_1 = []

find_static_10_5        = []
flync_static_10_5       = []
pulsar_static_10_5      = []
free_beacon_static_10_5 = []

find_static_10_10        = []
flync_static_10_10       = []
pulsar_static_10_10      = []
free_beacon_static_10_10 = []

find_static_10_20        = []
flync_static_10_20       = []
pulsar_static_10_20      = []
free_beacon_static_10_20 = []

find_static_10_30        = []
flync_static_10_30       = []
pulsar_static_10_30      = []
free_beacon_static_10_30 = []


find_static_50_1        = []
flync_static_50_1       = []
pulsar_static_50_1      = []
free_beacon_static_50_1 = []

find_static_50_5        = []
flync_static_50_5       = []
pulsar_static_50_5      = []
free_beacon_static_50_5 = []

find_static_50_10        = []
flync_static_50_10       = []
pulsar_static_50_10      = []
free_beacon_static_50_10 = []

find_static_50_20        = []
flync_static_50_20       = []
pulsar_static_50_20      = []
free_beacon_static_50_20 = []

find_static_50_30        = []
flync_static_50_30       = []
pulsar_static_50_30      = []
free_beacon_static_50_30 = []


find_random_2_1        = []
flync_random_2_1       = []
pulsar_random_2_1      = []
free_beacon_random_2_1 = []

find_random_2_5        = []
flync_random_2_5       = []
pulsar_random_2_5      = []
free_beacon_random_2_5 = []

find_random_2_10        = []
flync_random_2_10       = []
pulsar_random_2_10      = []
free_beacon_random_2_10 = []

find_random_2_20        = []
flync_random_2_20       = []
pulsar_random_2_20      = []
free_beacon_random_2_20 = []

find_random_2_30        = []
flync_random_2_30       = []
pulsar_random_2_30      = []
free_beacon_random_2_30 = []


find_random_10_1        = []
flync_random_10_1       = []
pulsar_random_10_1      = []
free_beacon_random_10_1 = []

find_random_10_5        = []
flync_random_10_5       = []
pulsar_random_10_5      = []
free_beacon_random_10_5 = []

find_random_10_10        = []
flync_random_10_10       = []
pulsar_random_10_10      = []
free_beacon_random_10_10 = []

find_random_10_20        = []
flync_random_10_20       = []
pulsar_random_10_20      = []
free_beacon_random_10_20 = []

find_random_10_30        = []
flync_random_10_30       = []
pulsar_random_10_30      = []
free_beacon_random_10_30 = []


find_random_50_1        = []
flync_random_50_1       = []
pulsar_random_50_1      = []
free_beacon_random_50_1 = []

find_random_50_5        = []
flync_random_50_5       = []
pulsar_random_50_5      = []
free_beacon_random_50_5 = []

find_random_50_10        = []
flync_random_50_10       = []
pulsar_random_50_10      = []
free_beacon_random_50_10 = []

find_random_50_20        = []
flync_random_50_20       = []
pulsar_random_50_20      = []
free_beacon_random_50_20 = []

find_random_50_30        = []
flync_random_50_30       = []
pulsar_random_50_30      = []
free_beacon_random_50_30 = []


find_cars_2_1        = []
flync_cars_2_1       = []
pulsar_cars_2_1      = []
free_beacon_cars_2_1 = []

find_cars_2_5        = []
flync_cars_2_5       = []
pulsar_cars_2_5      = []
free_beacon_cars_2_5 = []

find_cars_2_10        = []
flync_cars_2_10       = []
pulsar_cars_2_10      = []
free_beacon_cars_2_10 = []

find_cars_2_20        = []
flync_cars_2_20       = []
pulsar_cars_2_20      = []
free_beacon_cars_2_20 = []

find_cars_2_30        = []
flync_cars_2_30       = []
pulsar_cars_2_30      = []
free_beacon_cars_2_30 = []


find_cars_10_1        = []
flync_cars_10_1       = []
pulsar_cars_10_1      = []
free_beacon_cars_10_1 = []

find_cars_10_5        = []
flync_cars_10_5       = []
pulsar_cars_10_5      = []
free_beacon_cars_10_5 = []

find_cars_10_10        = []
flync_cars_10_10       = []
pulsar_cars_10_10      = []
free_beacon_cars_10_10 = []

find_cars_10_20        = []
flync_cars_10_20       = []
pulsar_cars_10_20      = []
free_beacon_cars_10_20 = []

find_cars_10_30        = []
flync_cars_10_30       = []
pulsar_cars_10_30      = []
free_beacon_cars_10_30 = []


find_cars_50_1        = []
flync_cars_50_1       = []
pulsar_cars_50_1      = []
free_beacon_cars_50_1 = []

find_cars_50_5        = []
flync_cars_50_5       = []
pulsar_cars_50_5      = []
free_beacon_cars_50_5 = []

find_cars_50_10        = []
flync_cars_50_10       = []
pulsar_cars_50_10      = []
free_beacon_cars_50_10 = []

find_cars_50_20        = []
flync_cars_50_20       = []
pulsar_cars_50_20      = []
free_beacon_cars_50_20 = []

find_cars_50_30        = []
flync_cars_50_30       = []
pulsar_cars_50_30      = []
free_beacon_cars_50_30 = []



find_jogging_2_1        = []
flync_jogging_2_1       = []
pulsar_jogging_2_1      = []
free_beacon_jogging_2_1 = []

find_jogging_2_5        = []
flync_jogging_2_5       = []
pulsar_jogging_2_5      = []
free_beacon_jogging_2_5 = []

find_jogging_2_10        = []
flync_jogging_2_10       = []
pulsar_jogging_2_10      = []
free_beacon_jogging_2_10 = []

find_jogging_2_20        = []
flync_jogging_2_20       = []
pulsar_jogging_2_20      = []
free_beacon_jogging_2_20 = []

find_jogging_2_30        = []
flync_jogging_2_30       = []
pulsar_jogging_2_30      = []
free_beacon_jogging_2_30 = []


find_jogging_10_1        = []
flync_jogging_10_1       = []
pulsar_jogging_10_1      = []
free_beacon_jogging_10_1 = []

find_jogging_10_5        = []
flync_jogging_10_5       = []
pulsar_jogging_10_5      = []
free_beacon_jogging_10_5 = []

find_jogging_10_10        = []
flync_jogging_10_10       = []
pulsar_jogging_10_10      = []
free_beacon_jogging_10_10 = []

find_jogging_10_20        = []
flync_jogging_10_20       = []
pulsar_jogging_10_20      = []
free_beacon_jogging_10_20 = []

find_jogging_10_30        = []
flync_jogging_10_30       = []
pulsar_jogging_10_30      = []
free_beacon_jogging_10_30 = []


find_jogging_50_1        = []
flync_jogging_50_1       = []
pulsar_jogging_50_1      = []
free_beacon_jogging_50_1 = []

find_jogging_50_5        = []
flync_jogging_50_5       = []
pulsar_jogging_50_5      = []
free_beacon_jogging_50_5 = []

find_jogging_50_10        = []
flync_jogging_50_10       = []
pulsar_jogging_50_10      = []
free_beacon_jogging_50_10 = []

find_jogging_50_20        = []
flync_jogging_50_20       = []
pulsar_jogging_50_20      = []
free_beacon_jogging_50_20 = []

find_jogging_50_30        = []
flync_jogging_50_30       = []
pulsar_jogging_50_30      = []
free_beacon_jogging_50_30 = []


find_office_2_1        = []
flync_office_2_1       = []
pulsar_office_2_1      = []
free_beacon_office_2_1 = []

find_office_2_5        = []
flync_office_2_5       = []
pulsar_office_2_5      = []
free_beacon_office_2_5 = []

find_office_2_10        = []
flync_office_2_10       = []
pulsar_office_2_10      = []
free_beacon_office_2_10 = []

find_office_2_20        = []
flync_office_2_20       = []
pulsar_office_2_20      = []
free_beacon_office_2_20 = []

find_office_2_30        = []
flync_office_2_30       = []
pulsar_office_2_30      = []
free_beacon_office_2_30 = []



find_office_10_1        = []
flync_office_10_1       = []
pulsar_office_10_1      = []
free_beacon_office_10_1 = []

find_office_10_5        = []
flync_office_10_5       = []
pulsar_office_10_5      = []
free_beacon_office_10_5 = []

find_office_10_10        = []
flync_office_10_10       = []
pulsar_office_10_10      = []
free_beacon_office_10_10 = []

find_office_10_20        = []
flync_office_10_20       = []
pulsar_office_10_20      = []
free_beacon_office_10_20 = []

find_office_10_30        = []
flync_office_10_30       = []
pulsar_office_10_30      = []
free_beacon_office_10_30 = []


find_office_50_1        = []
flync_office_50_1       = []
pulsar_office_50_1      = []
free_beacon_office_50_1 = []

find_office_50_5        = []
flync_office_50_5       = []
pulsar_office_50_5      = []
free_beacon_office_50_5 = []

find_office_50_10        = []
flync_office_50_10       = []
pulsar_office_50_10      = []
free_beacon_office_50_10 = []

find_office_50_20        = []
flync_office_50_20       = []
pulsar_office_50_20      = []
free_beacon_office_50_20 = []

find_office_50_30        = []
flync_office_50_30       = []
pulsar_office_50_30      = []
free_beacon_office_50_30 = []

find_stairs_2_1        = []
flync_stairs_2_1       = []
pulsar_stairs_2_1      = []
free_beacon_stairs_2_1 = []

find_stairs_2_5        = []
flync_stairs_2_5       = []
pulsar_stairs_2_5      = []
free_beacon_stairs_2_5 = []

find_stairs_2_10        = []
flync_stairs_2_10       = []
pulsar_stairs_2_10      = []
free_beacon_stairs_2_10 = []

find_stairs_2_20        = []
flync_stairs_2_20       = []
pulsar_stairs_2_20      = []
free_beacon_stairs_2_20 = []

find_stairs_2_30        = []
flync_stairs_2_30       = []
pulsar_stairs_2_30      = []
free_beacon_stairs_2_30 = []



find_stairs_10_1        = []
flync_stairs_10_1       = []
pulsar_stairs_10_1      = []
free_beacon_stairs_10_1 = []

find_stairs_10_5        = []
flync_stairs_10_5       = []
pulsar_stairs_10_5      = []
free_beacon_stairs_10_5 = []

find_stairs_10_10        = []
flync_stairs_10_10       = []
pulsar_stairs_10_10      = []
free_beacon_stairs_10_10 = []

find_stairs_10_20        = []
flync_stairs_10_20       = []
pulsar_stairs_10_20      = []
free_beacon_stairs_10_20 = []

find_stairs_10_30        = []
flync_stairs_10_30       = []
pulsar_stairs_10_30      = []
free_beacon_stairs_10_30 = []


find_stairs_50_1        = []
flync_stairs_50_1       = []
pulsar_stairs_50_1      = []
free_beacon_stairs_50_1 = []

find_stairs_50_5        = []
flync_stairs_50_5       = []
pulsar_stairs_50_5      = []
free_beacon_stairs_50_5 = []

find_stairs_50_10        = []
flync_stairs_50_10       = []
pulsar_stairs_50_10      = []
free_beacon_stairs_50_10 = []

find_stairs_50_20        = []
flync_stairs_50_20       = []
pulsar_stairs_50_20      = []
free_beacon_stairs_50_20 = []

find_stairs_50_30        = []
flync_stairs_50_30       = []
pulsar_stairs_50_30      = []
free_beacon_stairs_50_30 = []

find_washer_2_1        = []
flync_washer_2_1       = []
pulsar_washer_2_1      = []
free_beacon_washer_2_1 = []

find_washer_2_5        = []
flync_washer_2_5       = []
pulsar_washer_2_5      = []
free_beacon_washer_2_5 = []

find_washer_2_10        = []
flync_washer_2_10       = []
pulsar_washer_2_10      = []
free_beacon_washer_2_10 = []

find_washer_2_20        = []
flync_washer_2_20       = []
pulsar_washer_2_20      = []
free_beacon_washer_2_20 = []

find_washer_2_30        = []
flync_washer_2_30       = []
pulsar_washer_2_30      = []
free_beacon_washer_2_30 = []



find_washer_10_1        = []
flync_washer_10_1       = []
pulsar_washer_10_1      = []
free_beacon_washer_10_1 = []

find_washer_10_5        = []
flync_washer_10_5       = []
pulsar_washer_10_5      = []
free_beacon_washer_10_5 = []

find_washer_10_10        = []
flync_washer_10_10       = []
pulsar_washer_10_10      = []
free_beacon_washer_10_10 = []

find_washer_10_20        = []
flync_washer_10_20       = []
pulsar_washer_10_20      = []
free_beacon_washer_10_20 = []

find_washer_10_30        = []
flync_washer_10_30       = []
pulsar_washer_10_30      = []
free_beacon_washer_10_30 = []


find_washer_50_1        = []
flync_washer_50_1       = []
pulsar_washer_50_1      = []
free_beacon_washer_50_1 = []

find_washer_50_5        = []
flync_washer_50_5       = []
pulsar_washer_50_5      = []
free_beacon_washer_50_5 = []

find_washer_50_10        = []
flync_washer_50_10       = []
pulsar_washer_50_10      = []
free_beacon_washer_50_10 = []

find_washer_50_20        = []
flync_washer_50_20       = []
pulsar_washer_50_20      = []
free_beacon_washer_50_20 = []

find_washer_50_30        = []
flync_washer_50_30       = []
pulsar_washer_50_30      = []
free_beacon_washer_50_30 = []



fontSize  = 12

lineWidth = 1.5



data_sets = [
    
[[[find_static_2_1, find_static_10_1, find_static_50_1], 
  [flync_static_2_1, flync_static_10_1, flync_static_50_1], 
  [pulsar_static_2_1, pulsar_static_10_1, pulsar_static_50_1],             
  [free_beacon_static_2_1, free_beacon_static_10_1, free_beacon_static_50_1]], 

              
 [[find_random_2_1, find_random_10_1, find_random_50_1], 
  [flync_random_2_1, flync_random_10_1, flync_random_50_1], 
  [pulsar_random_2_1, pulsar_random_10_1, pulsar_random_50_1], 
  [free_beacon_random_2_1, free_beacon_random_10_1, free_beacon_random_50_1]], 


 [[find_cars_2_1, find_cars_10_1, find_cars_50_1], 
  [flync_cars_2_1, flync_cars_10_1, flync_cars_50_1], 
  [pulsar_cars_2_1, pulsar_cars_10_1, pulsar_cars_50_1], 
  [free_beacon_cars_2_1, free_beacon_cars_10_1, free_beacon_cars_50_1]],


 [[find_jogging_2_1, find_jogging_10_1, find_jogging_50_1], 
  [flync_jogging_2_1, flync_jogging_10_1, flync_jogging_50_1], 
  [pulsar_jogging_2_1, pulsar_jogging_10_1, pulsar_jogging_50_1], 
  [free_beacon_jogging_2_1, free_beacon_jogging_10_1, free_beacon_jogging_50_1]], 


 [[find_office_2_1, find_office_10_1, find_office_50_1],
   [flync_office_2_1, flync_office_10_1, flync_office_50_1],         
    [pulsar_office_2_1, pulsar_office_10_1, pulsar_office_50_1], 
    [free_beacon_office_2_1, free_beacon_office_10_1, free_beacon_office_50_1]], 


 [[find_stairs_2_1, find_stairs_10_1, find_stairs_50_1], 
  [flync_stairs_2_1, flync_stairs_10_1, flync_stairs_50_1], 
  [pulsar_stairs_2_1, pulsar_stairs_10_1, pulsar_stairs_50_1],
  [free_beacon_stairs_2_1, free_beacon_stairs_10_1, free_beacon_stairs_50_1]], 


 [[find_washer_2_1, find_washer_10_1, find_washer_50_1], 
  [flync_washer_2_1, flync_washer_10_1, flync_washer_50_1], 
  [pulsar_washer_2_1, pulsar_washer_10_1, pulsar_washer_50_1],
  [free_beacon_washer_2_1, free_beacon_washer_10_1, free_beacon_washer_50_1]]

],


[[[find_static_2_5, find_static_10_5, find_static_50_5], 
  [flync_static_2_5, flync_static_10_5, flync_static_50_5], 
  [pulsar_static_2_5, pulsar_static_10_5, pulsar_static_50_5],             
  [free_beacon_static_2_5, free_beacon_static_10_5, free_beacon_static_50_5]], 

              
 [[find_random_2_5, find_random_10_5, find_random_50_5], 
  [flync_random_2_5, flync_random_10_5, flync_random_50_5], 
  [pulsar_random_2_5, pulsar_random_10_5, pulsar_random_50_5], 
  [free_beacon_random_2_5, free_beacon_random_10_5, free_beacon_random_50_5]], 


 [[find_cars_2_5, find_cars_10_5, find_cars_50_5], 
  [flync_cars_2_5, flync_cars_10_5, flync_cars_50_5], 
  [pulsar_cars_2_5, pulsar_cars_10_5, pulsar_cars_50_5], 
  [free_beacon_cars_2_5, free_beacon_cars_10_5, free_beacon_cars_50_5]],


 [[find_jogging_2_5, find_jogging_10_5, find_jogging_50_5], 
  [flync_jogging_2_5, flync_jogging_10_5, flync_jogging_50_5], 
  [pulsar_jogging_2_5, pulsar_jogging_10_5, pulsar_jogging_50_5], 
  [free_beacon_jogging_2_5, free_beacon_jogging_10_5, free_beacon_jogging_50_5]], 


 [[find_office_2_5, find_office_10_5, find_office_50_5],
   [flync_office_2_5, flync_office_10_5, flync_office_50_5],         
    [pulsar_office_2_5, pulsar_office_10_5, pulsar_office_50_5], 
    [free_beacon_office_2_5, free_beacon_office_10_5, free_beacon_office_50_5]], 


 [[find_stairs_2_5, find_stairs_10_5, find_stairs_50_5], 
  [flync_stairs_2_5, flync_stairs_10_5, flync_stairs_50_5], 
  [pulsar_stairs_2_5, pulsar_stairs_10_5, pulsar_stairs_50_5],
  [free_beacon_stairs_2_5, free_beacon_stairs_10_5, free_beacon_stairs_50_5]], 


 [[find_washer_2_5, find_washer_10_5, find_washer_50_5], 
  [flync_washer_2_5, flync_washer_10_5, flync_washer_50_5], 
  [pulsar_washer_2_5, pulsar_washer_10_5, pulsar_washer_50_5],
  [free_beacon_washer_2_5, free_beacon_washer_10_5, free_beacon_washer_50_5]]

],


[[[find_static_2_10, find_static_10_10, find_static_50_10], 
  [flync_static_2_10, flync_static_10_10, flync_static_50_10], 
  [pulsar_static_2_10, pulsar_static_10_10, pulsar_static_50_10],             
  [free_beacon_static_2_10, free_beacon_static_10_10, free_beacon_static_50_10]], 

              
 [[find_random_2_10, find_random_10_10, find_random_50_10], 
  [flync_random_2_10, flync_random_10_10, flync_random_50_10], 
  [pulsar_random_2_10, pulsar_random_10_10, pulsar_random_50_10], 
  [free_beacon_random_2_10, free_beacon_random_10_10, free_beacon_random_50_10]], 


 [[find_cars_2_10, find_cars_10_10, find_cars_50_10], 
  [flync_cars_2_10, flync_cars_10_10, flync_cars_50_10], 
  [pulsar_cars_2_10, pulsar_cars_10_10, pulsar_cars_50_10], 
  [free_beacon_cars_2_10, free_beacon_cars_10_10, free_beacon_cars_50_10]],


 [[find_jogging_2_10, find_jogging_10_10, find_jogging_50_10], 
  [flync_jogging_2_10, flync_jogging_10_10, flync_jogging_50_10], 
  [pulsar_jogging_2_10, pulsar_jogging_10_10, pulsar_jogging_50_10], 
  [free_beacon_jogging_2_10, free_beacon_jogging_10_10, free_beacon_jogging_50_10]], 


 [[find_office_2_10, find_office_10_10, find_office_50_10],
   [flync_office_2_10, flync_office_10_10, flync_office_50_10],         
    [pulsar_office_2_10, pulsar_office_10_10, pulsar_office_50_10], 
    [free_beacon_office_2_10, free_beacon_office_10_10, free_beacon_office_50_10]], 


 [[find_stairs_2_10, find_stairs_10_10, find_stairs_50_10], 
  [flync_stairs_2_10, flync_stairs_10_10, flync_stairs_50_10], 
  [pulsar_stairs_2_10, pulsar_stairs_10_10, pulsar_stairs_50_10],
  [free_beacon_stairs_2_10, free_beacon_stairs_10_10, free_beacon_stairs_50_10]], 


 [[find_washer_2_10, find_washer_10_10, find_washer_50_10], 
  [flync_washer_2_10, flync_washer_10_10, flync_washer_50_10], 
  [pulsar_washer_2_10, pulsar_washer_10_10, pulsar_washer_50_10],
  [free_beacon_washer_2_10, free_beacon_washer_10_10, free_beacon_washer_50_10]]

],


[[[find_static_2_20, find_static_10_20, find_static_50_20], 
  [flync_static_2_20, flync_static_10_20, flync_static_50_20], 
  [pulsar_static_2_20, pulsar_static_10_20, pulsar_static_50_20],             
  [free_beacon_static_2_20, free_beacon_static_10_20, free_beacon_static_50_20]], 

              
 [[find_random_2_20, find_random_10_20, find_random_50_20], 
  [flync_random_2_20, flync_random_10_20, flync_random_50_20], 
  [pulsar_random_2_20, pulsar_random_10_20, pulsar_random_50_20], 
  [free_beacon_random_2_20, free_beacon_random_10_20, free_beacon_random_50_20]], 


 [[find_cars_2_20, find_cars_10_20, find_cars_50_20], 
  [flync_cars_2_20, flync_cars_10_20, flync_cars_50_20], 
  [pulsar_cars_2_20, pulsar_cars_10_20, pulsar_cars_50_20], 
  [free_beacon_cars_2_20, free_beacon_cars_10_20, free_beacon_cars_50_20]],


 [[find_jogging_2_20, find_jogging_10_20, find_jogging_50_20], 
  [flync_jogging_2_20, flync_jogging_10_20, flync_jogging_50_20], 
  [pulsar_jogging_2_20, pulsar_jogging_10_20, pulsar_jogging_50_20], 
  [free_beacon_jogging_2_20, free_beacon_jogging_10_20, free_beacon_jogging_50_20]], 


 [[find_office_2_20, find_office_10_20, find_office_50_20],
   [flync_office_2_20, flync_office_10_20, flync_office_50_20],         
    [pulsar_office_2_20, pulsar_office_10_20, pulsar_office_50_20], 
    [free_beacon_office_2_20, free_beacon_office_10_20, free_beacon_office_50_20]], 


 [[find_stairs_2_20, find_stairs_10_20, find_stairs_50_20], 
  [flync_stairs_2_20, flync_stairs_10_20, flync_stairs_50_20], 
  [pulsar_stairs_2_20, pulsar_stairs_10_20, pulsar_stairs_50_20],
  [free_beacon_stairs_2_20, free_beacon_stairs_10_20, free_beacon_stairs_50_20]], 


 [[find_washer_2_20, find_washer_10_20, find_washer_50_20], 
  [flync_washer_2_20, flync_washer_10_20, flync_washer_50_20], 
  [pulsar_washer_2_20, pulsar_washer_10_20, pulsar_washer_50_20],
  [free_beacon_washer_2_20, free_beacon_washer_10_20, free_beacon_washer_50_20]]

],



[[[find_static_2_30, find_static_10_30, find_static_50_30], 
  [flync_static_2_30, flync_static_10_30, flync_static_50_30], 
  [pulsar_static_2_30, pulsar_static_10_30, pulsar_static_50_30],             
  [free_beacon_static_2_30, free_beacon_static_10_30, free_beacon_static_50_30]], 

              
 [[find_random_2_30, find_random_10_30, find_random_50_30], 
  [flync_random_2_30, flync_random_10_30, flync_random_50_30], 
  [pulsar_random_2_30, pulsar_random_10_30, pulsar_random_50_30], 
  [free_beacon_random_2_30, free_beacon_random_10_30, free_beacon_random_50_30]], 


 [[find_cars_2_30, find_cars_10_30, find_cars_50_30], 
  [flync_cars_2_30, flync_cars_10_30, flync_cars_50_30], 
  [pulsar_cars_2_30, pulsar_cars_10_30, pulsar_cars_50_30], 
  [free_beacon_cars_2_30, free_beacon_cars_10_30, free_beacon_cars_50_30]],


 [[find_jogging_2_30, find_jogging_10_30, find_jogging_50_30], 
  [flync_jogging_2_30, flync_jogging_10_30, flync_jogging_50_30], 
  [pulsar_jogging_2_30, pulsar_jogging_10_30, pulsar_jogging_50_30], 
  [free_beacon_jogging_2_30, free_beacon_jogging_10_30, free_beacon_jogging_50_30]], 


 [[find_office_2_30, find_office_10_30, find_office_50_30],
   [flync_office_2_30, flync_office_10_30, flync_office_50_30],         
    [pulsar_office_2_30, pulsar_office_10_30, pulsar_office_50_30], 
    [free_beacon_office_2_30, free_beacon_office_10_30, free_beacon_office_50_30]], 


 [[find_stairs_2_30, find_stairs_10_30, find_stairs_50_30], 
  [flync_stairs_2_30, flync_stairs_10_30, flync_stairs_50_30], 
  [pulsar_stairs_2_30, pulsar_stairs_10_30, pulsar_stairs_50_30],
  [free_beacon_stairs_2_30, free_beacon_stairs_10_30, free_beacon_stairs_50_30]], 


 [[find_washer_2_30, find_washer_10_30, find_washer_50_30], 
  [flync_washer_2_30, flync_washer_10_30, flync_washer_50_30], 
  [pulsar_washer_2_30, pulsar_washer_10_30, pulsar_washer_50_30],
  [free_beacon_washer_2_30, free_beacon_washer_10_30, free_beacon_washer_50_30]]

]



    
]


# collect the data
pr_index = 0
for pr in poweroff_rate: 
    i = 0
    for scenario in energy_scenarios:
        j = 0
        for method in syn_methods:
            k = 0
            for num in node_sets:
                file = open("poweroff_"+str(num)+"_"+ method.lower()+"_syn_in_"+ scenario.upper()+"_"+ pr+".csv", mode='r')
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    data_sets[pr_index][i][j][k].append(int(row[0]))
                k += 1
            j += 1
        i += 1
    pr_index = pr_index + 1


pr_index = 0
for pr in poweroff_rate: 
    # plot the data
    fig, ax = plt.subplots(nrows=3, ncols=7, figsize=(21, 9))
    markers = ['o', 's', '^', 'v']
    lineStyles  = ['-', '--', '-.', ':']  

    scenarios_len = len(energy_scenarios_names)
    methods_len = len(syn_methods_name)
    nums_len = len(node_sets)  

    for i in range(nums_len):
        for j in range(scenarios_len):
            _ax = ax[i][j]
            for k in range(methods_len):
                dataSet = data_sets[pr_index][j][k][i]
                sorted_set = np.sort(dataSet)
                cdf = np.arange(1, len(sorted_set) + 1) / len(sorted_set)
                _ax.plot(sorted_set, cdf, marker=markers[k], color = colors[k], linestyle = lineStyles[k],
                     linewidth=1, markersize=1)

            if j == 0:
               _ax.set_ylabel("CDF", fontsize=fontSize)
            _ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
            _ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
            if (i == (nums_len -1)):
                _ax.set_xlabel(energy_scenarios_names[j])
            if (j == 3):
                _ax.set_title(node_sets_name[i]+" [nodes]")
            _ax.tick_params(axis='both', which='major', labelsize=fontSize)


    handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
    fig.legend(handles, syn_methods_name, loc='upper right')
    plt.tight_layout()
    fig.savefig(f""+title+"_"+ pr +"_simulation.pdf", format="pdf", bbox_inches='tight')
    pr_index = pr_index + 1













