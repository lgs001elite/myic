import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import csv




syn_methods = ["Find", "Flync", "Pulsar", "Free_beacon"]

syn_legend_names = ["Find", "Flync_Find", "Pulsar", "FreeBeacon", "Medians", "Means"]

node_sets = [2, 10, 50]
node_sets_name = ["2", "10", "50"]

#poweroff_rate = ["1", "5", "10", "20", "30"]
poweroff_rate = ["1", "10", "20"]

energy_scenarios = ["Static_trace", "Complex_trace", "Cars_trace", "Jogging_trace", "Office_trace", "Stairs_trace", "Washer_trace"]
energy_scenarios_names = ["Static trace", "Random trace", "Cars trace", "Jogging trace", "Office trace", "Stairs trace", "Washer trace"]

title ="box_free_beacon_poweroff_rate_"
colors = ['steelblue', 'darkorange', 'forestgreen', 'firebrick', "purple", "tomato"]
styles = ['-', '-', '-', '-', '--', '--']
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



fontSize  = 16

lineWidth = 1.5

plt.rcParams.update({'font.size': 16})


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

# plot the data
fig, ax = plt.subplots(nrows=3, ncols=7, figsize=(21, 9))
markers = ['o', 's', '^', 'v']
lineStyles  = ['-', '--', '-.', ':']  
pr_index = 0
for pr in poweroff_rate: 
    scenarios_len = len(energy_scenarios_names)
    methods_len = len(syn_methods)
    nums_len = len(node_sets)  
    for i in range(1):
        for j in range(scenarios_len):
            _ax = ax[pr_index][j]
            # Initialize lists to store medians and means
            all_medians = []
            all_means = []
            for k in range(methods_len):
                boxplot = _ax.boxplot(data_sets[pr_index][j][k][2], positions= [k + 2 * (methods_len + 1) + 1], patch_artist=True, 
                    boxprops=dict(facecolor=colors[k], color=colors[k], edgecolor=colors[k]),
                    whiskerprops=dict(color=colors[k], linewidth=lineWidth),
                    capprops=dict(color=colors[k], linewidth=lineWidth),
                    medianprops=dict(color=colors[k], linewidth=lineWidth),
                    flierprops=dict(marker='o', markerfacecolor=colors[k], markeredgecolor=colors[k], markersize=lineWidth, alpha=0.5),
                    showmeans=True)
                # Extract median and mean for this box plot
                median = boxplot['medians'][0].get_ydata()[0]
                mean = boxplot['means'][0].get_ydata()[0]
                # Store medians and means
                all_medians.append((k + 2 * (methods_len + 1) + 1, median))
                all_means.append((k + 2 * (methods_len + 1) + 1, mean))
            print("ave:"+str(np.mean(data_sets[pr_index][j][3][2])))
            # Unpack medians and means into x and y coordinates
            median_x, median_y = zip(*all_medians)
            mean_x, mean_y = zip(*all_means)

            # Connect medians and means with lines
            _ax.plot(median_x, median_y, color=colors[4], linestyle='--', linewidth=2, marker='o')
            _ax.plot(mean_x, mean_y, color=colors[5], linestyle='--', linewidth=2, marker='o')

            # Annotate difference
            # Calculate differences and annotate them on the plot
            for u in range(3):
                diff = mean_y[u] / mean_y[3]
                _ax.annotate(f'{diff:.2f}X', xy=(mean_x[u], mean_y[u]), xytext=(mean_x[u], max(mean_y[u], max(data_sets[pr_index][j][u][i])) + mean_y[u]),
                    ha='center', va='top', arrowprops=dict(facecolor='black', arrowstyle='->'),
                bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='yellow', alpha=0.8))
            # Set y_labels
            if j == 0:
                _ax.set_ylabel("Latency (Time Slots)", fontsize=fontSize)
            _ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
            _ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
            _ax.set_yscale('log')
            if (j == 3):
                _ax.set_title("#"+poweroff_rate[pr_index]+"% poweroff rate")
            _ax.set_xticks([])
            _ax.tick_params(axis='both', which='major', labelsize=fontSize)
            if pr == '20':
                _ax.set_xlabel(energy_scenarios_names[j], fontsize=fontSize)
            if (pr_index == 0) and (j == (scenarios_len -1)):
               handles = [plt.Line2D([0], [0], color=color, lw=lineWidth, ls=style ) for color, style in zip(colors, styles)]
               _ax.legend(handles, syn_legend_names, loc='lower right')
    pr_index = pr_index + 1
    fig.savefig(f"poweroff_simulation.pdf", format="pdf", bbox_inches='tight')















