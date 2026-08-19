from tkinter import *
from minesweeper import Minesweeper

root = Tk()
root.title("Minesweeper")
root.geometry("330x500")
bg = PhotoImage(file = "image/background.png")
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

stack = []
opened_cell = []
flag = 0
bt_size = 1
flag_cell = []

def choose_level(level):
    if level == 1:
        return Minesweeper(8, 8, 7)
    elif level == 2:
        return Minesweeper(16, 16, 40)
    elif level == 3:
        return Minesweeper(24, 16, 90)
    else:
        return Minesweeper(24, 24, 150)

def right_click(event, index):
    global mfield, flag, fr_tbar, flag_cell
    if index in flag_cell:
        mfield[index].config(text=" ")
        flag -= 1
        flag_cell.remove(index)
    else:
        mfield[index].config(text="🚩")
        flag += 1
        flag_cell.append(index)

    lab_flag = Label(fr_tbar, text = f"Flags left: {map.nmine - flag}")
    lab_flag.grid(row=0, column=0)

    
def click(index):
    global map, mfield, remain_cell, flag_cell
    if index in flag_cell:
        return
    if map.check_mine(index):
        game_over()
        return
    stack.append(index)
    while stack:
        item = stack.pop(0)
        if item in opened_cell or\
           item in flag_cell:
            continue
        else:
            opened_cell.append(item)
        remain_cell -= 1
        if int(map.get_number_of_mines(item)) > 0:
            txt = map.get_number_of_mines(item)
            mfield[item].config(text=str(txt), bg="grey65")
        else:
            neighbor_list = map.get_side_neighbor(item)
            stack.extend(neighbor_list)
            mfield[item].config(bg="grey")
    if remain_cell == 0:
        win()
                 
def first_click(index):
    global map, flag, mfield
    map.create_map(index)
    for i in range (map.wcell * map.hcell):
        mfield[i].config(command=lambda x=i: click(x))
        mfield[i].bind('<Button-3>', lambda event, x=i: right_click(event, x))
    click(index)

def create_interface_game(level):
    global map, flag, mfield, remain_cell, fr_tbar
    for widget in root.winfo_children():
        widget.destroy()
        
    map = choose_level(level)
    remain_cell = map.hcell * map.wcell - map.nmine 
    mfield = []

    fr_tbar = LabelFrame(root)
    fr_tbar.grid(row=0, column=0)

    fr_game = LabelFrame(root)
    fr_game.grid(row=1, column=0)

    fr_dbar = LabelFrame(root)
    fr_dbar.grid(row=2, column=0)

    lab_flag = Label(fr_tbar, text = f"Flags left: {map.nmine - flag}")
    lab_flag.grid(row=0, column=0)

    for i in range(map.hcell * map.wcell):
        mfield.append(Button(fr_game, height = bt_size, width = bt_size,
                             command=lambda x=i: first_click(x)))
        mfield[i].grid(row=i//map.wcell, column= i%map.wcell)

    root.geometry("")

def win():
    window = Toplevel(root)
    window.title("Winner")
    window.geometry("300x300")
    win_bg = PhotoImage(file = "image/win.png")
    label = Label(window, image = win_bg)
    label.image = win_bg
    label.place(x = 0, y = 0)

    window.protocol("WM_DELETE_WINDOW", root.destroy)

def game_over():
    global map, mfield
    for i in range(map.hcell * map.wcell):
        if map.check_mine(i):
            mfield[i].config(text= "💣")

    window = Toplevel(root)
    window.title("Game Over")
    window.geometry("300x300")
    bomb_bg = PhotoImage(file = "image/bomb.png")
    label = Label(window, image = bomb_bg)
    label.image = bomb_bg
    label.place(x = 0, y = 0)

    window.protocol("WM_DELETE_WINDOW", root.destroy)


Label(
    root, 
    text="MINESWEEPER", 
    font=("Arial", 18, "bold"),
    bg="#FFFFFF",
    fg="blue"
).pack(pady=40)
Label(
    root, 
    text="Choose your level", 
    font=("Arial", 15),
    bg="#FFFFFF"
).pack(pady=(0, 18))

Button(
    root,
    text="Easy",
    width=18,
    height=2,
    command=lambda: create_interface_game(1)
).pack(pady=10, padx=30, fill="x")
Button(
    root,
    text="Normal",
    width=18,
    height=2,
    command=lambda: create_interface_game(2)
).pack(pady=10, padx=30, fill="x")
Button(
    root,
    text="Hard",
    width=18,
    height=2,
    command=lambda: create_interface_game(3)
).pack(pady=10, padx=30, fill="x")
Button(
    root,
    text="Crazy",
    width=18,
    height=2,
    command=lambda: create_interface_game(4)
).pack(pady=10, padx=30, fill="x")


root.mainloop()