import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        firstHit = False
        xPos = 4
        yPos = 4
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            for n in range(1, 20):
                pygame.draw.line(screen, "black", (32 * n, 0), (32 * n, 512))
            for n in range(1, 16):
                pygame.draw.line(screen, "black", (0, 32*n), (640, 32*n))
            if (firstHit == False):
                screen.blit(mole_image, mole_image.get_rect(topleft=(4,4)))
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    for n in range(0,17):
                        if ((pygame.mouse.get_pos() == (xPos+12-n, yPos+12))):
                            xPos = random.randint(0,19)*32 + 4
                            yPos = random.randint(0, 15)*32 + 4
                            firstHit = True
                        for m in range(0,17):
                            if ((pygame.mouse.get_pos() == (xPos+12-n, yPos+12-m))):
                                xPos = random.randint(0,19)*32 + 4
                                yPos = random.randint(0, 15)*32 + 4
                                firstHit = True
                        for m in range(0,17):
                            if ((pygame.mouse.get_pos() == (xPos+12-n, yPos+12+m))):
                                xPos = random.randint(0,19)*32 + 4
                                yPos = random.randint(0, 15)*32 + 4
                                firstHit = True
                    for n in range(0, 17):
                        if ((pygame.mouse.get_pos() == (xPos + 12 + n, yPos + 12))):
                            xPos = random.randint(0, 19) * 32 + 4
                            yPos = random.randint(0, 15) * 32 + 4
                            firstHit = True
                        for m in range(0, 17):
                            if ((pygame.mouse.get_pos() == (xPos + 12 + n, yPos + 12 - m))):
                                xPos = random.randint(0, 19) * 32 + 4
                                yPos = random.randint(0, 15) * 32 + 4
                                firstHit = True
                        for m in range(0, 17):
                            if ((pygame.mouse.get_pos() == (xPos + 12 + n, yPos + 12 + m))):
                                xPos = random.randint(0, 19) * 32 + 4
                                yPos = random.randint(0, 15) * 32 + 4
                                firstHit = True
            else:
                screen.blit(mole_image, mole_image.get_rect(topleft=(xPos, yPos)))
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    for n in range(0, 9):
                        if ((pygame.mouse.get_pos() == (xPos + 12 - n, yPos + 12))):
                            xPos = random.randint(0, 19) * 32 + 4
                            yPos = random.randint(0, 15) * 32 + 4
                        for m in range(0, 9):
                            if ((pygame.mouse.get_pos() == (xPos + 12 -n , yPos + 12 - m))):
                                xPos = random.randint(0, 19) * 32 + 4
                                yPos = random.randint(0, 15) * 32 + 4
                        for m in range(0, 9):
                            if ((pygame.mouse.get_pos() == (xPos + 12 - n, yPos + 12 + m))):
                                xPos = random.randint(0, 19) * 32 + 4
                                yPos = random.randint(0, 15) * 32 + 4
                    for n in range(0, 9):
                        if ((pygame.mouse.get_pos() == (xPos + 12 + n, yPos + 12))):
                            xPos = random.randint(0, 19) * 32 + 4
                            yPos = random.randint(0, 15) * 32 + 4
                        for m in range(0, 9):
                            if ((pygame.mouse.get_pos() == (xPos + 12 + n, yPos + 12 - m))):
                                xPos = random.randint(0, 19) * 32 + 4
                                yPos = random.randint(0, 15) * 32 + 4
                        for m in range(0, 9):
                            if ((pygame.mouse.get_pos() == (xPos + 12 + n, yPos + 12 + m))):
                                xPos = random.randint(0, 19) * 32 + 4
                                yPos = random.randint(0, 15) * 32 + 4
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
