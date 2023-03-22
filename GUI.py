import tkinter as tk
import Functions
import Instruments
from tkinter import ttk
import pandas as pd
import Plot

txw = 60                                            # setting the text box width
txh = 10                                            # setting the text box height
font_tuple = ("Helvetica", 12, "bold")
font_tuple_heading = ("Helvetica", 14, "bold")
# program_color = '#C0C0C0'
widget_color = '#FFFFFF'

root = tk.Tk()
root.geometry('1900x980')
root.title('The Orchestra')
root.grid()
root.config()


plot_frame = tk.Frame(root)
plot_frame.grid(row=1, column=0, padx=60, pady=40)

plot_btn_fr = tk.Frame(root)
plot_btn_fr.grid(row=1, column=1, padx=20, columnspan=4)

instr = tk.Frame(root)
instr.grid(row=0, column=0, columnspan=2)


s = ttk.Style()
s.configure('.', font=('Helvetica', 14))


current_selected_instr = tk.Text(instr, height=txh*0.1, relief='flat', bg=widget_color)                       # shows the current selected instrument
current_selected_instr.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

range_info = ttk.Label(instr, text="Range")
range_info.grid(row=1, column=0, padx=20, pady=10)
range_of_instr = tk.Text(instr, height=txh*0.4, width=txw, relief='flat', bg=widget_color)
range_of_instr.grid(row=2, column=0, padx=10)

transp_info = ttk.Label(instr, text="Transposition")
transp_info.grid(row=1, column=1, padx=20, pady=10)
transp_info_instr = tk.Text(instr, height=txh*0.4, width=txw, relief='flat', bg=widget_color)
transp_info_instr.grid(row=2, column=1, padx=10)

qual_info = ttk.Label(instr, text="Qualities")
qual_info.grid(row=4, column=0, padx=20, pady=10)
qual_info_instr = tk.Text(instr, height=txh, width=txw, relief='flat', bg=widget_color)
qual_info_instr.grid(row=5, column=0, padx=10)

roles_info = ttk.Label(instr, text="Roles and additional info")
roles_info.grid(row=4, column=1, padx=20, pady=10)
roles_info_instr = tk.Text(instr, height=txh, width=txw, relief='flat', bg=widget_color)
roles_info_instr.grid(row=5, column=1, padx=10)


def set_entries(range, qualities, transposition, roles):

    range_of_instr.config(state='normal')               # enable write mode on text widget
    range_of_instr.delete(0.0, tk.END)                  # delete previous entry, if there is one
    range_of_instr.insert(tk.END, range)                # set new entry from input
    range_of_instr.config(font=font_tuple)
    range_of_instr.config(state='disabled')             # and disable write mode -> read only

    qual_info_instr.config(state='normal')              # with all entries
    qual_info_instr.delete(0.0, tk.END)
    for quality in qualities:                           # qualities is a list, which has to be treated differently
        qual_info_instr.insert(tk.END, quality)
    qual_info_instr.config(font=font_tuple)
    qual_info_instr.config(state='disabled')

    transp_info_instr.config(state='normal')
    transp_info_instr.delete(0.0, tk.END)
    transp_info_instr.insert(tk.END, transposition)
    transp_info_instr.config(font=font_tuple)
    transp_info_instr.config(state='disabled')

    roles_info_instr.config(state='normal')
    roles_info_instr.delete(0.0, tk.END)
    roles_info_instr.insert(tk.END, roles)
    roles_info_instr.config(font=font_tuple)
    roles_info_instr.config(state='disabled')


def show_current_instr(instrument):                             # updates the current instrument in the label
    current_selected_instr.config(state='normal')
    current_selected_instr.delete(0.0, tk.END)
    current_selected_instr.insert(tk.END, instrument)
    current_selected_instr.tag_add('center', 0.0, tk.END)
    current_selected_instr.tag_config('center', justify='center')
    current_selected_instr.config(font=font_tuple_heading)
    current_selected_instr.config(state='disabled')


def violin_data():                                                          # get instruments data with functions from Functions module
    range = Functions.get_range("Strings", "violin")
    qualities = Functions.get_qualities("Strings", "violin")
    transposition = Functions.get_transposition("Strings", "violin")
    roles = Functions.get_roles("Strings", "violin")
    show_current_instr("Violin")
    set_entries(range, qualities, transposition, roles)                     # and use the function above to set it correctly


def viola_data():
    range = Functions.get_range("Strings", "viola")
    qualities = Functions.get_qualities("Strings", "viola")
    transposition = Functions.get_transposition("Strings", "viola")
    roles = Functions.get_roles("Strings", "viola")
    show_current_instr("Viola")
    set_entries(range, qualities, transposition, roles)


def cello_data():
    range = Functions.get_range("Strings", "violoncello")
    qualities = Functions.get_qualities("Strings", "violoncello")
    transposition = Functions.get_transposition("Strings", "violoncello")
    roles = Functions.get_roles("Strings", "violoncello")
    show_current_instr("Violoncello")
    set_entries(range, qualities, transposition, roles)


def bass_data():
    range = Functions.get_range("Strings", "double_bass")
    qualities = Functions.get_qualities("Strings", "double_bass")
    transposition = Functions.get_transposition("Strings", "double_bass")
    roles = Functions.get_roles("Strings", "double_bass")
    show_current_instr("Double Bass")
    set_entries(range, qualities, transposition, roles)


def pic_data():
    range = Functions.get_range("Woodwinds", "piccolo")
    qualities = Functions.get_qualities("Woodwinds", "piccolo")
    transposition = Functions.get_transposition("Woodwinds", "piccolo")
    roles = Functions.get_roles("Woodwinds", "piccolo")
    show_current_instr("Piccolo Flute")
    set_entries(range, qualities, transposition, roles)


def flute_data():
    range = Functions.get_range("Woodwinds", "flute")
    qualities = Functions.get_qualities("Woodwinds", "flute")
    transposition = Functions.get_transposition("Woodwinds", "flute")
    roles = Functions.get_roles("Woodwinds", "flute")
    show_current_instr("Flute")
    set_entries(range, qualities, transposition, roles)


def oboe_data():
    range = Functions.get_range("Woodwinds", "oboe")
    qualities = Functions.get_qualities("Woodwinds", "oboe")
    transposition = Functions.get_transposition("Woodwinds", "oboe")
    roles = Functions.get_roles("Woodwinds", "oboe")
    show_current_instr("Oboe")
    set_entries(range, qualities, transposition, roles)


def cor_data():
    range = Functions.get_range("Woodwinds", "cor_anglais")
    qualities = Functions.get_qualities("Woodwinds", "cor_anglais")
    transposition = Functions.get_transposition("Woodwinds", "cor_anglais")
    roles = Functions.get_roles("Woodwinds", "cor_anglais")
    show_current_instr("Cor Anglais")
    set_entries(range, qualities, transposition, roles)


def clar_data():
    range = Functions.get_range("Woodwinds", "clarinet")
    qualities = Functions.get_qualities("Woodwinds", "clarinet")
    transposition = Functions.get_transposition("Woodwinds", "clarinet")
    roles = Functions.get_roles("Woodwinds", "clarinet")
    show_current_instr("Clarinet")
    set_entries(range, qualities, transposition, roles)


def bclar_data():
    range = Functions.get_range("Woodwinds", "bass_clarinet")
    qualities = Functions.get_qualities("Woodwinds", "bass_clarinet")
    transposition = Functions.get_transposition("Woodwinds", "bass_clarinet")
    roles = Functions.get_roles("Woodwinds", "bass_clarinet")
    show_current_instr("Bass Clarinet")
    set_entries(range, qualities, transposition, roles)


def bassoon_data():
    range = Functions.get_range("Woodwinds", "bassoon")
    qualities = Functions.get_qualities("Woodwinds", "bassoon")
    transposition = Functions.get_transposition("Woodwinds", "bassoon")
    roles = Functions.get_roles("Woodwinds", "bassoon")
    show_current_instr("Bassoon")
    set_entries(range, qualities, transposition, roles)


def cbassoon_data():
    range = Functions.get_range("Woodwinds", "contrabassoon")
    qualities = Functions.get_qualities("Woodwinds", "contrabassoon")
    transposition = Functions.get_transposition("Woodwinds", "contrabassoon")
    roles = Functions.get_roles("Woodwinds", "contrabassoon")
    show_current_instr("Contrabassoon")
    set_entries(range, qualities, transposition, roles)


def horn_data():
    range = Functions.get_range("Brass", "french_horn")
    qualities = Functions.get_qualities("Brass", "french_horn")
    transposition = Functions.get_transposition("Brass", "french_horn")
    roles = Functions.get_roles("Brass", "french_horn")
    show_current_instr("French Horn")
    set_entries(range, qualities, transposition, roles)


def trumpet_data():
    range = Functions.get_range("Brass", "trumpet")
    qualities = Functions.get_qualities("Brass", "trumpet")
    transposition = Functions.get_transposition("Brass", "trumpet")
    roles = Functions.get_roles("Brass", "trumpet")
    show_current_instr("Trumpet")
    set_entries(range, qualities, transposition, roles)


def t_tromb_data():
    range = Functions.get_range("Brass", "tenor_trombone")
    qualities = Functions.get_qualities("Brass", "tenor_trombone")
    transposition = Functions.get_transposition("Brass", "tenor_trombone")
    roles = Functions.get_roles("Brass", "tenor_trombone")
    show_current_instr("Tenor Trombone")
    set_entries(range, qualities, transposition, roles)


def b_tromb_data():
    range = Functions.get_range("Brass", "bass_trombone")
    qualities = Functions.get_qualities("Brass", "bass_trombone")
    transposition = Functions.get_transposition("Brass", "bass_trombone")
    roles = Functions.get_roles("Brass", "bass_trombone")
    show_current_instr("Bass Trombone")
    set_entries(range, qualities, transposition, roles)


def cimb_data():
    range = Functions.get_range("Brass", "cimbasso")
    qualities = Functions.get_qualities("Brass", "cimbasso")
    transposition = Functions.get_transposition("Brass", "cimbasso")
    roles = Functions.get_roles("Brass", "cimbasso")
    show_current_instr("Cimbasso")
    set_entries(range, qualities, transposition, roles)


def tuba_data():
    range = Functions.get_range("Brass", "tuba")
    qualities = Functions.get_qualities("Brass", "tuba")
    transposition = Functions.get_transposition("Brass", "tuba")
    roles = Functions.get_roles("Brass", "tuba")
    show_current_instr("Tuba")
    set_entries(range, qualities, transposition, roles)


def timp_data():
    range = Functions.get_range("Percussion", "timpani")
    qualities = Functions.get_qualities("Percussion", "timpani")
    transposition = Functions.get_transposition("Percussion", "timpani")
    roles = Functions.get_roles("Percussion", "timpani")
    show_current_instr("Timpani")
    set_entries(range, qualities, transposition, roles)


def harp_data():
    range = Functions.get_range("Percussion", "harp")
    qualities = Functions.get_qualities("Percussion", "harp")
    transposition = Functions.get_transposition("Percussion", "harp")
    roles = Functions.get_roles("Percussion", "harp")
    show_current_instr("Harp")
    set_entries(range, qualities, transposition, roles)


def marimba_data():
    range = Functions.get_range("Percussion", "marimba")
    qualities = Functions.get_qualities("Percussion", "marimba")
    transposition = Functions.get_transposition("Percussion", "marimba")
    roles = Functions.get_roles("Percussion", "marimba")
    show_current_instr("Marimba")
    set_entries(range, qualities, transposition, roles)


def celeste_data():
    range = Functions.get_range("Percussion", "celeste")
    qualities = Functions.get_qualities("Percussion", "celeste")
    transposition = Functions.get_transposition("Percussion", "celeste")
    roles = Functions.get_roles("Percussion", "celeste")
    show_current_instr("Celeste")
    set_entries(range, qualities, transposition, roles)


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

menu3.add_command(label="Timpani", command=timp_data)
menu3.add_command(label="Harp", command=harp_data)
menu3.add_command(label="Celeste", command=celeste_data)
menu3.add_command(label="Marimba", command=marimba_data)

menu4.add_command(label="Violin", command=violin_data)
menu4.add_command(label="Viola", command=viola_data)
menu4.add_command(label="Violoncello", command=cello_data)
menu4.add_command(label="Double Bass", command=bass_data)

root.config(menu=menubar)


instr_list = []
for section in Instruments.all_instruments.keys():
    p = Functions.get_section(section)
    for instr in p.keys():
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


root.mainloop()
