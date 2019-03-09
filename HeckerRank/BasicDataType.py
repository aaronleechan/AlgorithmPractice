'''
 lexicographic increasing order
'''

def lexicographicOrder(array):

    x = array[0]
    y = array[1]
    z = array[2]
    n = array[3]
    array1 = []
    array2 = []
    array3 = []
    result1 = []
    finalResult = []

    for i in range (x+1):
        array1.append(i)

    for j in range (y+1):
        array2.append(j)

    for k in range (z+1):
        array3.append(k)

    for x in array1:
        for y in array2:
            for z in array3:
                if(x+y+z) != n:
                    result1 = [];
                    result1.append(x)
                    result1.append(y)
                    result1.append(z)
                    finalResult.append(result1)

    print(finalResult)

"Soution lexicographicOrder"
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())
    # print([ [a,b,c]
    #     for a in range(x+1)
    #     for b in range(y+1)
    #     for c in range(z+1)
    #     if a+b+c != n
    #  ])

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     for i in arr:
#         print(i)
#
#     listnew=[]
#     for i in arr:
#          if i not in listnew:
#             listnew.append(i)
#
#     listnew.sort(reverse=True)
#     print(listnew[1])


# if __name__ == '__main__':
#     marksheet = []
#     s = set()
#     result = []
#     for _ in range(0, int(input())):
#         marksheet.append([input(), float(input())])
#
#     for key, value in marksheet:
#         s.add(value)
#
#     sortedArray = sorted(s)
#
#     for key, value in marksheet:
#         if value == sortedArray[1]:
#             result.append(key)
#
#     for a in sorted(result):
#         print(a)



def main():
    lexicographicOrdertest = [1,1,1,2]
    lexicographicOrder(lexicographicOrdertest)

if __name__ == "__main__":
    main()
