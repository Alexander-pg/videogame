import pygame
import random
import os
pygame.font.init()

WIDTH,HEIGHT = 900,600

bg = (0,0,0)

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

WINDOW.fill(bg)

pygame.display.set_caption("THIS IS BLACK SPACE")

FPS = 60

VEL = 8

WHITE=(255,255,255)

BULLETS_VEL = 8

MAX_BALAS = 5

ASTEROID_HIT =pygame.USEREVENT + 1

SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 70,60

SPACESPHIP_IMAGE = pygame.image.load("greybetty.png")

ASTEROID_IMAGE = pygame.image.load("spaceobject.png")

ASTEROID = pygame.transform.scale(ASTEROID_IMAGE,(60,50))

SPACESHIP = pygame.transform.scale(SPACESPHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))

SPACE = pygame.transform.scale(pygame.image.load("universe.jpg"),(WIDTH,HEIGHT))

FONT_SCORE = pygame.font.SysFont("comicsans",40)
FONT_WINNER = pygame.font.SysFont("comicsans",100)

def move_asteroid(astrde,astrde_rain):
    for astrde in astrde_rain:
        astrde.y += 2

        if astrde.y == 600-70:
            astrde_rain.remove(astrde)




def shoot_bullets(ship_bullets,astrde,astrde_rain):
    for bullet in ship_bullets:
        bullet.y -= 5

        if bullet.y <= 10:
            ship_bullets.remove(bullet)

        elif astrde.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ASTEROID_HIT))
            ship_bullets.remove(bullet)
            for astrde in astrde_rain:
                astrde_rain.remove(astrde)

def draw_window(ship,ship_bullets,astrde,astrde_rain,score):
    WINDOW.blit(SPACE, (0, 0))
    WINDOW.blit(SPACESHIP,(ship.x,ship.y))
    #WINDOW.blit(ASTEROID,(astrde.x,astrde.y))

    ship_score_text = FONT_SCORE.render("Score: " + str(score), 1, WHITE)
    WINDOW.blit(ship_score_text, (WIDTH - ship_score_text.get_width() - 10, 10))

    for bullet in ship_bullets:
        pygame.draw.rect(WINDOW,WHITE,bullet)

    for astrde in astrde_rain:
        WINDOW.blit(ASTEROID,(astrde.x,astrde.y))

    pygame.display.update()

def move_ship(key_press,ship):

    if key_press[pygame.K_UP] and ship.y + VEL > 0:
        ship.y -= VEL

    if key_press[pygame.K_DOWN] and ship.y + ship.height +VEL < HEIGHT:
        ship.y += VEL

    if key_press[pygame.K_LEFT] and ship.x + VEL > 0 :
        ship.x -= VEL

    if key_press[pygame.K_RIGHT] and ship.x + ship.width + VEL < WIDTH:
        ship.x += VEL


def appear_winner(text):
    show_text = FONT_WINNER.render(text,1,WHITE)
    WINDOW.blit(show_text,(WIDTH/2 - show_text.get_width()/2,HEIGHT/2 - show_text.get_height()))
    pygame.display.update()
    pygame.time.delay(5000)

def main():

    ship = pygame.Rect(450,400,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    ship_balas=[]

    #astrde = pygame.Rect(random.randrange(WIDTH - 60),(random.randrange(280)),60,50)
    astrde = False

    astrde_rain = []


    run = True
    clock = pygame.time.Clock()

    ship_bullets = []

    score = 0

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    bullet = pygame.Rect(ship.x + ship.width /2,ship.y + ship.height/2,5,20)
                    ship_bullets.append(bullet)

                if event.key == pygame.K_RCTRL:
                    astrde = pygame.Rect(random.randrange(WIDTH - 60),(random.randrange(280)),60,50)
                    astrde_rain.append(astrde)

            if event.type == ASTEROID_HIT:
                score += 1

        winner = ""
        if score == 5:
            winner = "Congrats!"
            appear_winner(winner)
            break

        key_press = pygame.key.get_pressed()



        move_ship(key_press,ship)
        move_asteroid(astrde,astrde_rain)
        shoot_bullets(ship_bullets,astrde,astrde_rain)
        draw_window(ship,ship_bullets,astrde,astrde_rain,score)

    pygame.quit()

if __name__ == "__main__":
    main()
