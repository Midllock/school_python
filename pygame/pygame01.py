import pygame

# Nastavení okna
pygame.init()
width, height = 800, 600
screen = pygame.display.set_caption("Geometrické tvary")
screen = pygame.display.set_mode((width, height))

#hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill nastaví barvu
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 100, 400))
    pygame.draw.circle(screen, (0, 255, 0), (400, 300), 100)
    pygame.draw.polygon(screen, (0, 0, 225), [(350, 150), (450, 150), (400, 50)])
    pygame.display.update()

# zavření porgramu
pygame.quit()

