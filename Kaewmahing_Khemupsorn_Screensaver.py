# Example file showing a basic pygame "game loop"
import pygame
import random
from pygame.draw import circle, line, rect
from pygame.math import Vector2

screen_width = 1270
screen_height = 720

position = Vector2(screen_width/2, screen_height/2 -100)

rect_width = 300
rect_height = 75

radius = 50

speed = 10
ball_vel = 5
ball2_vel_y = 5

# pygame setup
#เริ่มการทำงานPygame
pygame.init()

#RGB
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GRAY = (128,128,128)


#สร้างหน้าจอเกม
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

paddle_rect = pygame.Rect(0, 0, rect_width, rect_height)
paddle_rect.centerx = screen_width // 2
paddle_rect.centery = screen_height // 2 + 250

ball_rect = pygame.Rect(0,0, radius*2, radius*2)
ball_rect.x = random.randint(0,screen_width)
ball_rect.y = 0

ball2_rect = pygame.Rect(0,0, radius*2, radius*2)
ball2_rect.x = random.randint(0,screen_width )
ball2_rect.y = -100

#screen
screen.fill(WHITE)
screen_rect = screen.get_rect()
print(screen_rect.width)




running=True
is_colliderect = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if paddle_rect.colliderect(ball_rect):
        print("Hit")
        ball_rect.x = random.randint(0,screen_width)
        ball_rect.y=0
    
    if paddle_rect.colliderect(ball2_rect):
        ball2_vel_y *= -1
        is_colliderect = True

    keys = pygame.key.get_pressed()
   
    if keys[pygame.K_LEFT] and paddle_rect.left>0:
        paddle_rect.x-=speed
    if keys[pygame.K_RIGHT] and paddle_rect.right<screen_width:
        paddle_rect.x+=speed

    if ball_rect.y < screen_height:
        ball_rect.y+=ball_vel
    else:
        ball_rect.x = random.randint(0,screen_width)
        ball_rect.y=0
    
    ball2_rect.y += ball2_vel_y
    
    if ball2_rect.bottom >= screen_height :
        ball2_vel_y *= -1
        is_colliderect = True
    if is_colliderect == True and  ball2_rect.top <=0 :
        ball2_vel_y *= -1


   
       
    
 

   
    #paddle_rect
    screen.fill(WHITE)
    paddle = rect(screen, RED, paddle_rect) 

    ball = circle(screen, BLUE,ball_rect.center, radius)
    ball2 = circle(screen, GRAY,ball2_rect.center, radius)
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()