import pygame
import simpleaudio as sa

pygame.init()

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("Simple Game")

pygame.mixer.music.load("bgmusic.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

sound = sa.WaveObject.from_wave_file('sound.wav')

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
        play = sound.play()

    if keys[pygame.K_RIGHT]:
        x += vel
        play = sound.play()

    if keys[pygame.K_UP]:
        pygame.mixer.music.set_volume(1.0)

    if keys[pygame.K_DOWN]:
        pygame.mixer.music.set_volume(0.0)

    window.fill((0,0,0))
    pygame.draw.rect(window, (255,0,0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
