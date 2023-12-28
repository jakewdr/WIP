import pygame
import time


class Window:
    def __init__(self, width: int, height: int, fullscreen: int, caption: str):
        self.window = pygame.display.set_mode((width, height), fullscreen, vsync=0)
        # self.window = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF, fullscreen, vsync=0)
        pygame.display.set_caption(caption)
        self.previous_time = time.time()

    def swap_buffers(self):
        pygame.display.flip()

    # def draw(self, sprite: "Sprite"):
    # self.window.blit(sprite.surface, (sprite.position.x, sprite.position.y))

    def clear(self):
        self.window.fill((0, 0, 0))

    def get_dt(self):
        current_time = time.time()
        dt = current_time - self.previous_time
        self.previous_time = current_time
        return dt
