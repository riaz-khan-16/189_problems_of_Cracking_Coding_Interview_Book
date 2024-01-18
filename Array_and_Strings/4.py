# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. 
#                          A palindrome is a word or phrase that is the same forwards and backwards. A 
#                          permutation
#                          is a rearrangement of letters. The palindrome does not need to be limited to 
#                          just dictionary words.

#                         EXAMPLE
#                         Input: Tact Coa
#                         Output: True (permutations: "taco cat", "atco eta", etc.)


s='abcabc'


# check the length
def lenthEven(s):
    if len(s)%2==0:
        return True
    else:
        return False


# find set
def findset(s):
    u=[]
    for i in s:
        if i not in u:
            u.append(i)
    return u

u=findset(s)

#find counts
def findcount(s,u):
    counts=[]
    for i in u:
        counts.append(s.count(i))
    return counts   


counts=findcount(s,u)


def isalldouble(counts):
    for i in counts:
        if i%2==1:
            return False

    return True

def isOneCentre(counts):
    centre=0
    for i in counts:
        if i==1:
            centre=centre+1
    if centre>1:
        return False
    else:
        return True        




if lenthEven(s):
    print(isalldouble(counts))
else:
    print(isOneCentre(counts))


