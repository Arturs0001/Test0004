import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.15
        self.gladness -= 3
        self.money -= 5

    def to_sleep(self):
        print("Go sleep")
        self.gladness += 3

    def to_chill(self):
        print("Time to chill")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 5

    def work(self):
        print("Time to work")
        earnings = random.randint(10, 50)
        self.money += earnings
        self.gladness -= 5
        self.progress += 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Get out from here!")
            self.alive = False
        elif self.gladness <= 0:
            print("Мне хочется плакать")
            self.alive = False
        elif self.progress > 5:
            print("Passed Externally")
            self.alive = False
            self.gladness += 50

    def end_of_the_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        d = f"Day {day} of {self.name} life"
        print(f"{d:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.work()
        self.end_of_the_day()
        self.is_alive()


nick = Student("Nick")
for day in range(1, 366):
    if not nick.alive:
        break
    nick.live(day)
