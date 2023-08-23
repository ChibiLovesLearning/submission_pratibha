import pygame, random, math, sys, time
from pygame import display, image, font, event, draw

pygame.init()

game_state = 0
score = 0
lives = 3
end_text = ""

caption = display.set_caption("My Submission Game")
screen = display.set_mode((800, 600))

icon = image.load("images/icon.png")
display.set_icon(icon)

yellow = (255, 255, 0)
rectX = 0
rectY = 275

bg_image = image.load("images/bg.png")

rabbit = image.load("images/rabbit.png")
rabbit_x = 400
rabbit_y = 300
rabbit_x_change = 0
rabbit_y_change = 0

carrot = []
carrot_x = []
carrot_y = []
for i in range(15):
  carrot.append(image.load("images/carrot.png"))
  carrot_x.append(random.randint(60, 750))
  carrot_y.append(random.randint(50, 500))

fox = []
fox_x = []
fox_y = []
fox_x_change = []
fox_y_change = []
for i in range(6):
  fox.append(image.load("images/fox.png"))
  fox_x.append(random.randint(60, 750))
  fox_y.append(random.randint(0, 500))
  fox_x_change.append(1)
  fox_y_change.append(40)

text = font.Font("font/ARCADE.TTF", 32)
livesText = font.Font("font/ARCADE.TTF", 32)

def show_font():
  if game_state == 1:
    render = text.render("Score: " + str(score), True, (255,255,255))
    screen.blit(render, (650, 10))
    render = livesText.render("Lives: " + str(lives), True, (255,255,255))
    screen.blit(render, (20, 10))
  elif game_state == 0:
    render = text.render("Get the rabbit 30 carrots to win", True, (255,255,255))
    screen.blit(render, (200, 100))
  else:
    render = text.render(end_text, True, (254,133,127))
    screen.blit(render, (275, 230))

for i in range(1,15):
  rectX = rectX + 50
  rectangle = (rectX, rectY, 30, 30)
  draw.rect(screen, yellow, rectangle)
  show_font()
  display.flip()
  time.sleep(0.3)
  game_state = 1

def place_rabbit(x, y):
  screen.blit(rabbit, (x, y))

def place_carrot(i):
  screen.blit(carrot[i], (carrot_x[i], carrot_y[i]))

def place_fox(i):
  screen.blit(fox[i], (fox_x[i], fox_y[i]))

def isCollision(x1, y1, x2, y2):
  dis = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2,2))
  if dis <= 27:
    return True
  return False

while True:
  screen.blit(bg_image, (0,0))
  events = event.get()
  for e in events:
    if e.type == pygame.QUIT:
      sys.exit()
    if e.type == pygame.KEYDOWN:
      if e.key == pygame.K_RIGHT:
        rabbit_x_change = 4
      if e.key == pygame.K_LEFT:
        rabbit_x_change = -4
      if e.key == pygame.K_UP:
        rabbit_y_change = -4
      if e.key == pygame.K_DOWN:
        rabbit_y_change = 4
    if e.type == pygame.KEYUP:
      rabbit_x_change = 0
      rabbit_y_change = 0

  rabbit_x += rabbit_x_change
  rabbit_y += rabbit_y_change

  for i in range(15):
    if isCollision(carrot_x[i], carrot_y[i], rabbit_x, rabbit_y):
      carrot_x[i] = random.randint(60, 750) 
      carrot_y[i] = random.randint(0, 500)
      if game_state == 1:
        score += 1
      if score == 30:
        end_text = "You Won! Great Job!"
        game_state = 2
    place_carrot(i)

  for i in range(6):
    fox_x[i] += fox_x_change[i]
    if fox_x[i] <= 0:
      fox_x_change[i] = 1 
      fox_y[i] += fox_y_change[i] 
    if fox_x[i] >= 750:
      fox_x_change[i] = -1
      fox_y[i] += fox_y_change[i] 
    if fox_y[i] > 550:
      fox_x[i] = random.randint(64, 736) 
      fox_y[i] = random.randint(0, 510)
    if isCollision(fox_x[i], fox_y[i], rabbit_x, rabbit_y):
      fox_x[i] = random.randint(60, 750) 
      fox_y[i] = random.randint(0, 500)
      if game_state == 1:
        score -= 1
        lives -= 1
      if lives == 0:
        end_text = "Game Over!"
        game_state = 2
    place_fox(i)
    
  if rabbit_x <= 0:
    rabbit_x = 0
  elif rabbit_x > 750:
    rabbit_x = 750

  if rabbit_y <= 0:
    rabbit_y = 0
  elif rabbit_y > 550:
    rabbit_y = 550

  place_rabbit(rabbit_x, rabbit_y)

  if game_state == 2:
    screen.fill((249,254,127))

  show_font()
        
  display.flip()

pygame.quit()
