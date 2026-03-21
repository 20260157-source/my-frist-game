import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dash Mode! (Press SHIFT to speed up)")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# 현재 배경색 상태 (기본값: 흰색)
bg_color = WHITE

# 원과 네모의 초기 위치, 크기, **기본 속도** 설정
circle_x = 400
circle_y = 300
circle_radius = 50
base_circle_speed = 5  # 기본 속도 변수명 변경

rect_x = 200
rect_y = 200
rect_width = 80
rect_height = 80
base_rect_speed = 5    # 기본 속도 변수명 변경

font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 키보드가 '눌렸을 때' 색상 변경 (1, 2, 3)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                bg_color = RED
            elif event.key == pygame.K_2:
                bg_color = GREEN
            elif event.key == pygame.K_3:
                bg_color = YELLOW

    # 눌려있는 모든 키의 상태를 가져옴
    keys = pygame.key.get_pressed()

    # --- 새로 추가된 부분: Shift 키를 누르면 속도 2배 ---
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        current_circle_speed = base_circle_speed * 2
        current_rect_speed = base_rect_speed * 2
    else:
        current_circle_speed = base_circle_speed
        current_rect_speed = base_rect_speed
    # ----------------------------------------------------

    # 1. 보라색 원 이동 (W, A, S, D 키) + 현재 속도 적용
    if keys[pygame.K_a]:
        circle_x -= current_circle_speed
    if keys[pygame.K_d]:
        circle_x += current_circle_speed
    if keys[pygame.K_w]:
        circle_y -= current_circle_speed
    if keys[pygame.K_s]:
        circle_y += current_circle_speed

    # 2. 파란색 네모 이동 (방향키) + 현재 속도 적용
    if keys[pygame.K_LEFT]:
        rect_x -= current_rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += current_rect_speed
    if keys[pygame.K_UP]:
        rect_y -= current_rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += current_rect_speed

    # 화면 경계 제한
    circle_x = max(circle_radius, min(800 - circle_radius, circle_x))
    circle_y = max(circle_radius, min(600 - circle_radius, circle_y))

    rect_x = max(0, min(800 - rect_width, rect_x))
    rect_y = max(0, min(600 - rect_height, rect_y))

    # 화면 칠하기 및 도형 그리기
    screen.fill(bg_color)
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))
    pygame.draw.circle(screen, PURPLE, (int(circle_x), int(circle_y)), circle_radius)

    # FPS 표시
    fps_text = f"FPS: {clock.get_fps():.1f}"
    fps_surface = font.render(fps_text, True, BLACK)
    screen.blit(fps_surface, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()