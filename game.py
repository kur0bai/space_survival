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
            WIDTH//2 - 15, HEIGHT - 30, WIDTH//2 + 15, HEIGHT - 10, fill="white")
        self.bullets = []
        self.enemies = []

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.shoot)
