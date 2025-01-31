import math
import threading
import time

import pygame
import sys
from Pixel import Pixel
from math import sin, cos, radians

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Screen:

    def __init__(self, size: tuple):
        self.size = size
        self.pixels: list[list[Pixel]] = [[Pixel((i, j)) for i in range(0, self.size[0])] for j in range(0, self.size[1])]
        self.screen = pygame.display.set_mode((self.size[0] * 10, self.size[1] * 10))

    def render(self, action):
        running = True
        self.screen.fill(WHITE)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self._clear()
            self._update()
            pygame.display.flip()

            action()
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

    @staticmethod
    def rotate(vec, theta=0, axes="z") -> tuple:
        theta = radians(theta)
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

    @staticmethod
    def zoom(vec, k: int) -> tuple:
        return int(vec[0] * k), int(vec[1] * k), int(vec[2] * k)

    @staticmethod
    def translation(vec, t_vec):
        return vec[0] + t_vec[0], vec[1] + t_vec[1], vec[2] + t_vec[2]

    @staticmethod
    def _projection(pos_3d: tuple, d=64) -> tuple:
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
