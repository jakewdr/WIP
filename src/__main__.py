# Imports ->

import decoder
import pygame
import cfg
import sys
import os

# Bundled parts imports ->

import game
import engine

game.check()
engine.check()

# Important Paths ->

scriptPath = str(os.path.realpath(__file__).replace(os.sep, "/"))  # Gets the path of the current running python script and makes sure forward-slashes are used
bundlePath = scriptPath.replace("/__main__.py", "")
containingFolder = scriptPath.replace("bundle.py/__main__.py", "")  # Removes the bundle and script path from the string

# Constants - >
WIDTH, HEIGHT = 1080, 720
FPS = 60

# Colours ->
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

coloursConfig = cfg.unpackCfg(containingFolder + "colours.cfg")
BACKGROUNDCOLOUR = coloursConfig.get("background")
LINECOLOUR = coloursConfig.get("line")
WALLCOLOUR = coloursConfig.get("walls")
del coloursConfig


def main():
	print(os.getcwd())
	global room_rect
	# width #height
	wall = engine.Wall(WIDTH // 2 - 4000, HEIGHT // 2 - 200, 40, 200)

	screen = game.Window(WIDTH, HEIGHT, 0, "Torsion-alphatest")

	# screen = pygame.display.set_mode((WIDTH, HEIGHT))
	# pygame.display.set_caption("Torsion-alphatest")

	# window class used for organisational purposes

	Yakuza = decoder.decodeImageFile(containingFolder + "assets/Template.pak", "images/y6.png")
	Neco = decoder.decodeImageFile(containingFolder + "assets/Template.pak", "images/neco.png")

	player = engine.Entity(70, 70, 50, 50, "image", BLUE, Yakuza)
	third_entity = engine.Entity(95, 300, 50, 50, "image", RED, Neco)
	entities = [player, third_entity]

	room_rect = pygame.Rect(50, 50, WIDTH - 100, HEIGHT - 100)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				player.line_end = pygame.mouse.get_pos()
				player.line_exists = not player.line_exists

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
				# third_entity.random_swing(WIDTH, HEIGHT)
				third_entity.random_swing(player)

		for entity in entities:
			entity.accelerate_along_line(WIDTH, HEIGHT)
			entity.update(entities, room_rect)
			if entity.rect.colliderect(wall.rect):  # wall collision thingy
				entity.velocity[0] *= -1
				entity.velocity[1] *= -1

		screen.window.fill(BACKGROUNDCOLOUR)
		pygame.draw.rect(screen.window, WALLCOLOUR, room_rect, 2)

		wall.draw(screen.window)

		[entity.draw(screen.window, entity.imageMode) for entity in entities]  # List comprehension because we gaming

		# Print fps

		pygame.display.update() # Switch th .flip() when GPU rendering :p
		# pygame.time.wait(int( (2*(1000/(FPS))) - (1000/(clock.get_fps() + 1)) )) # clock shenanigans to counter lag - DONT GET RID OF JUST YET PLS
		pygame.time.wait(int(1000 / (FPS)))  # Normal clock, * 1000 cos .wait is in ms


if __name__ == "__main__":
	pygame.init()  # Initialize pygame
	clock = pygame.time.Clock()
	main()
