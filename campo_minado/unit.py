from tkinter import *
import random
import new
import configure
import ctypes
import sys

class Cell:
    all = []
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

def create_btn_object(self, location):
    btn = Button(
        location,
        width=12,
        height=4,
    )
    btn.bind('<Button-1>', self.left_click_actions)#botao esquerdo para clicar
    btn.bind('<Button-3>', self.right_click_actions) #botao direito correçoes


def show_mines(self):
    self.cell_btn_object.configure(bg="red")
    ctypes.windll.user32.messageBoxW(0, "Voce clicou em uma mina", "Jogue de novo", 0)
    sys.exit()

def get_cell_bt_axis(self, x,y):
    

def surroudend_cells(self):
    cells = [
        self.get_cell_by_axis
    ]
