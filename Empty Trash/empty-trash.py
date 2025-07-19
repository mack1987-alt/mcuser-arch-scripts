# Version 1.6
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext

def display_trash_contents():
    trash_dir = os.path.join(os.path.expanduser('~'), '.local/share/Trash')
    contents = ""
    if os.path.exists(trash_dir):
        for root, dirs, files in os.walk(trash_dir):
            for name in files:
                contents += os.path.join(root, name) + '\n'
            for name in dirs:
                contents += os.path.join(root, name) + '\n'
    else:
        contents = "Trash is empty."
    return contents

def empty_trash():
    trash_dir = os.path.join(os.path.expanduser('~'), '.local/share/Trash')
    deleted_files = 0
    deleted_folders = 0

    if os.path.exists(trash_dir):
        if messagebox.askyesno("Confirm Deletion", "Are you sure you want to empty the trash?"):
            for root, dirs, files in os.walk(trash_dir, topdown=False):
                for name in files:
                    try:
                        os.remove(os.path.join(root, name))
                        deleted_files += 1
                    except Exception as e:
                        print(f"Error deleting file {name}: {e}")
                for name in dirs:
                    try:
                        os.rmdir(os.path.join(root, name))
                        deleted_folders += 1
                    except Exception as e:
                        print(f"Error deleting folder {name}: {e}")
            messagebox.showinfo("Trash Emptied", f"{deleted_files} files and {deleted_folders} folders deleted.")
    else:
        messagebox.showinfo("Trash Empty", "Trash is already empty. Nothing to delete.")
    
    # Update trash contents display
    update_trash_display()

def update_trash_display():
    trash_contents_text.config(state=tk.NORMAL)
    trash_contents_text.delete(1.0, tk.END)
    trash_contents_text.insert(tk.END, display_trash_contents())
    trash_contents_text.config(state=tk.DISABLED)

def main():
    global trash_contents_text

    root = tk.Tk()
    root.title("Empty Trash")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    button = tk.Button(frame, text="Empty Trash", command=empty_trash)
    button.pack(pady=10)

    trash_contents_text = scrolledtext.ScrolledText(frame, width=50, height=20, state=tk.DISABLED)
    trash_contents_text.pack(padx=10, pady=10)

    # Initial display of trash contents
    update_trash_display()

    root.mainloop()

if __name__ == "__main__":
    main()
