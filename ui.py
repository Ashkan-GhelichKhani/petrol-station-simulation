"""
Author: Ashkan Ghelichkhani
Email: g.ashkan97@gmail.com
GitHub: https://github.com/Ashkan-GhelichKhani
Project: Petrol Station Simulation System
Start Date: December 5, 2020

This module builds the tkinter-based user interface for configuring and running the simulation.
"""

import tkinter as tk
from tkinter import messagebox
import subprocess

from simulation import Station
from plotting import show_graphs
from config import *

# Run simulation with current input values
def start_simulation_with_gui(entries, graph_frame):
    try:
        values = [int(entry.get()) for entry in entries]
        station = Station(*values)
        station.run()
        show_graphs(station.completed_cars, graph_frame)
        messagebox.showinfo("Simulation Complete", "Simulation finished successfully.\nResults saved in the 'output' folder.")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer values.")

# Try installing matplotlib via pip
def install_matplotlib():
    try:
        subprocess.check_call(["pip", "install", "matplotlib"])
        messagebox.showinfo("Success", "matplotlib has been installed.")
    except Exception as e:
        messagebox.showerror("Installation Failed", f"Error: {e}")

# Build the tkinter window
def build_gui():
    root = tk.Tk()
    root.title("Petrol Station Simulation")
    root.geometry("1080x768")
    root.resizable(True, True)

    # App title
    tk.Label(root, text="Petrol Station Simulation System", font=("Arial", 18, "bold"), pady=20).pack()

    # Form container
    form_frame = tk.Frame(root)
    form_frame.pack(pady=10)

    # Categories and fields
    categories = [
        ("Basic Settings", [
            ("Simulation Time (seconds):", DEFAULT_SIM_TIME),
            ("Number of Cars:", DEFAULT_CAR_COUNT)
        ]),
        ("Pump Configuration", [
            ("Number of Pumps:", DEFAULT_NUM_PUMPS),
            ("Nozzles per Pump:", DEFAULT_NOZZLES_PER_PUMP)
        ]),
        ("Activity Times", [
            ("Stop Time:", DEFAULT_STOP_TIME),
            ("Pay Time:", DEFAULT_PAY_TIME),
            ("Leave Time:", DEFAULT_LEAVE_TIME)
        ]),
        ("Fuel Settings", [
            ("Min Fuel (liters):", DEFAULT_MIN_FUEL),
            ("Max Fuel (liters):", DEFAULT_MAX_FUEL),
            ("Fuel Step:", DEFAULT_FUEL_STEP)
        ])
    ]

    entries = []
    for section, fields in categories:
        section_label = tk.Label(form_frame, text=section, font=("Arial", 12, "bold"))
        section_label.pack(anchor="w", pady=(10, 2))
        group_frame = tk.Frame(form_frame)
        group_frame.pack(fill="x", padx=10)
        for i in range(0, len(fields), 2):
            row_frame = tk.Frame(group_frame)
            row_frame.pack(fill="x", pady=2)
            for j in range(2):
                if i + j < len(fields):
                    label_text, default_value = fields[i + j]
                    tk.Label(row_frame, text=label_text, width=25, anchor="e", padx=5).grid(row=0, column=2 * j)
                    entry = tk.Entry(row_frame)
                    entry.insert(0, str(default_value))
                    entry.grid(row=0, column=2 * j + 1, padx=5)
                    entries.append(entry)

    # Graph output area
    graph_frame = tk.Frame(root)
    graph_frame.pack(padx=10, pady=20, fill="both", expand=True)

    # Control buttons
    tk.Button(root, text="Start Simulation", command=lambda: start_simulation_with_gui(entries, graph_frame)).pack(pady=5)
    tk.Button(root, text="Install matplotlib", command=install_matplotlib).pack(pady=2)

    root.mainloop()
