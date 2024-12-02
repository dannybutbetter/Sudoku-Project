#Cell class of the Sudoku Project
import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen
        self.sketched_value=0
        self.selected=False

    def set_cell_value(self, value):
        self.value=value

    def set_sketched_value(self, value):
        self.sketched_value=value

    def draw(self):
        x = self.col * self.cell_size
        y = self.row * self.cell_size

        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, self.cell_size, self.cell_size), 1)

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, self.cell_size, self.cell_size), 3)

        font = pygame.font.Font(None, 40)
        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + 20, y + 10))
        elif self.sketched_value != 0:
            sketched_font = pygame.font.Font(None, 25)
            sketched_text = sketched_font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(sketched_text, (x + 5, y + 5))
