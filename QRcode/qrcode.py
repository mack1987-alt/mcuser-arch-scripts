# QR Code App
# Author: mack1987-alt
# Version 2.01
import tkinter as tk
from tkinter import filedialog, messagebox
import pyqrcode
from PIL import Image, ImageTk
import os

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Label and entry for input
        self.label = tk.Label(root, text="Enter text or URL:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)

        # Generate button
        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr)
        self.generate_button.pack(pady=10)

        # QR code display label
        self.qr_label = tk.Label(root)
        self.qr_label.pack(pady=10)

        # Save button (initially disabled)
        self.save_button = tk.Button(root, text="Save QR Code", command=self.save_qr, state=tk.DISABLED)
        self.save_button.pack(pady=10)

        # Store the generated QR image and PhotoImage reference
        self.qr_image = None
        self.photo_image = None
        self.temp_file = "temp_qr.png"

    def generate_qr(self):
        link = self.entry.get().strip()
        if not link:
            messagebox.showerror("Error", "Please enter some text or URL.")
            return

        try:
            # Create QR code
            qr_code = pyqrcode.create(link)

            # Save temporarily
            qr_code.png(self.temp_file, scale=6)

            # Open and display
            self.qr_image = Image.open(self.temp_file)
            self.photo_image = ImageTk.PhotoImage(self.qr_image)
            self.qr_label.config(image=self.photo_image)

            # Enable save button
            self.save_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate QR code: {str(e)}")

    def save_qr(self):
        if not self.qr_image:
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            try:
                self.qr_image.save(file_path)
                messagebox.showinfo("Success", "QR code saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save QR code: {str(e)}")

    def __del__(self):
        # Clean up temp file on exit
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()