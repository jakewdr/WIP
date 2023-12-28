import pygame
import random


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
LINECOLOUR = (153, 37, 190)


def check():
    print("Game engine connected :p")


class Collisions:
    def wall_collision(entity, room_rect):
        wall_rebound_acc = 0.83  # Multiplier applied to velocity once rebounded

        if entity.rect.left < room_rect.left:  # If left hand side of player is to left of left side of wall  # type: ignore
            entity.rect.left = room_rect.left  # move player such that its left side is to the right of the wall instantly
            entity.velocity[0] *= -1 * wall_rebound_acc  # reverse velocity in x direction and apply rebound multiplier

        if entity.rect.right > room_rect.right:  # See similar above func for notes
            entity.rect.right = room_rect.right
            entity.velocity[0] *= -1 * wall_rebound_acc

        if entity.rect.top < room_rect.top:
            # entity.rect.top = max(entity.rect.top, room_rect.top)
            entity.rect.top = room_rect.top
            entity.velocity[1] *= -1 * wall_rebound_acc

        if entity.rect.bottom > room_rect.bottom:
            # entity.rect.bottom = min(entity.rect.bottom, room_rect.bottom)
            entity.rect.bottom = room_rect.bottom
            entity.velocity[1] *= -1 * wall_rebound_acc

    def resolve_collision(entity1, entity2, direction):
        _entity_rebound_acc = 0.83  # Multiplier applied to velocity once rebounded, or reciprocal applied if entity hit by faster moving entity in same direction

        if entity2.velocity[direction] != 0 and entity1.velocity[direction] / (entity2.velocity[direction]) < 0:
            entity1.velocity[direction] *= -1 * _entity_rebound_acc
            entity2.velocity[direction] *= -1 * _entity_rebound_acc

        else:
            if abs(entity1.velocity[direction]) < abs(entity2.velocity[direction]):
                entity1.velocity[direction] *= 1 / _entity_rebound_acc
                entity2.velocity[direction] *= -1 * _entity_rebound_acc

            else:
                entity1.velocity[direction] *= -1 * _entity_rebound_acc
                entity2.velocity[direction] *= 1 / _entity_rebound_acc

    def entity_collision_check(entity1, entity2):  # Kinda hard to get ur head round so read comments carefully to understand lol
        if min(abs(entity1.rect.left - entity2.rect.right), abs(entity1.rect.right - entity2.rect.left)) < min(
            abs(entity1.rect.top - entity2.rect.bottom), abs(entity1.rect.bottom - entity2.rect.top)
        ):  # Check that the x distance between them is greater than the y distance between them (as even if they collide in the y direction, they could still have different x coords). Use absolute of the distances otherwise some could be negative
            entity1.rect.center = entity1.previousCoordinates  # move entity to back where it was before collision
            Collisions.resolve_collision(entity1, entity2, 0)

        if min(abs(entity1.rect.left - entity2.rect.right), abs(entity1.rect.right - entity2.rect.left)) > min(abs(entity1.rect.top - entity2.rect.bottom), abs(entity1.rect.bottom - entity2.rect.top)):
            entity1.rect.center = entity1.previousCoordinates
            Collisions.resolve_collision(entity1, entity2, 1)

        if min(abs(entity1.rect.left - entity2.rect.right), abs(entity1.rect.right - entity2.rect.left)) == min(abs(entity1.rect.top - entity2.rect.bottom), abs(entity1.rect.bottom - entity2.rect.top)):  # If colliding exactly diagonally somehow, just move back out and check the next frame
            entity1.rect.center = entity1.previousCoordinates

        # If they collide diagonally, just wait until next frame to check

    def entity_collision(entity1, entities):
        _entity_rebound_acc = 0.83  # Multiplier applied to velocity once rebounded, or reciprocal applied if entity hit by faster moving entity in same direction

        entities = list(entities)
        entities.pop(entities.index(entity1))

        for entity2 in entities:
            if entity1.lastCollided.count(entity2) == 0 and entity1.rect.colliderect(entity2):
                Collisions.entity_collision_check(entity1, entity2)

                entity1.lastCollided.append(entity2)
                entity2.lastCollided.append(entity1)

            elif entity1.lastCollided.count(entity2) > 0 and not entity1.rect.colliderect(entity2):
                entity1.lastCollided.remove(entity2)


# Entity class
class Entity:
    def __init__(self, x, y, width, height, imageMode, color, image):
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = [0.0, 0.0]
        self.lastCollided = []
        self.line_end = None
        self.line_exists = False
        self.imageMode = imageMode
        self.previousCoordinates = self.rect.center

        if self.imageMode == "color":
            self.color = color  # changed back to colour cause i think the images are casing the lag heheheha grrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
        elif self.imageMode == "image":
            self.image = pygame.image.load(image)  # Load the image
            self.image = pygame.transform.scale(self.image, (width, height))

    def apply_gravity(self):
        self.velocity[1] += 0.5  # Adds velocity in downwards dir (down is pos)

    def apply_air_res(self):
        air_res = 0.998
        self.velocity[0] *= air_res
        self.velocity[1] *= air_res

    def accelerate_along_line(self, WIDTH, HEIGHT):  # Uhh idk what this does chat gpt did it so pls comment later
        if self.line_exists and self.line_end:
            direction_vector = pygame.math.Vector2(self.line_end[0] - self.rect.centerx, self.line_end[1] - self.rect.centery + 0.1)
            distance = direction_vector.length()
            direction_vector = direction_vector.normalize()
            base_acceleration = -5.5
            scaled_acceleration = distance * (((WIDTH**2) + (HEIGHT**2)) ** 0.5) * (10 ** (base_acceleration))
            self.velocity[0] += direction_vector.x * scaled_acceleration
            self.velocity[1] += direction_vector.y * scaled_acceleration

    def random_swing(self, player, WIDTH, HEIGHT):
        _random_x = random.randint(0, WIDTH)  # pick a random x-value within box i think (?)
        _random_y = random.randint(0, HEIGHT)  # ^
        # self.line_end = (random_x, random_y) # set line end to random point within box
        self.line_end = player.rect.center  # set line end to random point within box
        self.line_exists = True  # Set the line to existing

    def update(self, entities, room_rect):
        self.previousCoordinates = self.rect.center
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        self.apply_gravity()
        self.apply_air_res()
        Collisions.wall_collision(self, room_rect)
        Collisions.entity_collision(self, entities)

    def draw(self, window, imageMode):
        if imageMode == "color":
            pygame.draw.rect(window, self.color, self.rect)  # changed back to colour cause i think the images are casing the lag # heheheha grrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr  nono more like HEHEHEHEHA GRrrRRrrrrrr
        elif imageMode == "image":
            window.blit(self.image, self.rect)

        if self.line_exists and self.line_end:
            line_start = (self.rect.centerx, self.rect.centery)
            pygame.draw.line(window, LINECOLOUR, line_start, self.line_end, 4)


class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)
