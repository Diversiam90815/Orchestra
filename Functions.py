import Instruments
'''
These are functions retrieving data from the Instruments.py file and returning each key value of each instrument
as well as a whole section. 

'''


def select_instrument(section, instrument):
    """Selects and instrument from the Dictionary All Instruments in module Instruments.py """
    current_instr = Instruments.all_instruments[section][instrument]
    return current_instr


def get_section(section):
    """Returns the current section as a dict with all corresponding instruments as keys and their info as values from Instruments.py"""
    current_section = Instruments.all_instruments[section]
    return current_section


def get_range(section, instrument):
    """Returns an instrument's range from Instruments.py """
    current_instr = Instruments.all_instruments[section][instrument]
    current_range = current_instr["Range"]
    return current_range


def get_qualities(section, instrument):
    """Returns the instrument's qualities from Instruments.py"""
    current_instr = Instruments.all_instruments[section][instrument]
    current_quality = current_instr["Qualities"]
    try:
        current_qualities = []
        for key, value in current_quality.items():                      # Value 'Qualities' is mostly set up as another dict, so they have to be iterated over one by one
            current_qualities.append(f'{key} -> {value}\n')             # and put into a list, which gets returned
    except:
        current_qualities = current_quality                             # Some instances are not a dict, which leads to a bug if treated as above
    return current_qualities


def get_roles(section, instrument):
    """Returns the instrument's roles information from Instruments.py"""
    current_instr = Instruments.all_instruments[section][instrument]
    current_roles = current_instr["Roles"]
    return current_roles


def get_transposition(section, instrument):
    """Returns the instrument's transposition information from Instruments.py"""
    current_instr = Instruments.all_instruments[section][instrument]
    current_transposition = current_instr["Transposition"]
    return current_transposition
