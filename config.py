"""
Author: Ashkan Ghelichkhani
Email: g.ashkan97@gmail.com
GitHub: https://github.com/Ashkan-GhelichKhani
Project: Petrol Station Simulation System
Start Date: December 5, 2020

This file contains default configuration values and project metadata.
"""

# Total time of the simulation in seconds (e.g., 3600 = 1 hour)
DEFAULT_SIM_TIME = 3600

# Number of fuel pumps in the station
DEFAULT_NUM_PUMPS = 4

# Number of nozzles available per pump
DEFAULT_NOZZLES_PER_PUMP = 2

# Total number of cars to simulate during the simulation period
DEFAULT_CAR_COUNT = 200

# Time (in seconds) it takes for a car to stop at the station
DEFAULT_STOP_TIME = 20

# Time (in seconds) it takes to pay after refueling
DEFAULT_PAY_TIME = 30

# Time (in seconds) it takes to leave the station after payment
DEFAULT_LEAVE_TIME = 20

# Minimum liters of fuel requested by a car
DEFAULT_MIN_FUEL = 10

# Maximum liters of fuel requested by a car
DEFAULT_MAX_FUEL = 60

# Increment steps for fuel amounts (e.g., 5 = 10, 15, 20, ..., 60)
DEFAULT_FUEL_STEP = 5