import pygame

pygame.init()

screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128, 156, 117))

    pygame.display.update()

pygame.quit()
