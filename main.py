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
HULK_STARTING_VELOCITY = 5
HULK_ACCELARTION = 1

score = 0
player_lives = PLAYER_STARTING_LIVES

hulk_velocity = HULK_STARTING_VELOCITY
hulk_dx = random.choice([-1,1])
hulk_dy = random.choice([-1,1])

# SET COLOURS
WHITE = (255,255,255)
GREEN = (0,255,0)
YELLOW = (248, 231, 28)

# SET FONTS
font = pygame.font.Font("assets/Franxurter.ttf",36)
# SET TEXT
title_text = font.render("Catch the Hulk", True, WHITE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 550)

score_text = font.render("Score: " + str(score), True, GREEN)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 550)

lives_text = font.render("HULKS" + str(player_lives), True, WHITE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH -60, 50)

game_over_text = font.render("GAMEOVER", True, WHITE, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Click anywhere to play again", True, YELLOW, WHITE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

# SET SOUND & MUSIC
click_sound = pygame.mixer.Sound("assets/Hulk_Smash.wav")
miss_sound = pygame.mixer.Sound("assets/miss.wav")
pygame.mixer.music.load("assets/drums.wav")

# SET IMAGES
background_image = pygame.image.load("assets/Purple.png")
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

hulk_image = pygame.image.load("assets/HULK.png")
hulk_rect = hulk_image.get_rect()
hulk_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#  MAIN GAME LOOP

pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #A click is made
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            #The HULK was clicked
            if hulk_rect.collidepoint(mouse_x, mouse_y):
                click_sound.play()
                score += 1
                hulk_velocity += HULK_ACCELARTION

                #Move the clown in a new direction
                previous_dx = hulk_dx
                previous_dy = hulk_dy
                while(previous_dx == hulk_dx and previous_dy == hulk_dy):
                    hulk_dx = random.choice([-1, 1])
                    hulk_dy = random.choice([-1, 1])
            #We missed the HULK
            else:
                miss_sound.play()
                player_lives -= 1

    #Move the clown
    hulk_rect.x += hulk_dx*hulk_velocity
    hulk_rect.y += hulk_dy*hulk_velocity

    #Bounce the clown off the edges of the display
    if hulk_rect.left <= 0 or hulk_rect.right >= WINDOW_WIDTH:
        hulk_dx = -1*hulk_dx
    if hulk_rect.top <= 0 or hulk_rect.bottom >= WINDOW_HEIGHT:
        hulk_dy = -1*hulk_dy

    #Update HUD
    score_text = font.render("Score: " + str(score), True, YELLOW)
    lives_text = font.render("HULKS: " + str(player_lives), True, YELLOW)

    #Check for game over
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #Pause the game until the player clicks then reset the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #The player wants to play again.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES

                    hulk_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
                    hulk_velocity = HULK_STARTING_VELOCITY
                    hulk_dx = random.choice([-1, 1])
                    hulk_dy = random.choice([-1, 1])

                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                #The player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
             
    #Blit the background
    display_surface.blit(background_image, background_rect)

    #Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)

    #Blit assets
    display_surface.blit(hulk_image, hulk_rect)

    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()
