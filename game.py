import random
import tkinter as tk

WIDTH = 400
HEIGHT = 600
PLAYER_SPEED = 20
BULLET_SPEED = -10
ENEMY_SPEED = 2
ENEMY_BULLET_SPEED = -10


class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.player = self.canvas.create_rectangle(
            WIDTH//2 - 15, HEIGHT - 30, WIDTH//2 + 15, HEIGHT - 10,
            fill="white")
        self.bullets = []
        self.enemies = []

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.shoot)

    def move_left(self, event):
        self.canvas.move(self.player, -PLAYER_SPEED, 0)

    def move_right(self, event):
        self.canvas.move(self.player, PLAYER_SPEED, 0)

    def shoot(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        bullet = self.canvas.create_rectangle(
            (x1 + x2)//2 - 2, y1 - 10, (x1 + x2)//2 + 2, y1, fill="red")
        self.bullets.append(bullet)

    def spawn_enemies(self):
        for i in range(5):
            x = random.randint(0, WIDTH - 30)
            enemy = self.canvas.create_rectangle(
                x, 10, x + 30, 30, fill="green")
            self.enemies.append(enemy)
