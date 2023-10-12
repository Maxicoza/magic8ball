import pygame as pg
import pygame
from random import randint
from pygame.locals import *
import random

#screen size initialization
pygame.init()
pygame.font.init()
screen = pg.display.set_mode((800, 800))

#game state
state = 0

#colors
black = (0, 0, 0)
purple = (128, 0, 128)
darkblue = (0, 0, 128)
white = (255, 255, 255)

# while program running variable
running = True

# text font
text_font = pygame.font.SysFont("Arial", 40)


# the buttons
rect1 = pygame.Rect(200, 400, 400, 100) # the prediction button
rect2 = pygame.Rect(200, 500, 400, 100) # the start game button
rect3 = pygame.Rect(200, 650, 400, 100) # the exit game button
rect4 = pygame.Rect(200, 550, 400, 100) # the back to main menu button


#functions

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, white)
    screen.blit(img, (x, y))



def mainmenuState():
    if state == 0:
        screen.fill(darkblue)
        pg.draw.rect(screen, purple, rect2)
        pg.draw.rect(screen, purple, rect3)
        draw_text("MAGIC 8 BALL", text_font, (0, 0, 0), 100, 100)
        draw_text("Start Game", text_font, (0, 0, 0), 300, 525)
        draw_text("Exit Game", text_font, (0, 0, 0), 300, 675)
        pg.display.flip()

mainmenuState()

def gameState():
    if state == 1:
        screen.fill(darkblue)
        pg.draw.rect(screen, purple, rect1)
        draw_text("Get Magic Prediction", text_font, (0, 0, 0), 215, 425)
        pg.draw.rect(screen, purple, rect4)
        draw_text("Back to Main Menu", text_font, (0, 0, 0), 225, 575)
        pg.display.flip()


def magic8ball():
    answer = random.randint(1,8)
    if answer == 1:
        screen.fill(darkblue)
        pg.draw.rect(screen, purple, rect1)
        draw_text("Get Magic Prediction", text_font, (0, 0, 0), 215, 425)
        draw_text("Without a doubt", text_font, (0, 0, 0), 120, 50)
        pg.draw.rect(screen, purple, rect4)
        draw_text("Back to Main Menu", text_font, (0, 0, 0), 225, 575)
        pg.display.flip()
    elif answer == 2:
        screen.fill(darkblue)
        pg.draw.rect(screen, purple, rect1)
        draw_text("Get Magic Prediction", text_font, (0, 0, 0), 215, 425)
        draw_text("Better not tell you now", text_font, (0, 0, 0), 120, 50)
        pg.draw.rect(screen, purple, rect4)
        draw_text("Back to Main Menu", text_font, (0, 0, 0), 225, 575)
        pg.display.flip()
    elif answer == 3:
        screen.fill(darkblue)
        pg.draw.rect(screen, purple, rect1)
        draw_text("Get Magic Prediction", text_font, (0, 0, 0), 215, 425)
        draw_text("You may rely on it", text_font, (0, 0, 0), 120, 50)
        pg.draw.rect(screen, purple, rect4)
        draw_text("Back to Main Menu", text_font, (0, 0, 0), 225, 575)
        pg.display.flip()
    elif answer == 4:
        screen.fill(darkblue)
        pg.draw.rect(screen, purple, rect1)
        draw_text("Get Magic Prediction", text_font, (0, 0, 0), 215, 425)
        draw_text("Concentrate and ask again", text_font, (0, 0, 0), 120, 50)
        pg.draw.rect(screen, purple, rect4)
        draw_text("Back to Main Menu", text_font, (0, 0, 0), 225, 575)
        pg.display.flip()
    elif answer == 5:
        screen.fill(darkblue)
        pg.draw.rect(screen, purple, rect1)
        draw_text("Get Magic Prediction", text_font, (0, 0, 0), 215, 425)
        draw_text("As I see it, yes", text_font, (0, 0, 0), 120, 50)
        pg.draw.rect(screen, purple, rect4)
        draw_text("Back to Main Menu", text_font, (0, 0, 0), 225, 575)
        pg.display.flip()
    elif answer == 6:
        screen.fill(darkblue)
        pg.draw.rect(screen, purple, rect1)
        draw_text("Get Magic Prediction", text_font, (0, 0, 0), 215, 425)
        draw_text("Outlook not so good", text_font, (0, 0, 0), 120, 50)
        pg.draw.rect(screen, purple, rect4)
        draw_text("Back to Main Menu", text_font, (0, 0, 0), 225, 575)
        pg.display.flip()
    elif answer == 7:
        screen.fill(darkblue)
        pg.draw.rect(screen, purple, rect1)
        draw_text("Get Magic Prediction", text_font, (0, 0, 0), 215, 425)
        draw_text("Outlook good", text_font, (0, 0, 0), 120, 50)
        pg.draw.rect(screen, purple, rect4)
        draw_text("Back to Main Menu", text_font, (0, 0, 0), 225, 575)
        pg.display.flip()
    elif answer == 8:
        screen.fill(darkblue)
        pg.draw.rect(screen, purple, rect1)
        draw_text("Get Magic Prediction", text_font, (0, 0, 0), 215, 425)
        draw_text("My reply is no", text_font, (0, 0, 0), 120, 50)
        pg.draw.rect(screen, purple, rect4)
        draw_text("Back to Main Menu", text_font, (0, 0, 0), 225, 575)
        pg.display.flip()

while running:
    event_list = pygame.event.get() # returns an event list
    for event in event_list:
        if event.type == KEYDOWN and event.key== K_ESCAPE or event.type == QUIT: # if user press Esc
            running = False
            pygame.quit()

        if event.type == MOUSEBUTTONDOWN: # if the user pressed a mouse button
            mouse_pos = pygame.mouse.get_pos() # get the mouse pos

            if rect2.collidepoint(mouse_pos):
                state = 1
                gameState()

            if rect3.collidepoint(mouse_pos):
                running = False
                pygame.quit()

            if rect1.collidepoint(mouse_pos):
                magic8ball()

            if rect4.collidepoint(mouse_pos):
                state = 0
                mainmenuState()
mainmenuState()
