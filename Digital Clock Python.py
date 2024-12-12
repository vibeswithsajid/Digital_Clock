import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Set the window size
root.geometry("400x200")

# Set the background color
root.config(bg="black")

# Create a label to display the time
time_label = tk.Label(root, font=("calibri", 40, "bold"), background="black", foreground="white")
time_label.pack(anchor="center")

# Function to update the time
def update_time():
    current_time = time.strftime("%H:%M:%S")  # Get the current time in 24-hour format
    time_label.config(text=current_time)  # Update the label with the new time
    time_label.after(1000, update_time)  # Call this function every 1000ms (1 second)

# Call the update_time function
update_time()

# Start the main event loop
root.mainloop()
