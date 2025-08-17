import tkinter as tk

application = tk.Tk()

application.geometry("800x400")

application.title("CURD GUI in PYTHON")

label = tk.Label(application, text="Welcome to CURD GUI in PYTHON", bg="lightblue", font=("Arial", 20)).pack()

textbox = tk.Text(application, height=3, width=50)



application.mainloop()