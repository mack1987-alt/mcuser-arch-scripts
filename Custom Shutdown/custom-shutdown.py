# Version 1.1
# Does not work yet
import tkinter as tk
from tkinter import messagebox, ttk
import subprocess

class ShutdownApp:
    def __init__(self, master):
        self.master = master
        master.title("Shutdown Confirmation")
        master.geometry("400x200")

        self.label = tk.Label(master, text="Enter your password to execute:")
        self.label.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.execute_button = tk.Button(master, text="Execute", command=self.execute_command)
        self.execute_button.pack()

        self.cancel_button = tk.Button(master, text="Cancel", command=self.cancel)
        self.cancel_button.pack()

        self.progress_bar = ttk.Progressbar(master, orient="horizontal", length=200, mode="indeterminate")
        self.progress_bar.pack()

    def execute_command(self):
        password = self.password_entry.get()
        if password == "update":
            self.update_system()
        elif password == "shutdown":
            self.shutdown_system(password)
        else:
            messagebox.showerror("Invalid Password", "Invalid password. Please try again.")

    def update_system(self):
        try:
            command = ["pkexec", "pacman", "-Syu"]
            subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            messagebox.showinfo("Update Started", "System update process started in terminal.")
        except Exception as e:
            messagebox.showerror("Update Error", f"Failed to start update process: {str(e)}")

    def shutdown_system(self, password):
        try:
            shutdown_command = f"echo {password} | sudo -S shutdown -h now"
            subprocess.run(shutdown_command, shell=True, check=True, capture_output=True, text=True)
            messagebox.showinfo("Shutdown Started", "System shutdown process started.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Shutdown Error", f"Failed to shut down system: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def cancel(self):
        messagebox.showinfo("Execution Canceled", "Execution canceled. Exiting...")
        self.master.destroy()

root = tk.Tk()
app = ShutdownApp(root)
root.mainloop()
