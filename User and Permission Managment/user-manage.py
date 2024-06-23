import subprocess
import tkinter as tk
from tkinter import messagebox

def add_new_user():
    username = username_entry.get()
    password = password_entry.get()

    subprocess.run(['sudo', 'useradd', '-m', username])
    subprocess.run(['sudo', 'chpasswd'], input=f'{username}:{password}\n', text=True)
    subprocess.run(['sudo', 'usermod', '-aG', 'wheel', username])

    messagebox.showinfo("User Added", f"User '{username}' has been successfully added.")

root = tk.Tk()
root.title("Add New User")

username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

add_user_button = tk.Button(root, text="Add User", command=add_new_user)
add_user_button.pack()

root.mainloop()