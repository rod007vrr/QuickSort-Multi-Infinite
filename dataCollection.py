from testStructure import arrayTest
import openpyxl
#0 = qs
#1 = qsMulti - 10
#2 = qsMulti - root length
#3 = qsInf
#4 = timsort

wb = openpyxl.load_workbook("Sort_Data.xlsx")




for size in range(1, 9):

    test = arrayTest(10,10**size,10**(size+1))

    for sort in range(5):
        test.testArray(sort)
        for trial in range(len(test.times)):
            wb[test.sortUsed].cell(size+2, trial+2+0).value = test.times[trial]



wb.save("Sort_Data.xlsx")