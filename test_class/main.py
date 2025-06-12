import tkinter as tk
from gui.ScoreboardGUI import ScoreboardGUI
from gui.ManagerLoginGUI import ManagerLoginGUI


def main():
    root = tk.Tk()
    app = ManagerLoginGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

#if __name__ == "__main__":
#    root = tk.Tk()
#   app = ScoreboardGUI(root)
#   root.mainloop()