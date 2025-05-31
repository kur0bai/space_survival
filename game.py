import tkinter as tk
import random

WIDTH = 400
HEIGHT = 600
PLAYER_SPEED = 20
BULLET_SPEED = -10
ENEMY_SPEED = 2
ENEMY_BULLE_SPEED = -10
ENEMY_COUNT = 5


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

        self.spawn_enemies()
        self.update()

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
            x = random.randint(0, WIDTH - 20)
            enemy = self.canvas.create_rectangle(
                x, 10, x + 30, 30, fill="green")
            self.enemies.append(enemy)

    def update(self):
        for bullet in self.bullets[:]:
            self.canvas.move(bullet, 0, BULLET_SPEED)
            bx1, by1, bx2, by2 = self.canvas.coords(bullet)
            if by2 < 0:
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)

        for enemy in self.enemies[:]:
            self.canvas.move(enemy, 0, ENEMY_SPEED)
            ex1, ey1, ex2, ey2 = self.canvas.coords(enemy)
            if ey2 > HEIGHT:
                self.game_over()
                return
            for bullet in self.bullets[:]:
                bx1, by1, bx2, by2 = self.canvas.coords(bullet)
                if self.intersect((bx1, by1, bx2, by2), (ex1, ey1, ex2, ey2)):
                    self.canvas.delete(enemy)
                    self.canvas.delete(bullet)
                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    break

        self.root.after(50, self.update)

    def intersect(self, a, b):
        ax1, ay1, ax2, ay2 = a
        bx1, by1, bx2, by2 = b
        return not (ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2)

    #Show text if game is over
    def game_over(self):
        self.canvas.create_text(
            WIDTH//2, HEIGHT//2, fill="red", font=("Arial", 24),
            text="GAME OVER")


#Run the game
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Space survival")
    game = Game(root)
    root.mainloop()
