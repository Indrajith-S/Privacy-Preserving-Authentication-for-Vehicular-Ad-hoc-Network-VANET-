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

    start1= time.time()
    
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

    end1= time.time()

    el1= end1-start1
    
    bool1= False
    if (Lambda1==Lambda1_) and (Lambda2==Lambda2_) and (Lambda4==Lambda4_) and (C==C_):
        bool1= True
    else:
        print("Try Again")

    
#------------------------------------------------------RSU AUTH-------------------------------------------------------

    Phi1= random.randint(1, q-1)
    Phi2= random.randint(1, q-1)
    Phi3= random.randint(1, q-1)

    Li= mp.power(g1, (mp.log(mp.power(B1, Ri), g1))%q)
    f1= ((Ri+a)*b)%q
    DID_rsu= mp.power(g1, mod_inverse(inv2, q))

    start2= time.time()

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

    end2= time.time()
    el2= end2-start2
    
    bool2= False
    if (h1_==h1) and (h2_==h2) and (C2==C2_):
        bool2= True
    else:
        print("Try Again")


#---------------------------------------------------------------------------------------------------------------------

    print("\n------------------------------------------------USER AUTHENTICATION-----------------------------------------------")
    print("Lambda 1: ", Lambda1,"and Lambda 1`: ", Lambda1_,"\nLambda 2: ", Lambda2,"and Lambda 2`: ", Lambda2_
              ,"\nLambda 4: ", Lambda4,"and Lambda 4`: ", Lambda4_)
    print("Challenger: ",C," Challenger`: ",C_)
    if bool1:
        print("\nUser Successfully Authenticated")
    print("------------------------------------------------------------------------------------------------------------------")
    print("\n------------------------------------------------RSU AUTHENTICATION------------------------------------------------")       
    print("H1: ",h1," H1`: ",h1_)
    print("H2: ",h2," H2`: ",h2_)
    print("Challenger: ",C2," Challenger`: ",C2_)
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
        print("k1: ",k1)
        print("k2: ",k2)
        print("Vi: ",Vi)
        print("Ri: ",Ri)
        print("Alpha: ",alpha)
        print("Beta: ",beta)
        print("Gamma: ",gamma)
        print("Phi_1: ",Phi1)
        print("Phi_2: ",Phi2)
        print("Phi_3: ",Phi3)
        print("------------------------------------------------------------------------------------------------------------------")

        print("\n------------------------------------------------------------------------------------------------------------------")
        print("Computed Values: \n")
        print("Primitive Roots: ", g1, g2)
        print("A1: ",A1)
        print("B1: ",B1)
        print("c1: ",c1)
        print("Ei: ",Ei)
        print("Li: ",Li)
        print("Ti: ",Ti)
        print("f1: ",f1)
        print("x1: ",x1)
        print("x2: ",x2)
        print("x3: ",x3)
        print("DID_ui: ",DID_ui)
        print("DID_rsu: ",DID_rsu)
        print("Delta 1: ",Delta1)
        print("Delta 2: ",Delta2)
        print("Delta 3: ",Delta3)
        print("Delta 4: ",Delta4)
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

    
