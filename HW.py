import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.happiness = 50

    def play(self):
        if self.energy >= 10:
            print(f"{self.name}")
            self.energy -= 10
            self.happiness += 5
        else:
            print(f"{self.name}")

    def sleep(self):
        print(f"{self.name}")
        self.energy += 20

    def eat(self):
        print(f"{self.name}")
        self.energy += 10
        self.happiness += 3

    def check_status(self):
        print(f"{self.name}:{self.energy},{self.happiness}")


if __name__ == "__main__":
    cat = Cat("Барсик")

    for _ in range(5):
        action = random.choice(["play", "sleep", "eat"])
        if action == "play":
            cat.play()
        elif action == "sleep":
            cat.sleep()
        elif action == "eat":
            cat.eat()

        cat.check_status()
