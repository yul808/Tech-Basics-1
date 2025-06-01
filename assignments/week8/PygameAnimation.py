import pygame
import random

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = (255, 255, 255)
CHARACTERS = 10

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Image")
clock = pygame.time.Clock()

# Load and scale image
base_img = pygame.image.load("amongus.png").convert_alpha()
base_img = pygame.transform.scale(base_img, (80, 80))


# Define a class
class AnimatedImage:
    def __init__(self, image, screen):
        self.screen = screen
        self.image = image.copy() #use of .copy() explained to me by chatgpt (still not entirely clear on why its necessary...)

        # Random initial position and speed
        self.x = random.randint(0, SCREEN_WIDTH - 100)
        self.y = random.randint(0, SCREEN_HEIGHT - 100)
        self.speed = random.uniform(2, 6)

        # Random color tint
        color_tint = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
            50)
        self.image.fill(color_tint, special_flags=pygame.BLEND_RGBA_ADD)

    def move(self):
        self.x += self.speed
        if self.x > SCREEN_WIDTH:
            self.x = -80  # Work around, suggested by chatgpt

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


# Multiple instances
animated_objects = [AnimatedImage(base_img, screen) for i in range(CHARACTERS)]

# Main loop
flag = True
while flag:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    screen.fill(BACKGROUND_COLOR)

    for obj in animated_objects: #suggested by chatgpt
        obj.move()
        obj.draw()

    pygame.display.flip()

pygame.quit()

#error message analysis with chatgpt