import tkinter as tk
from tkinter import messagebox, ttk
import getpass
import subprocess
import os
import time

class ShutdownApp:
    def __init__(self, master):
        self.master = master
        master.title("Shutdown Confirmation")
        master.geometry("400x200")  # Increase window size

        self.label = tk.Label(master, text="Enter your password to shutdown:")
        self.label.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.shutdown_button = tk.Button(master, text="Shutdown", command=self.shutdown)
        self.shutdown_button.pack()

        self.cancel_button = tk.Button(master, text="Cancel", command=self.cancel)
        self.cancel_button.pack()

        self.progress_bar = tk.ttk.Progressbar(master, orient="horizontal", length=200, mode="indeterminate")
        self.progress_bar.pack()

    def shutdown(self):
        password = self.password_entry.get()
        if password == "update":
            self.update_system()
        else:
            messagebox.showerror("Invalid Password", "Invalid password. Please try again.")

    def update_system():
        root_password = getpass.getpass("Enter your root password: ")
        command = ["sudo", "-S", "pacman", "-Syu"]
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate(input=f"{root_password}\n".encode())
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            print(output.decode("utf-8"))
            messagebox.showinfo("Update Successful", "System updated successfully.")
        except subprocess.CalledProcessError as e:
            print(e.output.decode("utf-8"))
            messagebox.showerror("Update Failed", "Failed to update system.")
        finally:
            self.progress_bar.stop()

    def cancel(self):
        messagebox.showinfo("Shutdown Canceled", "Shutdown canceled. Exiting...")
        self.master.destroy()

root = tk.Tk()
app = ShutdownApp(root)
root.mainloop()