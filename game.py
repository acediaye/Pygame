import pygame

pygame.init()
screenwidth = 500
screenheight = 500
window = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("my game")

# character
x = 50
y = 50
width = 40
height = 60
velocity = 10
isJump = False
jumpCount = 10

run = True
while run:
    # game delay
    pygame.time.delay(100)  # ms

    # allow window quit
    for event in pygame.event.get(): # get queue of all commands
        if event.type == pygame.QUIT:
            run = False

    # key press: continue to trigger instead once
    # boundary checking
    # jumping mechanic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < screenwidth - width:
        x += velocity
    if not(isJump):
        if keys[pygame.K_UP] and y > 0:
            y -= velocity
        if keys[pygame.K_DOWN] and y < screenheight - height :
            y += velocity
        if keys[pygame.K_SPACE]:
            isJump = True
    else:  # is jump
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= round(neg * 1/2 * jumpCount * jumpCount)
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
#50, 40.5, 32, 24.5, 18, 12.5, 8, 4.5, 2, 0.5, 0, 0.5
    # rewrite background
    window.fill((0, 0, 0))

    # create rectangle
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update() # refresh window
pygame.quit()
