# 1. Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
#                cannot use additional data structures?









#Let the string is:
s='abcdefghb'





#With additional data structures
def isUnique(s):
        stack=[]                     #Take a stack
        for i in s:
            if i in stack:           #take each element and check weather  it is in the stack or not
                return False
            stack.append(i)
        return True    


#with out additional datastructures

def isUnique1(s):
     for i in s:
         
          if s.count(i)>1:
               return False
     return True

print(isUnique1(s))      







