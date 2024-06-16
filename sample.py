# Import necessary modules
import tkinter
import subprocess
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Create a Tkinter main window
root = tkinter.Tk()

# Set the title of the window
root.title("OTP Mail Verification")

# Set the dimensions of the window (400x400)
root.geometry("400x400")

# Make the window non-resizable
root.resizable(0, 0)

# Define colors for backgrounds
sky_color = "#76c3ef"
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

# Create a frame for displaying output (e.g., the image)
output_frame = tkinter.LabelFrame(sky_frame, bg=output_color, height=225, width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)

# Create a frame for user input
input_frame = tkinter.LabelFrame(grass_frame, bg=input_color, width=325)
input_frame.pack(pady=15)
input_frame.pack_propagate(0)

# Function to perform email verification
def verify():
    cmd = str(mail_entry.get())  # Get the email address from the entry field

    # Specify the path to the Python script for sending mail
    script_path = "C:\\Users\\surya\\OneDrive\\Desktop\\mini project\\sendmail.py"

    # Create a list with the command to run the script with the email address as an argument
    cmd_list = ['python', script_path, cmd]

    # Print the command being executed
    print("Executing command:", cmd_list)

    try:
        # Execute the command and capture the result
        subprocess.run(cmd_list, check=True)
    except subprocess.CalledProcessError as e:
        # Handle errors by printing an error message
        print("Error:", e)

# Load and display an image on the GUI
png_image = Image.open("C:\\Users\\surya\\OneDrive\\Desktop\\mini project\\main.jpg")
image = ImageTk.PhotoImage(png_image)
image_label = tkinter.Label(output_frame, image=image)
image_label.pack()

# Create a label for the "Email" input field
l = tkinter.Label(input_frame, text='Email')
l.grid(row=0, column=0, padx=10, pady=10)

# Create an entry field for the user to enter their email
mail_entry = tkinter.Entry(input_frame, width=25, font=small_font)
mail_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a "Submit" button that calls the "verify" function when clicked
submit_but = tkinter.Button(input_frame, font=large_font, text='Submit', command=verify)
submit_but.grid(row=0, column=2, padx=2, pady=10)

# Start the Tkinter main event loop
root.mainloop()
