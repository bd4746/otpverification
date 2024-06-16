import sys  # Import the sys module for accessing command-line arguments
from tkinter import messagebox  # Import the messagebox module from tkinter for displaying messages
from tkinter import *  # Import all modules from the tkinter library
import time  # Import the time module for timing functionality

# Get the OTP value from the command-line argument passed when the script is executed
b = sys.argv[1]

# Open the "otp.txt" file in read mode to read the stored OTP
f1 = open("otp.txt", "r")
b1 = f1.read()  # Read the OTP from the file
f1.close()  # Close the file

# Check if the provided OTP (b) matches the OTP from the file (b1)
if b == b1:
    # If the OTPs match, write "success" to the "status.txt" file
    f = open("status.txt", "w")
    f.write("success")
    f.close()
    # Display a success message using a message box
    messagebox.showinfo("Congratulations", "Your OTP was verified Successfully!!")
else:
    # If the OTPs do not match, write "failure" to the "status.txt" file
    f = open("status.txt", "w")
    f.write("failure")
    f.close()
