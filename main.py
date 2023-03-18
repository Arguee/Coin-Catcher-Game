# Imports
import pygame
from pygame import mixer
import random

# Initialize pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption("Coin Catcher")

# Set icon
icon = pygame.image.load("assets/coin.png")
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load("assets/player.png")
DEFAULT_IMAGE_SIZE = (100, 100)
player = pygame.transform.scale(playerImage, DEFAULT_IMAGE_SIZE)

# Coin
coinImage = pygame.image.load("assets/coin.png")
DEFAULT_COIN_SIZE = (40, 40)
coin = pygame.transform.scale(coinImage, DEFAULT_COIN_SIZE)
coinCollect = pygame.mixer.Sound("sounds/coinCollect.wav")


# Main Loop
def runGame():

    # Coin Pos
    coin_x = 820
    coin_y = random.randrange(60, 538)
    coin_xSpeed = 0.1

    # Score
    score = 0

    # Player Pos 
    player_x = 50
    player_y = 250
    player_ySpeed = 0.1

    # Font
    font = pygame.font.SysFont("comicsansms", 30)
    font1 = pygame.font.SysFont("comicsansms", 80)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #  Movements
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and player_y > 4:
            player_y -= player_ySpeed
        if key[pygame.K_s] and player_y < 495:
            player_y += player_ySpeed

        # Collision of coin and 
        if player_x + 60 > coin_x and player_x < coin_x + 40 and player_y + 60 > coin_y and player_y < coin_y + 40:
            coin_x = 820
            coin_y = random.randrange(60, 538)
            coinCollect.play()
            score = score+1

        # Background
        screen.fill((0, 200, 30))


        # Coin Movement
        if score ==5:
            coin_xSpeed =+ 0.3
            player_ySpeed =+ 0.2
        elif score ==15:
            coin_xSpeed =+ 0.5
            player_ySpeed =+ 0.3
        elif score ==25:
            coin_xSpeed =+ 0.6
            player_ySpeed =+ 0.4
        elif score ==35:
            coin_xSpeed =+ 0.7
            player_ySpeed =+ 0.5
        elif score ==50:
            coin_xSpeed =+ 0.9
            player_ySpeed =+ 0.8
        elif score ==60:
            coin_xSpeed =+ 1.1
            player_ySpeed =+ 1

        coin_x -= coin_xSpeed

        # Scoreboard and blitting
        finalScore = str(score)
        score_text = font.render("Score: " + finalScore, True, (255, 255, 255))
        
        screen.blit(score_text, (650, 10))
        screen.blit(player, (player_x, player_y))
        screen.blit(coin, (coin_x, coin_y))

        # Retry / end Screen
        if coin_x < 0:
            screen.fill((255, 255, 255))
            retry_text = font.render("Press SPACE BAR to retry", True, (0, 255, 100))           
            screen.blit(retry_text, (220, 300))
            score_text = font.render("Score: " + finalScore, True, (0, 0, 0))
            screen.blit(score_text, (330, 250))

            
            over = font1.render("GAME OVER ", True, (255, 0, 0))
            screen.blit(over, (180, 100))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                runGame()
        
        # ! Highscore
        with open("highscore.txt", "r") as f:
            highscore = f.read()
        if int(highscore) < score:
            with open("highscore.txt", "w") as f:
                f.write(str(score))

        # Update the screen
        pygame.time.Clock
        pygame.display.flip()

runGame()
pygame.quit()