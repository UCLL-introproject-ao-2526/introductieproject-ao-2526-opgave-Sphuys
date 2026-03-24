## Mijn project is nog altijd gebaseerd op blackjack qua structuur, maar ik heb de inhoud volledig veranderd.
##  De kaartlogica heb ik vervangen door een doolhof, beweging, pellets, spoken, fruit en botsingen. Zo heb ik de 
## tutorial niet gewoon gekopieerd, maar echt aangepast naar een eigen spel met eigen stijl en extra functies.

# Ik typ bij elke functie uitleg voor het makkelijker voor mezelf te maken.

import pygame
import random
import os

pygame.init()

# [feedback verwerkt] Duidelijkere namen gebruikt i.p.v. WIDTH en HEIGHT.
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 950
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('PAC MAN IN PINKLAND')

# fps bepaalt hoeveel keer per seconde het spel vernieuwt.
FPS = 60
timer = pygame.time.Clock()

# Deze fonts gebruiken we voor tekst op het scherm.
font_path = os.path.join(os.path.dirname(__file__), 'PressStart2P-Regular.ttf')
font = pygame.font.Font(font_path, 25)
smaller_font = pygame.font.Font(font_path, 20)
big_font = pygame.font.Font(font_path, 36)

# [feedback verwerkt] Kleuren als constanten in hoofdletters geschreven.
YELLOW = (255, 224, 130)
PURPLE = (186, 85, 211)
PINK_BG = (255, 230, 240)
HOT_PINK = (255, 105, 180)
LIGHT_PINK = (255, 182, 193)
DARK_PINK = (199, 21, 133)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (100, 180, 255)

# TILE is de grootte van 1 vakje van het doolhof.
TILE = 44
# [feedback verwerkt] Herhaalde berekening vervangen door TILE_CENTER.
TILE_CENTER = TILE // 2

# In dit bord betekent 1 een muur en 0 een pad met een pellet.
level_1 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

level_2 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,1,1,0,1,1,1,1,1,0,0,1,1,1,0,1,0,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

current_level = 1
board = level_1

maze_width = len(board[0]) * TILE
x_offset = (SCREEN_WIDTH - maze_width) // 2
y_offset = 100
PLAYER_START_X = x_offset + TILE + TILE_CENTER
PLAYER_START_Y = y_offset + TILE + TILE_CENTER

active = False
paused = False
game_over = False
winner = False
player_score = 0
lives = 3
power_mode = False
power_timer = 0
game_over_timer = 0
title_timer = 0

fruits = [(5, 10), (3, 4), (13, 15)]
eaten_fruits = set()

player_x = PLAYER_START_X
player_y = PLAYER_START_Y

# [feedback verwerkt] Ghosts niet langer als dictionary maar als class.
class Ghost:
    def __init__(self, x, y, start_x, start_y, direction, color):
        self.x = x
        self.y = y
        self.start_x = start_x
        self.start_y = start_y
        self.direction = direction
        self.color = color


ghosts = [
    Ghost(
        x_offset + 9 * TILE + TILE_CENTER,
        y_offset + 8 * TILE + TILE_CENTER,
        x_offset + 9 * TILE + TILE_CENTER,
        y_offset + 8 * TILE + TILE_CENTER,
        "right",
        LIGHT_PINK
    ),
    Ghost(
        x_offset + 15 * TILE + TILE_CENTER,
        y_offset + 13 * TILE + TILE_CENTER,
        x_offset + 15 * TILE + TILE_CENTER,
        y_offset + 13 * TILE + TILE_CENTER,
        "left",
        PURPLE
    ),
    Ghost(
        x_offset + 5 * TILE + TILE_CENTER,
        y_offset + 13 * TILE + TILE_CENTER,
        x_offset + 5 * TILE + TILE_CENTER,
        y_offset + 13 * TILE + TILE_CENTER,
        "left",
        RED
    )
]

player_speed = 4
ghost_speed = 3
player_direction = "right"
eaten_pellets = set()


def reset_positions():
    global player_x, player_y, player_direction

    player_x = PLAYER_START_X
    player_y = PLAYER_START_Y
    player_direction = "right"

    for ghost in ghosts:
        ghost.x = ghost.start_x
        ghost.y = ghost.start_y
        ghost.direction = random.choice(["right", "left", "up", "down"])


def reset_game():
    global player_score, lives, paused, game_over, winner
    global power_mode, power_timer, game_over_timer
    global current_level, board

    player_score = 0
    lives = 3
    paused = False
    game_over = False
    winner = False
    power_mode = False
    power_timer = 0
    game_over_timer = 0

    current_level = 1
    board = level_1

    eaten_pellets.clear()
    eaten_fruits.clear()
    reset_positions()


def draw_scores():
    level_text = smaller_font.render(f'LEVEL {current_level}', True, RED)
    screen.blit(level_text, level_text.get_rect(center=(SCREEN_WIDTH // 2, 40)))

    screen.blit(smaller_font.render(f'SCORE: {player_score}', True, RED), (20, SCREEN_HEIGHT - 80))
    screen.blit(smaller_font.render(f'LIVES: {lives}', True, RED), (20, SCREEN_HEIGHT - 40))


def draw_heart(x, y, color):
    pygame.draw.circle(screen, color, (x - 4, y - 2), 4)
    pygame.draw.circle(screen, color, (x + 4, y - 2), 4)
    pygame.draw.polygon(screen, color, [(x - 8, y), (x + 8, y), (x, y + 10)])


def draw_title_hearts():
    float_y = (title_timer // 20) % 2

    draw_heart(SCREEN_WIDTH // 2 - 180, 170 - float_y * 4, HOT_PINK)
    draw_heart(SCREEN_WIDTH // 2 + 180, 170 - float_y * 4, HOT_PINK)
    draw_heart(SCREEN_WIDTH // 2 - 220, 250 + float_y * 4, LIGHT_PINK)
    draw_heart(SCREEN_WIDTH // 2 + 220, 250 + float_y * 4, LIGHT_PINK)


def draw_ghost_shape(x, y, color):
    pygame.draw.circle(screen, color, (x, y - 6), 14)
    pygame.draw.rect(screen, color, [x - 14, y - 6, 28, 20])
    pygame.draw.circle(screen, color, (x - 9, y + 14), 5)
    pygame.draw.circle(screen, color, (x, y + 14), 5)
    pygame.draw.circle(screen, color, (x + 9, y + 14), 5)
    pygame.draw.circle(screen, WHITE, (x - 5, y - 8), 4)
    pygame.draw.circle(screen, WHITE, (x + 5, y - 8), 4)
    pygame.draw.circle(screen, BLACK, (x - 5, y - 8), 2)
    pygame.draw.circle(screen, BLACK, (x + 5, y - 8), 2)


def draw_cherry(x, y):
    pygame.draw.circle(screen, RED, (x - 4, y + 2), 5)
    pygame.draw.circle(screen, RED, (x + 4, y + 2), 5)
    pygame.draw.line(screen, DARK_PINK, (x - 4, y - 2), (x, y - 10), 2)
    pygame.draw.line(screen, DARK_PINK, (x + 4, y - 2), (x, y - 10), 2)
    pygame.draw.line(screen, DARK_PINK, (x, y - 10), (x + 3, y - 14), 2)


def draw_board():
    for row in range(len(board)):
        for col in range(len(board[row])):
            x = x_offset + col * TILE
            y = y_offset + row * TILE

            if board[row][col] == 1:
                pygame.draw.rect(screen, DARK_PINK, [x, y, TILE, TILE], 0, 10)
            elif (row, col) not in eaten_pellets:
                draw_heart(x + TILE_CENTER, y + TILE_CENTER - 2, HOT_PINK)

            if (row, col) in fruits and (row, col) not in eaten_fruits:
                draw_cherry(x + TILE_CENTER, y + TILE_CENTER)


def eat_fruit():
    global power_mode, power_timer

    col = (player_x - x_offset) // TILE
    row = (player_y - y_offset) // TILE
    current_pos = (row, col)

    if current_pos in fruits and current_pos not in eaten_fruits:
        eaten_fruits.add(current_pos)
        power_mode = True
        power_timer = 300


def draw_player():
    mouth_open = (pygame.time.get_ticks() // 150) % 2

    pygame.draw.circle(screen, YELLOW, (player_x, player_y), 20)

    if player_direction == "right":
        points = [(player_x, player_y), (player_x + 20, player_y - 6), (player_x + 20, player_y + 6)]
    elif player_direction == "left":
        points = [(player_x, player_y), (player_x - 20, player_y - 6), (player_x - 20, player_y + 6)]
    elif player_direction == "up":
        points = [(player_x, player_y), (player_x - 6, player_y - 20), (player_x + 6, player_y - 20)]
    else:
        points = [(player_x, player_y), (player_x - 6, player_y + 20), (player_x + 6, player_y + 20)]

    if mouth_open:
        pygame.draw.polygon(screen, PINK_BG, points)


def draw_ghosts():
    flickering = (pygame.time.get_ticks() // 150) % 2

    for ghost in ghosts:
        if power_mode:
            ghost_color = BLUE if flickering else WHITE
        else:
            ghost_color = ghost.color
        draw_ghost_shape(ghost.x, ghost.y, ghost_color)


def draw_game():
    buttons = {}

    if not active and not paused and not game_over and not winner:
        draw_title_hearts()

        title_text = big_font.render('PACMAN IN', True, RED)
        screen.blit(title_text, title_text.get_rect(center=(SCREEN_WIDTH // 2, 200)))

        subtitle_text = big_font.render('PINKLAND!', True, HOT_PINK)
        screen.blit(subtitle_text, subtitle_text.get_rect(center=(SCREEN_WIDTH // 2, 250)))

        start_button = pygame.draw.rect(screen, WHITE, [300, 350, 300, 100], 0, 5)
        pygame.draw.rect(screen, HOT_PINK, [300, 350, 300, 100], 3, 5)
        text = font.render('START', True, BLACK)
        screen.blit(text, text.get_rect(center=start_button.center))
        buttons["start"] = start_button

    if active and not paused and not game_over and not winner:
        pause_button = pygame.draw.rect(screen, WHITE, [20, 20, 180, 60], 0, 5)
        pygame.draw.rect(screen, HOT_PINK, [20, 20, 180, 60], 3, 5)
        pause_text = smaller_font.render('PAUSE', True, BLACK)
        screen.blit(pause_text, pause_text.get_rect(center=pause_button.center))
        buttons["pause"] = pause_button

    if paused:
        pause_text = big_font.render('PAUSED', True, RED)
        screen.blit(pause_text, pause_text.get_rect(center=(SCREEN_WIDTH // 2, 280)))

        resume_button = pygame.draw.rect(screen, WHITE, [280, 380, 340, 80], 0, 5)
        pygame.draw.rect(screen, HOT_PINK, [280, 380, 340, 80], 3, 5)
        resume_text = font.render('RESUME', True, BLACK)
        screen.blit(resume_text, resume_text.get_rect(center=resume_button.center))
        buttons["resume"] = resume_button

        menu_button = pygame.draw.rect(screen, WHITE, [280, 490, 340, 80], 0, 5)
        pygame.draw.rect(screen, HOT_PINK, [280, 490, 340, 80], 3, 5)
        menu_text = font.render('MENU', True, BLACK)
        screen.blit(menu_text, menu_text.get_rect(center=menu_button.center))
        buttons["menu"] = menu_button

    if game_over:
        if (game_over_timer // 30) % 2 == 0:
            text = big_font.render('GAME OVER', True, RED)
            screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, 350)))

        restart_button = pygame.draw.rect(screen, WHITE, [300, 450, 300, 100], 0, 5)
        pygame.draw.rect(screen, HOT_PINK, [300, 450, 300, 100], 3, 5)
        restart_text = font.render('RESTART', True, BLACK)
        screen.blit(restart_text, restart_text.get_rect(center=restart_button.center))
        buttons["restart"] = restart_button

    if winner:
        if (game_over_timer // 30) % 2 == 0:
            text = big_font.render('YOU WIN!', True, RED)
            screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, 350)))

        restart_button = pygame.draw.rect(screen, WHITE, [300, 450, 300, 100], 0, 5)
        pygame.draw.rect(screen, HOT_PINK, [300, 450, 300, 100], 3, 5)
        restart_text = font.render('PLAY AGAIN', True, BLACK)
        screen.blit(restart_text, restart_text.get_rect(center=restart_button.center))
        buttons["restart"] = restart_button

    return buttons


def can_move(new_x, new_y):
    col = (new_x - x_offset) // TILE
    row = (new_y - y_offset) // TILE

    if row < 0 or row >= len(board):
        return False
    if col < 0 or col >= len(board[0]):
        return False
    if board[row][col] == 1:
        return False
    return True


def move_player():
    global player_x, player_y

    new_x = player_x
    new_y = player_y

    if player_direction == "right":
        new_x += player_speed
    elif player_direction == "left":
        new_x -= player_speed
    elif player_direction == "up":
        new_y -= player_speed
    elif player_direction == "down":
        new_y += player_speed

    if can_move(new_x, new_y):
        player_x = new_x
        player_y = new_y


def move_ghost(ghost):
    new_x = ghost.x
    new_y = ghost.y

    if ghost.direction == "right":
        new_x += ghost_speed
    elif ghost.direction == "left":
        new_x -= ghost_speed
    elif ghost.direction == "up":
        new_y -= ghost_speed
    elif ghost.direction == "down":
        new_y += ghost_speed

    if can_move(new_x, new_y):
        ghost.x = new_x
        ghost.y = new_y
    else:
        ghost.direction = random.choice(["right", "left", "up", "down"])


def eat_pellet():
    global player_score

    col = (player_x - x_offset) // TILE
    row = (player_y - y_offset) // TILE
    pellet = (row, col)

    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        if board[row][col] == 0 and pellet not in eaten_pellets:
            eaten_pellets.add(pellet)
            player_score += 10


def check_win():
    global winner, active, current_level, board

    total_pellets = 0
    for row in board:
        total_pellets += row.count(0)

    if len(eaten_pellets) == total_pellets:
        if current_level == 1:
            current_level = 2
            board = level_2
            eaten_pellets.clear()
            eaten_fruits.clear()
            reset_positions()
        else:
            winner = True
            active = False


def check_collision():
    global lives, game_over, active, player_score

    for ghost in ghosts:
        distance = ((player_x - ghost.x) ** 2 + (player_y - ghost.y) ** 2) ** 0.5

        if distance < 24:
            if power_mode:
                player_score += 50
                ghost.x = ghost.start_x
                ghost.y = ghost.start_y
                ghost.direction = random.choice(["right", "left", "up", "down"])
            else:
                lives -= 1

                if lives <= 0:
                    game_over = True
                    active = False
                else:
                    reset_positions()
            break


run = True
while run:
    timer.tick(FPS)
    screen.fill(PINK_BG)

    if active and not paused and not game_over and not winner:
        move_player()

        for ghost in ghosts:
            move_ghost(ghost)

        eat_pellet()
        eat_fruit()
        check_collision()
        check_win()

    if active or paused or game_over or winner:
        draw_board()
        draw_player()
        draw_ghosts()
        draw_scores()

    if not active and not paused and not game_over and not winner:
        title_timer += 1

    buttons = draw_game()

    if power_mode:
        power_timer -= 1
        if power_timer <= 0:
            power_mode = False

    if game_over or winner:
        game_over_timer += 1
    else:
        game_over_timer = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            if "start" in buttons and buttons["start"].collidepoint(event.pos):
                active = True
                reset_game()

            elif "pause" in buttons and buttons["pause"].collidepoint(event.pos):
                paused = True

            elif "resume" in buttons and buttons["resume"].collidepoint(event.pos):
                paused = False

            elif "menu" in buttons and buttons["menu"].collidepoint(event.pos):
                active = False
                paused = False

            elif "restart" in buttons and buttons["restart"].collidepoint(event.pos):
                active = True
                reset_game()

        if event.type == pygame.KEYDOWN and active and not paused and not game_over and not winner:
            if event.key == pygame.K_RIGHT:
                player_direction = "right"
            elif event.key == pygame.K_LEFT:
                player_direction = "left"
            elif event.key == pygame.K_UP:
                player_direction = "up"
            elif event.key == pygame.K_DOWN:
                player_direction = "down"

    pygame.display.flip()

pygame.quit()
