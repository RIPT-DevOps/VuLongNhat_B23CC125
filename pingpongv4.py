import os
import pygame, sys, random

# Force pygame to use dummy audio driver if no sound device is available
os.environ["SDL_AUDIODRIVER"] = "dummy"

def hoat_anh_bong():
    global toc_bong_x, toc_bong_y, diem_P1_bandau, diem_P2_bandau, thoi_gian_ghi_diem
    bong.x += toc_bong_x
    bong.y += toc_bong_y
    if bong.top <= 0 or bong.bottom >= rong:
        toc_bong_y *= -1
    if bong.left <= 0:
        diem_P1_bandau += 1
        thoi_gian_ghi_diem = pygame.time.get_ticks()
        try:
            tieng_ghi_ban.play()
        except pygame.error:
            print("Audio not available.")
    if bong.right >= dai:
        diem_P2_bandau += 1
        thoi_gian_ghi_diem = pygame.time.get_ticks()
        try:
            tieng_ghi_ban.play()
        except pygame.error:
            print("Audio not available.")
    if bong.colliderect(P1) or bong.colliderect(P2):
        toc_bong_x *= -1
        try:
            tieng_cham_thanh.play()
        except pygame.error:
            print("Audio not available.")

def thanh_bong_1():
    P1.y += toc_thanh_p1
    if P1.top <= 0:
        P1.top = 0
    if P1.bottom >= rong:
        P1.bottom = rong

def thanh_bong_2():
    P2.y += toc_thanh_p2
    if P2.top <= 0:
        P2.top = 0
    if P2.bottom >= rong:
        P2.bottom = rong

def bong_khoi_dong():
    global toc_bong_x, toc_bong_y, thoi_gian_ghi_diem
    thoi_gian_hien_tai = pygame.time.get_ticks()
    bong.center = (dai/2, rong/2)
    if thoi_gian_hien_tai - thoi_gian_ghi_diem < 700:
        so_3 = khuon_chu.render("3", False, 'white')
        man.blit(so_3, (dai/2 - 10, rong/2 + 20))
    if 700 < thoi_gian_hien_tai - thoi_gian_ghi_diem < 1400:
        so_2 = khuon_chu.render("2", False, 'white')
        man.blit(so_2, (dai/2 - 10, rong/2 + 20))
    if 1400 < thoi_gian_hien_tai - thoi_gian_ghi_diem < 2100:
        so_1 = khuon_chu.render("1", False, 'white')
        man.blit(so_1, (dai/2 - 10, rong/2 + 20))
    if thoi_gian_hien_tai - thoi_gian_ghi_diem < 2100:
        toc_bong_x, toc_bong_y = 0, 0
    else:
        toc_bong_y = 5 * random.choice((1, -1))
        toc_bong_x = 5 * random.choice((1, -1))
        thoi_gian_ghi_diem = None

# Initialize pygame
pygame.init()

# Initialize pygame mixer with error handling
try:
    pygame.mixer.init()
except pygame.error:
    print("Audio device not available.")

fps = pygame.time.Clock()

# Screen settings
dai = 1280
rong = 720
man = pygame.display.set_mode((dai, rong))
pygame.display.set_caption('Pong')

# Ball and players
bong = pygame.Rect(dai/2 - 20, rong/2 - 20, 40, 40)
P1 = pygame.Rect(dai - 20, rong/2 - 70, 10, 140)
P2 = pygame.Rect(10, rong/2 - 70, 10, 140)
toc_bong_x = 10
toc_bong_y = 10
toc_thanh_p1 = 0
toc_thanh_p2 = 0

# Scores
diem_P1_bandau = 0
diem_P2_bandau = 0
khuon_chu = pygame.font.Font("FreeSansBold.ttf", 20)

# Time for score reset
thoi_gian_ghi_diem = True

# Sound initialization with error handling
try:
    tieng_ghi_ban = pygame.mixer.Sound("ghi_ban.ogg")
    tieng_ghi_ban.set_volume(1)
    tieng_cham_thanh = pygame.mixer.Sound("pong.ogg")
    tieng_cham_thanh.set_volume(1)
    pygame.mixer.music.load('y2mate.com - Driftveil City Pokémon Black  White.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
except pygame.error:
    print("Audio device or file not available.")

# Game loop
while True:
    # Handle quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                toc_thanh_p1 += 5
            if event.key == pygame.K_UP:
                toc_thanh_p1 -= 5
            if event.key == pygame.K_s:
                toc_thanh_p2 += 5
            if event.key == pygame.K_w:
                toc_thanh_p2 -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                toc_thanh_p1 -= 5
            if event.key == pygame.K_UP:
                toc_thanh_p1 += 5
            if event.key == pygame.K_s:
                toc_thanh_p2 -= 5
            if event.key == pygame.K_w:
                toc_thanh_p2 += 5

    # Player movement
    P1.y += toc_thanh_p1
    P2.y += toc_thanh_p2
    thanh_bong_1()
    thanh_bong_2()

    # Render the game screen
    man.fill('grey11')
    pygame.draw.rect(man, 'blue', P1)
    pygame.draw.rect(man, 'red', P2)
    pygame.draw.ellipse(man, 'white', bong)
    pygame.draw.aaline(man, 'white', (dai/2, 0), (dai/2, rong))

    # Animate the ball
    hoat_anh_bong()

    # Display scores
    if thoi_gian_ghi_diem:
        bong_khoi_dong()

    diem_player = khuon_chu.render(f"{diem_P1_bandau}", False, 'blue')
    man.blit(diem_player, (dai/2 + 40, rong/2))
    diem_dich = khuon_chu.render(f"{diem_P2_bandau}", False, 'red')
    man.blit(diem_dich, (dai/2 - 50, rong/2))

    # Refresh the display and set FPS
    pygame.display.flip()
    fps.tick(75)
