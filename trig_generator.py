import math
from math import radians
import mcschematic
from mcschematic import MCSchematic


def sin(degree):
    if degree == 30:
        sine = 0.5
    else:
        sine = math.sin(radians(degree))
    sine = int(sine * 0b10000000)
    return sine / 0b10000000


def cos(degree):
    if degree == 60:
        cosine = 0.5
    else:
        cosine = math.cos(radians(degree))
    cosine = int(cosine * 0b10000000)
    return cosine / 0b10000000


def get_trig_bin(trig, degree):
    value = trig(degree)
    value *= 0b10000000
    value = int(value)
    bin_str = bin(value)[2:].zfill(8)
    return [int(i) for i in bin_str]


def get_schem(start, end, trig, file):
    schem = MCSchematic()
    pos = [[0, i - 1, 0] for i in range(0, -15, -2)]
    for degree in range(start, end + 1):
        binary: list = get_trig_bin(trig, degree)
        print(degree, binary)
        for i in range(8):
            if binary[i] == 0:
                schem.setBlock((pos[i][0], pos[i][1], pos[i][2]), "minecraft:barrel[facing=up]")
            elif binary[i] == 1:
                schem.setBlock((pos[i][0], pos[i][1], pos[i][2]), "minecraft:barrel[facing=up]{Items:[{Slot:0b,"
                                                                  "id:'minecraft:redstone',Count:1b}]}")
            pos[i][2] -= 2
    schem.save("./schematics", file, mcschematic.Version.JE_1_19)


def error_analysis():
    for i in range(360):
        try:
            print(abs(sin(i) - math.sin(radians(i))) / abs(math.sin(radians(i))))
            print("-------------------------------------------------------")
            print(i, sin(i), math.sin(radians(i)))
            print("-------------------------------------------------------")
            print(abs(sin(i) - math.sin(radians(i))))
            print("=======================================================")
            print(abs(cos(i) - math.cos(radians(i))) / math.cos(radians(i)))
            print("-------------------------------------------------------")
            print(i, cos(i), math.cos(radians(i)))
            print("-------------------------------------------------------")
            print(abs(cos(i) - math.cos(radians(i))))
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        except ZeroDivisionError:
            pass


def main():
    get_schem(0, 44, sin, "sin_0_44")
    # error_analysis()


if __name__ == "__main__":
    main()
