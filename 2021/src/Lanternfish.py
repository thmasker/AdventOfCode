class Lanternfish:
    def __init__(self, timer=6):
        self.timer = timer

    def update(self):
        if self.timer == 0:
            self.timer = 6
            return Lanternfish(8)
        else:
            self.timer -= 1
