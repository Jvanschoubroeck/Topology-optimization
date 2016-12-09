import numpy as np

def binary_filter(array, average, lb=0, ub=1):
    """Filter values of an array to lower and upper values without trespassing the average.
    
    Parameters
    ----------
    array: numpy array
        Input array.
    average: float
        Upper bound for the average of the new array.
    lb: float, optional
        Lower boundary for values in return array.
    ub: float, optional
        Upper bounday for values in return array.
        
    Returns
    -------
    array: numpy array
        Array with values equal to lb and ub. The average of this array is equal or smaller to average.
        
    Notes
    -----
    Average must be below upper bound, otherwise filter makes no sense and all elements should
    just be equal to ub.
    
    Examples
    --------
    Examples should be written in doctest format, and should illustrate how
    to use the function.

    >>> x = np.array([[0.68, 0.24, 0.42], [0.49, 0.87, 0.79], [0.2, 0.2, 0.8]])
    >>> binary_filter(x, .6)
    array[[ 1.  0.  0.]
          [ 1.  1.  1.]
          [ 0.  0.  1.]]
          
    >>> binary_filter(x, .6, .2, .8)
    array[[ 0.8  0.2  0.2]
          [ 0.8  0.8  0.8]
          [ 0.2  0.2  0.8]]
    
    """
    
    try:
        number_of_elements = array.shape[0] * array.shape[1]
    except IndexError:
        number_of_elements = array.shape[0]
        
    minimum_array_value = np.min(array)
    
    for n, m in enumerate(reversed(np.sort(array.flatten()))):
        elements_above_m = np.where(array > m)[0].shape[0]
        new_array_average = ((elements_above_m * ub) + (number_of_elements - elements_above_m) * lb) / number_of_elements
        if new_array_average > average:
            minimum_array_value = np.sort(array.flatten())[-1 - (n - 1)]
            break
            
    new_array = array.copy()
    
    new_array[np.where(new_array > minimum_array_value)] = ub
    new_array[np.where(new_array != ub)] = lb
    
    return new_array

