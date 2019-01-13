# Author: Milo Dietrick

from pathlib import Path
import timeit
import math
import itertools
import random

# code for timer found at
# https://stackoverflow.com/questions/15707056/get-time-of-execution-of-a-block-of-code-in-python-2-7
# start_time = timeit.default_timer()
# print("K nearest time:" timeit.default_timer() - start_time)
def calculate_distance( l1, l2):
   return pow( pow((l1[0]-l2[0]), 2) + pow((l1[1] - l2[1]),2), .5 ) 


# #TESTING POINTS FROM INPUT FILE
# initial =[[0,0], [10,0], [0,5], [10,5]]


#GENERATE RANDOM POINTS
initial=[]
for i in range (16):
  a = [random.randint(1,11), random.randint(1,11)]
  initial.append(a)


c=initial.copy()
#NEAREST NEIGHBHOR HEURISTIC
best_order = [initial[0]]
total_distance = 0.0

print("\n order before nearest tsp: ", initial)

j=0
# length = len(b) -2
initial.pop(0)

start_time = timeit.default_timer()
while len(initial) > 0:
    #calculate the closest point
    dist = []    
    for i in initial:
        dist.append (calculate_distance( best_order[j], i)) #calculate distance     
    total_distance += min(dist)  
    best_order.append(initial[dist.index(min(dist))]) #find the point with the shortest distance   

    if len(initial) == 1: #if its the last iteration add the starting point to the end of the list
        total_distance += calculate_distance(best_order[0], initial[0])
        best_order.append(best_order[0])
    initial.pop(dist.index(min(dist)))
    j+=1 
end_time = timeit.default_timer() - start_time
print("\n K_nearest \n total distance", total_distance)
print("best order", best_order)
print("K nearest time:", end_time)


#EXHAUSTIVE
initial = c[0]
c.pop(0)
dist = []
y = []

start_time = timeit.default_timer()
for x in itertools.permutations(c,len(c)):
  total_distance = 0
  x=list(x)
  x.insert(0, initial)
  x.insert(len(x), initial)
  for i in range (len(x) - 1):
    distance = calculate_distance(x[i], x[i+1])
    total_distance += distance
  dist.append(total_distance)
  y.append(x)
end_time = timeit.default_timer() - start_time
print("\n Exhaustive approach")
print("Best order: ", y[dist.index(min(dist))])
print("Shortest dsitance",  min(dist))
print("Exhaustive time:", end_time)
  
    