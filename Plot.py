import Functions
import Instruments
import pandas as pd
import matplotlib.pyplot as plt
import Additional_Functions

## getting a list of tuples including the section name, instrument name and range in MIDI notation

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

Notes = [n for n in range(21, 109)]                         # x-Achse
Instruments = data["Instrument"]                            # y-Achse
Left_val = data["Range_low"]
Right_val = data["Range_high"]
data["width"] = data["Range_high"] - data["Range_low"]


filt_string = data["Section"] == "Strings"
String_instruments = data.loc[filt_string, "Instrument"]
Left_val_string = data.loc[filt_string, "Range_low"]
Right_val_string = data.loc[filt_string, "Range_high"]
data["width_strings"] = data.loc[filt_string, "Range_high"] - data.loc[filt_string, "Range_low"]
data_strings_width = data["width_strings"].dropna()                                              # delete empty values


filt_woods = data["Section"] == "Woodwinds"
Woodwind_instruments = data.loc[filt_woods, "Instrument"]
Left_val_woods = data.loc[filt_woods, "Range_low"]
Right_val_woods = data.loc[filt_woods, "Range_high"]
data["width_woods"] = data.loc[filt_woods, "Range_high"] - data.loc[filt_woods, "Range_low"]
data_woods_width = data["width_woods"].dropna()

filt_brass = data["Section"] == "Brass"
Brass_instruments = data.loc[filt_brass, "Instrument"]
Left_val_brass = data.loc[filt_brass, "Range_low"]
Right_val_brass = data.loc[filt_brass, "Range_high"]
data["width_brass"] = data.loc[filt_brass, "Range_high"] - data.loc[filt_brass, "Range_low"]
data_brass_width = data["width_brass"].dropna()


plt.figure()
plt.xlim([min(Notes), max(Notes)])
plt.gca().barh(String_instruments, data_strings_width, left=Left_val_string, height=0.5, color="blue")
plt.gca().barh(Woodwind_instruments, data_woods_width, left=Left_val_woods, height=0.5, color="green")
plt.gca().barh(Brass_instruments, data_brass_width, left=Left_val_brass, height=0.5, color="yellow")

plt.title("Instruments in their range")
plt.xlabel("Noten in MIDI")
plt.ylabel("Instrumente")
plt.tight_layout()
plt.show()
