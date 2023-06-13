import tkinter as tk

# Function to evaluate the expression and display the result
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        output_label.config(text="Result: " + str(result))
    except Exception as e:
        output_label.config(text="Error: " + str(e))

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to input the expression
entry = tk.Entry(window, width=30)
entry.pack()

# Create a button to calculate the expression
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create a label to display the result or error message
output_label = tk.Label(window, text="")
output_label.pack()

# Start the main event loop
window.mainloop()
