import Additional_Functions as adf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

'''
This module creates a class responsible for plotting the data correctly. The instance of the class is inside GUI. 

The plot shows the notation range on the x axis, which goes from A0 (21 in MIDI) up to C8 (108 in MIDI).
The instruments are plotted in horizontal bars showing their minimum and maximum note values. 

'''


class Plot:

    def __init__(self, masterframe, size, data):
        self.data = data
        self.instruments = self.data["Instrument"]
        self.left_val = self.data["Range_low"]
        self.right_val = self.data["Range_high"]
        self.data["width"] = self.data["Range_high"] - self.data["Range_low"]               # bars are located by their left value and width
        self.figure = plt.Figure(size)
        self.axes = self.figure.add_subplot()
        self.axes.set_xlim(21, 108, auto=False)                                             # notation on the x-axis range from 21 to 108
        self.axes.grid(visible=True, axis='x')
        self.c1 = FigureCanvasTkAgg(self.figure, master=masterframe)
        self.c1.get_tk_widget().grid(column=0, row=0)                                       # creates a tk reference widget
        self.axes.set_title("Instruments in their range")
        self.axes.set_xlabel("Notes")
        self.axes.set_ylabel("Instruments")
        self.figure.tight_layout()
        self.figure.subplots_adjust(left=0.17)                                              # the plot position has to be adjusted for the instruments to show
        self.axes.set_xticks(adf.set_xticks_labels(), adf.set_x_axis())                     # set the corresponding note names as labels at each octave

    def plot_strings(self):
        """Plots the ranges of the instruments of the String choir."""
        filt_string = self.data["Section"] == "Strings"
        String_instruments = self.data.loc[filt_string, "Instrument"]
        Left_val_string = self.data.loc[filt_string, "Range_low"]                           # horizontal bar is fixed on the left_val
        Right_val_string = self.data.loc[filt_string, "Range_high"]
        self.data["width_strings"] = Right_val_string - Left_val_string                     # and the width is added to get to the right_val
        data_strings_width = self.data["width_strings"].dropna()                            # Deletes empty entries, which would cause problems during plotting due to a mismatch

        self.axes.barh(String_instruments, data_strings_width, left=Left_val_string,
                       height=0.5, color="blue", edgecolor='black')
        self.axes.set_xticks(adf.set_xticks_labels(), adf.set_x_axis())
        self.c1.draw()

    def plot_woods(self):
        """Plots the ranges of the instruments from the Woodwind choir."""
        filt_woods = self.data["Section"] == "Woodwinds"
        Woodwind_instruments = self.data.loc[filt_woods, "Instrument"]
        Left_val_woods = self.data.loc[filt_woods, "Range_low"]
        Right_val_woods = self.data.loc[filt_woods, "Range_high"]
        self.data["width_woods"] = Right_val_woods - Left_val_woods
        data_woods_width = self.data["width_woods"].dropna()

        self.axes.barh(Woodwind_instruments, data_woods_width, left=Left_val_woods,
                       height=0.5, color="green", edgecolor='black')
        self.axes.set_xticks(adf.set_xticks_labels(), adf.set_x_axis())
        self.c1.draw()

    def plot_brass(self):
        """Plots the ranges of the instruments from the Brass choir."""
        filt_brass = self.data["Section"] == "Brass"
        Brass_instruments = self.data.loc[filt_brass, "Instrument"]
        Left_val_brass = self.data.loc[filt_brass, "Range_low"]
        Right_val_brass = self.data.loc[filt_brass, "Range_high"]
        self.data["width_brass"] = Right_val_brass - Left_val_brass
        data_brass_width = self.data["width_brass"].dropna()

        self.axes.barh(Brass_instruments, data_brass_width, left=Left_val_brass,
                       height=0.5, color="yellow", edgecolor='black')
        self.axes.set_xticks(adf.set_xticks_labels(), adf.set_x_axis())
        self.c1.draw()

    def plot_perc(self):
        """Plots the ranges of the instruments from the Percussion choir."""
        filt_perc = self.data["Section"] == "Percussion"
        Perc_instruments = self.data.loc[filt_perc, "Instrument"]
        Left_val_perc = self.data.loc[filt_perc, "Range_low"]
        Right_val_perc = self.data.loc[filt_perc, "Range_high"]
        self.data["width_perc"] = Right_val_perc - Left_val_perc
        data_perc_width = self.data["width_perc"].dropna()

        self.axes.barh(Perc_instruments, data_perc_width, left=Left_val_perc,
                       height=0.5, color="red", edgecolor='black')
        self.axes.set_xticks(adf.set_xticks_labels(), adf.set_x_axis())
        self.c1.draw()

    def plot_orchestra(self):
        """Plots the ranges of the instruments of the whole orchestra. Each section has their individual color."""
        self.plot_strings()
        self.plot_brass()
        self.plot_woods()
        self.plot_perc()
        self.c1.draw()

    def clearplot(self):
        """Clears the existing sections."""
        self.axes.cla()
        self.axes.set_xlim(21, 108, auto=False)
        self.axes.grid(visible=True, axis='x')
        self.axes.set_xticks(adf.set_xticks_labels(), adf.set_x_axis())
        self.c1.draw()
