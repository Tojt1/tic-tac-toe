import tkinter as tk
from tkinter import messagebox

wynikx = 0
wyniko = 0

class Kolkoikrzyzyk:
    def __init__(self, windows):
        self.wynikx = 0
        self.wyniko = 0
        self.window = windows
        self.window.title("kółko i krzyżyk")

        self.obecny_gracz = "X"
        self.label = tk.Label(text=f"ruch osoby: {self.obecny_gracz}")
        self.label.grid(row=4, column=0)
        self.labelx = tk.Label(text=f"wynik:"f"x: {self.wynikx}")
        self.labelx.grid(row=5, column=0)
        self.labelo = tk.Label(text=f"o: {self.wyniko}")
        self.labelo.grid(row=6, column=0)


        self.plansza = [["" for _ in range(3)] for _ in range(3)]

        self.przyciski = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.przyciski[i][j] = tk.Button(windows, text="", font=("Helvetica", 16), height=2, width=5,
                                                 command=lambda row=i, col=j: self.klikniety_przycisk(row, col))
                self.przyciski[i][j].grid(row=i, column=j)

    def klikniety_przycisk(self, row, col):

        if self.plansza[row][col] == "":
            self.plansza[row][col] = self.obecny_gracz
            self.przyciski[row][col].config(text=self.obecny_gracz)

        if self.win_check():
            messagebox.showinfo("wygrana", f"Brawo graczowi {self.obecny_gracz} udało się wygrąć")
            self.number_of_wins()
            self.restart_game()
        elif self.remis_check():
            messagebox.showinfo("Remis", "Nikt nie wygrał tej rundy")
            self.restart_game()
        else:
            self.obecny_gracz = 'o' if self.obecny_gracz == 'X' else 'X'

        self.label.config(text=f"ruch osoby: {self.obecny_gracz}")
        self.labelx.config(text=f"wynik:"f"x: {self.wynikx}")
        self.labelo.config(text=f"o: {self.wyniko}")


    def win_check(self):
        for i in range(3):
            if self.plansza[i][0] == self.plansza[i][1] == self.plansza[i][2] != '':
                return True
            if self.plansza[0][i] == self.plansza[1][i] == self.plansza[2][i] != '':
                return True
            if self.plansza[0][0] == self.plansza[1][1] == self.plansza[2][2] != "":
                return True
            if self.plansza[2][0] == self.plansza[1][1] == self.plansza[0][2] != '':
                return True

    def remis_check(self):
        for i in range(3):
            for j in range(3):
                if self.plansza[i][j] == "":
                    return False

        return True

    def restart_game(self):
        for i in range(3):
            for j in range(3):
                self.plansza[i][j] = ''
                self.przyciski[i][j].config(text='')
        self.obecny_gracz = 'X'

    def number_of_wins(self):
        if self.obecny_gracz == "X":
            self.wynikx = self.wynikx+1
        if self.obecny_gracz == "o":
            self.wyniko = self.wyniko+1
        return self.wynikx, self.wyniko


if __name__ == '__main__':
    window = tk.Tk()
    game = Kolkoikrzyzyk(window)
    window.mainloop()
