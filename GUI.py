import tkinter as tk
import Functions
from tkinter import ttk


root = tk.Tk()

instr = tk.Frame(root)
instr.grid()

txw = 60                            # setting the text box width
txh = 10                            # setting the text box height

range_info = ttk.Label(instr, text="Range")
range_info.grid(row=0, column=0, sticky="nswe")
range_of_instr = tk.Text(instr, height=txh, width=txw)
range_of_instr.grid(row=1, column=0)

transp_info = ttk.Label(instr, text="Transposition")
transp_info.grid(row=0, column=1, sticky="nswe")
transp_info_instr = tk.Text(instr, height=txh, width=txw)
transp_info_instr.grid(row=1, column=1)

qual_info = ttk.Label(instr, text="Qualities")
qual_info.grid(row=2, column=0, sticky="nswe")
qual_info_instr = tk.Text(instr, height=txh, width=txw)
qual_info_instr.grid(row=3, column=0)

roles_info = ttk.Label(instr, text="Roles and additional info")
roles_info.grid(row=2, column=1, sticky="nswe")
roles_info_instr = tk.Text(instr, height=txh, width=txw)
roles_info_instr.grid(row=3, column=1)


def set_entries(range, qualities, transposition, roles):

    range_of_instr.config(state='normal')               # enable write mode on text widget
    range_of_instr.delete(1.0, tk.END)                  # delete previous entry, if there is one
    range_of_instr.insert(tk.END, range)                # set new entry from input
    range_of_instr.config(state='disabled')             # and disable write mode -> read only

    qual_info_instr.config(state='normal')              # with all entries
    qual_info_instr.delete(1.0, tk.END)
    qual_info_instr.insert(tk.END, qualities)
    qual_info_instr.config(state='disabled')

    transp_info_instr.config(state='normal')
    transp_info_instr.delete(1.0, tk.END)
    transp_info_instr.insert(tk.END, transposition)
    transp_info_instr.config(state='disabled')

    roles_info_instr.config(state='normal')
    roles_info_instr.delete(1.0, tk.END)
    roles_info_instr.insert(tk.END, roles)
    roles_info_instr.config(state='disabled')


def violin_data():                                                          # get instruments data with functions from Functions module
    range = Functions.get_range("Strings", "violin")
    qualities = Functions.get_qualities("Strings", "violin")
    transposition = Functions.get_transposition("Strings", "violin")
    roles = Functions.get_roles("Strings", "violin")

    set_entries(range, qualities, transposition, roles)                     # and use the function above to set it correctly


def viola_data():
    range = Functions.get_range("Strings", "viola")
    qualities = Functions.get_qualities("Strings", "viola")
    transposition = Functions.get_transposition("Strings", "viola")
    roles = Functions.get_roles("Strings", "viola")

    set_entries(range, qualities, transposition, roles)


def cello_data():
    range = Functions.get_range("Strings", "violoncello")
    qualities = Functions.get_qualities("Strings", "violoncello")
    transposition = Functions.get_transposition("Strings", "violoncello")
    roles = Functions.get_roles("Strings", "violoncello")

    set_entries(range, qualities, transposition, roles)


def bass_data():
    range = Functions.get_range("Strings", "double_bass")
    qualities = Functions.get_qualities("Strings", "double_bass")
    transposition = Functions.get_transposition("Strings", "double_bass")
    roles = Functions.get_roles("Strings", "double_bass")

    set_entries(range, qualities, transposition, roles)


def pic_data():
    range = Functions.get_range("Woodwinds", "piccolo")
    qualities = Functions.get_qualities("Woodwinds", "piccolo")
    transposition = Functions.get_transposition("Woodwinds", "piccolo")
    roles = Functions.get_roles("Woodwinds", "piccolo")

    set_entries(range, qualities, transposition, roles)


def flute_data():
    range = Functions.get_range("Woodwinds", "flute")
    qualities = Functions.get_qualities("Woodwinds", "flute")
    transposition = Functions.get_transposition("Woodwinds", "flute")
    roles = Functions.get_roles("Woodwinds", "flute")

    set_entries(range, qualities, transposition, roles)


def oboe_data():
    range = Functions.get_range("Woodwinds", "oboe")
    qualities = Functions.get_qualities("Woodwinds", "oboe")
    transposition = Functions.get_transposition("Woodwinds", "oboe")
    roles = Functions.get_roles("Woodwinds", "oboe")

    set_entries(range, qualities, transposition, roles)


def cor_data():
    range = Functions.get_range("Woodwinds", "cor_anglais")
    qualities = Functions.get_qualities("Woodwinds", "cor_anglais")
    transposition = Functions.get_transposition("Woodwinds", "cor_anglais")
    roles = Functions.get_roles("Woodwinds", "cor_anglais")

    set_entries(range, qualities, transposition, roles)


def clar_data():
    range = Functions.get_range("Woodwinds", "clarinet")
    qualities = Functions.get_qualities("Woodwinds", "clarinet")
    transposition = Functions.get_transposition("Woodwinds", "clarinet")
    roles = Functions.get_roles("Woodwinds", "clarinet")

    set_entries(range, qualities, transposition, roles)


def bclar_data():
    range = Functions.get_range("Woodwinds", "bass_clarinet")
    qualities = Functions.get_qualities("Woodwinds", "bass_clarinet")
    transposition = Functions.get_transposition("Woodwinds", "bass_clarinet")
    roles = Functions.get_roles("Woodwinds", "bass_clarinet")

    set_entries(range, qualities, transposition, roles)


def bassoon_data():
    range = Functions.get_range("Woodwinds", "bassoon")
    qualities = Functions.get_qualities("Woodwinds", "bassoon")
    transposition = Functions.get_transposition("Woodwinds", "bassoon")
    roles = Functions.get_roles("Woodwinds", "bassoon")

    set_entries(range, qualities, transposition, roles)


def cbassoon_data():
    range = Functions.get_range("Woodwinds", "contrabassoon")
    qualities = Functions.get_qualities("Woodwinds", "contrabassoon")
    transposition = Functions.get_transposition("Woodwinds", "contrabassoon")
    roles = Functions.get_roles("Woodwinds", "contrabassoon")

    set_entries(range, qualities, transposition, roles)


def horn_data():
    range = Functions.get_range("Brass", "french_horn")
    qualities = Functions.get_qualities("Brass", "french_horn")
    transposition = Functions.get_transposition("Brass", "french_horn")
    roles = Functions.get_roles("Brass", "french_horn")

    set_entries(range, qualities, transposition, roles)


def trumpet_data():
    range = Functions.get_range("Brass", "trumpet")
    qualities = Functions.get_qualities("Brass", "trumpet")
    transposition = Functions.get_transposition("Brass", "trumpet")
    roles = Functions.get_roles("Brass", "trumpet")

    set_entries(range, qualities, transposition, roles)


def t_tromb_data():
    range = Functions.get_range("Brass", "tenor_trombone")
    qualities = Functions.get_qualities("Brass", "tenor_trombone")
    transposition = Functions.get_transposition("Brass", "tenor_trombone")
    roles = Functions.get_roles("Brass", "tenor_trombone")

    set_entries(range, qualities, transposition, roles)


def b_tromb_data():
    range = Functions.get_range("Brass", "bass_trombone")
    qualities = Functions.get_qualities("Brass", "bass_trombone")
    transposition = Functions.get_transposition("Brass", "bass_trombone")
    roles = Functions.get_roles("Brass", "bass_trombone")

    set_entries(range, qualities, transposition, roles)


def cimb_data():
    range = Functions.get_range("Brass", "cimbasso")
    qualities = Functions.get_qualities("Brass", "cimbasso")
    transposition = Functions.get_transposition("Brass", "cimbasso")
    roles = Functions.get_roles("Brass", "cimbasso")

    set_entries(range, qualities, transposition, roles)


def tuba_data():
    range = Functions.get_range("Brass", "tuba")
    qualities = Functions.get_qualities("Brass", "tuba")
    transposition = Functions.get_transposition("Brass", "tuba")
    roles = Functions.get_roles("Brass", "tuba")

    set_entries(range, qualities, transposition, roles)


root.geometry('1600x900')
root.title('The Orchestra')
root.grid()

menubar = tk.Menu(root)
menu1 = tk.Menu(tearoff=0)
menu2 = tk.Menu(tearoff=0)
menu3 = tk.Menu(tearoff=0)
menu4 = tk.Menu(tearoff=0)

menubar.add_cascade(label="Woodwinds", menu=menu1)
menubar.add_cascade(label="Brass", menu=menu2)
menubar.add_cascade(label="Percussion", menu=menu3)
menubar.add_cascade(label="Strings", menu=menu4)


menu1.add_command(label="Piccolo", command=pic_data)
menu1.add_command(label="Flute", command=flute_data)
menu1.add_command(label="Oboe", command=oboe_data)
menu1.add_command(label="Cor Anglais", command=cor_data)
menu1.add_command(label="Clarinet", command=clar_data)
menu1.add_command(label="Bass Clarinet", command=bclar_data)
menu1.add_command(label="Bassoon", command=bassoon_data)
menu1.add_command(label="Contrabassoon", command=cbassoon_data)


menu2.add_command(label="French Horn", command=horn_data)
menu2.add_command(label="Trumpet", command=trumpet_data)
menu2.add_command(label="Tenor Trombone", command=t_tromb_data)
menu2.add_command(label="Bass Trombone", command=b_tromb_data)
menu2.add_command(label="Cimbasso", command=cimb_data)
menu2.add_command(label="Tuba", command=tuba_data)

menu3.add_command(label="Harp")

menu4.add_command(label="Violin", command=violin_data)
menu4.add_command(label="Viola", command=viola_data)
menu4.add_command(label="Violoncello", command=cello_data)
menu4.add_command(label="Double Bass", command=bass_data)

root.config(menu=menubar)


root.mainloop()
