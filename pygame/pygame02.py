import pygame

# Nastavení
pygame.init()
width, height = 800, 600
screen = pygame.display.set_caption("Geometrické tvary")
screen = pygame.display.set_mode((width, height))
x1=50
x2=50

ball= [400,300, 50]
direction_vector = [-0.2, 0.2]

direction = 1
r = 50

#hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x1 += 0.2
    if x1 > width + r:
        x1 = - r
    # Fill nastaví barvu
            
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (140, 255, 255), (x1, 200), r)
    x2 += 0.5 * direction
    if x2 > width - r:
        direction = -1
    elif x2 < r:
        direction = 1
    
    pygame.draw.circle(screen, (255, 140, 200), (x2, 400), r)
    ball[0] += direction_vector[0]
    ball[1] += direction_vector[1]

    if ball[0] < r or ball[0] > width - r:
        direction_vector[0] *= -1
    if ball[1] < r or ball[1] > height - r:
        direction_vector[1] *= - 1

    pygame.draw.circle(screen, (255, 255, 0), (ball[0], ball[1]), ball[2])


    pygame.display.update()

# zavření porgramu
pygame.quit()