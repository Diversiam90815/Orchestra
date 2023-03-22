import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Plot:

    def __init__(self, masterframe, size, data):
        self.notes = [n for n in range(21, 109)]  # x-Achse
        self.data = data
        self.instruments = self.data["Instrument"]
        self.left_val = self.data["Range_low"]
        self.right_val = self.data["Range_high"]
        self.data["width"] = self.data["Range_high"] - self.data["Range_low"]
        self.figure = plt.Figure(size)
        self.axes = self.figure.add_subplot()
        self.axes.set_xlim(21, 108, auto=False)
        self.axes.grid(visible=True, axis='x')
        self.c1 = FigureCanvasTkAgg(self.figure, master=masterframe)
        self.c1.get_tk_widget().grid(column=0, row=0)  # Get reference to tk_widget
        self.axes.set_title("Instruments in their range")
        self.axes.set_xlabel("Notation [in MIDI]")
        self.axes.set_ylabel("Instruments")
        self.figure.tight_layout()

    def plot_strings(self):
        filt_string = self.data["Section"] == "Strings"
        String_instruments = self.data.loc[filt_string, "Instrument"]
        Left_val_string = self.data.loc[filt_string, "Range_low"]
        Right_val_string = self.data.loc[filt_string, "Range_high"]
        self.data["width_strings"] = Right_val_string - Left_val_string
        data_strings_width = self.data["width_strings"].dropna()

        self.axes.barh(String_instruments, data_strings_width, left=Left_val_string, height=0.5, color="blue")
        self.c1.draw()

    def plot_woods(self):
        filt_woods = self.data["Section"] == "Woodwinds"
        Woodwind_instruments = self.data.loc[filt_woods, "Instrument"]
        Left_val_woods = self.data.loc[filt_woods, "Range_low"]
        Right_val_woods = self.data.loc[filt_woods, "Range_high"]
        self.data["width_woods"] = Right_val_woods - Left_val_woods
        data_woods_width = self.data["width_woods"].dropna()

        self.axes.barh(Woodwind_instruments, data_woods_width, left=Left_val_woods, height=0.5, color="green")
        self.c1.draw()

    def plot_brass(self):
        filt_brass = self.data["Section"] == "Brass"
        Brass_instruments = self.data.loc[filt_brass, "Instrument"]
        Left_val_brass = self.data.loc[filt_brass, "Range_low"]
        Right_val_brass = self.data.loc[filt_brass, "Range_high"]
        self.data["width_brass"] = Right_val_brass - Left_val_brass
        data_brass_width = self.data["width_brass"].dropna()

        self.axes.barh(Brass_instruments, data_brass_width, left=Left_val_brass, height=0.5, color="yellow")
        self.c1.draw()

    def plot_perc(self):
        filt_perc = self.data["Section"] == "Percussion"
        Perc_instruments = self.data.loc[filt_perc, "Instrument"]
        Left_val_perc = self.data.loc[filt_perc, "Range_low"]
        Right_val_perc = self.data.loc[filt_perc, "Range_high"]
        self.data["width_perc"] = Right_val_perc - Left_val_perc
        data_perc_width = self.data["width_perc"].dropna()

        self.axes.barh(Perc_instruments, data_perc_width, left=Left_val_perc, height=0.5, color="red")
        self.c1.draw()

    def plot_orchestra(self):
        self.plot_strings()
        self.plot_brass()
        self.plot_woods()
        self.plot_perc()
        self.c1.draw()

    def clearplot(self):
        self.axes.cla()
        self.axes.set_xlim(21, 108, auto=False)
        self.axes.grid(visible=True, axis='x')
        self.c1.draw()
