#General imports
import time
import math
from generateArray import genArray
#Sort immports
from qsInf import quickSortInfinite
from qsMulti import quickSortMulti
from qs import quickSort

class arrayTest:
    def __init__(self, numPoints, arraySize, arrayMax):
        self.numPoints = numPoints
        self.arraySize = arraySize
        self.arrayMax = arrayMax
        self.arrays = []
        for n in range(numPoints):
            self.arrays.append(genArray(self.arraySize, self.arrayMax))
        print(f"Generated arrays for array size: {arraySize}")
    def testArray(self, sort):
        arraysDupe = []
        for copy in self.arrays:
            arraysDupe.append(copy.copy())
        self.times = []
        if sort == 0:
            self.sortUsed = "QuickSort"
            for indivArray in arraysDupe:
                tStart = time.perf_counter()
                quickSort(indivArray)
                tEnd = time.perf_counter()
                self.times.append(tEnd-tStart)
        elif sort == 1:
            self.sortUsed = "QuickSortMulti - 10"
            for indivArray in arraysDupe:
                tStart = time.perf_counter()
                quickSortMulti(indivArray, 10)
                tEnd = time.perf_counter()
                self.times.append(tEnd-tStart)
        elif sort == 2:
            self.sortUsed = "QuickSortMulti - root length"
            for indivArray in arraysDupe:
                tStart = time.perf_counter()
                quickSortMulti(indivArray, round(math.sqrt(self.arraySize)))
                tEnd = time.perf_counter()
                self.times.append(tEnd-tStart)
        elif sort == 3:
            self.sortUsed = "QuickSortInfinite"
            for indivArray in arraysDupe:
                tStart = time.perf_counter()
                quickSortInfinite(indivArray)
                tEnd = time.perf_counter()
                self.times.append(tEnd-tStart)
        elif sort == 4:
            self.sortUsed = "Timsort"
            for indivArray in arraysDupe:
                tStart = time.perf_counter()
                indivArray.sort()
                tEnd = time.perf_counter()
                self.times.append(tEnd-tStart)
        print(f"   Sorted arrays for: {self.sortUsed}")
        
