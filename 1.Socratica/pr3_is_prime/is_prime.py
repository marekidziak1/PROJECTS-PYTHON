import time
import math
def is_prime_v1(n):
    '''Return True if the number is prime. Otherwise False'''
    t0=time.time()
    if n==1:
        return False
    for d in range(2,n): 
        if n%d==0:
           return False
    return True
t0=time.time()
for i in range(10000):
    is_prime_v1(i) 
t1=time.time()
print(t1-t0)

def is_prime_v2(n):
    '''Return True if number is prime. Otherwise False.
       PLUS max divisor is fixed as sqrt of number'''
    if n==1:
        return False
    max_divisor=math.floor(math.sqrt(n))
    for d in range(2,1+max_divisor):
        if n%d==0:
            return False;
    return True

t0=time.time()
for i in range(10000):
    is_prime_v2(i) 
t1=time.time()
print(t1-t0)

def is_prime_v3(n):
    '''Return True if number is prime. Otherwise False.
       PLUS max divisor is fixed as sqrt of number
       PLUS only odd numbers are checked'''
    if n==1:
        return False
    elif n==2:
        return True
    elif n>2 and n%2==0:
        return False
    max_divisor=math.floor(math.sqrt(n))
    for d in range(3,1+max_divisor,2):
        if n%d==0:
            return False;
    return True

t0=time.time()
for i in range(10000):
    is_prime_v3(i) 
t1=time.time()
print(t1-t0)