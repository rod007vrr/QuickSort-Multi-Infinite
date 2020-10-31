import math
import time
from generateArray import genArray

def firstSort(array, pivotnum):
    #Chooses pivots
    numPivots = pivotnum
    pivots = []
    for n in range(numPivots):
        pivots.append(array.pop())
    #Code from Geeks for geeks that orders pivots
    for i in range(len(pivots)): 
        key = pivots[i] 
        j = i-1
        while j >=0 and key < pivots[j]: 
                pivots[j+1] = pivots[j] 
                j -= 1
        pivots[j+1] = key
    #In-place moves pivots into array
    for n in range(len(pivots)):
        array.insert(n,[pivots[n]]) #adding in in reverse
    #Extra space for those over larger pivots
    array.insert(numPivots,[])
    #Sorts the array
    for n in range(len(array)-numPivots-1):
        temp = array.pop()
        for x in range(numPivots):
            if temp<array[x][0]:
                array[x].append(temp)
                break
        else:
            array[numPivots].append(temp)
    #Remove any empty arrays
    try: 
        array.remove([])
    except ValueError:
        pass


def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def sort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        sort(arr, low, pi-1) 
        sort(arr, pi+1, high) 

def quickSortMulti(array, pvt):
    firstSort(array, pvt)
    for n in array:
        sort(n, 0, len(n)-1)
    final = []
    
    def normalize(arr):
        for n in arr:
            if type(n) != list:
                final.append(n)
            else:
                normalize(n)
        return arr
    normalize([array])
    return final
