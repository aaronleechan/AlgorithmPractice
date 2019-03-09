def rearrange(st):
    word = list(st)
    number = 0
    arrayString = []

    for i in word:
        if i.isdigit():
            number = number + int(i)
        else:
            arrayString.append(i)
    # arrayString.append(number)
    arrayString = sorted(arrayString)
    number = str(number)
    arrayString.append(str(number))
    print(arrayString)
    print(''.join(arrayString))
    # arrayString.append(number)
    # print(arrayString)






def main():
    str = "AC2BEW3"
    rearrange(str)


if __name__ ==  "__main__":
	main()