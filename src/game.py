import time

import pygame


class Window:
    def __init__(self, width: int, height: int, fullscreen: int, caption: str):
        self.window = pygame.display.set_mode((width, height), fullscreen)
        pygame.display.set_caption(caption)
        self.previous_time = time.perf_counter_ns()

    def swap_buffers(self):
        pygame.display.flip()

    # def draw(self, sprite: "Sprite"):
    # self.window.blit(sprite.surface, (sprite.position.x, sprite.position.y))

    def clear(self):
        self.window.fill((0, 0, 0))

    def get_dt(self):  # I'm assuming this is delta time
        current_time = time.perf_counter_ns()
        dt = current_time - self.previous_time
        self.previous_time = current_time
        return dt
