import numpy as np

def calculate(list):
    #check that the list passed contains 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
        
    #convert the list to a 3x3 Numpy array
    array = np.array(list).reshape((3,3))    
    
    #calculate the mean along both axes and the flattened matrix
    mean = [np.mean(array, axis=0).tolist(),
            np.mean(array, axis=1).tolist(),
            np.mean(array).tolist()]
    
    #calculate the variance
    variance = [np.var(array, axis=0).tolist(),
                np.var(array, axis=1).tolist(),
                np.var(array).tolist()]
    
    #calculate the std deviation
    std_dev = [np.std(array, axis=0).tolist(),
               np.std(array, axis=1).tolist(),
               np.std(array).tolist()]
    
    #calculate the max
    maximum = [np.max(array, axis=0).tolist(),
               np.max(array, axis=1).tolist(),
               np.max(array).tolist()]
    
    #calculate the min
    minimum = [np.min(array, axis=0).tolist(),
               np.min(array, axis=1).tolist(),
               np.min(array).tolist()]
    
    #calculate the sum
    summation = [np.sum(array, axis=0).tolist(),
                 np.sum(array, axis=1).tolist(),
                 np.sum(array).tolist()]

    #create the dictionary for output
    calculations = {'mean': mean,
                    'variance': variance,
                    'standard deviation': std_dev,
                    'max': maximum,
                    'min': minimum,
                    'sum': summation}

    return calculations



list = (0,1,2,3,4,5,6,7)

print(calculate(list))