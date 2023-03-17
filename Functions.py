import Instruments
'''
These are functions retrieving data from the Instruments file and returning each key value of each instrument
as well as a collection. 

'''


def select_instrument(section, instrument):                             # selecting an instrument
    current_instr = Instruments.all_instruments[section][instrument]
    return current_instr


def get_range(section, instrument):                                     # get instrument range
    current_instr = Instruments.all_instruments[section][instrument]
    current_range = current_instr["Range"]
    return current_range


def get_qualities(section, instrument):                                 # get instrument qualities
    current_instr = Instruments.all_instruments[section][instrument]
    current_qualities = current_instr["Qualities"]
    return current_qualities


def get_roles(section, instrument):                                     # get instrument roles
    current_instr = Instruments.all_instruments[section][instrument]
    current_roles = current_instr["Roles"]
    return current_roles


def get_transposition(section, instrument):                             # get instrument transposition
    current_instr = Instruments.all_instruments[section][instrument]
    current_transposition = current_instr["Transposition"]
    return current_transposition
