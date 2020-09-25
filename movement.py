import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("my game")

x = 50
y = 50
width = 40
height = 60
velocity = 5

run = True
while run:
    # game delay
    pygame.time.delay(100)  # ms

    # allow window quit
    for event in pygame.event.get(): # get queue of all commands
        if event.type == pygame.QUIT:
            run = False

    # key press: continue to trigger instead once
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity

    # rewrite background
    window.fill((0, 0, 0))

    # create rectangle
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update() # refresh window
pygame.quit()
