'''
Binary Search
Best Time Complexity O(1)
Average Time Complexity O(log n)
Worst Time Complexity O(log n)
Worst Space Complexity O(1)
'''

pos = -1

def binarySearch(array,find):
    lower = 0
    upper = len(array)
    sortArray = sorted(array)
    print(sortArray)
    while lower <= upper:
        mid = (lower + upper) // 2
        if sortArray[mid] == find:
            globals()['pos'] = mid
            return True
        else:
            if(sortArray[mid] < find):
                lower = mid
            else:
                upper = mid
    return False


def main():
    array = [2,3,4,1,9,4,3]
    find = 1
    if binarySearch(array,find):
        print("Found at " , pos+1)
    else:
        print(" Not Found ")

if __name__ == "__main__":
    main()

