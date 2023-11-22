##import math
##def extended_gcd(a, b):
##    if a == 0:
##        return b, 0, 1
##    else:
##        gcd, x, y = extended_gcd(b % a, a)
##        return gcd, y - (b // a) * x, x
##
##def mod_inverse(a, m):
##    gcd, x, y = extended_gcd(a, m)
##    if gcd != 1:
##        raise ValueError("Inverse does not exist")
##    else:
##        return x % m
##
### Example usage:
##a = 17
##m = 13
##inverse_mod = mod_inverse(a, m)
##print(f"The inverse of {a} modulo {m} is {inverse_mod}")
##inverse_mod = mod_inverse(10, 7)
##print("inv: ", inverse_mod)
##
##Ti= 2**inverse_mod
##print(Ti)
##
##Lambda2_temp1_= int(math.log((16384**16)*(65536**14), 2))
##Lambda2_temp2_= int(math.log((16384**15)*(65536**16), 2))
##Lambda2_= 2**((Lambda2_temp1_-Lambda2_temp2_)%19)
##print(int(Lambda2_))
##print(math.log(131072, 2))
##

import tkinter as tk
from tkinter import messagebox
import random
import time
from mpmath import mp

mp.dps = 100

# Global variables for Lambda values
Lambda1 = 0  # Update with the actual initial values
Lambda1_ = 0
Lambda2 = 0
Lambda2_ = 0

def display_results():
    global Lambda1, Lambda1_, Lambda2, Lambda2_
    
    result_text = (
        f"Lambda 1: {Lambda1} and Lambda 1`: {Lambda1_}\n"
        f"Lambda 2: {Lambda2} and Lambda 2`: {Lambda2_}\n\n"
        f"Privacy Preserving Authentication {'Successfully Completed!' if (Lambda1 == Lambda1_) and (Lambda2 == Lambda2_) else 'Failed'}"
    )
    result_label.config(text=result_text)
    result_window.deiconify()

def animate_encryption():
    global Lambda1, Lambda1_, Lambda2, Lambda2_
    
    # Clear the canvas
    canvas.delete("all")
    
    # Create random numbers
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    
    # Display random numbers on the canvas
    canvas.create_text(100, 50, text=str(num1), font=("Helvetica", 16), fill="blue")
    canvas.create_text(200, 50, text=str(num2), font=("Helvetica", 16), fill="blue")
    canvas.create_text(300, 50, text=str(num3), font=("Helvetica", 16), fill="blue")
    
    # Encryption animation
    for i in range(20):
        canvas.delete("all")
        
        # Encrypt numbers
        enc_num1 = mp.power(num1, i)
        enc_num2 = mp.power(num2, i)
        enc_num3 = mp.power(num3, i)
        
        # Display encrypted numbers on the canvas
        canvas.create_text(100, 50, text=str(enc_num1), font=("Helvetica", 16), fill="green")
        canvas.create_text(200, 50, text=str(enc_num2), font=("Helvetica", 16), fill="green")
        canvas.create_text(300, 50, text=str(enc_num3), font=("Helvetica", 16), fill="green")
        
        # Update the window
        root.update()
        
        # Pause for a short duration
        time.sleep(0.2)
    
    # Update Lambda values (replace with actual values)
    Lambda1 = enc_num1
    Lambda1_ = enc_num2
    Lambda2 = enc_num3
    Lambda2_ = enc_num1
    
    # Display the final results
    display_results()

# Main Section
q = int(input("Enter Value of q: "))
if not isPrime(q):
    sys.exit("Not a Prime Number")

# ... (Previous code)

# Main Section
# ...

# Create Tkinter window
root = tk.Tk()
root.title("Privacy Preserving Authentication")

# Create a canvas for animation
canvas = tk.Canvas(root, width=400, height=100, bg="white")
canvas.pack(pady=10)

# Create a button to trigger the encryption animation
animate_button = tk.Button(root, text="Animate Encryption", command=animate_encryption)
animate_button.pack(pady=10)

# Create a hidden window for displaying the results
result_window = tk.Toplevel(root)
result_window.title("Authentication Results")
result_window.geometry("400x200")
result_window.withdraw()

# Label for displaying the results
result_label = tk.Label(result_window, text="", justify="left")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

 
##
