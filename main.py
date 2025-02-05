from Screen import Screen

theta = 0
d = 3


def main():
    global theta, flag
    screen = Screen((64, 64))

    def _action():
        global theta
        print(theta)
        points = [(16, 16, 16), (16, 16, -16), (48, 16, 16), (48, 16, -16),
                  (16, 48, 16), (16, 48, -16), (48, 48, 16), (48, 48, -16)]
        origin = (32, 32, 0)
        for i in range(0, 8):
            points[i] = (points[i][0] - origin[0], points[i][1] - origin[1], points[i][2] - origin[2])
            # points[i] = screen.rotate(points[i], theta, axes="y")
            points[i] = screen.rotate(points[i], theta, axes="x")
            points[i] = (points[i][0] + origin[0], points[i][1] + origin[1], points[i][2] + origin[2])
        lines = [[points[0], points[1]],
                 [points[2], points[3]],
                 [points[4], points[5]],
                 [points[6], points[7]],
                 [points[0], points[4]],
                 [points[1], points[5]],
                 [points[2], points[6]],
                 [points[3], points[7]],
                 [points[0], points[2]],
                 [points[1], points[3]],
                 [points[4], points[6]],
                 [points[5], points[7]]]
        for line in lines:
            screen.draw_line(line[0], line[1])
        theta += 5
        if theta >= 360:
            theta = 0

    screen.render(_action)


if __name__ == "__main__":
    main()