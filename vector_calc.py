from trig_generator import sin, cos


def rotate(vec, theta=0, axes="z") -> tuple:
    # theta = radians(theta)
    x = r_x = vec[0]
    y = r_y = vec[1]
    z = r_z = vec[2]
    if axes == "z":
        r_x = int(x * cos(theta) - y * sin(theta))
        r_y = int(x * sin(theta) + y * cos(theta))
        return r_x, r_y, r_z
    elif axes == "x":
        r_y = int(y * cos(theta) - z * sin(theta))
        r_z = int(y * sin(theta) + z * cos(theta))
        return r_x, r_y, r_z
    elif axes == "y":
        r_x = int(x * cos(theta) + z * sin(theta))
        r_z = int(- x * sin(theta) + z * cos(theta))
        return r_x, r_y, r_z


def zoom(vec, *args) -> tuple:
    temp = list(vec)
    for i in args:
        for j in range(3):
            temp[j] *= i
    return tuple(temp)


def translation(*args: tuple):
    temp = [0, 0, 0]
    for i in args:
        for j in range(3):
            temp[j] += i[j]
    return temp


def add(vec1, vec2):
    return vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2]


def sub(vec1, vec2):
    return vec1[0] - vec2[0], vec1[1] - vec2[1], vec1[2] - vec2[2]
