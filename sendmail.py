import subprocess  # Import the subprocess module for running external commands
import math  # Import the math module for mathematical operations
import random  # Import the random module for generating random numbers
import smtplib  # Import the smtplib module for sending emails
import sys  # Import the sys module for accessing command-line arguments

# Get the email address as a command-line argument
mailid = sys.argv[1]

# Define a string of digits for OTP generation
digits = "0123456789"

# Initialize an empty string to store the OTP
OTP = ""

# Generate a 6-digit OTP by randomly selecting digits from the 'digits' string
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]

# Create a message containing the OTP
msg = 'Your OTP Verification for app is ' + OTP + ' Note.. Please enter OTP within 2 minutes and 3 attempts, otherwise, it becomes invalid'

# Open a file named "otp.txt" in write mode and write the OTP to it
file2 = open("otp.txt", "w")
file2.write(OTP)
file2.close()

# Set up SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Enter your Gmail credentials here (replace with actual email and password)
email_address = 'suryah6009@gmail.com'
email_password = 'cgihtohlufurhreh'

try:
    # Create an SMTP client and connect to the SMTP server
    s = smtplib.SMTP(smtp_server, smtp_port)
    s.starttls()  # Start a secure TLS connection
    s.login(email_address, email_password)  # Log in to your Gmail account

    # Send the email containing the OTP
    s.sendmail(email_address, mailid, msg)

    # Close the SMTP connection
    s.quit()

    # Specify the path to another Python script to be executed
    script_path = "C:\\Users\\surya\\OneDrive\\Desktop\\mini project\\otpveripage.py"

    # Create a list with the command to execute the script
    cmd_list = ['python', script_path]

    # Print a message indicating the command about to be executed
    print("Executing command:", cmd_list)

    try:
        # Execute the specified command (run the other Python script)
        subprocess.run(cmd_list, check=True)

    except subprocess.CalledProcessError as e:
        print("Error:", e)

except Exception as e:
    # Handle any exceptions that may occur during the execution of the script
    print("An error occurred:", str(e))
