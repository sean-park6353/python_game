import pygame

white = (255, 255, 255)
pad_width = 1024
pad_height = 512


def runGame():
    global gamepad, clock
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        gamepad.fill(white)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()


def initGame():
    global gamepad, clock

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('PyFlying')

    clock = pygame.time.Clock()
    runGame()


initGame()
