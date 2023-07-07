
import random

class Shape:
    shapes = [
        [(0, 0), (0, 1), (1, 0), (1, 1)],  # O
        [(0, 0), (0, 1), (0, 2), (0, 3)],  # I
        [(0, 0), (0, 1), (1, 1), (2, 1)],  # L
        [(0, 1), (1, 1), (2, 1), (2, 0)],  # J
        [(0, 1), (1, 1), (2, 1), (1, 0)],  # T
        [(0, 1), (1, 1), (1, 0), (2, 0)],  # Z
        [(0, 0), (1, 0), (1, 1), (2, 1)]   # S
    ]

class Block:
    def __init__(self, shape=None, color=None, pos=None):
        if shape is None:
            shape = random.choice(Shape.shapes)
        if color is None:
            color = random.randint(1, 7)
        if pos is None:
            pos = [5, 0]
        self.shape = shape
        self.color = color
        self.pos = pos
        self.rotation = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4
        new_shape = []
        for x, y in self.shape:
            new_x, new_y = y, -x
            new_shape.append((new_x, new_y))
        self.shape = new_shape

    def move_down(self):
        self.pos[1] += 1

    def move_left(self):
        self.pos[0] -= 1

    def move_right(self):
        self.pos[0] += 1

    def draw(self):
        for y in range(2):
            for x in range(2):
                if (x, y) in self.shape:
                    print(self.color, end='')
                else:
                    print('.', end='')
            print()

class Game:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.score = 0
        self.blocks = []
        self.current_block = Block()
        self.next_block = Block()

    def can_move_down(self):
        for x, y in self.current_block.shape:
            if y + self.current_block.pos[1] + 1 >= self.height:
                return False
        return True

    def can_move_left(self):
        for x, y in self.current_block.shape:
            if x + self.current_block.pos[0] - 1 < 0:
                return False
        return True

    def can_move_right(self):
        for x, y in self.current_block.shape:
            if x + self.current_block.pos[0] + 1 >= self.width:
                return False
        return True

    def can_rotate(self):
        block = Block(shape=self.current_block.shape, pos=self.current_block.pos)
        block.rotate()
        for x, y in block.shape:
            if x + block.pos[0] < 0 or x + block.pos[0] >= self.width or y + block.pos[1] >= self.height:
                return False
        return True

    def fix_block(self):
        for x, y in self.current_block.shape:
            self.blocks.append((x + self.current_block.pos[0], y + self.current_block.pos[1], self.current_block.color))
        self.current_block = self.next_block
        self.next_block = Block()
        # check for complete lines
        lines = []
        for y in range(self.height):
            if all((x, y) in [(bx, by) for bx, by, _ in self.blocks] for x in range(self.width)):
                lines.append(y)
        # remove complete lines
        for y in reversed(lines):
            for x, y, c in self.blocks:
                if y == y:
                    self.blocks.remove((x, y, c))
                    self.score += 10

    def run(self):
        while True:
            print("Score: {}".format(self.score))
            print("Next Block:")
            self.next_block.draw()
            print("Current Block:")
            self.current_block.draw()
            for y in range(self.height):
                for x in range(self.width):
                    if (x, y) in self.current_block.shape:
                        print(self.current_block.color, end='')
                    # elif (x, y) in [(bx, by) for bx, by, _ in self.blocks]:
                    #     print([c for _, _, c in self.blocks if (x, y) == (bx, by)][0], end='')
                    elif (x, y) in [(bx, by) for bx, by, _ in self.blocks]:
                        print([c for bx, by, c in self.blocks if (x, y) == (bx, by)][0], end='')
                    else:
                        print('.', end='')
                print()
            if not self.can_move_down():
                self.fix_block()
            else:
                self.current_block.move_down()
            cmd = input("Enter command (l: move left, r: move right, d: move down, u: rotate): ")
            if cmd == 'l' and self.can_move_left():
                self.current_block.move_left()
            elif cmd == 'r' and self.can_move_right():
                self.current_block.move_right()
            elif cmd == 'd':
                if self.can_move_down():
                    self.current_block.move_down()
                else:
                    self.fix_block()
            elif cmd == 'u' and self.can_rotate():
                self.current_block.rotate()

if __name__ == '__main__':
    game = Game()
    game.run()