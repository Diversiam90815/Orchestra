"""
This module is for functions used in the Instruments.py and Plot.py modules. These are mainly to create and return proper notation values
to be able to calculate and plot in a proper style.

"""

"""

Notes are displayed in note name + octave number (e.g. A3, G5). The code creates a list of tuples with the form of
(MIDI note value (integer from 21 to 108), note name, octave). This list of tuples is later used to either get the 
note value, MIDI note value, calculate with those and plot them. 

"""

notes = ["A", "A#", "B", "C", "C#", "D",
         "D#", "E", "F", "F#", "G", "G#"]

i = 0                                                       # i is the octave number
a = 0                                                       # a is later used to correctly iterate over the MIDI values
notation = []
notes = notes * 8                                           # overall range is about 8 octaves
midi_note = [n for n in range(21, 109)]                     # notes in MIDI values. Start: A0 is 21; End: C8 is 108

for note in notes:
    z = midi_note[notes.index(note)]
    if note == "C":                                         # Octave count i starts at each instance of note C
        i += 1
    if note == "A":                                         # a is counting up everytime [notes] is iterated
        a += 1
    if a > 1:                                               # so the MIDI values continue counting and don't restart from 21 on each iteration
        z = int(z) + (a-1) * 12
    notation.append((z, note, i))                           # Notation is a tuple (MIDI Note, Note Name, Octave)
    if i == 8:                                              # total range is from octave 1 to C8 (octave 8)
        break


def get_note(note, octave):
    """Returns the index of the given note in the notation list."""
    y = 0
    for y in range(len(notation)):
        if notation[y][1] == note \
                and notation[y][2] == octave:               # input note/octave is going through the list until matched
            return y


def return_note(note, octave):
    """Returns only the note name and the corresponding octave as a string value."""
    asd = get_note(note, octave)
    note1 = notation[asd]
    n = note1[1]
    o = note1[2]
    return f'{n}{o}'


def return_midi_note(note, octave):
    """Returns the MIDI note value from a given note name and octave."""
    ind = get_note(note, octave)
    z = notation[ind]
    t = z[0]
    return t


def get_note_from_midi(mid):
    """Returns the note name and octave number as a string from a given MIDI note value."""
    y = 0
    for y in range(len(notation)):
        if notation[y][0] == mid:
            note = notation[y][1]
            octave = notation[y][2]
            return f'{note}{octave}'


def set_xticks_labels():
    """Returns a list of MIDI values at each octave shift (each instance of note 'C'). Since the range starts from A0,
     the corresponding MIDI note value 21 is included by default."""
    x_ticks_labels = [21]                           # 21 == A0
    y = 24                                          # 24 == C1
    while y <= 108:
        x_ticks_labels.append(y)
        y = y + 12
    return x_ticks_labels


def set_x_axis():
    """Returns a list of the notes corresponding each octave shift in the range (including A0). The range goes from A0 to C8."""
    x_values = set_xticks_labels()
    x_names = []
    for value in x_values:
        z = get_note_from_midi(value)
        x_names.append(z)
    return x_names
