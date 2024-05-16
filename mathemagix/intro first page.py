import tkinter as tk
from tkinter import messagebox
import random

def check_answer(user_answer, correct_answer):
    try:
        user_answer = float(user_answer)
        if user_answer == correct_answer:
            return True
        else:
            return False
    except ValueError:
        return False

def submit_answer():
    num1 = num1_entry.get()
    num2 = num2_entry.get()
    user_input = user_answer_entry.get()

    # Validate input fields
    if not (num1 and num2 and user_input):
        messagebox.showerror("Error", "Please fill in all text boxes")
        return

    # Validate numerical inputs
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
        return

    selected_operation = operation_var.get()

    # Perform selected operation
    if selected_operation == "+":
        correct_answer = num1 + num2
    elif selected_operation == "-":
        correct_answer = num1 - num2
    elif selected_operation == "×":
        correct_answer = num1 * num2
    elif selected_operation == "÷":
        if num2 != 0:
            correct_answer = num1 / num2
        else:
            messagebox.showerror("Error", "Cannot divide by zero")
            return
    else:
        return

    # Check user's answer
    if check_answer(user_input, correct_answer):
        messagebox.showinfo("congrats", "That's right!")
    else:
        response = messagebox.askquestion("let's get you some help", "Would you like a hint?")
        if response == 'yes':
            hint = generate_hint(selected_operation, num1, num2)
            messagebox.showinfo("Hint", hint)

def generate_hint(operation, num1, num2):
    if operation == "+":
        return f" For single digits, focus on memorizing basic addition facts. For double digits, add the tens first, then the ones, carrying over if necessary. And for triple digits, add the hundreds first, then the tens, and finally the ones, carrying over where needed. {num1} and {num2}"
    elif operation == "-":
        return f"For single digit subtraction, subtract the numbers directly. For double digits, subtract the ones first, then the tens, borrowing if necessary. For triple digits, subtract the ones, then the tens, then the hundreds, borrowing as needed. {num1} and {num2}"
    elif operation == "×":
        return f"For single digit multiplication, directly multiply the numbers. For double digits, multiply the digits in each place value separately, then add the results, carrying over when needed. For triple digits, multiply the digits in each place value separately, starting from the rightmost digit, then add the results, carrying over as necessary. {num1} and {num2}"
    elif operation == "÷":
        return f"For single digit division, divide the numbers directly. For double digits, break down the divisor into factors of 10 (e.g., 20 becomes 2x10) and perform the division accordingly. For triple digits, break down the divisor into factors of 100 (e.g., 200 becomes 2x100) and adjust the dividend accordingly, then proceed with division. {num1} by {num2}"
    else:
        return "No hint available"

def clear_all():
    # Clear all input fields and result label
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    user_answer_entry.delete(0, tk.END)

# Create a tkinter window
root = tk.Tk()
root.title("Brainiax Maths ➗")
light_blue = "#ADD8E6"
root.configure(bg=light_blue)

# Set window size and position
window_width = 600
window_height = 450
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create canvas for scattered symbols pattern
canvas = tk.Canvas(root, width=window_width, height=window_height, bg=light_blue, highlightthickness=0)
canvas.pack()

# Draw scattered symbols
for _ in range(500):
    x = random.randint(0, window_width)
    y = random.randint(0, window_height)
    symbol = random.choice(["x", "+", "-", "&", "$", "%", "!"])
    canvas.create_text(x, y, text=symbol, font=("Arial", 10), fill="white")

# Create entry box for first number
num1_label = tk.Label(root, text="Enter first number:", font=("Arial", 20), bg=light_blue)
num1_label.place(relx=0.1, rely=0.1)
num1_entry = tk.Entry(root, font=("Arial", 20))
num1_entry.place(relx=0.1, rely=0.2)

# Operation dropdown menu
operation_var = tk.StringVar()
operation_var.set("+")  # Default operation
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "×", "÷")
operation_menu.config(font=("Arial", 20))
operation_menu.place(relx=0.1, rely=0.3)

# Create entry box for second number
num2_label = tk.Label(root, text="Enter second number:", font=("Arial", 20), bg=light_blue)
num2_label.place(relx=0.1, rely=0.4)
num2_entry = tk.Entry(root, font=("Arial", 20))
num2_entry.place(relx=0.1, rely=0.5)

# Create entry box for user's answer
user_answer_label = tk.Label(root, text="Your answer:", font=("Arial", 20), bg=light_blue)
user_answer_label.place(relx=0.1, rely=0.6)
user_answer_entry = tk.Entry(root, font=("Arial", 20))
user_answer_entry.place(relx=0.1, rely=0.7)

# Create a frame for buttons
button_frame = tk.Frame(root, bg=light_blue)
button_frame.place(relx=0.1, rely=0.8)

# Create submit button
submit_button = tk.Button(button_frame, text="Submit", font=("Arial", 20), command=submit_answer)
submit_button.pack(side=tk.LEFT, padx=10)

# Create clear all button
clear_button = tk.Button(button_frame, text="Clear All", font=("Arial", 20), command=clear_all)
clear_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
