class Pixel:

    def __init__(self, pos: tuple):
        self.state = 0
        self.pos: tuple = pos

    def on(self):
        self.state = 1

    def off(self):
        self.state = 0

    def is_on(self) -> bool:
        return self.state == 1
