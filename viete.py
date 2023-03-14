import mpmath

prec = 100000
mpmath.mp.dps = (prec+5)

denom = mpmath.mpf(0)
num = mpmath.mpf(2)

pi = mpmath.mpf(1)

# cprecs = 1000
nrounds = int((prec+5)/0.58)

num = mpmath.power(num, nrounds+1)
pi = mpmath.fmul(pi,num)
for i in range(nrounds):
    denom = mpmath.fadd(denom,mpmath.mpf(2))
    denom = mpmath.sqrt(denom)
    # pi = mpmath.fmul(pi,num)
    pi = mpmath.fdiv(pi,denom)
    print('Completed %.2f%%'%(100*(i+1)/nrounds),end='\r')

print()

string = mpmath.nstr(pi,prec)

file = open('solution.txt','w')
file.write(string)
file.close()