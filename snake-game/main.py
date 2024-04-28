import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 10
base_speed = 10
food_radius = snake_block // 2

pygame.font.init()

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 35)
font = pygame.font.Font(None, 50)


def score(score):
  value = score_font.render("Your Score: " + str(score), True, black)
  dis.blit(value, [0, 0])


def snake(snake_block, snake_List):
  for x in snake_List:
    pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])


def message(msg1, msg2, color):
  mesg1 = font_style.render(msg1, True, color)
  mesg2 = font_style.render(msg2, True, color)

  # Get the size of the text
  text_width1, text_height1 = mesg1.get_size()
  text_width2, text_height2 = mesg2.get_size()

  # Calculate the x and y coordinates for the text
  x1 = (dis_width - text_width1) / 2
  y1 = (dis_height - text_height1) / 2
  x2 = (dis_width - text_width2) / 2
  y2 = y1 + text_height1

  dis.blit(mesg1, [x1, y1])
  dis.blit(mesg2, [x2, y2])


def gameLoop():
  game_over = False
  game_close = False

  x1 = dis_width / 2
  y1 = dis_height / 2

  x1_change = 0
  y1_change = 0

  snake_List = []
  snake_length = 1

  snake_speed = base_speed + snake_length

  foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
  foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

  while not game_over:

    while game_close == True:
      dis.fill(blue)
      message("You Lost!", "Press C-Continue or Q-Quit", red)
      score(snake_length - 1)
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            game_over = True
            game_close = False
          if event.key == pygame.K_c:
            gameLoop()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          game_over = True
          game_close = False
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP and y1_change == 0:
              y1_change = -snake_block
              x1_change = 0
          elif event.key == pygame.K_DOWN and y1_change == 0:
              y1_change = snake_block
              x1_change = 0
          elif event.key == pygame.K_LEFT and x1_change == 0:
              x1_change = -snake_block
              y1_change = 0
          elif event.key == pygame.K_RIGHT and x1_change == 0:
              x1_change = snake_block
              y1_change = 0
          elif event.key == pygame.K_SPACE:
            paused = True
            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        paused = False
                pause_text = font.render("||", True, (255, 255, 255))
                dis.blit(pause_text, [dis_width // 2, dis_height // 2])
                pygame.display.update()

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
      game_close = True
    x1 += x1_change
    y1 += y1_change
    dis.fill(blue)
    pygame.draw.circle(dis, green, (int(foodx) + food_radius, int(foody) + food_radius), food_radius)
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)
    if len(snake_List) > snake_length:
      del snake_List[0]

    for x in snake_List[:-1]:
      if x == snake_Head:
        game_close = True

    snake(snake_block, snake_List)
    score(snake_length - 1)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
      foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
      foody = round(
          random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
      snake_length += 1

    clock.tick(snake_speed)

  pygame.quit()
  quit()


gameLoop()
