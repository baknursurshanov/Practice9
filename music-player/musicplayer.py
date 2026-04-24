import pygame
import os

pygame.init()
pygame.mixer.init()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("music player")

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

songs = [f for f in os.listdir('.') if f.endswith(('.mp3'))]
current_track_index = 0

def play_music():
    if songs:
        pygame.mixer.music.load(songs[current_track_index])
        pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track_index
    if songs:
        current_track_index = (current_track_index + 1) % len(songs)
        play_music()

def prev_track():
    global current_track_index
    if songs:
        current_track_index = (current_track_index - 1) % len(songs)
        play_music()

font = pygame.font.SysFont("arial", 20)
clock = pygame.time.Clock()

running = True
is_playing = False

while running:
    screen.fill(black)
    
    if not songs:
        text = font.render("no music files found!", True, white)
        screen.blit(text, (50, 100))
    else:
        track_name = songs[current_track_index]
        track_text = font.render(f"playing: {track_name}", True, green if is_playing else white)
        screen.blit(track_text, (50, 100))
    
    controls = ["p - play", "s - stop", "n - next", "b - back", "q - quit"]
    for i, line in enumerate(controls):
        label = font.render(line, True, white)
        screen.blit(label, (50, 180 + i * 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and songs:
                if not is_playing:
                    play_music()
                    is_playing = True
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                stop_music()
                is_playing = False
            elif event.key == pygame.K_n and songs:
                next_track()
                is_playing = True
            elif event.key == pygame.K_b and songs:
                prev_track()
                is_playing = True
            elif event.key == pygame.K_q:
                running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()