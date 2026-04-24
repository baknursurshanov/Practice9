import pygame
import datetime
import os

pygame.init()
screen = pygame.display.set_mode((1200, 700))
white = (255, 255, 255)

base = os.path.dirname(os.path.abspath(__file__))

bg = pygame.image.load(os.path.join(base, 'clock.png')).convert_alpha()
mickey = pygame.image.load(os.path.join(base, 'mickey.png')).convert_alpha()
hand_l = pygame.image.load(os.path.join(base, 'lruka.png')).convert_alpha()
hand_r = pygame.image.load(os.path.join(base, 'pruka.png')).convert_alpha()

bg = pygame.transform.scale(bg, (800, 600))
mickey = pygame.transform.scale(mickey, (350, 350))
h_l_base = pygame.transform.scale(hand_l, (60, 200))
h_r_base = pygame.transform.scale(hand_r, (80, 150))

clock_center = (600, 340)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    now = datetime.datetime.now()
    m_ang = -(now.minute * 6)
    h_ang = -(now.hour * 30 + now.minute * 0.5)

    screen.fill(white)
    
    screen.blit(bg, bg.get_rect(center=clock_center))
    screen.blit(mickey, mickey.get_rect(center=clock_center))

    rot_m = pygame.transform.rotate(h_l_base, m_ang)
    rot_h = pygame.transform.rotate(h_r_base, h_ang)

    screen.blit(rot_h, rot_h.get_rect(center=clock_center))
    screen.blit(rot_m, rot_m.get_rect(center=clock_center))

    pygame.display.flip()
    clock.tick(60)