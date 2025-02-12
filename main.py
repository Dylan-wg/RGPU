from Screen import Screen
from vector_calc import *

theta = 0
d = 3
points = [(12, 12, 40), (12, 12, 0), (52, 12, 40), (52, 12, 0),
          (12, 52, 40), (12, 52, 0), (52, 52, 40), (52, 52, 0)]
origin = (32, 32, 20)


def main():
    global theta, points, theta
    screen = Screen((64, 64))

    def _action():
        global theta, points, theta
        points_copy = points[:]
        if theta == 180:
            for i in range(8):
                points_copy[i] = (points_copy[i][0] - origin[0], points[i][1] - origin[1], points[i][2] - origin[2])
                points_copy[i] = rotate(points_copy[i], theta, axes="y")
                # points_copy[i] = rotate(points_copy[i], theta, axes="x")
                points_copy[i] = (points_copy[i][0] + origin[0], points_copy[i][1] + origin[1], points_copy[i][2] + origin[2])

        # print(theta)
        for i in range(0, 8):
            points_copy[i] = (points_copy[i][0] - origin[0], points[i][1] - origin[1], points[i][2] - origin[2])
            points_copy[i] = rotate(points_copy[i], theta, axes="y")
            # points_copy[i] = rotate(points_copy[i], theta, axes="x")
            points_copy[i] = (points_copy[i][0] + origin[0], points_copy[i][1] + origin[1], points_copy[i][2] + origin[2])
        lines = [[points_copy[0], points_copy[1]],
                 [points_copy[2], points_copy[3]],
                 [points_copy[4], points_copy[5]],
                 [points_copy[6], points_copy[7]],
                 [points_copy[0], points_copy[4]],
                 [points_copy[1], points_copy[5]],
                 [points_copy[2], points_copy[6]],
                 [points_copy[3], points_copy[7]],
                 [points_copy[0], points_copy[2]],
                 [points_copy[1], points_copy[3]],
                 [points_copy[4], points_copy[6]],
                 [points_copy[5], points_copy[7]]]
        for line in lines:
            screen.draw_line(line[0], line[1])
        theta += 5
        if theta > 180:
            theta = 0
    screen.render(_action)


if __name__ == "__main__":
    main()

