import pygame
import random
import sys

# Initsialiseeri Pygame
pygame.init()

# Algse ekraani seaded
screen_width = 800  # Algne laius
screen_height = 600  # Algne kõrgus
screen = pygame.display.set_mode((screen_width, screen_height))  # Mitte täisekraan
pygame.display.set_caption('Ussi Mäng')

# Lae legendi pilt
legend_image = pygame.image.load("Legend.png")
legend_width, legend_height = legend_image.get_size()

# Funktsioon legendi akna avamiseks
def open_legend():
    legend_screen = pygame.display.set_mode((legend_width, legend_height))
    legend_screen.blit(legend_image, (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Tagasi algmenüüsse klahviga "Q"
                    pygame.display.set_mode((screen_width, screen_height))  # Taasta peamise mänguakna suurus
                    main_menu()

# Värvid
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 165, 0)
purple = (128, 0, 128)
dark_red = (139, 0, 0)  # Mürgise toidu värv

# Vikerkaare värvid
rainbow_colors = [red, orange, yellow, green, blue, purple]

# Fontid
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Ussi bloki suurus
snake_block = 10

# Funktsioon sõnumi kuvamiseks
def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [x, y])

# Ussi joonistamine
def draw_snake(snake_list, color):
    for x in snake_list:
        pygame.draw.rect(screen, color, [x[0], x[1], snake_block, snake_block])

# Söögi asukoha genereerimine
def generate_food():
    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
    return foodx, foody

# Eriliste toitude genereerimine
def generate_special_food():
    food_type = random.choice(['multiplier', 'poison'])
    foodx, foody = generate_food()
    return foodx, foody, food_type

# Mängu tsükkel
def gameLoop(infinite_mode=False, difficulty="easy", multiplayer=False):
    global snake_block
    game_over = False
    game_close = False

    x1, y1 = screen_width / 2, screen_height / 2
    x2, y2 = screen_width / 3, screen_height / 3 if multiplayer else (None, None)
    x1_change, y1_change = 0, 0
    x2_change, y2_change = 0, 0 if multiplayer else (None, None)

    snake_list1, snake_list2 = [], []
    snake_length1, snake_length2 = 1, 1

    foodx, foody = generate_food()
    special_foodx, special_foody, special_food_type = generate_special_food()

    clock = pygame.time.Clock()
    if difficulty == "easy":
        snake_speed = 15
    elif difficulty == "normal":
        snake_speed = 20
    elif difficulty == "hard":
        snake_speed = 25

    direction1, direction2 = None, None

    score1, score2 = 0, 0
    multiplier_active, multiplier_timer = False, 0
    rainbow_index1, rainbow_index2 = 0, 0

    while not game_over:

        while game_close:
            screen.fill(black)
            message("Kaotasid! Vajuta Q lõpetamiseks või C uuesti mängimiseks", red, screen_width / 6, screen_height / 3)
            message("Vajuta M, et minna algmenüüsse", red, screen_width / 6, screen_height / 3 + 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop(infinite_mode, difficulty, multiplayer)
                    if event.key == pygame.K_m:
                        return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if direction1 != "RIGHT":
                        x1_change = -snake_block
                        y1_change = 0
                        direction1 = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    if direction1 != "LEFT":
                        x1_change = snake_block
                        y1_change = 0
                        direction1 = "RIGHT"
                elif event.key == pygame.K_UP:
                    if direction1 != "DOWN":
                        y1_change = -snake_block
                        x1_change = 0
                        direction1 = "UP"
                elif event.key == pygame.K_DOWN:
                    if direction1 != "UP":
                        y1_change = snake_block
                        x1_change = 0
                        direction1 = "DOWN"
                
                if multiplayer:
                    if event.key == pygame.K_a:
                        if direction2 != "RIGHT":
                            x2_change = -snake_block
                            y2_change = 0
                            direction2 = "LEFT"
                    elif event.key == pygame.K_d:
                        if direction2 != "LEFT":
                            x2_change = snake_block
                            y2_change = 0
                            direction2 = "RIGHT"
                    elif event.key == pygame.K_w:
                        if direction2 != "DOWN":
                            y2_change = -snake_block
                            x2_change = 0
                            direction2 = "UP"
                    elif event.key == pygame.K_s:
                        if direction2 != "UP":
                            y2_change = snake_block
                            x2_change = 0
                            direction2 = "DOWN"

        if infinite_mode:
            if x1 >= screen_width:
                x1 = 0
            elif x1 < 0:
                x1 = screen_width - snake_block
            elif y1 >= screen_height:
                y1 = 0
            elif y1 < 0:
                y1 = screen_height - snake_block
            if multiplayer:
                if x2 >= screen_width:
                    x2 = 0
                elif x2 < 0:
                    x2 = screen_width - snake_block
                elif y2 >= screen_height:
                    y2 = 0
                elif y2 < 0:
                    y2 = screen_height - snake_block
        else:
            if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
                game_close = True
            if multiplayer:
                if x2 >= screen_width or x2 < 0 or y2 >= screen_height or y2 < 0:
                    game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        if special_food_type == 'multiplier':
            pygame.draw.rect(screen, yellow, [special_foodx, special_foody, snake_block, snake_block])
        elif special_food_type == 'poison':
            pygame.draw.rect(screen, dark_red, [special_foodx, special_foody, snake_block, snake_block])

        snake_head1 = [x1, y1]
        snake_list1.append(snake_head1)
        if len(snake_list1) > snake_length1:
            del snake_list1[0]

        for x in snake_list1[:-1]:
            if x == snake_head1:
                game_close = True

        draw_snake(snake_list1, rainbow_colors[rainbow_index1 % len(rainbow_colors)])
        score_text1 = score_font.render("Score 1: " + str(score1), True, white)
        screen.blit(score_text1, [10, 10])

        if multiplayer:
            x2 += x2_change
            y2 += y2_change  # Lisatud liikumine y2 jaoks
            snake_head2 = [x2, y2]
            snake_list2.append(snake_head2)
            if len(snake_list2) > snake_length2:
                del snake_list2[0]

            for x in snake_list2[:-1]:
                if x == snake_head2:
                    game_close = True

            draw_snake(snake_list2, rainbow_colors[rainbow_index2 % len(rainbow_colors)])
            score_text2 = score_font.render("Score 2: " + str(score2), True, white)
            screen.blit(score_text2, [10, 40])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food()
            snake_length1 += 1
            score1 += 1 if not multiplier_active else 2
            rainbow_index1 += 1

        if x1 == special_foodx and y1 == special_foody:
            if special_food_type == 'multiplier':
                multiplier_active = True
                multiplier_timer = 100  # Aktiivne 100 tsüklit
            elif special_food_type == 'poison':
                snake_length1 = max(1, snake_length1 - 1)
                score1 = max(0, score1 - 1)
            special_foodx, special_foody, special_food_type = generate_special_food()

        if multiplayer:
            if x2 == foodx and y2 == foody:
                foodx, foody = generate_food()
                snake_length2 += 1
                score2 += 1 if not multiplier_active else 2
                rainbow_index2 += 1

            if x2 == special_foodx and y2 == special_foody:
                if special_food_type == 'multiplier':
                    multiplier_active = True
                    multiplier_timer = 100
                elif special_food_type == 'poison':
                    snake_length2 = max(1, snake_length2 - 1)
                    score2 = max(0, score2 - 1)
                special_foodx, special_foody, special_food_type = generate_special_food()

        if multiplier_active:
            multiplier_timer -= 1
            if multiplier_timer <= 0:
                multiplier_active = False

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Vali mängurežiim ja raskusaste
def choose_game_mode(multiplayer=False):
    mode_selected = False
    while not mode_selected:
        screen.fill(black)
        message("Vali mängurežiim:", white, screen_width / 4, screen_height / 4)
        message("1 - Infinite Gamemode", white, screen_width / 4, screen_height / 2)
        message("2 - Normal Gamemode", white, screen_width / 4, screen_height / 2 + 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = choose_difficulty()
                    gameLoop(infinite_mode=True, difficulty=difficulty, multiplayer=multiplayer)
                    mode_selected = True
                elif event.key == pygame.K_2:
                    difficulty = choose_difficulty()
                    gameLoop(infinite_mode=False, difficulty=difficulty, multiplayer=multiplayer)
                    mode_selected = True

# Vali raskusaste
def choose_difficulty():
    difficulty_selected = False
    difficulty = "easy"
    while not difficulty_selected:
        screen.fill(black)
        message("Vali raskusaste:", white, screen_width / 4, screen_height / 4)
        message("1 - Easy", white, screen_width / 4, screen_height / 2)
        message("2 - Normal", white, screen_width / 4, screen_height / 2 + 50)
        message("3 - Hard", white, screen_width / 4, screen_height / 2 + 100)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = "easy"
                    difficulty_selected = True
                elif event.key == pygame.K_2:
                    difficulty = "normal"
                    difficulty_selected = True
                elif event.key == pygame.K_3:
                    difficulty = "hard"
                    difficulty_selected = True
    return difficulty

# Algusmenüü
def main_menu():
    menu = True
    while menu:
        screen.fill((0, 0, 0))
        message("Tere tulemast Ussi Mängu", (255, 255, 255), screen_width / 4, screen_height / 4)
        message("Vajuta Enter, et alustada ühe mängijaga režiimi", (255, 255, 255), screen_width / 4, screen_height / 2)
        message("Vajuta M, et alustada kahemängijaga režiimi", (255, 255, 255), screen_width / 4, screen_height / 2 + 50)
        message("Vajuta L, et näha legendi", (255, 255, 255), screen_width / 4, screen_height / 2 + 100)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    choose_game_mode(multiplayer=False)
                if event.key == pygame.K_m:
                    choose_game_mode(multiplayer=True)
                if event.key == pygame.K_l:  # Ava legendi aken klahviga "L"
                    open_legend()

main_menu()