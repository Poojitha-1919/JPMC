import math
def prime(a):
  for i in range(math.sqrt(a)):
    if(a%i==0):
      return false
    else:
      return true
