import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
from datetime import datetime

class BackupApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Directory Backup Tool")
        self.geometry("600x400")
        self.configure(background='#f0f0f0')

        self.directories_to_backup = []
        self.backup_location = "/path/to/backup/location/"

        self.create_widgets()

    def create_widgets(self):
        # Frame for directory selection
        self.dir_frame = tk.Frame(self, bg='#f0f0f0')
        self.dir_frame.pack(fill='x', padx=10, pady=10)

        self.dir_label = tk.Label(self.dir_frame, text="Directories to Backup:", font=("Helvetica", 14), bg='#f0f0f0')
        self.dir_label.pack(side='left', padx=10)

        self.add_dir_button = tk.Button(self.dir_frame, text="Add Directory", command=self.add_directory)
        self.add_dir_button.pack(side='left', padx=10)

        self.dir_listbox = tk.Listbox(self, selectmode=tk.MULTIPLE, width=80, height=10)
        self.dir_listbox.pack(padx=10, pady=10)

        # Frame for backup location selection
        self.backup_frame = tk.Frame(self, bg='#f0f0f0')
        self.backup_frame.pack(fill='x', padx=10, pady=10)

        self.backup_label = tk.Label(self.backup_frame, text="Backup Location:", font=("Helvetica", 14), bg='#f0f0f0')
        self.backup_label.pack(side='left', padx=10)

        self.backup_entry = tk.Entry(self.backup_frame, width=50)
        self.backup_entry.pack(side='left', padx=10)

        self.backup_button = tk.Button(self.backup_frame, text="Select Location", command=self.select_backup_location)
        self.backup_button.pack(side='left', padx=10)

        # Backup button
        self.backup_button = tk.Button(self, text="Start Backup", command=self.start_backup, bg='#4CAF50', fg='white', font=("Helvetica", 14))
        self.backup_button.pack(pady=20)

    def add_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directories_to_backup.append(directory)
            self.dir_listbox.insert(tk.END, directory)

    def select_backup_location(self):
        location = filedialog.askdirectory()
        if location:
            self.backup_location = location.rstrip('/')  # Remove trailing slash if present
            self.backup_entry.delete(0, tk.END)
            self.backup_entry.insert(0, self.backup_location)
            print(f"Backup location set to: {self.backup_location}")  # Debugging: Print the backup location

    def start_backup(self):
        # Debugging: Print the current state of backup location
        print(f"Backup location at start: {self.backup_location}")

        if not self.directories_to_backup:
            messagebox.showwarning("Warning", "No directories selected for backup.")
            return

        if not self.backup_location or not os.path.isdir(self.backup_location):
            messagebox.showwarning("Warning", "No backup location selected.")
            return

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_dir = os.path.join(self.backup_location, f"backup_{timestamp}")
        os.makedirs(backup_dir, exist_ok=True)

        for directory in self.directories_to_backup:
            if os.path.exists(directory):
                shutil.copytree(directory, os.path.join(backup_dir, os.path.basename(directory)))
                print(f"Backed up {directory} to {backup_dir}")
            else:
                print(f"Directory {directory} does not exist.")
                messagebox.showerror("Error", f"Directory {directory} does not exist.")

        messagebox.showinfo("Success", f"Backup completed successfully to {backup_dir}")

if __name__ == "__main__":
    app = BackupApp()
    app.mainloop()