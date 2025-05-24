"""
Author: Ashkan Ghelichkhani
Email: g.ashkan97@gmail.com
GitHub: https://github.com/Ashkan-GhelichKhani
Project: Petrol Station Simulation System
Start Date: December 5, 2020

This module defines all simulation-related classes, including Car, Nozzle, Pump, and Station.
"""

import random
import csv
import os

# Car class represents each vehicle entering the station
class Car:
    def __init__(self, input_time, stop_time, pay_time, leave_time, min_fuel, max_fuel, fuel_step):
        self.input_time = input_time                      # Time car enters the station
        self.stop_time = stop_time                        # Time to stop at the pump
        self.pay_time = pay_time                          # Time taken to pay
        self.leave_time = leave_time                      # Time to leave after payment
        # Random fuel amount requested within range
        self.req = random.randrange(min_fuel, max_fuel + 1, fuel_step)

    def refuel_time(self):
        # Total time for refueling: fuel duration + stop + pay + leave
        return (self.req * 3) + self.stop_time + self.pay_time + self.leave_time


# Nozzle class simulates a refueling nozzle
class Nozzle:
    def __init__(self):
        self.remaining_time = 0  # Countdown until nozzle is free

    def is_available(self):
        return self.remaining_time == 0  # True if nozzle is ready

    def assign_car(self, duration):
        self.remaining_time = duration  # Occupy nozzle for the refueling duration

    def tick(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1  # Decrease remaining time by one second


# Pump class holds a queue of cars and multiple nozzles
class Pump:
    def __init__(self, nozzle_count):
        self.nozzles = [Nozzle() for _ in range(nozzle_count)]  # List of nozzles
        self.queue = []  # Queue of waiting cars

    def process_queue(self, current_time, completed_cars):
        # Try to assign waiting cars to available nozzles
        for nozzle in self.nozzles:
            if nozzle.is_available() and self.queue:
                car = self.queue.pop(0)
                wait_time = current_time - car.input_time
                duration = car.refuel_time()
                nozzle.assign_car(duration)
                completed_cars.append((
                    car.input_time,  # Entry time
                    car.req,         # Fuel requested
                    duration,        # Refueling time
                    current_time,    # Time assigned to pump
                    wait_time        # Total waiting time
                ))
        # Tick each nozzle to simulate time passing
        for nozzle in self.nozzles:
            nozzle.tick()


# Station class handles the entire simulation logic
class Station:
    def __init__(self, sim_time, car_count, pump_count, nozzles_per_pump, stop_time, pay_time, leave_time, min_fuel, max_fuel, fuel_step):
        self.sim_time = sim_time
        self.car_count = car_count
        self.completed_cars = []  # List of serviced cars
        self.pumps = [Pump(nozzles_per_pump) for _ in range(pump_count)]  # Initialize pumps
        self.input_times = sorted(random.randint(1, sim_time) for _ in range(car_count))  # Car arrival times
        self.stop_time = stop_time
        self.pay_time = pay_time
        self.leave_time = leave_time
        self.min_fuel = min_fuel
        self.max_fuel = max_fuel
        self.fuel_step = fuel_step

    def assign_to_shortest_queue(self, car):
        # Find the pump with the shortest queue and assign the car to it
        shortest_pump = min(self.pumps, key=lambda p: len(p.queue))
        shortest_pump.queue.append(car)

    def run(self):
        tnow = 0
        input_index = 0
        while tnow <= self.sim_time:
            # Check if any car arrives at current time
            while input_index < self.car_count and self.input_times[input_index] == tnow:
                car = Car(tnow, self.stop_time, self.pay_time, self.leave_time, self.min_fuel, self.max_fuel, self.fuel_step)
                self.assign_to_shortest_queue(car)
                input_index += 1
            # Let each pump process its queue for current time step
            for pump in self.pumps:
                pump.process_queue(tnow, self.completed_cars)
            tnow += 1  # Move to the next time unit (second)

         # Save completed cars to CSV
        os.makedirs("output", exist_ok=True)
        with open("output/Refueled.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Input Time", "Fuel Requested", "Refuel Time", "Start Time", "Wait Time"])
            writer.writerows(self.completed_cars)

        # Save remaining queues to separate CSV files
        for i, pump in enumerate(self.pumps):
            with open(f"output/Queue_{i}.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Input Time", "Fuel Requested", "Refuel Time"])
                for car in pump.queue:
                    writer.writerow([
                        car.input_time,
                        car.req,
                        car.refuel_time()
                    ])