import pygame
import os
import sys


class Hero(pygame.sprite.Sprite):
    def __init__(self, *args):
        super().__init__(*args)
        self.cursor = load_image('creature.png')

        self.image = self.cursor
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args) -> None:
        if args:
            event = args[0]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.rect.y -= 10
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.rect.y += 10
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.rect.x -= 10
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.rect.x += 10


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = image.convert()
    return image


def main():
    pygame.init()
    size = 300, 300
    running = True

    screen = pygame.display.set_mode(size)

    group_hero = pygame.sprite.Group()
    Hero(group_hero)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                group_hero.update(event)
        screen.fill('White')

        group_hero.update()
        group_hero.draw(screen)

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
