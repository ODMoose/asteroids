import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():

    pygame.init()

    clock_obj = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True: 
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock_obj.tick(60)/1000

        screen.fill("black")

        player.draw(screen)

        player.update(dt)

        pygame.display.flip()

        


if __name__ == "__main__":
    main()
