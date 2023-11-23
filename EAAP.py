#---------------------------------------------Import Modules----------------------------------------------------------

import random
import math
import sys
from easygui import passwordbox
import matplotlib.pyplot as plt
import numpy as np
import time
from mpmath import mp
##It allows you to perform mathematical operations with a higher precision than the built-in float type in Python.
##This can be useful when working with very large or very small numbers, or when high precision is required
##in calculations.
mp.dps= 10000

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


#-----------------------------------------------------------MAIN------------------------------------------------------


#--------------------------------------------------------USER AUTH----------------------------------------------------

while True:
    user_input = input("\nEnter a Prime Number or type 'exit' to end: ")
    if user_input.lower() == 'exit':
        print("Thank you for your time 👋")
        break

    try:
        q = int(user_input)          
    except ValueError:
        sys.exit("Invalid input. Please enter an integer or type 'exit'.")

    if q<5:
        sys.exit("Please Enter a Prime Number Greater than 3.")
    if not isPrime(q):
        sys.exit("Not a Prime Number")

    
    
    primitive_roots = findPrimitive(q)

    if len(primitive_roots) < 2:
        result = f"No second primitive root found for {n}."
    else:
        result = [primitive_roots[0], primitive_roots[1]]

#---------------------------------------------------------------------------------------------------------------------

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

    start1= time.time()
    
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

    end1= time.time()
    el1= end1-start1
    
    bool1= False
    if (Lambda1==Lambda1_) and (Lambda2==Lambda2_) and (Ni==A1):
        bool1= True
    else:
        print("Try Again")


#------------------------------------------------------RSU AUTH-------------------------------------------------------

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

    start2= time.time()
    
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

    end2= time.time()
    el2= end2-start2
    
    bool2= False
    if (H1_==h1) and (H2_==h2):
        bool2= True
    else:
        print("Try Again")


#---------------------------------------------------------------------------------------------------------------------

    print("\n------------------------------------------------USER AUTHENTICATION-----------------------------------------------")
    print("Lambda 1: ", Lambda1,"and Lambda 1`: ", Lambda1_,"\nLambda 2: ", Lambda2,"and Lambda 2`: ", Lambda2_)
    print("Ni: ",Ni," and A1: ",A1)
    if bool1:
        print("\nUser Successfully Authenticated")
    print("------------------------------------------------------------------------------------------------------------------")
    print("\n------------------------------------------------RSU AUTHENTICATION------------------------------------------------")       
    print("H1: ",h1," H1`: ",H1_)
    print("H2: ",h2," H2`: ",H2_)
    if bool2:
        print("\nRSU Successfully Authenticated")
    print("------------------------------------------------------------------------------------------------------------------")        


#---------------------------------------------------------------------------------------------------------------------      

    if bool1 and bool2:
        print("\nPrivacy Preserving Authentication Successfully Completed!")

#---------------------------------------------------------------------------------------------------------------------


    elapsed= el1+el2

    password= passwordbox("Enter Password to Reveal Variables: ")
    if password=="l":
        
        print("\n------------------------------------------------------------------------------------------------------------------")
        print("Random Values Taken: \n")
        print("a: ",a)
        print("b: ",b)
        print("n_i: ",n_i)
        print("Mu: ",Mu)
        print("k1: ",k1)
        print("k2: ",k2)
        print("Vi: ",Vi)
        print("Rk: ",Rk)
        print("Ri: ",Ri)
        print("Omega: ",Omega)
        print("Phi_1: ",Phi_1)
        print("Phi_2: ",Phi_2)
        print("------------------------------------------------------------------------------------------------------------------")

        print("\n------------------------------------------------------------------------------------------------------------------")
        print("Computed Values: \n")
        print("Primitive Roots: ", g1, g2)
        print("Primitive Roots: ", g1, g2)
        print("Ei: ",Ei)
        print("DID_ui: ",DID_ui)
        print("Gamma_u: ",Gamma_u," Gamma_v: ",Gamma_v)
        print("Lambda: ",Lambda)
        print("Delta 1: ",Delta1," Delta 2: ",Delta2)
        print("Theta_u: ",Theta_u," Theta_v: ",Theta_v)
        print("h: ",h)
        print("H_alpha: ",H_alpha)
        print("H_beta: ",H_beta)
        print("H_gamma: ",H_gamma)
        print("Elapsed Time: ",elapsed)
        print("==================================================================================================================")



    else:
        print("Password Incorrect! Try Again.")





#---------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------

    try:
        users = eval(input("\nEnter 5 inputs of users: "))
    
        # Check if users is a list and has exactly 5 elements
        if not isinstance(users, list) or len(users)!= 5:
            sys.exit("Input must be a list with exactly 5 elements.")
        
    # You can add more specific checks for each element in the list if needed.

    except ValueError as ve:
        sys.exit(f"Error: {ve}")
    except Exception as e:
        sys.exit(f"An unexpected error occurred: {e}")
    
    def plotres(users):
        Tm= 0.6
        Tep= 1.6
        Tep_1= 0.7
        Tep_2= 0.6
    ##    ecpp= (10+n)*Tm
    ##    gsb= (4*n*Tep_1) + (5*n*Tep_2)
    ##    kpsd= ((4+n)*Tep_1) + (5*n*Tep_2)
    ##    eaap= (4*Tep_1) + (n*Tep_2)
        ECPP = [(10+int(users[0]))*Tm, (10+int(users[1]))*Tm, (10+int(users[2]))*Tm, (10+int(users[3]))*Tm, (10+int(users[4]))*Tm]
        GSB = [(4*int(users[0])*Tep_1) + (5*int(users[0])*Tep_2), (4*int(users[1])*Tep_1) + (5*int(users[1])*Tep_2), (4*int(users[2])*Tep_1) + (5*int(users[2])*Tep_2), (4*int(users[3])*Tep_1) + (5*int(users[3])*Tep_2), (4*int(users[4])*Tep_1) + (5*int(users[4])*Tep_2)]
        KPSD = [((4+int(users[0]))*Tep_1) + (5*int(users[0])*Tep_2), ((4+int(users[1]))*Tep_1) + (5*int(users[1])*Tep_2), ((4+int(users[2]))*Tep_1) + (5*int(users[2])*Tep_2), ((4+int(users[3]))*Tep_1) + (5*int(users[3])*Tep_2), ((4+int(users[4]))*Tep_1) + (5*int(users[4])*Tep_2)]
        EAAP = [(4*Tep_1) + (int(users[0])*Tep_2), (4*Tep_1) + (int(users[1])*Tep_2), (4*Tep_1) + (int(users[2])*Tep_2), (4*Tep_1) + (int(users[3])*Tep_2), (4*Tep_1) + (int(users[4])*Tep_2)]

        # Set the width of the bars
        bar_width = 0.2

        # Set the positions of bars on X-axis for two sets
        r1 = np.arange(len(users))
        r2 = [x + bar_width for x in r1]
        r3 = [x + bar_width for x in r2]
        r4 = [x + bar_width for x in r3]
        r5 = [x + bar_width for x in r4]

        # Plotting the bars
        plt.bar(r1, GSB, width=bar_width, label='GSB')
        plt.bar(r2, KPSD, width=bar_width, label='KPSD')
        plt.bar(r3, ECPP, width=bar_width, label='ECPP')
        plt.bar(r4, EAAP, width=bar_width, label='EAAP')


        # Add labels to the plot
        plt.xlabel('\nNumber of Users')
        plt.ylabel("Computational Time in 'ms'\n\n")
        plt.title('Computational Efficiency\n')
    ##    plt.xticks([r + bar_width/2 for r in range(len(users))], users)

        plt.legend(loc='upper left')
        # Add grid lines
        plt.grid(True)
        # Set background style
        plt.style.use('seaborn-v0_8-darkgrid')
        
        # Show the plot
        plt.show()
        

    plotres(users)

    def plot_line_graph(users):
        Tm = 0.6
        Tep_1 = 0.7
        Tep_2 = 0.6
        Tep= 1.6
        ECPP = [(10 + int(users[0])) * Tm, (10 + int(users[1])) * Tm, (10 + int(users[2])) * Tm, (10 + int(users[3])) * Tm, (10 + int(users[4])) * Tm]
        GSB = [(4 * int(users[0]) * Tep_1) + (5 * int(users[0]) * Tep_2),
               (4 * int(users[1]) * Tep_1) + (5 * int(users[1]) * Tep_2),
               (4 * int(users[2]) * Tep_1) + (5 * int(users[2]) * Tep_2),
               (4 * int(users[3]) * Tep_1) + (5 * int(users[3]) * Tep_2),
               (4 * int(users[4]) * Tep_1) + (5 * int(users[4]) * Tep_2)]
        KPSD = [((4 + int(users[0])) * Tep_1) + (5 * int(users[0]) * Tep_2),
                ((4 + int(users[1])) * Tep_1) + (5 * int(users[1]) * Tep_2),
                ((4 + int(users[2])) * Tep_1) + (5 * int(users[2]) * Tep_2),
                ((4 + int(users[3])) * Tep_1) + (5 * int(users[3]) * Tep_2),
                ((4 + int(users[4])) * Tep_1) + (5 * int(users[4]) * Tep_2)]
        EAAP = [(4 * Tep_1) + (int(users[0]) * Tep_2),
                (4 * Tep_1) + (int(users[1]) * Tep_2),
                (4 * Tep_1) + (int(users[2]) * Tep_2),
                (4 * Tep_1) + (int(users[3]) * Tep_2),
                (4 * Tep_1) + (int(users[4]) * Tep_2)]

        # Plotting the line graph
        plt.plot(users, GSB, marker='o', label='GSB')
        plt.plot(users, KPSD, marker='o', label='KPSD')
        plt.plot(users, ECPP, marker='o', label='ECPP')
        plt.plot(users, EAAP, marker='o', label='EAAP')

        # Add labels to the plot
        plt.xlabel('\nNumber of Users')
        plt.ylabel("Computational Time in 'ms'\n\n")
        plt.title('Computational Efficiency - Line Graph\n')

        plt.legend(loc='upper left')
        # Add grid lines
        plt.grid(True)
        # Set background style
        plt.style.use('seaborn-v0_8-darkgrid')
        
        # Show the plot
        plt.show()

    plot_line_graph(users)








    





    
