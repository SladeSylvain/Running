import pygame
import sys
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = fonty.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 40))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect, initial_speed in obstacle_list:
            obstacle_rect.x -= initial_speed

            if obstacle_rect.bottom >= 300:
                screen.blit(Erizo_surf, obstacle_rect)
            else:
                screen.blit(Pajaro_surf, obstacle_rect)

        obstacle_list = [(obstacle, speed) for obstacle, speed in obstacle_list if obstacle.x > -200]

        return obstacle_list
    else:
        return []

def spawn_obstacle():
    if randint(0, 2):
        return character_2.get_rect(midbottom=(randint(900, 1200), randint(150, 220))), obstacle_speed
    else:
        return character_1.get_rect(midbottom=(randint(900, 1200), 320)), obstacle_speed

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect, _ in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_surface_4
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]

# Inicialización
pygame.init()
Clock = pygame.time.Clock()

# Definición de la pantalla
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Running")
fonty = pygame.font.Font("KdamThmorPro-Regular.ttf", 30)
game_active = True
start_time = 0
score = 0

# Carga de imágenes
sky = pygame.image.load("gif.gif").convert_alpha()
sky = pygame.transform.scale(sky, (800, 400))
ground = pygame.image.load("ground6.xcf").convert_alpha()
ground = pygame.transform.scale(ground, (800, 100))

character = pygame.image.load("gato_1.xcf").convert_alpha()
character = pygame.transform.scale(character, (60, 60))
character = pygame.transform.flip(character, True, False)
character_rect = character.get_rect(midbottom=(2000, 330))

#snowy
snowy = pygame.image.load("Back_1.gif").convert_alpha()
snowy = pygame.transform.scale(snowy,(800,400))

# Erizo
character_1 = pygame.image.load("personaje_1.1.xcf").convert_alpha()
character_1_1 = pygame.image.load("personaje_2_1.xcf").convert_alpha()
character_1_2 = pygame.image.load("personaje_3_1.xcf").convert_alpha()
character_1_3 = pygame.image.load("personaje_4_1.xcf").convert_alpha()

character_1 = pygame.transform.scale(character_1, (40, 40))
character_1_1 = pygame.transform.scale(character_1_1, (40, 40))
character_1_2 = pygame.transform.scale(character_1_2, (40, 40))
character_1_3 = pygame.transform.scale(character_1_3, (40, 40))

character_1 = pygame.transform.flip(character_1, True, False)
character_1_1 = pygame.transform.flip(character_1_1, True, False)
character_1_2 = pygame.transform.flip(character_1_2, True, False)
character_1_3 = pygame.transform.flip(character_1_3, True, False)

character_1_rect = character_1.get_rect(midbottom=(900, 320))

Erizo_frames = [character_1, character_1_1, character_1_2, character_1_3]
Erizo_frames_index = 0
Erizo_surf = Erizo_frames[Erizo_frames_index]

character_2 = pygame.image.load("Pajaro_1.xcf").convert_alpha()
character_2_1 = pygame.image.load("Pajaro_2.xcf").convert_alpha()

character_2 = pygame.transform.scale(character_2, (60, 60))
character_2_1 = pygame.transform.scale(character_2_1, (60, 60))

character_2 = pygame.transform.flip(character_2, True, False)
character_2_1 = pygame.transform.flip(character_2_1, True, False)
character_2_rect = character_2.get_rect(midbottom=(1400, 100))

Pajaro_frames = [character_2, character_2_1]
Pajaro_frames_index = 0
Pajaro_surf = Pajaro_frames[Pajaro_frames_index]

obstacle_rect_list = []

player_surface_1 = pygame.image.load("Racoon_1.xcf").convert_alpha()
player_surface_2 = pygame.image.load("Racoon_2.xcf").convert_alpha()
player_surface_3 = pygame.image.load("Racoon_1.xcf").convert_alpha()

player_surface_2 = pygame.transform.scale(player_surface_2, (85, 85))
player_surface_1 = pygame.transform.scale(player_surface_1, (85, 85))
player_surface_3 = pygame.transform.scale(player_surface_3, (85, 85))

player_walk = [player_surface_1, player_surface_2, player_surface_3]
player_index = 0
player_surface_4 = pygame.image.load("Racoon_1.xcf").convert_alpha()
player_surface_4 = pygame.transform.scale(player_surface_4, (85, 85))

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 2
player_rect.height = 60
player_rect.width = 60

player_stand = pygame.image.load("Fullbodynoknok.xcf").convert_alpha()
player_stand = pygame.transform.scale(player_stand, (300, 300))
player_stand_rect = player_stand.get_rect(center=(400, 200))

text = fonty.render("Try Again", False, (0, 0, 0))
text_rect = text.get_rect(center=(200, 250))
text_2 = fonty.render("Press Space", False, (0, 0, 0))
text_rect_2 = text.get_rect(center=(600, 250))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1987)

Erizo_animation_timer = pygame.USEREVENT + 4
pygame.time.set_timer(Erizo_animation_timer, 500)

Pajaro_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(Pajaro_animation_timer, 200)

speed_increase_timer = pygame.USEREVENT 
pygame.time.set_timer(speed_increase_timer, 800)  # Cada 1000 milisegundos (1 segundo)

# Audios
pygame.mixer.init()  # Inicializar el módulo mixer
musica_fondo = pygame.mixer.music.load("music_1.mp3")
musica_fondo = pygame.mixer_music.play(-1)

## Salto

# Velocidad inicial de los obstáculos
obstacle_speed = 5

# Velocidad de fondo
background_speed = 2
background_x = 0

# Velocidad de suelo
ground_speed = 10
ground_x = 0

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 290:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
                pygame.mixer.music.play(-1)  # Volver a reproducir la música al comenzar una nueva partida

        if game_active:
            if event.type == obstacle_timer:
                obstacle_rect_list.append(spawn_obstacle())

            if event.type == Erizo_animation_timer:
                Erizo_frames_index = (Erizo_frames_index + 1) % len(Erizo_frames)
                Erizo_surf = Erizo_frames[Erizo_frames_index]

            if event.type == Pajaro_animation_timer:
                Pajaro_frames_index = (Pajaro_frames_index + 1) % len(Pajaro_frames)
                Pajaro_surf = Pajaro_frames[Pajaro_frames_index]

            if event.type == speed_increase_timer:
                # Aumentar la velocidad cada segundo
                obstacle_speed += 0.4

    if game_active:
        # Actualizar la posición del fondo y suelo
        background_x -= background_speed
        ground_x -= ground_speed

        # Dibujar el cielo
        screen.blit(sky, (background_x % sky.get_width() - sky.get_width(), 0))
        screen.blit(sky, (background_x % sky.get_width(), 0))

        # Dibujar el suelo
        screen.blit(ground, (ground_x % ground.get_width() - ground.get_width(), 300))
        screen.blit(ground, (ground_x % ground.get_width(), 300))

        score = display_score()
        display_score()

        screen.blit(player_surf, player_rect)
        screen.blit(character, character_rect)
        screen.blit(character_1, character_1_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        player_animation()
        if player_rect.bottom >= 290:
            player_rect.bottom = 290

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_active = collisions(player_rect, obstacle_rect_list)

        # Restablecer la velocidad de los obstáculos después de perder
        if not game_active:
            obstacle_speed = 5

    else:
        screen.blit(snowy,(0,0))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 350)
        player_gravity = 0

        score_message = fonty.render(f"Score: {score}", False, (0, 0, 0))
        score_message_rect = score_message.get_rect(center=(400, 380))
        screen.blit(score_message, score_message_rect)
        screen.blit(text, text_rect)
        screen.blit(text_2, text_rect_2)
        pygame.mixer.music.fadeout(2000)

    pygame.display.update()
    Clock.tick(60)
