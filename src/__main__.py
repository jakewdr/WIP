import pygame
import random
import sys
import os







### uhhhhhhhhhhhh ok so basically either have all important vars up here pls at some point ;lol :3ccccccc







# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1080, 720
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)














class Collisions:

    def wall_collision(entity):

        wall_rebound_acc = 0.83 # Multiplier applied to velocity once rebounded

        if entity.rect.left < room_rect.left: # If left hand side of player is to left of left side of wall  # type: ignore
            entity.rect.left = room_rect.left # move player such that its left side is to the right of the wall instantly
            entity.velocity[0] *= -1 * wall_rebound_acc # reverse velocity in x direction and apply rebound multiplier

        if entity.rect.right > room_rect.right: # See similar above func for notes
            entity.rect.right = room_rect.right
            entity.velocity[0] *= -1 * wall_rebound_acc

        if entity.rect.top < room_rect.top:
            #entity.rect.top = max(entity.rect.top, room_rect.top)
            entity.rect.top = room_rect.top
            entity.velocity[1] *= -1 * wall_rebound_acc

        if entity.rect.bottom > room_rect.bottom:
            #entity.rect.bottom = min(entity.rect.bottom, room_rect.bottom)
            entity.rect.bottom = room_rect.bottom
            entity.velocity[1] *= -1 * wall_rebound_acc

    def resolve_collision(entity1, entity2, direction):

        entity_rebound_acc = 0.83  # Multiplier applied to velocity once rebounded, or reciprocal applied if entity hit by faster moving entity in same direction 

        if entity2.velocity[direction] != 0 and entity1.velocity[direction] / (entity2.velocity[direction]) < 0:

            entity1.velocity[direction] *= -1 * entity_rebound_acc
            entity2.velocity[direction] *= -1 * entity_rebound_acc

        else:

            if abs(entity1.velocity[direction]) < abs(entity2.velocity[direction]):
                entity1.velocity[direction] *= 1 / entity_rebound_acc
                entity2.velocity[direction] *= -1 * entity_rebound_acc

            else:

                entity1.velocity[direction] *= -1 * entity_rebound_acc
                entity2.velocity[direction] *= 1 / entity_rebound_acc

    def entity_collision_check(entity1, entity2): # Kinda hard to get ur head round so read comments carefully to understand lol

        if min(abs(entity1.rect.left - entity2.rect.right), abs(entity1.rect.right - entity2.rect.left)) < min(abs(entity1.rect.top - entity2.rect.bottom), abs(entity1.rect.bottom - entity2.rect.top)): #Check that the x distance between them is greater than the y distance between them (as even if they collide in the y direction, they could still have different x coords). Use absolute of the distances otherwise some could be negative

            if abs(entity1.rect.left - entity2.rect.right) < abs(entity1.rect.right - entity2.rect.left): #Then, check that it is the left side of entity1 that is colliding (as even if they collided on the right hand side of entity1, the left side of entity1 would still be past the left side of entity2) by finding the absolute of the differences
                entity1.rect.left = entity2.rect.right + 1 # +1 so that they are not intersecting after moving out to prevent clipping when at rest against each other
                Collisions.resolve_collision(entity1, entity2, 0)

            if abs(entity1.rect.left - entity2.rect.right) > abs(entity1.rect.right - entity2.rect.left):
                entity1.rect.right = entity2.rect.left - 1
                Collisions.resolve_collision(entity1, entity2, 0)

        if min(abs(entity1.rect.left - entity2.rect.right), abs(entity1.rect.right - entity2.rect.left)) > min(abs(entity1.rect.top - entity2.rect.bottom), abs(entity1.rect.bottom - entity2.rect.top)):

            if abs(entity1.rect.top - entity2.rect.bottom) < abs(entity1.rect.bottom - entity2.rect.top):
                entity1.rect.top = entity2.rect.bottom + 1
                Collisions.resolve_collision(entity1, entity2, 1)

            if abs(entity1.rect.top - entity2.rect.bottom) > abs(entity1.rect.bottom - entity2.rect.top):
                entity1.rect.bottom = entity2.rect.top - 1
                Collisions.resolve_collision(entity1, entity2, 1)

        if min(abs(entity1.rect.left - entity2.rect.right), abs(entity1.rect.right - entity2.rect.left)) == min(abs(entity1.rect.top - entity2.rect.bottom), abs(entity1.rect.bottom - entity2.rect.top)):

            if abs(entity1.rect.left - entity2.rect.right) < abs(entity1.rect.right - entity2.rect.left):
                entity1.rect.left = entity2.rect.right + 1
                Collisions.resolve_collision(entity1, entity2, 0)

            if abs(entity1.rect.left - entity2.rect.right) > abs(entity1.rect.right - entity2.rect.left):
                entity1.rect.right = entity2.rect.left - 1
                Collisions.resolve_collision(entity1, entity2, 0)

            if abs(entity1.rect.top - entity2.rect.bottom) < abs(entity1.rect.bottom - entity2.rect.top):
                entity1.rect.top = entity2.rect.bottom + 1
                Collisions.resolve_collision(entity1, entity2, 1)

            if abs(entity1.rect.top - entity2.rect.bottom) > abs(entity1.rect.bottom - entity2.rect.top):
                entity1.rect.bottom = entity2.rect.top - 1
                Collisions.resolve_collision(entity1, entity2, 1)

    def entity_collision(entity1, entities):

        entity_rebound_acc = 0.83  # Multiplier applied to velocity once rebounded, or reciprocal applied if entity hit by faster moving entity in same direction 

        entities = list(entities)
        entities.pop(entities.index(entity1))

        for entity2 in entities:

            if entity1.last_collided.count(entity2) == 0 and entity1.rect.colliderect(entity2):

                Collisions.entity_collision_check(entity1, entity2)

                entity1.last_collided.append(entity2)
                entity2.last_collided.append(entity1)

            elif entity1.last_collided.count(entity2) > 0 and not entity1.rect.colliderect(entity2):
                entity1.last_collided.remove(entity2)





















# Entity class
class Entity:

    def __init__(self, x, y, width, height, imagemode, color, image):
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = [0.0, 0.0]
        self.last_collided = []
        self.line_end = None
        self.line_exists = False
        self.imagemode = imagemode

        if self.imagemode == "color":
            self.color = color  # changed back to colour cause i think the images are casing the lag # heheheha grrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
        elif self.imagemode == "image":
            self.image = pygame.image.load(image)  # Load the image
            self.image = pygame.transform.scale(self.image, (width, height))

    def apply_gravity(self):
        self.velocity[1] += 0.5 # Adds velocity in downwards dir (down is pos)

    def apply_air_res(self):
        air_res = 0.998
        self.velocity[0] *= air_res
        self.velocity[1] *= air_res

    def accelerate_along_line(self): # Uhh idk what this does chat gpt did it so pls comment later
        if self.line_exists and self.line_end:
            direction_vector = pygame.math.Vector2(self.line_end[0] - self.rect.centerx, self.line_end[1] - self.rect.centery + 0.1)
            distance = direction_vector.length()
            direction_vector = direction_vector.normalize()
            base_acceleration = -5.5
            scaled_acceleration = distance * (((WIDTH**2) + (HEIGHT**2))**0.5) * (10**(base_acceleration))
            self.velocity[0] += direction_vector.x * scaled_acceleration
            self.velocity[1] += direction_vector.y * scaled_acceleration





    def random_swing(self, player):
        random_x = random.randint(0, WIDTH) # pick a random x-value within box i think (?)
        random_y = random.randint(0, HEIGHT) # ^
        #self.line_end = (random_x, random_y) # set line end to random point within box
        self.line_end = player.rect.center # set line end to random point within box
        self.line_exists = True # Set the line to existing




    def update(self, entities):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        self.apply_gravity()
        self.apply_air_res()
        Collisions.wall_collision(self)
        Collisions.entity_collision(self, entities)


    def draw(self, screen, imagemode):
        if imagemode == "color":
            pygame.draw.rect(screen, self.color, self.rect) # changed back to colour cause i think the images are casing the lag # heheheha grrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr  nono more like HEHEHEHEHA GRrrRRrrrrrr
        elif imagemode == "image":
            screen.blit(self.image, self.rect)

        if self.line_exists and self.line_end:
            line_start = (self.rect.centerx, self.rect.centery)
            pygame.draw.line(screen, BLACK, line_start, self.line_end, 4)









class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)

    def draw(self,screen):
        pygame.draw.rect(screen, RED, self.rect)








def main():
    global room_rect
                                                #width #height
    wall = Wall(WIDTH //2-4000 , HEIGHT // 2 - 200, 40, 200)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Torsion-alphatest")
    
    scriptPath = str(os.path.realpath(__file__).replace(os.sep, '/')) # Gets the path of the current running python script and makes sure forward-slashes are used
    containingFolder = scriptPath.replace("bundle.py/__main__.py", "") # Removes the bundle and script path from the string

    player = Entity(70, 70, 50, 50, "image", BLUE, containingFolder + "/assets/ble.jpg")
    third_entity = Entity(95, 300, 50, 50, "image",  RED, containingFolder + "/assets/fis.jpg")
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



            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==  3:
                #third_entity.random_swing()
                third_entity.random_swing(player)
        third_entity.random_swing(player)
        #third_entity.random_swing()




        for entity in entities:
            entity.accelerate_along_line()
            entity.update(entities)
            if entity.rect.colliderect(wall.rect): #wall collision thingy 
              entity.velocity[0] *= -1
              entity.velocity[1] *= -1
        

        screen.fill(WHITE)
        pygame.draw.rect(screen, (0, 0, 255), room_rect, 2)

        wall.draw(screen)

        [entity.draw(screen, entity.imagemode) for entity in entities] # List comprehension because we gaming

        pygame.display.flip()
        pygame.time.wait(int(1000/FPS)) # wait is in ms so multiply delta t by 1000


if __name__ == "__main__":
    main()