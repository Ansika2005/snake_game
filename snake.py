import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set screen width and height
width = 600
height = 400

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake block size and speed
block_size = 10
speed = 15

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Clock for controlling speed
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.SysFont("bahnschrift", 25)

def display_score(score):
    value = font.render(f"Score: {score}", True, white)
    screen.blit(value, [10, 10])

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    dx = 0
    dy = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:
        while game_close:
            screen.fill(black)
            message = font.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            screen.blit(message, [width / 6, height / 3])
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -block_size
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = block_size
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -block_size
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = block_size
                    dx = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += dx
        y += dy
        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(speed)

    pygame.quit()
    quit()

# Run the game
game_loop()
