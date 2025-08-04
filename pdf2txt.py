import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def pdf_to_text(pdf_path, output_folder):
    try:
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        txt_path = os.path.join(output_folder, f"{pdf_name}.txt")

        doc = fitz.open(pdf_path)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page in doc:
                text = page.get_text()
                txt_file.write(text + '\n')
        doc.close()

        messagebox.showinfo("Success", f"Text extracted and saved to:\n{txt_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_pdf():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_entry.delete(0, tk.END)
    pdf_entry.insert(0, pdf_path)

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def convert_pdf():
    pdf_path = pdf_entry.get()
    output_folder = folder_entry.get()
    if not pdf_path or not output_folder:
        messagebox.showwarning("Missing Information", "Please select both a PDF file and a destination folder.")
        return
    pdf_to_text(pdf_path, output_folder)

def quit_app():
    root.destroy()

# Create GUI window
root = tk.Tk()
root.title("PDF to Text Converter")

# PDF file selection
tk.Label(root, text="Select PDF File:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
pdf_entry = tk.Entry(root, width=50)
pdf_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=browse_pdf).grid(row=0, column=2, padx=10, pady=5)

# Destination folder selection
tk.Label(root, text="Select Destination Folder:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=browse_folder).grid(row=1, column=2, padx=10, pady=5)

# Convert and Quit buttons
tk.Button(root, text="Convert", command=convert_pdf, width=15).grid(row=2, column=1, pady=20)
tk.Button(root, text="Quit", command=quit_app, width=15).grid(row=2, column=2, pady=20)

root.mainloop()
