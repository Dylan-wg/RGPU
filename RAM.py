class RAM:

    def __init__(self, size):
        self.size = size
        self.memory = [0 for i in range(self.size)]

    def read(self, *addr) -> tuple:
        if not addr:
            return tuple(self.memory)
        return tuple([self.memory[i] for i in addr])

    def write(self, *args):
        try:
            for i in args:
                addr, value = i
                self.memory[addr] = value
        except IndexError:
            pass


class Vec_RAM(RAM):

    def __init__(self, size):
        super().__init__(size)
        self.memory = [(0, 0, 0) for i in range(self.size)]

