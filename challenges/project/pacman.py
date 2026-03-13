# Ik typ bij elke functie uitleg voor het makkelijker voor mezelf te maken.

import pygame
import random
import os

pygame.init()

# WIDTH en HEIGHT bepalen de grootte van het scherm.
WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('PAC MAN IN PINKLAND')

# fps bepaalt hoeveel keer per seconde het spel vernieuwt.
fps = 60
timer = pygame.time.Clock()

# Deze fonts gebruiken we voor tekst op het scherm.
font_path = os.path.join(os.path.dirname(__file__), 'PressStart2P-Regular.ttf')
font = pygame.font.Font(font_path, 25)
smaller_font = pygame.font.Font(font_path, 20)
big_font = pygame.font.Font(font_path, 36)


# Kleuren in RGB: (rood, groen, blauw).
yellow = (255, 224, 130)
purple = (186, 85, 211)
pink_bg = (255, 230, 240)
hot_pink = (255, 105, 180)
light_pink = (255, 182, 193)
dark_pink = (199, 21, 133)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (100, 180, 255)

# TILE is de grootte van 1 vakje van het doolhof.
TILE = 44

# In dit bord betekent 1 een muur en 0 een pad met een pellet.
board = [
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

# len(board[0]) telt hoeveel vakjes er in de eerste rij zitten.
maze_width = len(board[0]) * TILE
x_offset = (WIDTH - maze_width) // 2
y_offset = 100

# Deze variabelen onthouden de status van het spel.
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

# Lijst met fruitjes op open vakjes van het bord.
fruits = [(5, 10), (3, 4), (13, 15)]
eaten_fruits = set()

# Dit zijn de pixelposities van speler en ghosts.
player_x = x_offset + TILE + TILE // 2
player_y = y_offset + TILE + TILE // 2

# Elke ghost is een dictionary met x, y, startpositie, richting en kleur.
ghosts = [
    {
        "x": x_offset + 9 * TILE + TILE // 2,
        "y": y_offset + 8 * TILE + TILE // 2,
        "start_x": x_offset + 9 * TILE + TILE // 2,
        "start_y": y_offset + 8 * TILE + TILE // 2,
        "direction": "right",
        "color": light_pink
    },
    {
        "x": x_offset + 15 * TILE + TILE // 2,
        "y": y_offset + 13 * TILE + TILE // 2,
        "start_x": x_offset + 15 * TILE + TILE // 2,
        "start_y": y_offset + 13 * TILE + TILE // 2,
        "direction": "left",
        "color": purple
    },
    {
        "x": x_offset + 5 * TILE + TILE // 2,
        "y": y_offset + 13 * TILE + TILE // 2,
        "start_x": x_offset + 5 * TILE + TILE // 2,
        "start_y": y_offset + 13 * TILE + TILE // 2,
        "direction": "left",
        "color": red
    }
]

# Dit zijn de snelheden in pixels per frame.
player_speed = 4
ghost_speed = 3

# Richting van de speler.
player_direction = "right"

# Een set bewaart unieke waarden; hier bewaren we opgegeten pellets.
eaten_pellets = set()


# reset_positions()
# Deze functie zet alleen de speler en alle spookjes terug op hun startplaats.
# Dit gebruik je als de speler een leven verliest, zonder het hele spel te resetten.
def reset_positions():
    global player_x, player_y, player_direction

    player_x = x_offset + TILE + TILE // 2
    player_y = y_offset + TILE + TILE // 2
    player_direction = "right"

    for ghost in ghosts:
        ghost["x"] = ghost["start_x"]
        ghost["y"] = ghost["start_y"]
        ghost["direction"] = random.choice(["right", "left", "up", "down"])


# reset_game()
# Deze functie start een volledig nieuw spel.
# Score, levens, timers, fruit en pellets worden opnieuw ingesteld.
def reset_game():
    global player_score, lives, paused, game_over, winner
    global power_mode, power_timer, game_over_timer

    player_score = 0
    lives = 3
    paused = False
    game_over = False
    winner = False
    power_mode = False
    power_timer = 0
    game_over_timer = 0
    eaten_pellets.clear()
    eaten_fruits.clear()
    reset_positions()


# draw_scores()
# Deze functie tekent de score en het aantal levens onderaan op het scherm.
def draw_scores():
    screen.blit(smaller_font.render(f'SCORE: {player_score}', True, white), (20, HEIGHT - 80))
    screen.blit(smaller_font.render(f'LIVES: {lives}', True, white), (20, HEIGHT - 40))


# draw_heart()
# Deze functie tekent een klein hartje op een bepaalde plek.
# Die gebruik je als vorm voor de pellets.
def draw_heart(x, y, color):
    pygame.draw.circle(screen, color, (x - 4, y - 2), 4)
    pygame.draw.circle(screen, color, (x + 4, y - 2), 4)
    pygame.draw.polygon(screen, color, [(x - 8, y), (x + 8, y), (x, y + 10)])


# draw_title_hearts()
# Deze functie tekent hartjes rond de titel op het startscherm.
# Door title_timer bewegen ze een klein beetje op en neer.
def draw_title_hearts():
    float_y = (title_timer // 20) % 2

    draw_heart(WIDTH // 2 - 180, 170 - float_y * 4, hot_pink)
    draw_heart(WIDTH // 2 + 180, 170 - float_y * 4, hot_pink)
    draw_heart(WIDTH // 2 - 220, 250 + float_y * 4, light_pink)
    draw_heart(WIDTH // 2 + 220, 250 + float_y * 4, light_pink)


# draw_ghost_shape()
# Deze functie tekent een echt spookje:
# een hoofd, lichaam, golfjes onderaan en ogen.
def draw_ghost_shape(x, y, color):
    pygame.draw.circle(screen, color, (x, y - 6), 14)
    pygame.draw.rect(screen, color, [x - 14, y - 6, 28, 20])
    pygame.draw.circle(screen, color, (x - 9, y + 14), 5)
    pygame.draw.circle(screen, color, (x, y + 14), 5)
    pygame.draw.circle(screen, color, (x + 9, y + 14), 5)
    pygame.draw.circle(screen, white, (x - 5, y - 8), 4)
    pygame.draw.circle(screen, white, (x + 5, y - 8), 4)
    pygame.draw.circle(screen, black, (x - 5, y - 8), 2)
    pygame.draw.circle(screen, black, (x + 5, y - 8), 2)


# draw_board()
# Deze functie tekent het hele doolhof.
# Ze tekent muren, pellets en fruitjes op de juiste plaats.
def draw_board():
    for row in range(len(board)):
        for col in range(len(board[row])):
            x = x_offset + col * TILE
            y = y_offset + row * TILE

            if board[row][col] == 1:
                pygame.draw.rect(screen, dark_pink, [x, y, TILE, TILE], 0, 10)
            elif (row, col) not in eaten_pellets:
                draw_heart(x + TILE // 2, y + TILE // 2 - 2, hot_pink)

            if (row, col) in fruits and (row, col) not in eaten_fruits:
                draw_cherry(x + TILE // 2, y + TILE // 2)
def draw_cherry(x, y):
    pygame.draw.circle(screen, red, (x - 4, y + 2), 5)
    pygame.draw.circle(screen, red, (x + 4, y + 2), 5)
    pygame.draw.line(screen, dark_pink, (x - 4, y - 2), (x, y - 10), 2)
    pygame.draw.line(screen, dark_pink, (x + 4, y - 2), (x, y - 10), 2)
    pygame.draw.line(screen, dark_pink, (x, y - 10), (x + 3, y - 14), 2)



# eat_fruit()
# Deze functie controleert of Pacman op een fruitje staat.
# Als dat zo is, verdwijnt het fruit en wordt power_mode actief.
def eat_fruit():
    global power_mode, power_timer

    col = (player_x - x_offset) // TILE
    row = (player_y - y_offset) // TILE
    current_pos = (row, col)

    if current_pos in fruits and current_pos not in eaten_fruits:
        eaten_fruits.add(current_pos)
        power_mode = True
        power_timer = 300


# draw_player()
# Deze functie tekent Pacman als een cirkel met een mondje.
# Het mondje wijst naar de richting waarin Pacman beweegt.
def draw_player():
    pygame.draw.circle(screen, yellow, (player_x, player_y), 20)

    if player_direction == "right":
        points = [(player_x, player_y), (player_x + 20, player_y - 6), (player_x + 20, player_y + 6)]
    elif player_direction == "left":
        points = [(player_x, player_y), (player_x - 20, player_y - 6), (player_x - 20, player_y + 6)]
    elif player_direction == "up":
        points = [(player_x, player_y), (player_x - 6, player_y - 20), (player_x + 6, player_y - 20)]
    else:
        points = [(player_x, player_y), (player_x - 6, player_y + 20), (player_x + 6, player_y + 20)]

    pygame.draw.polygon(screen, pink_bg, points)


# draw_ghosts()
# Deze functie tekent alle spookjes uit de lijst.
# Als power_mode actief is, worden ze blauw.
def draw_ghosts():
    for ghost in ghosts:
        ghost_color = blue if power_mode else ghost["color"]
        draw_ghost_shape(ghost["x"], ghost["y"], ghost_color)


# draw_game()
# Deze functie tekent de menu's en knoppen van het spel.
# Ze toont:
# - startscherm
# - pauseknop
# - pauzemenu
# - game over scherm
# - winner scherm
# Ze geeft een dictionary met knoppen terug zodat je op klikken kan reageren.
def draw_game():
    buttons = {}

    if not active and not paused and not game_over and not winner:
        draw_title_hearts()

        title_text = big_font.render('PACMAN IN', True, red)
        screen.blit(title_text, title_text.get_rect(center=(WIDTH // 2, 200)))

        subtitle_text = big_font.render('PINKLAND!', True, hot_pink)
        screen.blit(subtitle_text, subtitle_text.get_rect(center=(WIDTH // 2, 250)))

        start_button = pygame.draw.rect(screen, white, [300, 350, 300, 100], 0, 5)
        pygame.draw.rect(screen, hot_pink, [300, 350, 300, 100], 3, 5)
        text = font.render('START', True, black)
        screen.blit(text, text.get_rect(center=start_button.center))
        buttons["start"] = start_button

    if active and not paused and not game_over and not winner:
        pause_button = pygame.draw.rect(screen, white, [20, 20, 180, 60], 0, 5)
        pygame.draw.rect(screen, hot_pink, [20, 20, 180, 60], 3, 5)
        pause_text = smaller_font.render('PAUSE', True, black)
        screen.blit(pause_text, pause_text.get_rect(center=pause_button.center))
        buttons["pause"] = pause_button

    if paused:
        pause_text = big_font.render('PAUSED', True, red)
        screen.blit(pause_text, pause_text.get_rect(center=(WIDTH // 2, 280)))

        resume_button = pygame.draw.rect(screen, white, [280, 380, 340, 80], 0, 5)
        pygame.draw.rect(screen, hot_pink, [280, 380, 340, 80], 3, 5)
        resume_text = font.render('RESUME', True, black)
        screen.blit(resume_text, resume_text.get_rect(center=resume_button.center))
        buttons["resume"] = resume_button

        menu_button = pygame.draw.rect(screen, white, [280, 490, 340, 80], 0, 5)
        pygame.draw.rect(screen, hot_pink, [280, 490, 340, 80], 3, 5)
        menu_text = font.render('MENU', True, black)
        screen.blit(menu_text, menu_text.get_rect(center=menu_button.center))
        buttons["menu"] = menu_button

    if game_over:
        if (game_over_timer // 30) % 2 == 0:
            text = big_font.render('GAME OVER', True, red)
            screen.blit(text, text.get_rect(center=(WIDTH // 2, 350)))

        restart_button = pygame.draw.rect(screen, white, [300, 450, 300, 100], 0, 5)
        pygame.draw.rect(screen, hot_pink, [300, 450, 300, 100], 3, 5)
        restart_text = font.render('RESTART', True, black)
        screen.blit(restart_text, restart_text.get_rect(center=restart_button.center))
        buttons["restart"] = restart_button

    if winner:
        if (game_over_timer // 30) % 2 == 0:
            text = big_font.render('YOU WIN!', True, red)
            screen.blit(text, text.get_rect(center=(WIDTH // 2, 350)))

        restart_button = pygame.draw.rect(screen, white, [300, 450, 300, 100], 0, 5)
        pygame.draw.rect(screen, hot_pink, [300, 450, 300, 100], 3, 5)
        restart_text = font.render('PLAY AGAIN', True, black)
        screen.blit(restart_text, restart_text.get_rect(center=restart_button.center))
        buttons["restart"] = restart_button

    return buttons


# can_move()
# Deze functie controleert of een nieuwe positie geldig is.
# Eerst zet ze pixels om naar row en col op het bord.
# Daarna kijkt ze of die positie binnen het bord ligt en geen muur is.
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


# move_player()
# Deze functie verplaatst Pacman smooth in pixels.
# Ze berekent eerst een nieuwe positie volgens de richting
# en controleert daarna of die positie geldig is.
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


# move_ghost()
# Deze functie verplaatst 1 spookje uit de lijst.
# Als het spook tegen een muur botst, kiest het een nieuwe willekeurige richting.
def move_ghost(ghost):
    new_x = ghost["x"]
    new_y = ghost["y"]

    if ghost["direction"] == "right":
        new_x += ghost_speed
    elif ghost["direction"] == "left":
        new_x -= ghost_speed
    elif ghost["direction"] == "up":
        new_y -= ghost_speed
    elif ghost["direction"] == "down":
        new_y += ghost_speed

    if can_move(new_x, new_y):
        ghost["x"] = new_x
        ghost["y"] = new_y
    else:
        ghost["direction"] = random.choice(["right", "left", "up", "down"])


# eat_pellet()
# Deze functie kijkt of Pacman op een pellet staat.
# Als dat zo is, wordt het pellet toegevoegd aan eaten_pellets
# en stijgt de score met 10 punten.
def eat_pellet():
    global player_score

    col = (player_x - x_offset) // TILE
    row = (player_y - y_offset) // TILE
    pellet = (row, col)

    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        if board[row][col] == 0 and pellet not in eaten_pellets:
            eaten_pellets.add(pellet)
            player_score += 10


# check_win()
# Deze functie kijkt of alle pellets opgegeten zijn.
# Als dat zo is, wint de speler en stopt het actieve spel.
def check_win():
    global winner, active

    total_pellets = 0
    for row in board:
        total_pellets += row.count(0)

    if len(eaten_pellets) == total_pellets:
        winner = True
        active = False


# check_collision()
# Deze functie controleert of Pacman een ghost raakt.
# Als power_mode actief is, eet Pacman het spook en krijgt hij bonuspunten.
# Anders verliest hij een leven.
def check_collision():
    global lives, game_over, active, player_score

    for ghost in ghosts:
        distance = ((player_x - ghost["x"]) ** 2 + (player_y - ghost["y"]) ** 2) ** 0.5

        if distance < 24:
            if power_mode:
                player_score += 50
                ghost["x"] = ghost["start_x"]
                ghost["y"] = ghost["start_y"]
                ghost["direction"] = random.choice(["right", "left", "up", "down"])
            else:
                lives -= 1

                if lives <= 0:
                    game_over = True
                    active = False
                else:
                    reset_positions()
            break


# Dit is de MAIN LOOP van het spel.
# Alles hierin blijft herhalen zolang run True is.
run = True
while run:
    timer.tick(fps)
    screen.fill(pink_bg)

    # Als het spel actief is en niet gepauzeerd, updaten we de game-logica.
    if active and not paused and not game_over and not winner:
        move_player()

        for ghost in ghosts:
            move_ghost(ghost)

        eat_pellet()
        eat_fruit()
        check_collision()
        check_win()

    # Als het spel zichtbaar moet zijn, tekenen we bord, speler, ghosts en score.
    if active or paused or game_over or winner:
        draw_board()
        draw_player()
        draw_ghosts()
        draw_scores()

    # Op het startscherm telt deze timer voor de titel-animatie.
    if not active and not paused and not game_over and not winner:
        title_timer += 1

    buttons = draw_game()

    # Als power_mode actief is, loopt de timer af.
    if power_mode:
        power_timer -= 1
        if power_timer <= 0:
            power_mode = False

    # Deze timer laat GAME OVER en YOU WIN knipperen.
    if game_over or winner:
        game_over_timer += 1
    else:
        game_over_timer = 0

    # Hier verwerken we muisklikken, toetsen en sluiten van het venster.
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
