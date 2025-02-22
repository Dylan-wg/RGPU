from Screen import Screen
from vector_calc import *
from RAM import *

theta = 0


def main():
    global theta
    screen = Screen((64, 64))
    vec_ram = Vec_RAM(32)
    vec_ram.write((0x0, (-20, -20, 20)),  # vectors
                  (0x1, (-20, -20, -20)),
                  (0x2, (20, -20, 20)),
                  (0x3, (20, -20, -20)),
                  (0x4, (-20, 20, 20)),
                  (0x5, (-20, 20, -20)),
                  (0x6, (20, 20, 20)),
                  (0x7, (20, 20, -20)),  # vectors
                  (0x8, (32, 32, 20)))  # origin
    lines_ram = RAM(32)
    lines_ram.write((0x0, 9),
                    (0x1, 10),
                    (0x2, 11),
                    (0x3, 12),
                    (0x4, 13),
                    (0x5, 14),
                    (0x6, 15),
                    (0x7, 16),
                    (0x8, 9),
                    (0x9, 13),
                    (0xa, 10),
                    (0xb, 14),
                    (0xc, 11),
                    (0xd, 15),
                    (0xe, 12),
                    (0xf, 16),
                    (0x10, 9),
                    (0x11, 11),
                    (0x12, 10),
                    (0x13, 12),
                    (0x14, 13),
                    (0x15, 15),
                    (0x16, 14),
                    (0x17, 16))

    def _action():
        global theta

        for i in range(8):
            vec = rotate(vec_ram.read(i)[0], theta, "x")
            vec_ram.write((i + 9, vec))

        for i in range(0, 24, 2):
            addr1, addr2 = lines_ram.read(i, i+1)
            origin = vec_ram.read(8)[0]
            screen.draw_line(add(vec_ram.read(addr1)[0], origin), add(vec_ram.read(addr2)[0], origin))

        theta += 5
        if theta > 180:
            theta = 0

    screen.render(_action)


if __name__ == "__main__":
    main()

