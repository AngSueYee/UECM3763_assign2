import pylab as p
import numpy as np

# Setup parameters
mu = 0.1
sigma = 0.26
S0 = 39
n_path = 1000
n = n_partitions = 1000
period= 3

# Find theoretical expectation and variance

T_Exp = S0 * p.exp(mu*period)
T_Var = (S0**2)*(np.exp(2*mu*period))*(np.exp(sigma*sigma*period)-1)
print('  ')
print('The theoretical expectation and variance:')
print('E(S(3)) = ' + str(T_Exp))
print('Var(S(3)) = ' + str(T_Var))

# Create Brownian paths
t = p.linspace(0,3,n+1)
dB = p.randn(n_path, n+1) / p.sqrt(n/period)
dB[:,0] = 0
B = dB.cumsum(axis=1)

# Calculate stock prices
nu = mu - sigma*sigma/2.0
S = p.zeros_like(B)
S[:,0] = S0
S[:,1:] = S0*p.exp(nu*t[1:]+sigma*B[:,1:])

# Plot 5 realization of GBM

S5= S[0:5]
p.plot(t,S5.transpose())
p.xlabel('Time,$t$')
p.ylabel('Stock prices,$S_t$')
p.title('5 realizations of the GBM with $\mu$ = 0.1 and $\sigma$ = 0.26\n')
p.show()

# Expectation value of S(3)
S3 = p.array(S[:,-1])
print ('Expectation value of S(3) =', np.mean(S3))

# Variance of S(3)
print ('Variance of S(3) =',np.var(S3))

# Find P[S(3)>39]
a = S3>39.0
b= sum(a)/len(a)
print ('P[S(3)>39]=',b)

# Find E[S(3)|S(3)>39]
c = S3*a
d = sum(c)/sum(a)
print ('E[S(3)|S(3)>39]=',d)