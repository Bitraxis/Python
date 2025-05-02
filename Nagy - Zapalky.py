from tkinter import *
from tkinter import ttk
import random


# Definicie (Object oriented programming wannabe) tu si definujem niake funkcie otvorenie noveho okna a hlavne funkcie hry, thanks python docs
# Vacsina print je na lepsi debug keby nahodou sa vsetko pokazi :( (stalo sa uz milion krat asi)
# Game funkcie definicie
def button_select(button_id):  # logika vyberania zápaliek
    if button_id in selected_buttons:
        selected_buttons.remove(button_id)
        buttons[button_id].config(relief="raised")
    elif len(selected_buttons) < 3:
        selected_buttons.append(button_id)
        buttons[button_id].config(relief="flat")
    print(f"Vybraté zápalky: {selected_buttons}")


def computer_turn():  # fake ai trosku kodu zo stackoverflow kde mi super ludia pomohli (Hlavne Kevin E ktory musel dumat so mnou (velka kontribucia ktoru som nemenil riadky 25 - 31))
    global last_player
    available_buttons = list(buttons.keys())
    if not available_buttons:
        result_label.config(text="Si vyhral!")
        return
    num_to_select = random.randint(1, min(3, len(available_buttons)))
    computer_selection = random.sample(available_buttons, num_to_select)
    print(f"Počítač vybral tieto zápalky: {computer_selection}")
    # Remove the selected buttons from the grid and set the result_label.config because for some reason python also needs to set result_label.config twice?
    for button_id in computer_selection:
        buttons[button_id].grid_remove()
        del buttons[button_id]
    if not buttons:
        result_label.config(text="Si vyhral!")
    return
    last_player = "Computer"  # pocitac nieco spravil
    result_label.config(text="Si na rade!")


def confirm_selection():
    global last_player
    print(f"Potvrdená selekcia: {selected_buttons}")
    for button_id in selected_buttons:
        buttons[button_id].grid_remove()
        del buttons[button_id]
    selected_buttons.clear()
    if not buttons:
        result_label.config(text="Počítač vyhral")
        return
    last_player = "Player"  # ktory hrac to teraz spravil
    computer_turn()  # to nase fake ai


# Hra definicie
# Lahka
def easy():
    lahka = Tk()
    lahka.geometry("320x200")
    lahka.title("Zápalky")
    global buttons, selected_buttons, result_label, last_player
    buttons = {}
    selected_buttons = []
    last_player = None
    rows = 4
    columns = 4
    row_val = 0
    while row_val < rows:
        column_val = 0
        while column_val < columns:
            button_id = row_val * columns + column_val
            button = Button(
                lahka, text="l", width=10, command=lambda b=button_id: button_select(b)
            )
            button.grid(row=row_val, column=column_val)
            buttons[button_id] = button
            column_val += 1
        row_val += 1
    ttk.Label(lahka, text="Vyber si 1 alebo 3 zapalky").grid(
        column=1, row=row_val, columnspan=2
    )
    ttk.Button(lahka, text="Potvrdiť výber", command=confirm_selection).grid(
        column=1, row=row_val + 1, columnspan=2
    )
    result_label = ttk.Label(lahka, text="Si na rade!")
    result_label.grid(column=0, row=row_val + 2, columnspan=4)


# Stredna
def medium():
    stredna = Tk()
    stredna.geometry("480x300")
    stredna.title("Zápalky")
    global buttons, selected_buttons, result_label, last_player
    buttons = {}
    selected_buttons = []
    last_player = None
    rows = 6
    columns = 6
    row_val = 0
    while row_val < rows:
        column_val = 0
        while column_val < columns:
            button_id = row_val * columns + column_val
            button = Button(
                stredna,
                text="l",
                width=10,
                command=lambda b=button_id: button_select(b),
            )
            button.grid(row=row_val, column=column_val)
            buttons[button_id] = button
            column_val += 1
        row_val += 1
    ttk.Label(stredna, text="Vyber si 1 alebo 3 zapalky").grid(
        column=1, row=row_val, columnspan=4
    )
    ttk.Button(stredna, text="Potvrdiť výber", command=confirm_selection).grid(
        column=1, row=row_val + 1, columnspan=4
    )
    result_label = ttk.Label(stredna, text="Si na rade!")
    result_label.grid(column=1, row=row_val + 2, columnspan=4)


# Tazka
def hard():
    tazka = Tk()
    tazka.geometry("725x320")
    tazka.title("Zápalky")
    global buttons, selected_buttons, result_label, last_player
    buttons = {}
    selected_buttons = []
    last_player = None
    rows = 9
    columns = 9
    row_val = 0
    while row_val < rows:
        column_val = 0
        while column_val < columns:
            button_id = row_val * columns + column_val
            button = Button(
                tazka, text="l", width=10, command=lambda b=button_id: button_select(b)
            )
            button.grid(row=row_val, column=column_val)
            buttons[button_id] = button
            column_val += 1
        row_val += 1
    ttk.Label(tazka, text="Vyber si 1 alebo 3 zapalky").grid(
        column=2, row=row_val, columnspan=5
    )
    ttk.Button(tazka, text="Potvrdiť výber", command=confirm_selection).grid(
        column=2, row=row_val + 1, columnspan=5
    )
    result_label = ttk.Label(tazka, text="Si na rade!")
    result_label.grid(column=2, row=row_val + 2, columnspan=5)


# Vlastna obtiaznost (dakujem githubu ludom na reddite a stackoverflowe ktorymi pomohli s tymto peklom, by som tu to aj linkol len je uz koniec decembra a moderatori to removli 10/10
def custom_difficulty(rows, columns):
    custom = Tk()
    custom.geometry(f"{columns * 100 + 50}x{rows * 50 + 100}")
    custom.title("Zápalky")
    global buttons, selected_buttons, result_label, last_player
    buttons = {}
    selected_buttons = []
    last_player = None
    row_val = 0

    while row_val < rows:
        column_val = 0
        while column_val < columns:
            button_id = row_val * columns + column_val
            button = Button(
                custom, text="l", width=10, command=lambda b=button_id: button_select(b)
            )
            button.grid(row=row_val, column=column_val)
            buttons[button_id] = button
            column_val += 1
        row_val += 1
    ttk.Label(custom, text="Vyber si 1 alebo 3 zapalky").grid(
        column=0, row=row_val, columnspan=columns
    )
    ttk.Button(custom, text="Potvrdiť výber", command=confirm_selection).grid(
        column=0, row=row_val + 1, columnspan=columns
    )
    result_label = ttk.Label(custom, text="Si na rade!")
    result_label.grid(column=0, row=row_val + 2, columnspan=columns)


def set_custom_difficulty():
    setup = Tk()
    setup.title("Nastavenie vlastnej obtiažnosti")
    ttk.Label(setup, text="Zadajte počet riadkov:").grid(column=0, row=0)
    rows_entry = ttk.Entry(setup)
    rows_entry.grid(column=1, row=0)
    ttk.Label(setup, text="Zadajte počet stĺpcov:").grid(column=0, row=1)
    columns_entry = ttk.Entry(setup)
    columns_entry.grid(column=1, row=1)

    def start_custom_game():
        try:
            rows = int(rows_entry.get())
            columns = int(columns_entry.get())
            if rows > 0 and columns > 0:
                setup.destroy()
                custom_difficulty(rows, columns)
            else:
                print("Hodnoty musia byť väčšie ako 0!")
        except ValueError:
            print("Zadajte platné čísla!")

    ttk.Button(setup, text="Začať hru", command=start_custom_game).grid(
        column=0, row=2, columnspan=2
    )


# Najprv si nastavim prve okno z menom obtiaznost tu ako z nazvu vyplyva vyberieme obtiaznost hry
obtiaznost = Tk()
obtiaznost.title("Vyber si obtiažnosť")
frm = ttk.Frame(obtiaznost, padding=10)
frm.grid()
ttk.Label(frm, text="Vyber si obtiažnosť").grid(column=0, row=0, columnspan=3)
ttk.Button(frm, text="Ľahká", command=easy).grid(column=0, row=1)
ttk.Button(frm, text="Stredná", command=medium).grid(column=1, row=1)
ttk.Button(frm, text="Ťažká", command=hard).grid(column=2, row=1)
ttk.Button(
    frm,
    text="Vlastná (Može byť divné pri veľkých číslach)",
    command=set_custom_difficulty,
).grid(
    column=0, row=2, columnspan=4
)  # po dlhom hladani som nasiel github repo kde niekdo spravil presne tuto hru tak som sa inspiroval ako spravit vlastnu obtiaznost ale moje riesenie nie je presne ako on mal len som potreboval bod odskoku
obtiaznost.mainloop()
# Chcel som aj konzolovu verziu len je 10.01.2025 a sa mi uz nechce, kod viem vysvetlit sak som na nom robil od zadania ulohy az poteraz, a vacsinu ktory som nerobil mi ludia vystvetlili (hlavne u/desrtfx na subreddite r/learnprogramming ktory mi pomohol ale aj tak zdovodnil ze moj post sa nehodil na ten subreddit)
