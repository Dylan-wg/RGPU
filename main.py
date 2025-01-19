from Screen import Screen

theta = 0
t_pos = [0, 0, 0]
k = 1
d = 3


def main():
    screen = Screen((64, 64))

    global theta, t_pos, k, d

    def _action():
        global theta, t_pos, k, d
        origin = (32, 32, 0)
        points = [(16, 16, 16), (16, 16, -16), (48, 16, 16), (48, 16, -16),
                  (16, 48, 16), (16, 48, -16), (48, 48, 16), (48, 48, -16)]
        for i in range(0, 8):
            points[i] = (points[i][0] - origin[0], points[i][1] - origin[1], points[i][2] - origin[2])
            points[i] = screen.rotate(points[i], theta, axes="y")
            points[i] = screen.translation(points[i], t_pos)
            # points[i] = screen.zoom(points[i], k)
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
        t_pos[2] += d
        if t_pos[2] >= 64:
            d = -3
        elif t_pos[2] <= -8:
            d = 3
        k *= 1.01

    screen.render(_action)


if __name__ == "__main__":
    main()