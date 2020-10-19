from tkinter import *
from detector import detection

window = Tk()

window.title("Covid Detection From X-Ray Scans")
window.configure(background="#3E4149", pady=20, padx=40)

file = ""


def clicked():
    result_LABEL.configure(text="Evaluating...")
    file = dir_INPUT.get()
    result = detection(file)
    complete(result)


def complete(result):
    # result_LABEL.configure(text=result)
    if result > 0:
        result_LABEL.configure(text="COVID-19 POSITIVE",
                               foreground="#fa6969", background="#660303")
    else:
        result_LABEL.configure(text="COVID-19 NEAGTIVE",
                               foreground="#6bfa69", background="#014a0b")


# Heading
heading_LABEL = Label(window, foreground="white", text="Covid-19 Test",
                      font=("sans-serif", 24), background="#3E4149")
heading_LABEL.pack()

# Input Label
input_LABEL = Label(window, foreground="#BDBDBD",
                    text="Path to Image...", font=("Calibri", 14), background="#3E4149", pady=20)
input_LABEL.pack()

# Input Box
dir_INPUT = Entry(window, width=35, font="Helvetica 20 bold")
dir_INPUT.pack(ipady=5, pady=10)

# Run Button
run_BUTTON = Button(window, text="Check", command=clicked, font=("Arial Medium", 12),
                    highlightbackground="#337dd6", background="#4287f5", foreground="#FFFFFF", pady=10, width=15)
run_BUTTON.pack(pady=10)

# Status
result_LABEL = Label(window, foreground="#f5c542", font=("Calibri", 14),
                     text="Ready...", background="#3E4149", pady=20, padx=20)
result_LABEL.pack()

window.mainloop()
