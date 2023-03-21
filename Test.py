import Functions
import Instruments
import Additional_Functions

'''
This is just for testing purposes.

'''


# z = Functions.get_range("Brass", "french_horn")
# b = tuple(z[0].strip("()").split(","))
# print(b[1], b[2])

# c = Additional_Functions.return_note("E", 3)
# print(c)
#
# z= Functions.get_qualities("Woodwinds", "clarinet")
# print(z, type(z))


z = Additional_Functions.return_midi_note("A#", 1)
print(z)