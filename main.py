import time
import pygame
from selenium import webdriver

pygame.init()

largeText = pygame.font.Font("freesansbold.ttf", 50)

WIDTH = 800
HEIGHT = 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Start/Stop Menu')

driver = webdriver.Firefox(executable_path="/home/david100awesome/Desktop/Web Surfing Bot/geckodriver")
webpage='https://www.walmart.com/ip/PlayStation-5-Console/363472942'
driver.get(webpage)

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, color, widthModifier, heightModifier):
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((WIDTH/2 - widthModifier),(HEIGHT/2 - heightModifier))
    WIN.blit(TextSurf, TextRect)

while True:
    start = True
    go = False

    if start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                driver.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    go = True
        
        WIN.fill((255,255,255))
        message_display("Press Y to start", (0,0,0), 0, 0)
        pygame.display.update()

        while go:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        pygame.quit()
                        go = False

            WIN.fill((255,255,255))
            message_display("Press S to stop", (0,0,0), 0, 0)
            pygame.display.update()

            time.sleep(1)
            driver.refresh()
                
