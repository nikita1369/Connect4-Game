import tkinter
from PIL import Image, ImageTk
from tkinter.font import BOLD
from tkinter.constants import BOTTOM
from connect.GUI_Multiplayer import GUI_Multiplayer


class GUI_Main:
    def __init__(self, root):
        #self.window = tkinter.Tk()
        self.root = root
        self.root.title("Connect 4")
        image_path = "/Users/Nikita/Documents/workspacepycharm/Connect4/connect/connect4_image.png"
        load = Image.open(image_path)
        self.render = ImageTk.PhotoImage(load)
        self.root.geometry("1100x750")  # You want the size of the app to be 500x500
        self.root.resizable(0, 0)  # Don't allow resizing in the x or y direction
        self.show_main_menu(self.render)
        self.root.mainloop()

    def show_main_menu(self, render):
        self.root.config(bg="#67c4ef")
        self.img = tkinter.Label(self.root, image=self.render, bg=self.root['bg'])
        self.img.place(x=-50, y=-150)

        self.bottom = tkinter.Frame(master=self.root, width="700", height="350", bg=self.root['bg'])
        self.bottom.pack(side="bottom")
        self.bottom.place(y=450, x=400)
        self.start_game_button = tkinter.Button(master=self.bottom, text="START GAME", font=("Helvetica", 20, BOLD), height=2,
                                           width=18, bg="red", fg="white", highlightbackground="red", command=self.user_interface)
        self.start_game_button.pack()

        self.scoreboard_button = tkinter.Button(master=self.bottom, text="SCOREBOARD", font=("Helvetica", 20, BOLD), height=2,
                                           width=18, bg="red", fg="white", highlightbackground="red")
        self.scoreboard_button.pack(pady=20)

    def user_interface(self):
        print("user interface loading")
        self.next = GUI_Multiplayer(self.root)

root = tkinter.Tk()
GUI_Main(root)