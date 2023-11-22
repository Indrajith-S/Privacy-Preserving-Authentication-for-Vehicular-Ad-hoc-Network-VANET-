import matplotlib.pyplot as plt
import numpy as np

def plotres():
    users= eval(input("Enter 5 inputs of users: "))
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

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()

plotres()
