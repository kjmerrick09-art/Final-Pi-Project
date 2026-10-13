import tkinter as tk

# Create root window
root = tk.Tk()
root.title("Tkinter Widget Examples")
root.geometry("800x600")

# 1. Label – Display text/images
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16), fg="blue")
label.pack(pady=10)

# 2. Button – Trigger action on click
def click_me():
    print("Button clicked!")
btn = tk.Button(root, text="Click Me", command=click_me)
btn.pack(pady=5)

# 3. Entry – Single-line text input
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

# 4. Checkbutton – Toggle on/off
var = tk.IntVar()
chk = tk.Checkbutton(root, text="Enable", variable=var)
chk.pack(pady=5)

# 5. Radiobutton – Single-choice option
var2 = tk.IntVar()
rad1 = tk.Radiobutton(root, text="Option 1", variable=var2, value=1)
rad1.pack(pady=2)
rad2 = tk.Radiobutton(root, text="Option 2", variable=var2, value=2)
rad2.pack(pady=2)

# 6. Listbox – Scrollable list
lb = tk.Listbox(root, width=20, height=4)
lb.insert(1, "Apple")
lb.insert(2, "Banana")
lb.insert(3, "Cherry")
lb.pack(pady=5)

# 7. Scale – Slider for numeric range
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack(pady=5)

# 8. Frame – Group widgets
frame = tk.Frame(root)
frame.pack(pady=10)
tk.Label(frame, text="Grouped Label").pack()
tk.Button(frame, text="Frame Button").pack()

# 9. Text – Multiline input
text = tk.Text(root, width=20, height=4)
text.pack(pady=5)

# 10. Label (with background)
label2 = tk.Label(root, text="Colored Label", bg="lightyellow", padx=10)
label2.pack(pady=5)

root.mainloop()
