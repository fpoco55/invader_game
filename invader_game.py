import pygame
import random

# ゲームの初期設定
pygame.init()

# 画面サイズ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 画面の設定
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("インベーダーゲーム")

# プレイヤーの設定
class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.speed = 5

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

# 敵の設定
class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.y = random.randint(-100, -40)
        self.speed = 2

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.speed

# プレイヤーと敵のリスト
player = Player()
enemies = []

# ゲームループ
clock = pygame.time.Clock()
running = True

# 敵の生成タイマー
enemy_timer = 0

while running:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キー入力処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")

    # 敵の生成
    enemy_timer += 1
    if enemy_timer >= 60:  # 1秒ごとに敵を生成
        enemies.append(Enemy())
        enemy_timer = 0

    # 敵の移動
    for enemy in enemies:
        enemy.move()
        # 敵が画面外に出たらリストから削除
        if enemy.y > SCREEN_HEIGHT:
            enemies.remove(enemy)
        # 当たり判定
        if (player.x < enemy.x + enemy.width and
            player.x + player.width > enemy.x and
            player.y < enemy.y + enemy.height and
            player.y + player.height > enemy.y):
            running = False

    # 画面の描画
    screen.fill(BLACK)
    player.draw()
    for enemy in enemies:
        enemy.draw()
    pygame.display.flip()

    # フレームレートの設定
    clock.tick(60)

pygame.quit()
