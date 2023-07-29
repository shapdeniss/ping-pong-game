from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        virtual_surface.blit(self.image, (self.rect.x, self.rect.y))


class Ball(GameSprite):
    def __init__(self):
        super().__init__("images/ball.png", WIDTH // 2 - 25, HEIGHT // 2 - 25, 50, 50, 10)


class Platform(GameSprite):
    def __init__(self, player_num):
        self.player_num = player_num
        if self.player_num == 1:
            self.x = 100
            self.angle = -90
        if self.player_num == 2:
            self.x = WIDTH - 120
            self.angle = 90

        super().__init__("images/platform.png", 0, 0, 150, 20, 10)

        self.image = transform.rotate(self.image, self.angle)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = HEIGHT // 2 - 75


WIDTH = 1280
HEIGHT = 720

ASPECT_RATIO = WIDTH / HEIGHT

window = display.set_mode((WIDTH, HEIGHT), RESIZABLE)
display.set_caption("Ping-pong")
clock = time.Clock()

virtual_surface = Surface((WIDTH, HEIGHT))
current_size = window.get_size()

ball = Ball()

player_1 = Platform(1)
player_2 = Platform(2)

finish = True
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            exit()
        if e.type == KEYDOWN:
            if e.type == K_ESCAPE:
                exit()
        if e.type == VIDEORESIZE:
            new_width = e.w
            new_height = int(new_width / ASPECT_RATIO)
            window = display.set_mode((new_width, new_height), RESIZABLE)
            current_size = window.get_size()

    virtual_surface.fill((240, 238, 180))

    ball.reset()

    player_1.reset()
    player_2.reset()

    scaled_surface = transform.scale(virtual_surface, current_size)
    window.blit(scaled_surface, (0, 0))
    clock.tick(60)
    display.update()