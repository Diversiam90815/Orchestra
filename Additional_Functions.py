## converting notes to MIDI numbers

notes = ["A", "A#", "B", "C", "C#", "D",
         "D#", "E", "F", "F#", "G", "G#"]                   # list of all note names (here I just used sharp keys)

i = 0                                                       # i is the octave number
a = 0                                                       # a is later used to correctly iterate over the MIDI values
notation = []                                               # list of tuple containing note names: (note,octave)
notes = notes * 8                                           # overall range is about 8 octaves
midi_note = [n for n in range(21, 109)]                     # notes in MIDI values. Start: A0 is 21; End: C8 is 108

for note in notes:
    z = midi_note[notes.index(note)]
    if note == "C":                                         # Octave count i starts at each instance of note C
        i += 1
    if note == "A":                                         # a is counting up everytime [notes] is iterated
        a += 1
    if a > 1:                                               # so the MIDI values continue counting and don't restart
        z = int(z) + (a-1) * 12
    notation.append((z, note, i))                           # Notation is a tuple (MIDI Note, Note Name, Octave)
    if i == 8:                                              # total range is from octave 1 to C8 (octave 8)
        break


def get_note(note, octave):                                 # retrieve the MIDI note value in notation
    y = 0                                                   # y is the list index
    for y in range(len(notation)):                          # list gets searched for match
        if notation[y][1] == note \
                and notation[y][2] == octave:               # input note/octave is going through the list until matched
            return y                                        # the searched note is at position y in notation


def return_note_value(note, octave):
    ind = get_note(note, octave)                            # position of the searched note is being called
    z = notation[ind]                                       # the note at position ind (before:y) is being called
    return z


def show_note(y):
    if y == notation[y]:
        n = notation[y][1]
        o = notation[y][2]
        return n, o
