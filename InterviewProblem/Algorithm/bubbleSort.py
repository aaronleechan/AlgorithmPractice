'''
Bubble Sort
Best Time Complexity O(n)
Average Time Complexity O(n^2)
Worst Time Complexity O(n^2)
Worst Space O(1)
'''

def bubbleSort(array):
    for i in range (0,len(array)-1):
        for j in range(0,len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    return array

def main():
    array = [1,4,5,2,9,3]
    result = bubbleSort(array)
    print(result)


if __name__ == "__main__":
    main()