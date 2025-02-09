import time
import pygame
import sys
from Pixel import Pixel
from trig_generator import sin, cos
# from math import sin, cos, radians

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Screen:

    def __init__(self, size: tuple, d=64):
        self.d = d
        self.size = size
        self.pixels: list[list[Pixel]] = [[Pixel((i, j)) for i in range(0, self.size[0])] for j in range(0, self.size[1])]
        self.screen = pygame.display.set_mode((self.size[0] * 10, self.size[1] * 10))

    def render(self, *args):
        running = True
        self.screen.fill(WHITE)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self._clear()
            self._update()
            pygame.display.flip()

            for i in args:
                i()

            self._update()
            pygame.display.flip()

            time.sleep(0.1)

        pygame.quit()
        sys.exit()

    def _draw(self, pos: tuple):
        try:
            self.pixels[pos[0]][pos[1]].on()
        except IndexError:
            pass

    def draw_point(self, *args):
        for pos in args:
            p = self._projection(pos)
            self.pixels[p[0]][p[1]].on()

    def draw_line(self, in_pos1, in_pos2):
        pos1 = self._projection(in_pos1)
        pos2 = self._projection(in_pos2)

        x = pos1[0]
        y = pos1[1]
        dx = abs(pos2[0] - pos1[0])
        dy = abs(pos2[1] - pos1[1])
        if pos2[0] - pos1[0] < 0:
            s1 = -1
        else:
            s1 = 1
        if pos2[1] - pos1[1] < 0:
            s2 = -1
        else:
            s2 = 1
        if dx < dy:
            dx, dy = dy, dx
            interchange = True
        else:
            interchange = False
        E = 2 * dy - dx
        A = 2 * dy
        B = 2 * dy - 2 * dx
        self._draw((x, y))
        for i in range(1, dx):
            if E < 0:
                if interchange:
                    y += s2
                else:
                    x += s1
                E += A
            else:
                y += s2
                x += s1
                E += B
            self._draw((x, y))

    def _projection(self, pos_3d: tuple) -> tuple:
        d = self.d
        x = pos_3d[0]
        y = pos_3d[1]
        z = pos_3d[2]
        x_p = 32 - ((d * (32 - x)) // (d + z))
        y_p = 32 - ((d * (32 - y)) // (d + z))
        return x_p, y_p

    def _update(self):
        for j in range(0, self.size[1]):
            for i in range(0, self.size[0]):
                if self.pixels[i][j].is_on():
                    pygame.draw.rect(self.screen, BLACK, (i * 10, (self.size[0] - 1 - j) * 10, 10, 10))
                else:
                    pygame.draw.rect(self.screen, WHITE, (i * 10, (self.size[0] - 1 - j) * 10, 10, 10))

    def _clear(self):
        for j in range(0, self.size[1]):
            for i in range(0, self.size[0]):
                self.pixels[i][j].off()
