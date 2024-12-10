import pygame
import sys
import random
def settings():
    global score_1, score_2, game_over, game_state
    
    score_1 = 0

    score_2 = 0
    
    game_state = 3
    game_over = False
def ball_animation():
    global ball_sp_x, ball_sp_y, score_1, score_2
    
    ball.x += ball_sp_x
    ball.y += ball_sp_y


    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_sp_y *= -1
    if ball.left <= 0:
        score_1 = score_1 + score_inc
        ball_restart()
    if ball.right >= screen_width:
        score_2 = score_2 + score_inc
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponet):
        ball_sp_x *= -1
        hit.play()

def player_anamation():

    player.y += player_sp
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opp_anamation():
    opponet.y += opponet_sp
    if opponet.top <= 0:
        opponet.top = 0
    if opponet.bottom >= screen_height:
        opponet.bottom = screen_height

def opp_cpu_animtion():
    if opponet.top < ball.y:
        opponet.top += opp_cpu_sp
    if opponet.bottom >ball.y:
        opponet.bottom -= opp_cpu_sp
    
    if opponet.top <= 0:
        opponet.top = 0
    if opponet.bottom >= screen_height:
        opponet.bottom = screen_height

def ball_restart():
    global ball_sp_y, ball_sp_x
    ball.center = (screen_width/2, screen_height/2)
    ball_sp_y *= random.choice((1, -1))
    ball_sp_x *= random.choice((1,-1))

def startgame():
    global player_sp, opponet_sp, game_state, game_over, score_1, score_2
    
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_sp  +=7
                if event.key == pygame.K_UP:
                    player_sp  -=7
                if event.key == pygame.K_w:
                    opponet_sp -=7
                if event.key == pygame.K_s:
                    opponet_sp +=7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_sp  -=7
                if event.key == pygame.K_UP:
                    player_sp  +=7
                if event.key == pygame.K_w:
                    opponet_sp +=7
                if event.key == pygame.K_s:
                    opponet_sp -=7
            
           
         
    

        ball_animation()
        player_anamation()
        if opp_cpu == 0:
            opp_cpu_animtion()
        if opp_cpu == 1:
            opp_anamation()

        if score_1 == 7 or score_2 == 7:
            game_over = True
            

        
     


    

        
        screen.fill(bg_color)
        font = pygame.font.Font('assets/Orbitron-SemiBold.ttf', 40)
        score_2_type = font.render(f'{score_2}', True, (255,255,255))
        score_1_type = font.render(f' {score_1}', True, (255,255,255))
        pygame.draw.rect(screen, lt_grey, player)
        pygame.draw.rect(screen, lt_grey, opponet)
        pygame.draw.ellipse(screen, lt_grey, ball)
        pygame.draw.aaline(screen, lt_grey, (screen_width/2,0), (screen_width/2,screen_height))
        screen.blit(score_2_type,(screen_width/3 , screen_height/8 ))
        screen.blit(score_1_type,(screen_width/3 *2, screen_height/8))

        if game_over:
            draw_game_over_screen()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
                
                game_state = "game"
                score_1 = 0
                score_2 = 0
                game_over = False
                ball_restart()
        if keys[pygame.K_q]:
                pygame.quit()
                quit()
        if keys[pygame.K_s]:
            settings()
        pygame.display.flip()
        clock.tick(60)

def draw_start_menu():
    screen.fill(bg_color)
    screen.blit(bg_image, (0,0))

    pygame.display.update()

def draw_game_over_screen():
   
   screen.fill((bg_color))
   screen.blit(game_over_img, (0,0))
  
   pygame.display.update()
   
def draw_settings_screen():
    screen.fill(bg_color)
    screen.blit(settings_image, (0,0))

    pygame.display.update()

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
 
pygame.display.set_caption("ty pong")
 
hit = pygame.mixer.Sound("assets/hit.mp3")
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 -15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opponet = pygame.Rect(10, screen_height/2 - 70, 10, 140)

colour = (255, 255, 255)
bg_color = (100,100,100)
lt_grey = (200,200,200)
bg_image = pygame.image.load("assets/main_screen.jpg")
settings_image = pygame.image.load("assets/settings.jpg")
game_over_img = pygame.image.load("assets/game_over.jpg")

ball_sp_x = 7 * random.choice((1, -1))
ball_sp_y = 7 * random.choice((1, -1))

player_sp = 0
opponet_sp = 0
opp_cpu_sp = 7
opp_cpu = 0

game_state = "start_menu"
score_1 = 0
score_2 = 0
score_inc = 1

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           quit()
    if game_state == "start_menu":
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
           game_state = "game"
           game_over = False
        if keys[pygame.K_s]:
            game_state = 3
            game_over =False
        if keys[pygame.K_q]:
           
           pygame.quit()
           quit()
    if game_state == 3:
        draw_settings_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
           game_state = "game"
          
        if keys[pygame.K_r]:
            bg_color = (139, 0, 0)
        if keys[pygame.K_g]:
            bg_color = [0, 139, 0]
        if keys[pygame.K_b]:
            bg_color = (0, 0, 139)
        if keys[pygame.K_k]:
            bg_color = (139, 139, 139)
        if keys[pygame.K_l]:
            bg_color = (0, 0, 0)
        if keys[pygame.K_e]:
            opp_cpu_sp = 6
        if keys[pygame.K_m]:
            opp_cpu_sp = 7
        if keys[pygame.K_h]:
            opp_cpu_sp = 10
        if keys[pygame.K_s]:
            ball_sp_y = 6 * random.choice((1, -1))
            ball_sp_x = 6 * random.choice((1, -1))
            opp_cpu_sp = 6
        if keys[pygame.K_n]:
            ball_sp_y = 7 * random.choice((1, -1))
            ball_sp_x = 7 * random.choice((1, -1))
            opp_cpu_sp = 7
        if keys[pygame.K_f]:
            ball_sp_y = 9 * random.choice((1, -1))
            ball_sp_x = 9 * random.choice((1, -1))
            opp_cpu_sp = 9
        if keys[pygame.K_c]:
            opp_cpu = 0
        if keys[pygame.K_o]:
            opp_cpu = 1
        if keys[pygame.K_q]:
            pygame.quit()
            quit()
    if game_state == "game_over":
        draw_game_over_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
                score_1 = 0
                score_2 = 0
                game_state = "game"
                game_over = False
        if keys[pygame.K_s]:
                score_1 = 0
                score_2 = 0
                game_state = 3
                game_over = False
        if keys[pygame.K_q]:
                pygame.quit()
                quit()
         
                
       

    if game_state == "game":
        
        startgame()

        
            