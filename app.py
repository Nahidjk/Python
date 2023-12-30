import tkinter as tk

def generate_code():
    width_value = width_entry.get()
    height_value = height_entry.get()

    html_code = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .box {{
            width: {width_value}px;
            height: {height_value}px;
            background-color: #3498db;
        }}
    </style>
</head>
<body>
    <div class="box"></div>
</body>
</html>
'''
    print(html_code)

# Create main window
window = tk.Tk()
window.title("HTML CSS Code Generator")

# Create input fields
width_label = tk.Label(window, text="Width:")
width_label.pack()
width_entry = tk.Entry(window)
width_entry.pack()

height_label = tk.Label(window, text="Height:")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

# Create generate button
generate_button = tk.Button(window, text="Generate Code", command=generate_code)
generate_button.pack()

# Run the application
window.mainloop()
