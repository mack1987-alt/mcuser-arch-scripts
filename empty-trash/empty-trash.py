import os
import tkinter as tk
from tkinter import messagebox

def empty_trash():
    trash_dir = os.path.join(os.path.expanduser('~'), '.local/share/Trash')
    deleted_files = 0
    deleted_folders = 0

    if os.path.exists(trash_dir):
        print("Trash contents before deletion:")
        for root, dirs, files in os.walk(trash_dir):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))
        if messagebox.askyesno("Confirm Deletion", "Are you sure you want to empty the trash?"):
            for root, dirs, files in os.walk(trash_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                    deleted_files += 1
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
                    deleted_folders += 1
            messagebox.showinfo("Trash Emptied", f"{deleted_files} files and {deleted_folders} folders deleted.")
    else:
        messagebox.showinfo("Trash Empty", "Trash is already empty. Nothing to delete.")

def main():
    root = tk.Tk()
    root.title("Empty Trash")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    button = tk.Button(frame, text="Empty Trash", command=empty_trash)
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()