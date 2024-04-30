s = 'ABC'

def permutation(p, up):
    if not up:  # Base case: if there are no characters left to permute, print the permutation
        print(p)
        return

    ch = up[0]  # Choose the first character from the remaining characters
    for i in range(0, len(p)+1):
        first = p[0:i]  # Divide the remaining characters into two parts
        second = p[i:len(up)+1]
        permutation(first + ch + second, up[1:])  # Recursively generate permutations of the remaining characters

permutation('', s)



        
