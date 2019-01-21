# Author: Milo Dietrick

from pathlib import Path
import numpy

input_file = str( Path.cwd() / 'tsp_input.txt')
with open (input_file, "r") as f:
  data=f.read().split()

num_nodes = data[0]
data.pop(0)
print("The number of nodes is:", num_nodes)

b=[]
i=0
while i < len(data)-1:
    a=[int(data[i]), int(data[i+1])]
    b.append(numpy.array(a))
    i += 2  
c = numpy.array(b)

#psuedocode from book
# p_0 = initial point
# i = 0
# while there are still unvisited points:
#     i = i+1
#     select p_i to be the closest unvisited point to p_i-1
#     visit p_i
#     return to P_0 from P_n-1


initial = c[0]
best_order = c[0]
print(best_order)
total_distance = 0.0
print(c)
while len(c) > 1:
    numpy.append(best_order, c[0])

    #calculate the closest point
    dist = []
    for i in range(1, len(c)):
        dist.append( numpy.linalg.norm(initial-c[i]) )
    shortest_dist = min(dist)
    total_distance += shortest_dist

    #put the point with the shortest distance into best_order

    print(shortest_dist)
    c = numpy.delete(c,(0),axis = 0)
print(best_order)