import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)
    result_label.config(text=f"Your BMI is: {bmi:.2f}")

def save_bmi():
    with open("bmi_data.txt", "a") as f:
        f.write(f"{weight_entry.get()}, {height_entry.get()}, {result_label.cget('text')}\n")

root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Enter your weight (kg):")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Enter your height (m):")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

save_button = tk.Button(root, text="Save BMI Data", command=save_bmi)
save_button.pack()

root.mainloop()
