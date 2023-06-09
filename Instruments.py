from Additional_Functions import return_note as ret
from Additional_Functions import return_midi_note as retM

'''
This is a collection of all instruments of a typical symphonic orchestra. This is a CIP (continual improvement project),
which means instruments and other features will be added over time as this project grows. 

The instruments and their data are collected in nested dictionaries (when applicable). To leave this document "clean", 
the relevant functions have been outsourced to the module 'Additional Functions'. 

The pitches are written pitches, except for the Transposition key (which shows the sounding pitches accordingly).

'''

all_instruments = {
    "Strings":
        {
            "violin":
                {
                    "Range": f'{ret("G", 3)} - {ret("A", 7)}',
                    "RangeM_low": f'{retM("G", 3)}',
                    "RangeM_high": f'{retM("A", 7)}',
                    "Qualities":
                        {
                            f'String {ret("G", 3)}': "thickest, and most sonorous",
                            f'String {ret("D", 4)}': "least distinctive, yet can exude warmth and lyricism",
                            f'String {ret("A", 4)}': "",
                            f'String {ret("E", 5)}': "most brilliant, gets a mysterious qualities at low dynamics"
                        },
                    "Transposition": "None",
                    "Roles": "1st Violin: Melody;\n"
                             "2nd Violin: supporting Harmony"
                },

            "viola":
                {
                    "Range": f'{ret("C", 3)} - {ret("E", 6)}',
                    "RangeM_low": f'{retM("C", 3)}',
                    "RangeM_high": f'{retM("E", 6)}',
                    "Qualities":
                        {
                            f'String {ret("C", 3)}': "most characteristic viola sound; somber,\n"
                                                     "  austere, sometimes a bit forbidding",
                            f'String {ret("G", 3)}': "dark",
                            f'String {ret("D", 4)}': "dark",
                            f'String {ret("A", 4)}': "piercing and nasal; combines beautifully with woodwinds \n"
                                                     "  (in some cases also with soft trumpet and trombones)"
                        },
                    "Transposition": "None",
                    "Roles": "often used to double the bassline or "
                             "  fill the harmony in the center\n"
                             "(often coupling 2nd Violins)"
                },

            "violoncello":
                {
                    "Range": f'{ret("C", 2)} - {ret("C", 6)}',
                    "RangeM_low": f'{retM("C", 2)}',
                    "RangeM_high": f'{retM("C", 6)}',
                    "Qualities":
                        {
                            f'String {ret("C", 2)}': "richly, sonorous bass",
                            f'String {ret("G", 2)}': "least strong, carries less well than the others",
                            f'String {ret("D", 3)}': "the most musically captivating, exuding warm and \n"
                                                     "  lyrical quality",
                            f'String {ret("A", 4)}': "most brilliant and piercing"
                        },
                    "Transposition": "None",
                    "Roles": "often doubled with: bassoon, double bass, horns, clarinet,\n"
                             "  trombone, tuba or pizz. cello with Timpani"
                },

            "double_bass":
                {
                    "Range": f'{ret("E", 2)} - {ret("C", 5)},\n '
                             f'(with C-extension: {ret("C", 2)} - {ret("C", 5)})',
                    "RangeM_low": f'{retM("C", 1)}',
                    "RangeM_high": f'{retM("C", 4)}',
                    "Qualities":
                        {
                            f'String {ret("E", 2)}': "weighty, dark, powerful -> sonorous fundamental bass",
                            f'String {ret("A", 2)}': "sonorous timbre, clearer and more precise",
                            f'String {ret("D", 3)}': "shares cellos range, but fuller, more powerful and darker",
                            f'String {ret("G", 3)}': "shares cellos range, but fuller, more powerful and darker"
                        },
                    "Transposition": f'One octave lower: {ret("E", 1)} - {ret("C", 4)}',
                    "Roles": "often identical to Cello part (esp. mid 18th century)"
                }
        },

    "Brass":
        {
            "french_horn":
                {
                    "Range": f'{ret("F#", 2)} - {ret("C", 6)}',
                    "RangeM_low": f'{retM("B", 1)}',
                    "RangeM_high": f'{retM("F", 5)}',
                    "Qualities":
                        {
                            f'{ret("C", 3)} - {ret("G", 3)}': "dark, a bit unfocused",
                            f'{ret("G", 3)} - {ret("C", 4)}': "deep and solid",
                            f'{ret("C", 4)} - {ret("G", 5)}': "bright & heroic",
                            f'{ret("G", 5)} - {ret("C", 6)}': "brilliant & loud"
                        },
                    "Transposition": f'F: P5th lower: {ret("B", 1)} - {ret("F", 5)}',
                    "Roles": "can play chromatically with valves;\n"
                             "creates a feeling of heroism (since the 18th century);\n"
                             "2 Horns == 1 Trumpet/Trombone (in power)"
                },

            "trumpet":
                {
                    "Range": f'{ret("F#", 3)} - {ret("D", 6)}',
                    "RangeM_low": f'{retM("F#", 3)}',
                    "RangeM_high": f'{retM("D", 6)}',
                    "Qualities":
                        {
                            f'{ret("F#", 3)} - {ret("B", 3)}': "rather dull",
                            f'{ret("C", 4)} - {ret("A", 5)}': "clear, bright and most articulate",
                            f'{ret("B", 5)} - {ret("D", 6)}': "brilliant, but shrill"
                        },
                    "Transposition": f'C: as written;\nBb: Maj2nd lower: {ret("E", 3)} - {ret("C", 6)}',
                    "Roles": "most agile of the brass choir;\n"
                             "creates an aura of anticipation and excitement;\n"
                             "often doubled in oboe & timpani"
                },

            "tenor_trombone":
                {
                    "Range": f'{ret("E", 2)} - {ret("A#", 4)}',
                    "RangeM_low": f'{retM("E", 2)}',
                    "RangeM_high": f'{retM("A#", 4)}',
                    "Qualities":
                        {
                            f'{ret("E", 2)} - {ret("G", 2)}': "dark, less strong",
                            f'{ret("A", 2)} - {ret("F", 4)}': "firm & powerful",
                            f'{ret("G", 4)} - {ret("A#", 4)}': "very intense"
                        },
                    "Transposition": "None",
                    "Roles": f'notes below {ret("G#", 3)} are only available in 1st position\n'
                             "  -> fast changing positions are difficult,\n"
                             "  if the positions are extreme;\n"
                             "can play glissandi very well;\n"
                             "great for harmony, contrapuntal lines or doubling"
                },

            "bass_trombone":
                {
                    "Range": f'{ret("A#", 1)} - {ret("A#", 4)}',
                    "RangeM_low": f'{retM("A#", 1)}',
                    "RangeM_high": f'{retM("A#", 4)}',
                    "Qualities":
                        {
                            f'{ret("A#", 1)} - {ret("F", 2)}': "heavy & quite strong",
                            f'{ret("G", 2)} - {ret("G", 3)}': "deep & solid",
                            f'{ret("A", 3)} - {ret("A#", 4)}': "very powerful"
                        },
                    "Transposition": "None",
                    "Roles": "can be light & delicate, or hard & menacing;\n"
                             "pedal tones (lowest harmonic) are easier than on the tenor trombone;\n"
                             "contrabass trombone is hard to play and today its parts\n"
                             "  are mostly assigned to the tuba"
                },

            "cimbasso":
                {
                    "Range": f'{ret("F", 1)} - {ret("F", 4)}',
                    "RangeM_low": f'{retM("F", 1)}',
                    "RangeM_high": f'{retM("F", 4)}',
                    "Qualities":
                        {
                            f'{ret("F", 1)} - {ret("G", 2)}': "full, clear, concise",
                            f'{ret("G#", 2)}- {ret("G", 3)}': "soft, round, bright",
                            f'{ret("G#", 3)}- {ret("F", 4)}': "softer and brighter"
                        },
                    "Transposition": "None",
                    "Roles": "similar to the tuba and b.trombone,yet not as \n"
                             "  metallic as the b.trombone and not as sluggish\n"
                             "  as the tuba (esp. in the lows);\n"
                             "mixes nicely with trombones and trumpets, horns, tuba and the \n"
                             "  contrabassoon"
                },

            "tuba":
                {
                    "Range": f'{ret("D", 1)} - {ret("G", 4)}',
                    "RangeM_low": f'{retM("D", 1)}',
                    "RangeM_high": f'{retM("G", 4)}',
                    "Qualities":
                        {
                            f'{ret("D", 1)} - {ret("A#", 1)}': "deep & heavy",
                            f'{ret("B", 2)} - {ret("E", 3)}': "very strong",
                            f'{ret("F", 3)} - {ret("G", 4)}': "getting weaker, but quite intense"
                        },
                    "Transposition": "None",
                    "Roles": "can play lyrical soft lines as well;\n"
                             "sometimes 2 tubas to compensate of the oversized \n"
                             "  horn / trumpet sections;\n"
                             "mixes nicely with trumpets and horns sluggish in the lows, \n"
                             "but very agile in the middle and up"
                }
        },

    "Woodwinds":
        {
            "piccolo":
                {
                    "Range": f'{ret("D", 4)} - {ret("C", 7)}',
                    "RangeM_low": f'{retM("D", 5)}',
                    "RangeM_high": f'{retM("C", 8)}',
                    "Qualities":
                        {
                            f'{ret("D", 4)} - {ret("G", 4)}': "quiet, hauntingly hallow",
                            f'{ret("A", 4)} - {ret("G", 5)}': "soft & mellow",
                            f'{ret("A", 5)} - {ret("G", 6)}': "bright & clear",
                            f'{ret("A", 6)} - {ret("C", 7)}': "shrill, edgy"
                        },
                    "Transposition": f'one octave higher: {ret("D", 5)} - {ret("C", 8)}',
                    "Roles": "--"
                },

            "flute":
                {
                    "Range": f'{ret("C", 4)} - {ret("D", 7)}',
                    "RangeM_low": f'{retM("C", 4)}',
                    "RangeM_high": f'{retM("D", 7)}',
                    "Qualities":
                        {
                            f'{ret("C", 4)} - {ret("G", 4)}': "weak, but lucious",
                            f'{ret("A", 4)} - {ret("G", 5)}': "sweet, but little power",
                            f'{ret("A", 5)} - {ret("G", 6)}': "clear, brilliant",
                            f'{ret("A", 6)} - {ret("D", 7)}': "a bit shrill"
                        },
                    "Transposition": "None",
                    "Roles": "--"
                },

            "oboe":
                {
                    "Range": f'{ret("A#", 3)} - {ret("A", 6)}',
                    "RangeM_low": f'{retM("A#", 3)}',
                    "RangeM_high": f'{retM("A", 6)}',
                    "Qualities":
                        {
                            f'{ret("A#", 3)} - {ret("F", 4)}': "thick, heavy",
                            f'{ret("G", 4)} - {ret("A", 5)}': "warm, prominent, reedy, poignant",
                            f'{ret("B", 5)} - {ret("E", 6)}': "thin, but clear",
                            f'{ret("F", 6)} - {ret("A", 6)}': "pinched & ineffective"
                        },
                    "Transposition": "None",
                    "Roles": "avoid ppp / pp in very low or high registers;\n"
                             "can hold longer notes, but not very fast repeating staccato notes"
                },

            "cor_anglais":
                {
                    "Range": f'{ret("B", 3)} - {ret("G", 6)}',
                    "RangeM_low": f'{retM("E", 2)}',
                    "RangeM_high": f'{retM("C", 6)}',
                    "Qualities":
                        {
                            f'{ret("B", 3)} - {ret("G", 4)}': "deep, rich, intense",
                            f'{ret("A", 4)} - {ret("A", 5)}': "mellow, reedy, sonorous",
                            f'{ret("A", 6)} - {ret("G", 6)}': "thin, pinched"
                        },
                    "Transposition": f'P5th lower: {ret("E", 2)} - {ret("C", 6)}',
                    "Roles": "melancholic touch, most used for sadness;\n"
                             "much more mellow than the oboe -> does not cut through \n"
                             " as easily as the oboe"
                },

            "clarinet":
                {
                    "Range": f'{ret("E", 3)} - {ret("C", 7)}',
                    "RangeM_low": f'{retM("D", 3)}',  # here: Bb Clarinet
                    "RangeM_high": f'{retM("B", 6)}',
                    "Qualities":
                        {
                            f'{ret("E", 3)} - {ret("F#", 4)}': "Chalumeau Register: deep & rich",
                            f'{ret("G", 4)} - {ret("A#", 4)}': "Throat Tones: rather pale",
                            f'{ret("B", 4)} - {ret("C", 6)}': "Clarino Register: bright, incisive, expressive",
                            f'{ret("D", 6)} - {ret("C", 7)}': "shrill, piercing"
                        },
                    "Transposition": f'Bb: Maj2nd lower: {ret("D", 3)} - {ret("B", 6)};\n'
                                     f'A: min3rd lower: {ret("C#", 3)} - {ret("A#", 6)}',
                    "Roles": f'homogenous across all pitches-dynamics;\n'
                             f'fingering break between: {ret("A#", 4)} - {ret("B", 4)};\n'
                             f'"Clarinet in A better for sharp keys;\n'
                             f'Clarinet in Bb better for flat keys;\n'
                             f'"Nightingale of the orchestra"'
                },

            "bass_clarinet":
                {
                    "Range": f'{ret("D#", 3)} - {ret("G", 6)}',
                    "RangeM_low": f'{retM("C#", 2)}',
                    "RangeM_high": f'{retM("E", 5)}',
                    "Qualities":
                        {
                            f'{ret("D#", 3)} - {ret("G", 3)}': "Chalumeau Register, mysterious, shadowy, sinister",
                            f'{ret("A", 3)} - {ret("G", 4)}': "Clarino Register",
                            f'{ret("A", 4)} - {ret("G", 6)}': "thin, difficult to produce"
                        },
                    "Transposition": f'treble clef: Maj9th lower: {ret("C#", 2)} - {ret("E", 5)} ->  most common;\n'
                                     f'bass clef: Maj2nd lower: {ret("D", 3)} - {ret("F", 6)}',
                    "Roles": "mostly notated in the treble clef nowadays;\n"
                             "very agile, but not as incisively as the smaller relative"
                },

            "bassoon":
                {
                    "Range": f'{ret("A#", 1)} - {ret("D#", 5)}',
                    "RangeM_low": f'{retM("A#", 1)}',
                    "RangeM_high": f'{retM("D#", 5)}',
                    "Qualities":
                        {
                            f'{ret("A#", 1)} - {ret("G", 2)}': "sonorous, dark, vibrant",
                            f'{ret("A", 2)} - {ret("D", 4)}': "sweet, more subdued, but expressive",
                            f'{ret("E", 4)} - {ret("A#", 4)}': "thin, but intense",
                            f'{ret("B", 4)} - {ret("D#", 5)}': "thin, often pinched"
                        },
                    "Transposition": "None",
                    "Roles": "often in unison with the clarinet;\n"
                             "lowest & highest P5 intervals are quite difficult/not playable \n"
                             " at low dynamics"
                },

            "contrabassoon":
                {
                    "Range": f'{ret("A#", 1)} - {ret("A#", 4)}',
                    "RangeM_low": f'{retM("A#", 0)}',
                    "RangeM_high": f'{retM("A#", 3)}',
                    "Qualities": f'similar characteristics as the bassoon, but slower and more \n'
                                 f' stubborn and resistant in the lows;\n'
                                 f'most effective range is its lowest 12th: {ret("A#", 1)} - {ret("F", 3)}',
                    "Transposition": f'Octave lower: {ret("A#", 0)} - {ret("A#", 3)}',
                    "Roles": "often doubled with double basses & bassoons / celli at octave;\n"
                             "in its higher register it's a lot paler and weaker than the bassoon;\n"
                             "needs periodic rests due to its size"
                }
        },
    "Percussion":
        {
            "harp":
                {
                    "Range": f'{ret("B", 1)} - {ret("F#", 7)}',
                    "RangeM_low": f'{retM("B", 1)}',
                    "RangeM_high": f'{retM("F#", 7)}',
                    "Qualities":
                        {
                            f'{ret("B", 1)} - {ret("B", 3)}': "dark, sonorous",
                            f'{ret("C", 3)} - {ret("C", 5)}': "rich, warm",
                            f'{ret("C#", 5)} - {ret("F#", 7)}': "bright, clear, not much dynamic range",
                        },
                    "Transposition": "None",
                    "Roles": f'Sometimes 2 harps are used;\n'
                             f'chords with 4 notes in each hand;\n'
                             f'pedals: DCB/EFGA;\n'
                             f'pres-de-la-table -> near the board -> creates a guitar like sound;\n'
                             f'bisbigliando (transl.: whispering) -> alternating picking;\n'
                             f'glissando -> heavenly sound'
                },

            "celeste":
                {
                    "Range": f'{ret("C", 3)} - {ret("C", 8)}',
                    "RangeM_low": f'{retM("C", 3)}',
                    "RangeM_high": f'{retM("C", 8)}',
                    "Qualities": f'silvery, glistening, ethereal, sweet, shimmering;\n'
                                 f'the timbre is homogenous across the pitches;\n'
                                 f'sounding warmer and rounder than the glockenspiel;\n'
                                 f'sound is not load -> gets covered easily by the orchestra;\n'
                                 f'though it is touch-responsive, the dynamic range is limited',
                    "Transposition": "None",
                    "Roles": "provides highlights in form of chords or single notes \n"
                             "(similar to triangle/glockenspiel);\n"
                             "doubling other voices in (multiple) octaves, unison or fifth;\n"
                             "piano figures consisting of glissando-like scales, arpeggios or \n"
                             "  octave tremolos"
                },

            "timpani":
                {
                    "Range": f'{ret("B", 1)} - {ret("C", 4)}',
                    "RangeM_low": f'{retM("B", 1)}',
                    "RangeM_high": f'{retM("C", 4)}',
                    "Qualities": f'dull, thunderous, deep, heavy, velvety, dry;\n'
                                 f'great dynamic range;\n'
                                 f'timbre is determined by the mallet, where the head is struck\n'
                                 f' and how hard',
                    "Transposition": "None",
                    "Roles": "doubled in unison with other bass instruments creates a \n"
                             "  homogeneous blend;\n"
                             "blends nicely with trumpets and horns (e.g. 2 horns + \n"
                             "  timpani in unison with other horns in octaves and \n"
                             "  trumpets in 2 octaves playing the root;\n"
                             "timpani rolls doubled with string tremolo chords have a \n"
                             "  tremendous effect;\n"
                             "mixes nicely with pizz. strings and harps "
                },

            "marimba":
                {
                    "Range": f'{ret("C", 2)} - {ret("C", 7)}',
                    "RangeM_low": f'{retM("C", 2)}',
                    "RangeM_high": f'{retM("C", 7)}',
                    "Qualities": f'dark, mellow,gentle, melodious, resonant;\n'
                                 f'sound depends on the mallet: the harder the mallet, the louder the\n'
                                 f' initial attack, and the more prominent the higher partials',
                    "Transposition": "None",
                    "Roles": "with percussion -> full sounding with celeste and glockenspiel \n"
                             "  in octaves or unison;\n"
                             "with brass -> as an accompaniment to trumpet melodies;\n"
                             "with woodwinds -> mellow-sounding and sonorous, blends well \n"
                             "  in octaves, especially with deep clarinets;\n"
                             "with strings -> full-sounding in unison and octaves with low strings,\n"
                             "  yet blend is incomplete"
                },
        }

    }

"""
Adding the techniques section is planned for a further implementation. Below are some unsorted fragments, which would
be used at a later version of the program. 


Techniques

Strings
    Techniques:             sul tasto  = light/easy
                            sul pont   = harsh/aggressive
                            down-bows   = heavier
                            up-bows     = lighter
"""
