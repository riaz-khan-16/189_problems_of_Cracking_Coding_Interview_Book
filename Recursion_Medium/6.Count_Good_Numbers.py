
p = 1e9 + 7


def efficient_power(x,n):
      res = 1;    
      x = int(x % p) 
      if (x == 0): 
         return 0 
      while n > 0:
        #If y is odd, multiply x with result
        if (n & 1):
            res = int((res*x) % p)
        #we have did the odd step is it was odd, now do the even step
        n = n//2
        x = int((x*x) % p)
      return res

def f(n):
    count_of_4s = n/2
    count_of_5s = n - count_of_4s
    ans = int(efficient_power(count_of_5s,n) % p)  * int(efficient_power(count_of_4s ,n) % p)
    return ans

print(f(4) )   