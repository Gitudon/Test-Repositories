import random
import time


class CicadaLifeCycle:
    def __init__(self, underground_years=random.randint(1, 20)):
        self.underground_years = underground_years
        self.age = 0
        self.above_ground = False

    def live_one_year(self):
        self.age += 1
        if self.age == self.underground_years:
            self.above_ground = True
            print(
                f"After {self.age} years underground, the cicada emerges above ground."
            )
        elif self.above_ground:
            print("The cicada enjoys its short time above ground.")
        else:
            print(f"The cicada is still underground, growing. Age: {self.age} years.")

    def complete_life_cycle(self):
        while self.age < self.underground_years + 1:
            self.live_one_year()
            time.sleep(1)  # Wait for 1 second between each year for simulation
        print("The cicada's brief time above ground has ended.")


if __name__ == "__main__":
    # Create a cicada and simulate its life cycle
    cicada = CicadaLifeCycle()
    cicada.complete_life_cycle()
