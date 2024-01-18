# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
# Hints:#92, #110


o='abbbcccccccccdddffffffffffffffffff'
com=''
i=0
count=1
while i<len(o)-1:
    cur=o[i]
    next=o[i+1]
    if cur==next:
        count=count+1
        i=i+1
    else:
        com=com+cur+str(count)
        i=i+1
        count=1
com=com+cur+str(count)



print(com)


