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
    if note == "C":
        i += 1
    if note == "A":
        a += 1
    if a > 1:
        z = int(z) + (a-1) * 12
    notation.append((z, note, i))                           # Notation is a tuple (MIDI Note, Note Name, Octave)
    if i == 8:
        break


def get_note(note, octave):                                 # retrieve the MIDI note value in notation
    y = 0
    for y in range(len(notation)):
        if notation[y][1] == note and notation[y][2] == octave:
            return y


def return_note_value(note, octave):
    ind = get_note(note, octave)
    z = notation[ind]
    return z
