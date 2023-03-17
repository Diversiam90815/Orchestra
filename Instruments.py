from Additional_Functions import return_note_value as ret
'''
This is a collection of all instruments of a typical symphonic orchestra. This is a CIP (continual improvement process),
which means instruments will be added over time as this project grows. 

The instruments and their data are collected in nested dictionaries. 

The pitches are written pitches, except for the Transposition key (which shows the sounding pitches accordingly).

'''

all_instruments = {
    "Strings":
        {
            "violin":
                {
                    "Range": f'{ret("G", 3)} - {ret("A", 7)}',
                    "Tuning": "G-D-A-E",
                    "Transposition": "None",
                    "Roles": "1st Violin: Melody; "
                             "2nd Violin: supporting Harmony"
                },

            "viola":
                {
                    "Range": f'{ret("C", 3)} - {ret("E", 6)}',
                    "Tuning": "C-G-D-A",
                    "Transposition": "None",
                    "Roles": "often used to double the bassline or "
                             "fill the harmony in the center(often coupling 2nd Violins)"
                },

            "violoncello":
                {
                    "Range": f'{ret("C", 2)} - {ret("C", 6)}',
                    "Tuning": "C-G-D-A",
                    "Transposition": "None",
                    "Roles": "often doubled with: bassoon, double bass, horns, clarinet, trombone, tuba "
                             "or pizz. cello with Timpani"
                },

            "double_bass":
                {
                    "Range": f'{ret("E", 2)} - {ret("C", 5)}, '
                             f'(with C-extension: {ret("C", 2)} - {ret("C", 5)}',
                    "Tuning": "E-A-D-G",
                    "Transposition": f'One octave lower {ret("E", 1)} - {ret("C", 4)}',
                    "Roles": "often identical to Cello part (esp. mid 18th century)"
                }
        },

    "Brass":
        {
            "french_horn":
                {
                    "Range": f'{ret("F#", 2)} - {ret("C", 6)}',
                    "Qualities":
                        {
                            f'{ret("C", 3)} - {ret("G", 3)}': "dark, a bit unfocused",
                            f'{ret("G", 3)} - {ret("C", 4)}': "deep and solid",
                            f'{ret("C", 4)} - {ret("G", 5)}': "bright & heroic",
                            f'{ret("G", 5)} - {ret("C", 6)}': "brilliant & loud"
                        },
                    "Transposition": f'F: P5th lower {ret("B", 1)} - {ret("F", 5)}',
                    "Roles": "can play chromatically with valves;"
                             "creates a feeling of heroism (since the 18th century);"
                             "2 Horns == 1 Trumpet/Trombone (in power)"
                },

            "trumpet":
                {
                    "Range": f'{ret("F#", 3)} - {ret("D", 6)}',
                    "Qualities":
                        {
                            f'{ret("F#", 3)} - {ret("B", 3)}': "rather dull",
                            f'{ret("C", 4)} - {ret("A", 5)}': "clear, bright and most articulate",
                            f'{ret("B", 5)} - {ret("D", 6)}': "brilliant, but shrill"
                        },
                    "Transposition": f'C: as written; Bb: Maj2nd lower {ret("E", 3)} - {ret("C", 6)}',
                    "Roles": "most agile of the brass choir; "
                             "creates an aura of anticipation and excitement; "
                             "often doubled in oboe & timpani"
                },

            "tenor_trombone":
                {
                    "Range": f'{ret("E", 2)} - {ret("A#", 4)}',
                    "Qualities":
                        {
                            f'{ret("E", 2)} - {ret("G", 2)}': "dark, less strong",
                            f'{ret("A", 2)} - {ret("F", 4)}': "firm & powerful",
                            f'{ret("G", 4)} - {ret("A#", 4)}': "very intense"
                        },
                    "Transposition": "None",
                    "Roles": f'notes below {ret("G#", 3)} are only available in 1st position '
                             "-> fast changing positions are difficult, if positions are extreme; "
                             "can play glissandi very well; "
                             "great for harmony, contrapuntal lines or doubling"
                },

            "bass_trombone":
                {
                    "Range": f'{ret("A#", 1)} - {ret("A#", 4)}',
                    "Qualities":
                        {
                            f'{ret("A#", 1)} - {ret("F", 2)}': "heavy & quite strong",
                            f'{ret("G", 2)} - {ret("G", 3)}': "deep & solid",
                            f'{ret("A", 3)} - {ret("A#", 4)}': "very powerful"
                        },
                    "Transposition": "None",
                    "Roles": "can be light & delicate, or hard & menacing; "
                             "pedal tones(lowest harmonic) are easier than on the tenor trombone; "
                             "contrabass trombone is hard to play and today its parts are mostly assigned to the tuba"
                },

            "cimbasso":
                {
                    "Range": f'{ret("F", 1)} - {ret("F", 4)}',
                    "Qualities":
                        {
                            f'{ret("F", 1)} - {ret("G", 2)}': "full, clear, concise",
                            f'{ret("G#", 2)}- {ret("G", 3)}': "soft, round, bright",
                            f'{ret("G#", 3)}- {ret("F", 4)}': "softer and brighter"
                        },
                    "Transposition": "None",
                    "Roles": "similar to the tuba and b.trombone, yet not as metallic as the b.trombone "
                             "and not as sluggish as the tuba (esp. in the lows);"
                             "mixes nicely with trombones and trumpets, horns, tuba and the contrabassoon"
                },

            "tuba":
                {
                    "Range": f'{ret("D", 1)} - {ret("G", 4)}',
                    "Qualities":
                        {
                            f'{ret("D", 1)} - {ret("A#", 1)}': "deep & heavy",
                            f'{ret("B", 2)} - {ret("E", 3)}': "very strong",
                            f'{ret("F", 3)} - {ret("G", 4)}': "getting weaker, but quite intense"
                        },
                    "Transposition": "None",
                    "Roles": "can play lyrical soft lines as well; "
                             "sometimes 2 tubas to compensate of the oversized horn / trumpet sections; "
                             "mixes nicely with trumpets and horns sluggish in the lows, "
                             "but very agile in the middle and up"
                }
        },

    "Woodwinds":
        {
            "piccolo":
                {
                    "Range": f'{ret("D", 4)} - {ret("C", 7)}',
                    "Qualities":
                        {
                            f'{ret("D", 4)} - {ret("G", 4)}': "quiet, hauntingly hallow",
                            f'{ret("A", 4)} - {ret("G", 5)}': "soft & mellow",
                            f'{ret("A", 5)} - {ret("G", 6)}': "bright & clear",
                            f'{ret("A", 6)} - {ret("C", 7)}': "shrill, edgy"
                        },
                    "Transposition": f'one octave higher {ret("D", 5)} - {ret("C", 8)}',
                    "Roles": "--"
                },

            "flute":
                {
                    "Range": f'{ret("C", 4)} - {ret("D", 7)}',
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
                    "Qualities":
                        {
                            f'{ret("A#", 3)} - {ret("F", 4)}': "thick, heavy",
                            f'{ret("G", 4)} - {ret("A", 5)}': "warm, prominent, reedy, poignant",
                            f'{ret("B", 5)} - {ret("E", 6)}': "thin, but clear",
                            f'{ret("F", 6)} - {ret("A", 6)}': "pinched & ineffective"
                        },
                    "Transposition": "None",
                    "Roles": "avoid ppp / pp in very low or high registers; "
                             "can hold longer notes, but not very fast repeating staccato notes"
                },

            "cor_anglais":
                {
                    "Range": f'{ret("B", 3)} - {ret("G", 6)}',
                    "Qualities":
                        {
                            f'{ret("B", 3)} - {ret("G", 4)}': "deep, rich, intense",
                            f'{ret("A", 4)} - {ret("A", 5)}': "mellow, reedy, sonorous",
                            f'{ret("A", 6)} - {ret("G", 6)}': "thin, pinched"
                        },
                    "Transposition": f'P5th lower {ret("E", 2)} - {ret("C", 6)}',
                    "Roles": "melancholic touch, most used for sadness; "
                             "much more mellow than the oboe -> does not cut through as easily as the oboe"
                },

            "clarinet":
                {
                    "Range": f'{ret("E", 3)} - {ret("C", 7)}',
                    "Qualities":
                        {
                            f'{ret("E", 3)} - {ret("F#", 4)}': "Chalumeau Register: deep & rich",
                            f'{ret("G", 4)} - {ret("A#", 4)}': "Throat Tones: rather pale",
                            f'{ret("B", 4)} - {ret("C", 6)}': "Clarino Register: bright, incisive, expressive",
                            f'{ret("D", 6)} - {ret("C", 7)}': "shrill, piercing"
                        },
                    "Transposition": f'Bb: Maj2 lower: {ret("D", 3)} - {ret("B", 6)}; '
                                     f'A: min3rd lower: {ret("C#", 3)} - {ret("A#", 6)}',
                    "Roles": f'homogenous across all pitches-dynamics; '
                             f'fingering break between {ret("A#", 4)} - {ret("B", 4)}; '
                             f'"Clarinet in A better for sharp keys; '
                             f'Clarinet in Bb better for flat keys; '
                             f'"Nightingale of the orchestra"'
                },

            "bass_clarinet":
                {
                    "Range": f'{ret("D#", 3)} - {ret("G", 6)}',
                    "Qualities":
                        {
                            f'{ret("D#", 3)} - {ret("G", 3)}': "Chalumeau Register, mysterious, shadowy, sinister",
                            f'{ret("A", 3)} - {ret("G", 4)}': "Clarino Register",
                            f'{ret("A", 4)} - {ret("G", 6)}': "thin, difficult to produce"
                        },
                    "Transposition": f'treble: Maj9th lower: {ret("C#", 2)} - {ret("E", 5)} ->  most common; '
                                     f'bass: Maj2nd lower: {ret("D", 3)} - {ret("F", 6)}',
                    "Roles": "mostly notated in the treble clef nowadays; "
                             "very agile, but not as incisively as the smaller relative"
                },

            "bassoon":
                {
                    "Range": f'{ret("A#", 1)} - {ret("D#", 5)}',
                    "Qualities":
                        {
                            f'{ret("A#", 1)} - {ret("G", 2)}': "sonorous, dark, vibrant",
                            f'{ret("A", 2)} - {ret("D", 4)}': "sweet, more subdued, but expressive",
                            f'{ret("E", 4)} - {ret("A#", 4)}': "thin, but intense",
                            f'{ret("B", 4)} - {ret("D#", 5)}': "thin, often pinched"
                        },
                    "Transposition": "None",
                    "Roles": "often in unison with the clarinet; "
                             "lowest & highest P5 intervals are quite difficult/not playable at low dynamics"
                },

            "contrabassoon":
                {
                    "Range": f'{ret("A#", 1)} - {ret("A#", 4)}',
                    "Qualities": f'similar characteristics as the bassoon, but slower more stubborn '
                                 f'and resistant in the lows; '
                                 f'most effective range is its lowest 12th: {ret("A#", 1)} - {ret("F", 3)}',
                    "Transposition": f'Octave lower: {ret("A#", 0)} - {ret("A#", 3)}',
                    "Roles": "often doubled with double basses & bassoons / celli at octave; "
                             "in its higher register it's a lot paler and weaker than the bassoon; "
                             "needs periodic rests due to its size"
                }
        }
    }

# ## Techniques
# Strings
#     Techniques:             sul tasto  = light/easy
#                             sul pont   = harsh/aggressive
#                             down-bows   = heavier
#                             up-bows     = lighter
#
