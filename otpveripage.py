from tkinter import *  # Import all modules from the tkinter library
from tkinter import messagebox  # Import the messagebox module for displaying messages
import tkinter  # Import the tkinter module for creating a GUI
import time  # Import the time module for timing functionality
import subprocess  # Import the subprocess module for running external commands
from tkinter import *  # Import all modules from the tkinter library (this line is redundant)
from tkinter import PhotoImage  # Import the PhotoImage module from tkinter
from PIL import Image, ImageTk  # Import modules from the Python Imaging Library (PIL)

# Create a tkinter window
root = tkinter.Tk()

# Set the window title, dimensions, and make it non-resizable
root.title("Verification Screen")
root.geometry("400x400")
root.resizable(0, 0)

sky_color = "#76c3ef"  # Define colors for various elements
grass_color = "#aad207"
output_color = "#dcf0fb"
input_color = "#ecf2ae"

# Define font styles
large_font = ('SimSun', 14)
small_font = ('SimSun', 11)

# Create a frame for the sky background
sky_frame = tkinter.Frame(root, bg=sky_color, height=230)
sky_frame.pack(fill="both", expand=True)

# Create a frame for the grass background
grass_frame = tkinter.Frame(root, bg=grass_color)
grass_frame.pack(fill="both", expand=True)

# Create an output frame within the sky frame
output_frame = tkinter.LabelFrame(sky_frame, bg=output_color, height=225, width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)

# Create an input frame within the grass frame
input_frame = tkinter.LabelFrame(grass_frame, bg=input_color, width=325)
input_frame.pack(pady=15)
input_frame.pack_propagate(0)

count = 3  # A global variable for counting attempts. Initially, there are 3 attempts.

# Define a function for OTP verification
def verify():
    global count
    global root
    end = time.time()  # Timer ends when the user clicks 'verify'
    t = format(end - start)  # Calculate the time difference
    print(float(t))  # Print the time in seconds

    if float(t) >= 120:  # Check if the user takes more than 2 minutes
        messagebox.showinfo("Time out", "Session Expired... Time out Please regenerate OTP")
        root.destroy()
    else:
        cmd1 = str(otp_entry.get())  # Get the entered OTP
        script_path = "C:\\Users\\surya\\OneDrive\\Desktop\\mini project\\verify.py"
        cmd_list = ['python', script_path, cmd1]
        print("Executing command:", cmd_list)
        try:
            subprocess.run(cmd_list, check=True)
        except subprocess.CalledProcessError as e:
            print("Error:", e)

        ok = 'Invalid OTP: ' + str((count - 1)) + ' attempts remaining'
        count = count - 1
        f1 = open("status.txt", "r")
        bh = f1.read()
        
        if count >= 1 and bh != "success":
            tkinter.messagebox.askretrycancel("Error", ok)
            f1.close()
        elif count == 0 and bh != "success":
            f = open("otp.txt", "w")
            f.write("")
            f.close()
            messagebox.showinfo("Oooo", "Your 3 attempts were over. Please regenerate OTP")
            f1.close()
            root.destroy()
        elif bh == "success":
            f1.close()
            root.destroy()

start = time.time()  # Start the timer once the screen is entered

# Load and display an image
png_image = Image.open("C:\\Users\\surya\\OneDrive\\Desktop\\mini project\\otp.jpg")
image = ImageTk.PhotoImage(png_image)
image_label = tkinter.Label(output_frame, image=image)
image_label.pack()

# Create labels and an entry field for OTP
min = tkinter.Label(output_frame, text='Enter OTP within 2 min', font=('arial', 14))
min.pack()
l = tkinter.Label(input_frame, text='Enter OTP')
l.grid(row=0, column=0, padx=10, pady=10)
otp_entry = tkinter.Entry(input_frame, width=25, font=small_font)
otp_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a 'Verify' button that calls the 'verify' function
submit_but = tkinter.Button(input_frame, font=large_font, text='Verify', command=verify)
submit_but.grid(row=0, column=2, padx=2, pady=10)

# Start the main tkinter event loop
root.mainloop()
