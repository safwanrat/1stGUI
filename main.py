'''
119 Safwan Rahman
This code extracts text from a PDF. The dynamic element was a scrollbar and a dropdown menu for changing the background color of the textbox.
'''

import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=4)

# logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        # text box, scrollbar
        scrollbar = tk.Scrollbar(root)
        text_box = tk.Text(root, yscrollcommand = scrollbar.set, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)
        scrollbar.config(command=text_box.yview)
        scrollbar.grid(column=2, row=3, sticky="NS")
        browse_text.set("Browse Again")

        # colors of text box background
        colors = ["white", "red", "orange", "purple", "blue"]
        default_color = tk.StringVar(root)
        default_color.set(colors[0])
        dropdown = tk.OptionMenu(root, default_color, *colors)
        dropdown.grid(column = 3, row = 3)
        def changing_color():
            for color in colors:
                if default_color.get() == color:
                    text_box.config(bg = default_color.get())

        change_bg_color = tk.Button(root, text = "Change Color of Background", command=changing_color)
        change_bg_color.grid(column = 4, row = 3)

# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column = 1, row = 2)

root.mainloop()
