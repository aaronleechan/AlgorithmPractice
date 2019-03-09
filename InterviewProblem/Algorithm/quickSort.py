'''
Quick Sort
Best Time Complexity O(n log n)
Average Time Complexity O(n log n)
Worst Time Complexity O(n^2)
Worst Space Complexity O(log n)
'''
def quickSort(array,lowIndex,highIndex):
    if ( (highIndex - lowIndex) > 0):
        p = partition(array,lowIndex,highIndex)
        quickSort(array,lowIndex,p-1)
        quickSort(array,p+1,highIndex)
#
#
def partition(array,lowIndex,highIndex):
    divider = lowIndex
    pivot = highIndex
    for i in range(lowIndex,highIndex):
        if (array[i] < array[pivot]):
            array[i],array[divider] = array[divider],array[i]
            divider += 1
    array[pivot], array[divider] = array[divider], array[pivot]
    return divider

def main():
    array = [2,3,1,9,5,4]
    quickSort(array,0,len(array)-1)
    print(array)


if __name__ ==  "__main__":
	main()