class Light:
    def __init__(self, name):
        self.name = name

    def on(self):
        print(f"{self.name} is on")

    def off(self):
        print(f"{self.name} is off")


class Fan:
    def __init__(self, name):
        self.name = name
        self.current_speed = None

    def on(self):
        self.current_speed = 3
        print(f"{self.name} is on at {self.current_speed}")

    def faster(self):
        self.current_speed += 1 if self.current_speed < 5 else 0
        print(f"{self.name} spins faster at {self.current_speed}")

    def slower(self):
        self.current_speed -= 1 if self.current_speed > 0 else 0
        print(f"{self.name} spins slower at {self.current_speed}")

    def off(self):
        self.current_speed = None
        print(f"{self.name} is off")
