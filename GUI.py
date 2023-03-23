import tkinter as tk
from tkinter import ttk
import pandas as pd
import Plot
import Functions
import Instruments


"""
This module is dedicated towards the GUI creation of the program using Tkinter. The GUI is divided into two main section:
The information panel and the plot. Each can be controlled separately. The code is designed in a way, which makes adding
new instruments easy. 

The information panel presents selective information
of each selected instrument. One can select the instrument via a dedicated menu at the top.

The plotting function can be accessed with dedicated buttons. Each button plots the ranges of the corresponding section's 
instruments in a plot. The plot is created in a class in the Plot.py module.

"""

root = tk.Tk()
root.geometry('1900x980')
root.title('The Orchestra')


"""
Setting the settings for the style of the GUI.
"""

TXW = 60                                            # setting the text box width
TXH = 10                                            # setting the text box height
FONT_TUPLE = ("Helvetica", 12, "bold")
FONT_TUPLE_HEADING = ("Helvetica", 14, "bold")
WIDGET_COLOR = '#FFFFFF'
s = ttk.Style()
s.configure('.', font=('Helvetica', 14))


"""
Creating and arranging the frames, we will later utilize.
"""

plot_frame = tk.Frame(root)
plot_frame.grid(row=1, column=0, padx=60, pady=40)

plot_btn_fr = tk.Frame(root)
plot_btn_fr.grid(row=1, column=1, padx=20, columnspan=4)

instr = tk.Frame(root)
instr.grid(row=0, column=0, columnspan=2)


"""
Creating the text and label widgets of the information panel.
"""

current_selected_instr = tk.Text(instr, height=TXH*0.1, relief='flat', bg=WIDGET_COLOR)                       # shows the current selected instrument
current_selected_instr.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

range_info = ttk.Label(instr, text="Range (written pitches)")
range_info.grid(row=1, column=0, padx=20, pady=10)
range_of_instr = tk.Text(instr, height=TXH*0.4, width=TXW, relief='flat', bg=WIDGET_COLOR)
range_of_instr.grid(row=2, column=0, padx=10)

transp_info = ttk.Label(instr, text="Transposition")
transp_info.grid(row=1, column=1, padx=20, pady=10)
transp_info_instr = tk.Text(instr, height=TXH*0.4, width=TXW, relief='flat', bg=WIDGET_COLOR)
transp_info_instr.grid(row=2, column=1, padx=10)

qual_info = ttk.Label(instr, text="Qualities (written pitches)")
qual_info.grid(row=4, column=0, padx=20, pady=10)
qual_info_instr = tk.Text(instr, height=TXH, width=TXW, relief='flat', bg=WIDGET_COLOR)
qual_info_instr.grid(row=5, column=0, padx=10)

roles_info = ttk.Label(instr, text="Roles and additional info")
roles_info.grid(row=4, column=1, padx=20, pady=10)
roles_info_instr = tk.Text(instr, height=TXH, width=TXW, relief='flat', bg=WIDGET_COLOR)
roles_info_instr.grid(row=5, column=1, padx=10)


def set_entries(range, qualities, transposition, roles):
    """Enters a given text to the text widgets of the information panel."""
    range_of_instr.config(state='normal')               # enable write mode on text widget
    range_of_instr.delete(0.0, tk.END)                  # delete previous entry, if there is one
    range_of_instr.insert(tk.END, range)                # set new entry from input
    range_of_instr.config(font=FONT_TUPLE)
    range_of_instr.config(state='disabled')             # and disable write mode -> read only

    qual_info_instr.config(state='normal')              # with all entries
    qual_info_instr.delete(0.0, tk.END)
    for quality in qualities:                           # qualities is a list, which has to be treated differently
        qual_info_instr.insert(tk.END, quality)
    qual_info_instr.config(font=FONT_TUPLE)
    qual_info_instr.config(state='disabled')

    transp_info_instr.config(state='normal')
    transp_info_instr.delete(0.0, tk.END)
    transp_info_instr.insert(tk.END, transposition)
    transp_info_instr.config(font=FONT_TUPLE)
    transp_info_instr.config(state='disabled')

    roles_info_instr.config(state='normal')
    roles_info_instr.delete(0.0, tk.END)
    roles_info_instr.insert(tk.END, roles)
    roles_info_instr.config(font=FONT_TUPLE)
    roles_info_instr.config(state='disabled')


def show_current_instr(instrument):
    """Updates the current selected instrument in the dedicated label"""
    current_selected_instr.config(state='normal')
    current_selected_instr.delete(0.0, tk.END)
    instrument = instrument.replace('_', ' ').title()                       # removes the underscore and makes it capital letter
    current_selected_instr.insert(tk.END, instrument)
    current_selected_instr.tag_add('center', 0.0, tk.END)
    current_selected_instr.tag_config('center', justify='center')           # centers the text within the widget
    current_selected_instr.config(font=FONT_TUPLE_HEADING)
    current_selected_instr.config(state='disabled')


def instr123_data(section1, instrument1):
    """Getting the data from a given instrument and processes them in the "set_entries" function. Also updating the current instruments title. """
    range = Functions.get_range(section1, instrument1)
    qualities = Functions.get_qualities(section1, instrument1)
    transposition = Functions.get_transposition(section1, instrument1)
    roles = Functions.get_roles(section1, instrument1)
    show_current_instr(instrument1)
    set_entries(range, qualities, transposition, roles)


"""
We configure the menu, from which we can select each available instrument. 
"""

menubar = tk.Menu(root)
menu1 = tk.Menu(tearoff=0)
menu2 = tk.Menu(tearoff=0)
menu3 = tk.Menu(tearoff=0)
menu4 = tk.Menu(tearoff=0)

menubar.add_cascade(label="Woodwinds", menu=menu1)
menubar.add_cascade(label="Brass", menu=menu2)
menubar.add_cascade(label="Percussion", menu=menu3)
menubar.add_cascade(label="Strings", menu=menu4)

menu1.add_command(label="Piccolo", command=lambda: instr123_data("Woodwinds", "piccolo"))
menu1.add_command(label="Flute", command=lambda: instr123_data("Woodwinds", "flute"))
menu1.add_command(label="Oboe", command=lambda: instr123_data("Woodwinds", "oboe"))
menu1.add_command(label="Cor Anglais", command=lambda: instr123_data("Woodwinds", "cor_anglais"))
menu1.add_command(label="Clarinet", command=lambda: instr123_data("Woodwinds", "clarinet"))
menu1.add_command(label="Bass Clarinet", command=lambda: instr123_data("Woodwinds", "bass_clarinet"))
menu1.add_command(label="Bassoon", command=lambda: instr123_data("Woodwinds", "bassoon"))
menu1.add_command(label="Contrabassoon", command=lambda: instr123_data("Woodwinds", "contrabassoon"))

menu2.add_command(label="French Horn", command=lambda: instr123_data("Brass", "french_horn"))
menu2.add_command(label="Trumpet", command=lambda: instr123_data("Brass", "trumpet"))
menu2.add_command(label="Tenor Trombone", command=lambda: instr123_data("Brass", "tenor_trombone"))
menu2.add_command(label="Bass Trombone", command=lambda: instr123_data("Brass", "bass_trombone"))
menu2.add_command(label="Cimbasso", command=lambda: instr123_data("Brass", "cimbasso"))
menu2.add_command(label="Tuba", command=lambda: instr123_data("Brass", "tuba"))

menu3.add_command(label="Timpani", command=lambda: instr123_data("Percussion", "timpani"))
menu3.add_command(label="Harp", command=lambda: instr123_data("Percussion", "harp"))
menu3.add_command(label="Celeste", command=lambda: instr123_data("Percussion", "celeste"))
menu3.add_command(label="Marimba", command=lambda: instr123_data("Percussion", "marimba"))

menu4.add_command(label="Violin", command=lambda: instr123_data("Strings", "violin"))
menu4.add_command(label="Viola", command=lambda: instr123_data("Strings", "viola"))
menu4.add_command(label="Violoncello", command=lambda: instr123_data("Strings", "violoncello"))
menu4.add_command(label="Double Bass", command=lambda: instr123_data("Strings", "double_bass"))

root.config(menu=menubar)


"""
Writing the relevant data in a sorted list. Using a dictionary format, we format the data into dataframe using Pandas. 
With Orch we instance the class Plot from Plot.py. 
"""

instr_list = []
for section in Instruments.all_instruments.keys():
    p = Functions.get_section(section)                                                  # p is representing the sections in form of a dictionary
    for instr in p.keys():                                                              # of which instruments we iterate
        instr_data = Functions.select_instrument(section, instr)
        midi_range_high = instr_data["RangeM_high"]
        midi_range_low = instr_data["RangeM_low"]
        instr_list.append((section, instr, midi_range_low, midi_range_high))

data_dict = {"Section": [instr_list[i][0] for i in range(len(instr_list))],
             "Instrument": [instr_list[i][1] for i in range(len(instr_list))],
             "Range_low": [float(instr_list[i][2]) for i in range(len(instr_list))],
             "Range_high": [float(instr_list[i][3]) for i in range(len(instr_list))]
             }

data = pd.DataFrame(data_dict)

Orch = Plot.Plot(plot_frame, (8, 5), data=data)


"""
Defining the plotting functions separately and their corresponding buttons. 
Doing this in the class would lead to unwanted results when plotting the whole orchestra. 
"""


def plot_strings():
    Orch.clearplot()
    Orch.plot_strings()


def plot_woods():
    Orch.clearplot()
    Orch.plot_woods()


def plot_brass():
    Orch.clearplot()
    Orch.plot_brass()


def plot_perc():
    Orch.clearplot()
    Orch.plot_perc()


def plot_whole_orchestra():
    Orch.clearplot()
    Orch.plot_orchestra()


plot_title = ttk.Label(plot_btn_fr, text="Show the ranges of each sections instruments:")
plot_title.grid(row=0, column=0, columnspan=2)
plot_strings_btn = ttk.Button(plot_btn_fr, text="Strings", command=plot_strings)
plot_strings_btn.grid(row=1, column=0)
plot_brass_btn = ttk.Button(plot_btn_fr, text="Brass", command=plot_brass)
plot_brass_btn.grid(row=1, column=1)
plot_woods_btn = ttk.Button(plot_btn_fr, text="Woodwinds", command=plot_woods)
plot_woods_btn.grid(row=2, column=0)
plot_perc_btn = ttk.Button(plot_btn_fr, text="Percussion", command=plot_perc)
plot_perc_btn.grid(row=2, column=1)
plot_orchestra_btn = ttk.Button(plot_btn_fr, text="Whole Orchestra", command=plot_whole_orchestra)
plot_orchestra_btn.grid(row=3, columnspan=2)
plot_clear_btn = ttk.Button(plot_btn_fr, text="Clear Data", command=Orch.clearplot)
plot_clear_btn.grid(row=4, columnspan=2)


root.mainloop()
