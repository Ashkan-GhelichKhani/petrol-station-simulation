"""
Author: Ashkan Ghelichkhani
Email: g.ashkan97@gmail.com
GitHub: https://github.com/Ashkan-GhelichKhani
Project: Petrol Station Simulation System
Start Date: December 5, 2020

This module provides functions for plotting simulation results using matplotlib.
"""

import tkinter as tk
from tkinter import messagebox, filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Display 3 key charts inside the tkinter frame
def show_graphs(data, container):
    # Clear previous widgets
    for widget in container.winfo_children():
        widget.destroy()

    # Extract data for charts
    input_times = [d[0] for d in data]  # Entry time of each car
    fuel_reqs = [d[1] for d in data]    # Fuel requested
    wait_times = [d[4] for d in data]   # Wait time before refueling

    # Create figure and subplots
    fig = Figure(figsize=(9, 5), dpi=100)

    # Histogram of waiting times
    ax1 = fig.add_subplot(131)
    ax1.hist(wait_times, bins=10, color="skyblue", edgecolor="black")
    ax1.set_title("Waiting Time Histogram")
    ax1.set_xlabel("Seconds")
    ax1.set_ylabel("Cars")

    # Line plot: cars served over time
    ax2 = fig.add_subplot(132)
    ax2.plot(sorted(input_times), range(1, len(input_times) + 1), color="green")
    ax2.set_title("Cars Served Over Time")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Cars")

    # Scatter plot: arrival time vs fuel requested
    ax3 = fig.add_subplot(133)
    ax3.scatter(input_times, fuel_reqs, color="red", s=10)
    ax3.set_title("Fuel Request per Car")
    ax3.set_xlabel("Arrival Time")
    ax3.set_ylabel("Fuel (liters)")

    # Embed the figure in tkinter
    canvas = FigureCanvasTkAgg(fig, master=container)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # Button to save the charts as image file
    def save_plot():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if file_path:
            fig.savefig(file_path)
            messagebox.showinfo("Saved", f"Charts saved to:\n{file_path}")

    tk.Button(container, text="Save Charts as Image", command=save_plot).pack(pady=5)
