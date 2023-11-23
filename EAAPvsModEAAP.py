import random
import math
import sys
from easygui import passwordbox
import matplotlib.pyplot as plt
import numpy as np
import time
from mpmath import mp

mp.dps = 10000


#---------------------------------------------Helper Functions--------------------------------------------------------

# PRIMITIVE ROOT CALCULATOR

from math import sqrt

# Returns True if n is prime
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to find primitive roots of n
def findPrimitive(n):
    if not isPrime(n):
        return -1

    phi = n - 1
    prime_factors = set()
    findPrimeFactors(prime_factors, phi)

    primitive_roots = []
    for r in range(2, phi + 1):
        is_primitive = True
        for it in prime_factors:
            if power(r, phi // it, n) == 1:
                is_primitive = False
                break
        if is_primitive:
            primitive_roots.append(r)
            if len(primitive_roots) == 2:
                break

    return primitive_roots

# Utility function to store prime factors of a number
def findPrimeFactors(s, n):
    while n % 2 == 0:
        s.add(2)
        n //= 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            s.add(i)
            n //= i
    if n > 2:
        s.add(n)

# Iterative Function to calculate (x^n)%p in O(log y)
def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y >>= 1
        x = (x * x) % p
    return res


#---------------------------------------------------------------------------------------------------------------------

# INVERSE MODULUS CALCULATOR

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        sys.exit("Inverse Doesn't Exist for the Random Variables taken. Please Try Again.")
        return None
    else:
        return x % m if x >= 0 else x % m + m


# Lists to store elapsed times
elapsed_times_code1 = []
elapsed_times_code2 = []

# Number of runs
num_runs = 10  

for _ in range(num_runs):
    
#--------------------------------------------------------AUTH 1-------------------------------------------------------
    user_input = input("\nEnter a Prime Number or type 'exit' to end: ")
    if user_input.lower() == 'exit':
        print("Thank you for your time 👋")
        break

    try:
        q = int(user_input)          
    except ValueError:
        sys.exit("Invalid input. Please enter an integer or type 'exit'.")

    if q < 5:
        sys.exit("Please Enter a Prime Number Greater than 3.")
    if not isPrime(q):
        sys.exit("Not a Prime Number")

    primitive_roots = findPrimitive(q)

    if len(primitive_roots) < 2:
        result = f"No second primitive root found for {q}."
    else:
        result = [primitive_roots[0], primitive_roots[1]]

    start_code1 = time.time()

    g1= result[0]
    g2= result[1]
    a= random.randint(1,q-1)
    b= random.randint(1,q-1)
    n_i= random.randint(1,q-1)
    A1= mp.mpf(g1**a)
    B1= g1**b
    Vi= random.randint(1,q-1)
    Mu= random.randint(1,q-1)
    k1= random.randint(1,q-1)
    k1= random.randint(1,q-1)
    k2= random.randint(1,q-1)
    temp= (Vi+a+b)%q
    while temp==0:
        a= random.randint(1,q-1)
        b= random.randint(1,q-1)
        Vi= random.randint(1, q-1)
        temp= (Vi+a+b)%q
    
    DID_ui= mp.power(g1, (n_i+a))
    if mp.log(DID_ui, g1)>=q:
        DID_ui= mp.power(g1, ((mp.log(DID_ui, g1))%q))
    

    inverse_mod= mod_inverse(temp, q)
    Ti= mp.power(g1, (inverse_mod))
    Ei= mp.power(g1, (q-n_i))

    Rk= random.randint(1, q-1)
    Yk= g2**Rk

    Gamma_u= mp.power(B1,Mu)
    if mp.log(Gamma_u, g1)>=q:
        Gamma_u= mp.power(g1,((mp.log(Gamma_u, g1))%q))
    Gamma_v= (Ti*(A1**Mu))
    if mp.log(Gamma_v, g1)>=q:
        Gamma_v= mp.power(g1, ((mp.log(Gamma_v, g1))%q))

    Lambda= (Mu+Rk)%q

    
    Lambda1= mp.power(Gamma_u,(Mu+k1))
    if mp.log(Lambda1, g1)>=q:
        Lambda1= mp.power(g1,((mp.log(Lambda1, g1))%q))

    Lambda2temp1= mp.log(mp.power(mp.mpf(Gamma_u), (Mu+k1)), g1)
    Lambda2temp2= mp.log(mp.power(mp.mpf(Gamma_v), (Mu+k2)), g1)
    Lambda2= mp.power(g1, ((Lambda2temp1-Lambda2temp2)%q))


    Delta1= (Rk-k1)%q
    Delta2= (Rk-k2)%q
    Ni= Ei*DID_ui
    if mp.log(Ni, g1)>=q:
        Ni= mp.power(g1, ((mp.log(Ni, g1))%q))

    #sig= mp.power(g1, (1/(Rk+H_m)))


    Lambda1_temp1= mp.log(mp.power(mp.mpf(Gamma_u), Lambda), g1)
    Lambda1_temp2= mp.log(mp.power(mp.mpf(Gamma_u), Delta1), g1)
    Lambda1_= mp.power(g1, ((Lambda1_temp1-Lambda1_temp2)%q))

    Lambda2_temp1_= mp.log(mp.power(mp.mpf(Gamma_u), Lambda)*mp.power(mp.mpf(Gamma_v), Delta2), g1)
    Lambda2_temp2_= mp.log(mp.power(mp.mpf(Gamma_u), Delta1)*mp.power(mp.mpf(Gamma_v), Lambda), g1)

    Lambda2_= mp.power(g1, ((Lambda2_temp1_-Lambda2_temp2_)%q))
    Ri= random.randint(1, q-1)
    Li= mp.power(B1, Ri)
    Omega= random.randint(1, q-1)
    Phi_1= random.randint(1, q-1)
    Phi_2= random.randint(1, q-1)
    
    Theta_u= mp.power(A1, Phi_1)*mp.power(g1, Omega)
    if mp.log(Theta_u, g1)>=q:
        Theta_u= mp.power(g1, ((mp.log(Theta_u, g1))%q))

    Theta_v= Li*mp.power(A1, Phi_2)
    if mp.log(Theta_v, g1)>=q:
        Theta_v= mp.power(g1, ((mp.log(Theta_v, g1))%q))

    h= (Omega+Phi_1)%q

    
    h1= mp.power(Theta_v, (Phi_1+Phi_2))
    if mp.log(h1, g1)>=q:
        h1= mp.power(g1, ((mp.log(h1, g1))%q))

    h2temp= mp.log(mp.power(mp.mpf(Theta_v), (Phi_2-Phi_1)), g1)
    h2= mp.power(mp.mpf(Theta_u), Phi_1)*mp.power(g1, (h2temp%q))
    if mp.log(h2, g1)>=q:
        h2= mp.power(g1, ((mp.log(h2, g1))%q))        

    H_alpha_temp1= mp.log(mp.power(mp.mpf(Theta_v), h), g1)
    H_alpha_temp2= mp.log(mp.power(mp.mpf(Theta_v), Omega), g1)
    H_alpha= mp.power(g1, (H_alpha_temp1-H_alpha_temp2)%q)

    H_beta= mp.power(Theta_v, Phi_2)
    if mp.log(H_beta, g1)>=q:
        H_beta= mp.power(g1, ((mp.log(H_beta, g1))%q))

    H_gamma= mp.power(Theta_u, Phi_1)
    if mp.log(H_gamma, g1)>=q:
        H_gamma= mp.power(g1, ((mp.log(H_gamma, g1))%q))

    H1_= H_alpha*H_beta
    if mp.log(H1_, g1)>=q:
        H1_= mp.power(g1, ((mp.log(H1_, g1))%q))

    H2_temp1= mp.log((H_beta*H_gamma), g1)
    H2_temp2= mp.log(H_alpha, g1)

    H2_= mp.power(g1, ((H2_temp1-H2_temp2)%q))

    end_code1 = time.time()
    elapsed_code1 = end_code1 - start_code1
    elapsed_times_code1.append(elapsed_code1)

#------------------------------------------------------AUTH 2---------------------------------------------------------
    start_code2 = time.time()
  
    g1= result[0]
    g2= result[1]
    a= random.randint(1,q-1)
    b= random.randint(1,q-1)
    n_i= random.randint(1,q-1)
    Vi= random.randint(1,q-1)
    alpha= random.randint(1,q-1)
    beta= random.randint(1,q-1)
    gamma= random.randint(1,q-1)
    k1= random.randint(1,q-1)
    k2= random.randint(1,q-1)
    Ri= random.randint(1, q-1)
    
    inv= (n_i+a)%q
    inv2= (Ri+a)%q
    while (inv==0 or inv2==0):
        a= random.randint(1,q-1)
        n_i= random.randint(1,q-1)
        Ri= random.randint(1, q-1)
        inv= (n_i+a)%q
        inv2= (Ri+a)%q
        
        
    A1= mp.power(g1, (a+b))
    if mp.log(A1, g1)>=q:
        A1= mp.power(g1, (mp.log(A1, g1))%q)

    B1= mp.power(g1, b)
    #print(n_i, a)
    DID_ui= mp.power(g1, mod_inverse(inv, q))
    c1= ((n_i+a)*mp.power(Vi, 2))%q
    Ti= mp.power(g1, Vi)
    Ei= mp.power(g1, a)

    
    Lambda1= mp.power(B1, (alpha+gamma))
    if mp.log(Lambda1, g1)>=q:
        Lambda1= mp.power(g1, (mp.log(Lambda1, g1))%q)

    Lambda2= mp.power(Ti, alpha)
    if mp.log(Lambda2, g1)>=q:
        Lambda2= mp.power(g1, (mp.log(Lambda2, g1))%q)

    Lambda3= (k1-alpha)%q
    Lambda4= mp.power(Ti, (gamma+beta+Vi))
    if mp.log(Lambda4, g1)>=q:
        Lambda4= mp.power(g1, (mp.log(Lambda4, g1))%q)

    Delta1= (alpha-k1)%q
    Delta2= (k1+gamma)%q
    Delta3= (gamma+beta)%q
    Delta4= -k1-gamma+alpha


    Lambda1_= mp.power(g1, (mp.log((mp.power(B1, Delta1)*mp.power(A1, Delta2)*mp.power(Ei, -Delta2)), g1))%q)

    Lambda2_= mp.power(g1, (mp.log((mp.power(B1, Lambda3)*mp.power(B1, Delta1)*mp.power(Ti, (Delta4+Delta2))), g1))%q)
    
    Lambda4_= mp.power(g1, (mp.log((mp.power(Ti, Delta3)*mp.power(DID_ui, c1)), g1))%q)

    Ctemp= (Lambda1, Lambda2, Lambda4, DID_ui)
    C_temp= (Lambda1_, Lambda2_, Lambda4_, DID_ui)

    C= str(hash(Ctemp))
    C_= str(hash(C_temp))

    Phi1= random.randint(1, q-1)
    Phi2= random.randint(1, q-1)
    Phi3= random.randint(1, q-1)

    Li= mp.power(g1, (mp.log(mp.power(B1, Ri), g1))%q)
    f1= ((Ri+a)*b)%q
    DID_rsu= mp.power(g1, mod_inverse(inv2, q))


    h1= mp.power(g1, (mp.log(mp.power(g1, (b*(Phi1+Phi3))%q), g1))%q)
    h2= mp.power(g1, (mp.log(mp.power(DID_rsu, Phi3*f1), g1))%q)

    x1= (Phi1-Phi2)%q
    x2= (Phi2+Phi3)%q
    x3= (-Phi1+Phi2+Phi3)%q

    h1_= mp.power(g1, (mp.log(mp.power(B1, x1+x2), g1))%q)
    h2_= mp.power(g1, (mp.log(mp.power(B1, x1+x3), g1))%q)
    
    Ctemp2= (h1, h2, Li, DID_rsu)
    C_temp2= (h1_, h2_, Li, DID_rsu)

    C2= str(hash(Ctemp2))
    C2_= str(hash(C_temp2))

    end_code2 = time.time()
    elapsed_code2 = end_code2 - start_code2
    elapsed_times_code2.append(elapsed_code2)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_runs + 1), elapsed_times_code1, label='EAAP')
plt.plot(range(1, num_runs + 1), elapsed_times_code2, label='Modified EAAP')
plt.xlabel('\nRun Number')
plt.ylabel('Elapsed Time (seconds)\n')
plt.title('Elapsed Time for EAAP vs Modified EAAP\n')
plt.legend(loc='upper left')
# Add grid lines
plt.grid(True)
# Set background style
plt.style.use('seaborn-v0_8-darkgrid')
plt.legend()
plt.show()
