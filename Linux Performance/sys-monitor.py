import tkinter as tk
from tkinter import ttk
import psutil
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy.interpolate import make_interp_spline

class SystemMonitor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Arch Linux System Monitor")
        self.geometry("600x400")
        # self.iconbitmap('icon.ico')  # Add an icon to the window if you have one
        self.configure(background='#000000')  # Set a background color to black
        
        self.create_widgets()
        self.update_stats()

    def create_widgets(self):
        # Create a frame for the labels
        self.label_frame = tk.Frame(self, bg='#000000')
        self.label_frame.pack(fill='x', padx=10, pady=10)

        self.cpu_label = ttk.Label(self.label_frame, text="CPU Usage: ", font=("DejaVu Sans", 14), foreground='#00FF00', background='#000000')
        self.cpu_label.pack(side='left', padx=10)

        self.memory_label = ttk.Label(self.label_frame, text="Memory Usage: ", font=("DejaVu Sans", 14), foreground='#00FF00', background='#000000')
        self.memory_label.pack(side='left', padx=10)

        self.disk_label = ttk.Label(self.label_frame, text="Disk Usage: ", font=("DejaVu Sans", 14), foreground='#00FF00', background='#000000')
        self.disk_label.pack(side='left', padx=10)

        # Create a frame for the graph
        self.graph_frame = tk.Frame(self, bg='#000000')
        self.graph_frame.pack(fill='both', expand=True, padx=10, pady=20)

        # Create a figure for the CPU usage graph
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.ax.set_facecolor('#000000')
        self.fig.patch.set_facecolor('#000000')
        self.ax.set_title("CPU Usage Over Time", fontdict={'family': 'DejaVu Sans', 'size': 16, 'color': '#00FF00'})
        self.ax.set_xlabel("Time (s)", fontdict={'family': 'DejaVu Sans', 'size': 12, 'color': '#00FF00'})
        self.ax.set_ylabel("CPU Usage (%)", fontdict={'family': 'DejaVu Sans', 'size': 12, 'color': '#00FF00'})
        self.line, = self.ax.plot([], [], lw=2, color='#FFFF00')
        self.x_data, self.y_data = [], []

        # Embed the plot in the Tkinter window
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)

    def update_stats(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')

        self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        self.memory_label.config(text=f"Memory Usage: {memory_info.percent}%")
        self.disk_label.config(text=f"Disk Usage: {disk_info.percent}%")

        # Update the graph data
        self.x_data.append(time.time())
        self.y_data.append(cpu_usage)
        self.x_data = self.x_data[-100:]  # Keep only the last 100 data points
        self.y_data = self.y_data[-100:]

        # Apply a moving average to smooth the data
        if len(self.y_data) > 5:
            y_smooth = np.convolve(self.y_data, np.ones(5)/5, mode='valid')
            x_smooth = self.x_data[:len(y_smooth)]
        else:
            y_smooth = self.y_data
            x_smooth = self.x_data

        # Interpolate to create a smooth curve
        if len(x_smooth) > 3:
            x_new = np.linspace(x_smooth[0], x_smooth[-1], 300)
            spl = make_interp_spline(x_smooth, y_smooth, k=3)
            y_new = spl(x_new)
        else:
            x_new = x_smooth
            y_new = y_smooth

        self.line.set_data(x_new, y_new)
        self.ax.relim()
        self.ax.autoscale_view()

        self.canvas.draw()

        # Update the stats every second
        self.after(1000, self.update_stats)

if __name__ == "__main__":
    app = SystemMonitor()
    app.mainloop()