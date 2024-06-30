import tkinter as tk
from tkinter import messagebox, ttk
import getpass
import subprocess
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

    def update_system(self):
        self.progress_bar.start()
        process = subprocess.Popen(["/home/mcuser/scripts/update-system.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        debug_window = tk.Toplevel(self.master)
        debug_window.title("Update System Debug")
        debug_window.geometry("600x400")
        debug_text = tk.Text(debug_window, wrap="word", width=80, height=20)
        debug_text.pack()

        while process.poll() is None:
            output = process.stdout.readline().decode("utf-8").strip()
            if output:
                print(output)
                debug_text.insert(tk.END, output + "\n")
                debug_window.update_idletasks()
            time.sleep(0.1)  # Add a short delay to allow the debug window to update

        self.progress_bar.stop()
        messagebox.showinfo("Shutdown", "Shutting down...")
        subprocess.run(["shutdown", "-h", "now"])

    def cancel(self):
        messagebox.showinfo("Shutdown Canceled", "Shutdown canceled. Exiting...")
        self.master.destroy()

root = tk.Tk()
app = ShutdownApp(root)
root.mainloop()