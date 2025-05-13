import pygame
from constants import *
#import os

#print(f"Current working directory: {os.getcwd()}")
#print(f"Files in directory: {os.listdir('.')}")

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
