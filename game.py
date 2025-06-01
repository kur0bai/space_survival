import tkinter as tk
import random

WIDTH = 400
HEIGHT = 600
PLAYER_SPEED = 20
BULLET_SPEED = -6


class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.player = self.canvas.create_rectangle(
            WIDTH//2 - 15, HEIGHT - 30, WIDTH//2 + 15,
            HEIGHT - 10, fill="white")

        # main elements
        self.bullets = []
        self.enemies = []
        self.level = 1
        self.enemy_count = 5
        self.enemy_speed = 1
        self.score = 0

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.shoot)

        self.score_text = self.canvas.create_text(
            10, 10, anchor='nw', text=f"Score: {self.score}", fill='white',
            font=('Arial', 16))

        self.start_level()

    def start_level(self):
        self.spawn_enemies()
        self.update()

    def move_left(self, event):
        self.canvas.move(self.player, -PLAYER_SPEED, 0)

    def move_right(self, event):
        self.canvas.move(self.player, PLAYER_SPEED, 0)

    def shoot(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        bullet = self.canvas.create_rectangle(
            (x1 + x2)//2 - 2, y1 - 10, (x1 + x2)//2 + 2, y1, fill="yellow")
        self.bullets.append(bullet)

    def spawn_enemies(self):
        for i in range(self.enemy_count + self.level):
            x = random.randint(0, WIDTH - 40)
            enemy = self.canvas.create_oval(
                x, 10, x + 30, 40, fill="brown")
            self.enemies.append(enemy)

    def update(self):
        for bullet in self.bullets[:]:
            self.canvas.move(bullet, 0, BULLET_SPEED)
            bx1, by1, bx2, by2 = self.canvas.coords(bullet)
            if by2 < 0:
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)

        for enemy in self.enemies[:]:
            self.canvas.move(enemy, 0, self.enemy_speed)
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
                    self.score += 5
                    self.canvas.itemconfig(
                        self.score_text, text=f"Score: {self.score}")
                    break
        # enemies defeated
        if not self.enemies:
            finished_text = self.canvas.create_text(
                200, 250,
                text=f"Completed level {self.level}!",
                font=("Arial", 20),
                fill="green"
            )
            self.canvas.after(2000, lambda: self.canvas.delete(finished_text))
            self.finished_level()

        self.root.after(50, self.update)

    def finished_level(self):
        self.level += 1
        root.after(1000, self.start_level())

    def intersect(self, a, b):
        ax1, ay1, ax2, ay2 = a
        bx1, by1, bx2, by2 = b
        return not (ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2)

    # show text if game is over
    def game_over(self):
        game_over_text = self.canvas.create_text(
            WIDTH//2, HEIGHT//2, fill="red", font=("Arial", 24),
            text="GAME OVER")
        self.canvas.after(2000, lambda: self.canvas.delete(game_over_text))
        self.canvas.create_text(
            200, 250,
            text=f"You score is {self.score}!",
            font=("Arial", 20),
            fill="green"
        )


# starting the game :D
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Space survival")
    game = Game(root)
    root.mainloop()
