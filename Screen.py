import pygame
import sys
from Pixel import Pixel

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
            action()
            self._update()
            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def draw(self, pos: tuple):
        self.pixels[pos[0]][pos[1]].on()

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
        self.draw((x, y))
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
            self.draw((x, y))

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
                    pygame.draw.rect(self.screen, BLACK, (i * 10, j * 10, 10, 10))
                else:
                    pygame.draw.rect(self.screen, WHITE, (i * 10, j * 10, 10, 10))
