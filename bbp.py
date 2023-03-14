import mpmath

prec = 1000000
mpmath.mp.dps = (prec+1)

pi = mpmath.mpf(0)

# cprecs = 1000
nrounds = int((prec)/1.2)
# nrounds = 1000

for i in range(nrounds):
    k8 = mpmath.fmul(8,i)
    t1 = mpmath.fdiv(4,mpmath.fadd(k8,1))
    t1 = mpmath.fadd(t1,mpmath.fdiv(-2,mpmath.fadd(k8,4)))
    t1 = mpmath.fadd(t1,mpmath.fdiv(-1,mpmath.fadd(k8,5)))
    t1 = mpmath.fadd(t1,mpmath.fdiv(-1,mpmath.fadd(k8,6)))
    t1 = mpmath.fdiv(t1,mpmath.power(16,i))

    pi = mpmath.fadd(pi,t1)
    print('Completed %.2f%%'%(100*(i+1)/nrounds),end='\r')

print()

string = mpmath.nstr(pi,prec+1)

file = open('solution.txt','w')
file.write(string)
file.close()