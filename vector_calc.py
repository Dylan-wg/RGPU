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


def zoom(vec, k: int) -> tuple:
    return int(vec[0] * k), int(vec[1] * k), int(vec[2] * k)


def translation(vec, t_vec):
    return vec[0] + t_vec[0], vec[1] + t_vec[1], vec[2] + t_vec[2]
