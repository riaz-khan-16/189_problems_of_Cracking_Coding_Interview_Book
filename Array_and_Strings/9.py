#Sring rotation

# String Rotation:Assumeyou have a method isSubstringwhich checks if oneword is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat")

new='abcd'
ori='cadb'


def main(ori,new):

      if len(new)!=len(ori):
            return False
      
      dummy=new
      for i in range(len(new)):
           last=dummy[-1]
           dummy=last+dummy
           dummy=dummy[0:len(new)]
           if ori==dummy:
                 return True
      return False     

         
      

print(main(ori,new))