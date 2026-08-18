#copy-paste from ai...

SHARPS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
FLATS  = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
# Keys that MUST use sharps
USES_SHARPS = {'G', 'D', 'A', 'E', 'B', 'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#'}

# C and a are special (natural), but instructions say use SHARPS for ascending
NATURAL = {'C', 'a'}
def get_chromatic_scale(tonic):
    # 1. Normalize
    if len(tonic) > 1:
        # Handle Bb, F# etc. Uppercase first letter, lowercase second.
        tonic = tonic[0].upper() + tonic[1:].lower()
    else:
        # Handle single letters (C, G, a)
        # Note: We keep minor keys lowercase for checking against our USES_SHARPS set
        pass

    # 2. Pick the source list
    if tonic in USES_SHARPS or tonic in NATURAL:
        source = SHARPS
    else:
        source = FLATS
    
    # 3. Find the index (The instructions say return uppercase letters)
    # We convert tonic to UPPER just to find it in our UPPERCASE lists
    tonic_upper = tonic.upper() if len(tonic) == 1 else tonic[0].upper() + tonic[1:]
    
    start_index = source.index(tonic_upper)
    
    # 4. Rotate the list
    # Everything from start to end + everything from beginning to start
    rotated = source[start_index:] + source[:start_index]
    return rotated
def generate_scale(tonic, intervals):
    # Get the 12-note base starting at our tonic
    chromatic = get_chromatic_scale(tonic)
    
    # The first note is always the tonic
    result = [chromatic[0]]
    current_index = 0
    
    # Dictionary to map interval letters to numbers
    steps = {'m': 1, 'M': 2, 'A': 3}
    
    for char in intervals:
        current_index += steps[char]
        # Append the note found at the new index
        result.append(chromatic[current_index])
        
    return result


#solution...

SHARP_PITCHES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
FLAT_PITCHES = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
SHARP_TONICS = [
    "C",
    "G",
    "D",
    "A",
    "E",
    "B",
    "F#",
    "a",
    "e",
    "b",
    "f#",
    "c#",
    "g#",
    "d#",
]
FLAT_TONICS = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]
INTERVALS = {"m": 1, "M": 2, "A": 3}


def validate_interval_steps(intervals: str):
    return all(char in INTERVALS for char in intervals)


def validate_intervals_length(intervals: str):
    return len(intervals) <= 8


def get_pitches(tonic: str):
    if tonic in SHARP_TONICS:
        return SHARP_PITCHES
    elif tonic in FLAT_TONICS:
        return FLAT_PITCHES
    return None


class Scale:
    def __init__(self, tonic: str):
        self.tonic = tonic
        self.tonic_capitalized = tonic.capitalize()
        self.pitches = get_pitches(self.tonic)

    def chromatic(self):
        tonic_idx = self.pitches.index(self.tonic_capitalized)
        return self.pitches[tonic_idx:] + self.pitches[:tonic_idx]

    def interval(self, intervals: str):
        if not validate_interval_steps(intervals):
            raise ValueError('The supported intervals are "m", "M" and "A"')
        elif not validate_intervals_length(intervals):
            raise ValueError("Maximum number of intervals is 8")
        else:
            # Shift the scale
            scale = self.chromatic() + [self.tonic_capitalized]
            curr_idx = 0
            result = [self.tonic_capitalized]
            print(scale)
            for interval in intervals:
                curr_idx += INTERVALS[interval]
                result.append(scale[curr_idx])

            return result