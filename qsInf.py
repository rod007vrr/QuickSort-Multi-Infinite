import math
import time
from generateArray import genArray

def inSort(array, pivots):
    #Chooses pivots
    numPivots = int(math.sqrt(len(array)))
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

def sort(array):
    for n in range(len(array)):
        if type(array[n]) != list or len(array[n]) <=1:
            pass #stops and goes to the next
        elif len(array[n]) == 2:
            if array[n][0]>array[n][1]:
                array[n][0], array[n][1] = array[n][1], array[n][0] #also stops and goes to the next
        else:
            inSort(array[n])
            sort(array[n])
    return array

def quickSortInfinite(array):
    sort([array])
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
