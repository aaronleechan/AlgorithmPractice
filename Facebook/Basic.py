'''
Letter Case Permutation
'''
def letterCasePermutation(S):
    print( "Come in ");
    res = []
    indices = []
    #Step 1: Seperate indices with characters in them.
    indices = [i for i, _ in enumerate(S) if _.isalpha()]
    #step 2 Gelerate all subsets of the indices array of characters
    print({"=======> ": len(indices)})
    for i in range(0,pow(2,len(indices))):
        if i == 0:
            res.append(S)
        else:
            j = i; bpos = 0; nsl = list(S)
            # print(j,bpos,nsl)
            while j > 0:
                ci2c = indices[bpos]
                if j&1 and S[ci2c].islower():
                    nsl[ci2c] = S[ci2c].upper()
                elif j&1 and S[ci2c].isupper():
                    nsl[ci2c] = S[ci2c].lower()
                bpos+=1
                j = j >> 1
            res.append("".join(nsl))
    return res










def main():
    lettercasepermutationString1 = ''
    lettercasepermutationString2 = '1klo'
    print(letterCasePermutation(lettercasepermutationString2))

if __name__ == "__main__":
    main()