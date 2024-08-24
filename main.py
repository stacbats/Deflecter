import pygame, random

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hulk Deflector")


# SET FPS & CLOCK
FPS = 60
clock = pygame.time.Clock()

# SET GAME VALUES
PLAYER_STARTING_LIVES = 6
HULK_STARTINGLVELOCITY = 5
HULK_ACCELARTION = 1

score = 0
player_lives = PLAYER_STARTING_LIVES

hulk_velocity = HULK_STARTINGLVELOCITY
hulk_dx = random.choice([-1,1])
hulk_dy = random.choice([-1,1])

# SET COLOURS
WHITE = (255,255,255)
GREEN = (0,255,0)
# SET FONTS
font = pygame.font.Font("assets/Franxurter.ttf", 32")
# SET TEXT

# SET SOUND & MUSIC

# SET IMAGES

#  MAIN GAME LOOP
running = True      # setting a boolean value
while running:
    # Checking to see if user wants to quit
    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            running = False

# END THE GAME
pygame.quit()
