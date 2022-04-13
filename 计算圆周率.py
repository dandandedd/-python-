import random
s = 1e6
n = 0
for i in range(int(s)):
     
   a = random.random()
   b = random.random()
   r = (a-0.5)**2 + (b-0.5)**2
   if r <=0.5**2:
    n = n + 1
   else :
    pass
pai = (n * 4)/s
print(pai)