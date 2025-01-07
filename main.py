from Screen import Screen
from threading import Thread


def main():
    screen = Screen((64, 64))

    def _action():
        screen.draw_line((1, 1, 32), (1, 1, 1))

    screen.render(_action)


if __name__ == "__main__":
    main()