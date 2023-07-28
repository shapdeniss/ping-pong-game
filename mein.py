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

