import numpy as np
from sklearn.datasets import make_moons


X,y = make_moons(n_samples = 200, noise = 0.05, random_state = 0)

def my_dbscan(data, eps, r):
    
    c = 0
    num_samples, num_features = np.shape(data)
    point_type = []
    clusterAssignment = []
    points_in_eps = []
    visited = []
  
    for point in X:
        
        result = type_point(point, data, eps, r)
        point_type.append(result["type"])
        points_in_eps.append(result["points_in_eps"])
    
        if point in visited:
            
            continue
        
        else: 
        
            visited.append(point) 
        
            if result["type"] == 1:
                
                c += 1
                
                #
                #
                #
                
                   
                    
            else:
            
                continue    
            
    return({"cluster":clusterAssignment, "type":point_type})
  
#
# a function that determines whether the specified point is 
# a core point, a non-core point, or noise
#
def type_point(point, all_points, eps, r):
    
    m,n = np.shape(all_points)
    points = []
    
    count = 0
    for i in range(m):
        
        if( np.linalg.norm(all_points[i,:] - point, ord = 2) <= eps ):
            
            count += 1
            points.append(i)
            
    if count >= r:
        
        core = 1
        
    else:
        
        core = -1
    
    return( {"type":core, "points_in_eps":points} )


# main
results = python_dbscan(X, 0.2, 5)
