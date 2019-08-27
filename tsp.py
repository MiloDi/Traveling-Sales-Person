# Author: Milo Dietrick
# Purpose: Nearest neighbhors and exhaustive approach for the traveling sales person problem

from pathlib import Path
import timeit
import math
import itertools
import random


def calculate_distance(point1, point2):
  """Caclulate the Euclidian distance between 2 points
  
  Arguments:
      point1 {List} -- Starting x permutations coordinate
      point2 {List} -- Ending x permutations coordinate
  
  Returns:
      [int] -- Distance between 2 points
  """
  return pow(pow((point1[0] - point2[0]), 2) + pow((point1[1] - point2[1]), 2), .5) 

def generate_random_points(numPoints, maxRange):
  """Generate random x, permutations coordinates
  
  Arguments:
      numPoints {int} -- Number of points to generate
      maxRange {int} -- Maximum range of the points
  
  Returns:
      List -- List containing lists of x, permutations coordinates
  """
  return [[random.randint(1, maxRange), random.randint(1, maxRange)] for i in range (numPoints)]

def nearest_neighbhor(points):
  """Finds the shortest route using the nearest neighbhors hueristic
  
  Arguments:
      points {List} -- List of points that must be visited
  """
  print("\nNearest neigbhor search \nOrder before search: ", points)
  counter=0
  best_order = [points[0]]
  points.pop(0)
  total_distance = 0.0
  start_time = timeit.default_timer()
  while len(points) > 0:
      dist = [(calculate_distance( best_order[counter], i)) for i in points]  
      total_distance += min(dist)   
      best_order.append(points[dist.index(min(dist))]) 
      #if its the last iteration add the starting point to the end of the list
      if len(points) == 1: 
          total_distance += calculate_distance(best_order[0], points[0])
          best_order.append(best_order[0])
      points.pop(dist.index(min(dist)))
      counter+=1
  #measure runtime    
  end_time = timeit.default_timer() - start_time
  print("Best order", best_order,"\nShortest distance", total_distance,"\nNearest Neighbhor time:", end_time)


def exhaustive_search(points):
  """Finds the shortest path using a exhaustive approach through each permutation
  
  Arguments:
      points {List} -- List of points that must be visited
  """
  initial = points[0]
  permutations = []
  print("\nExhaustive Search\nOrder before search: ", points)
  start_time = timeit.default_timer()
  for perm in itertools.permutations(points, len(points)):
    perm=list(perm)
    #ensure that the path goes back to the starting point
    perm.insert(0, initial)
    perm.insert(len(perm), initial)
    dist = [ calculate_distance(perm[i], perm[i+1]) for i in range (len(perm) - 1)]
    permutations.append(perm)
  #measure runtime
  end_time = timeit.default_timer() - start_time
  print("Best order: ", permutations[dist.index(min(dist))], "\nShortest distance",  min(dist), "\nExhaustive time:", end_time)\
    
  
if __name__ =='__main__':
  numPoints = input("How many points to run? ")
  maxRange = input("Maximum range of points: ")
  point_list = generate_random_points(int(numPoints), int(maxRange))
  
  nearest_neighbhor(point_list.copy())
  exhaustive_search(point_list.copy())
