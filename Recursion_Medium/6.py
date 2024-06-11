


p = 1e9 + 7
    

def power(x, y) :
      res = 1;    
      x = x % p
      if (x == 0):
          return 0

      while y > 0:
           
        # If y is odd, multiply x with result
        if (y & 1):
            res = (res*x) % p
        
        #we have did the odd step is it was odd, now do the even step
        y = y>>1; # // dividing y by 2, y>>1 is same as y/2
        x = (x*x) % p
      
      return res


