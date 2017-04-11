import numpy as np
from sklearn.datasets import make_moons

# create half moons
# play around with the parameters and see what happens!
X,y = make_moons(n_samples = 200, noise = 0.05, random_state = 0)

#
# param: data is an array of data
# param: eps is the radius of our ball
# param: r is the number of points that make a cluster
#
# return: the cluster assignments
#
def my_dbscan(data, eps, r):
    
    # intialize cluster number
    c = 0
    # determine dimensions .. not sure you need this though
    num_samples, num_features = np.shape(data)
    # intialize lists for point type, clusters, neighboring points of core points
    # and whether a point has been visited
    point_type = []
    clusterAssignment = []
    points_in_eps = []
    visited = []
  
    for point in data:
        
        # create a function that returns whether a point
        # is a core point or a noise point
        # and save the info in the variable result
        result = 
        point_type.append(result["type"])
        points_in_eps.append(result["points_in_eps"])
    
    	# check if the current point has been visited
      	# if so, move on
        if point in visited:
            
            continue
        
        # if not,
        else: 
        
        	# mark as visited
            visited.append(point) 
        
        	#             
                   
                    
             
            
    return({"cluster":clusterAssignment, "type":point_type})
  
  
  
#
# a function that determines whether the specified point is 
# a core point, a non-core point, or noise
#
# param: point is the current point
# param: all_points is the data
# param: eps is the radius of your  ball
# param: r is the number of points that make a core point
#
# return: the point type
# return: a list of the points within eps
#
def type_point(point, all_points, eps, r):
    
    m,n = np.shape(all_points)
    points = []
    
    count = 0
    for i in range(m):
        
        # determine whether something is a core point here
            
    return( {"type":core, "points_in_eps":points} )


# main
results = python_dbscan(X, 0.2, 5)
