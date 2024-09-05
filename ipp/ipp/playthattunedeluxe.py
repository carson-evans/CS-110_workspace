# Reads sound samples, each characterized by a pitch and a duration, from standard input; and plays
# the sound using standard audio.

import math
import stdarray
import stdaudio
import stdio


# Entry point.
def main():
    while not stdio.isEmpty():
        pitch = stdio.readInt()
        duration = stdio.readFloat()
        stdaudio.playSamples(_createRichNote(pitch, duration))
    stdaudio.wait()


# Returns an array of samples for a note superposed from three notes (at pitch, 2 x pitch,
# and 0.5 x pitch) and having the specified duration.
def _createRichNote(pitch, duration):
    NOTES_ON_SCALE = 12
    CONCERT_A = 440.0
    hz = CONCERT_A * math.pow(2, pitch / NOTES_ON_SCALE)
    mid = _createNote(hz, duration)
    hi = _createNote(2 * hz, duration)
    lo = _createNote(hz / 2, duration)
    hiAndLo = _superpose(hi, lo, 0.5, 0.5)
    return _superpose(mid, hiAndLo, 0.5, 0.5)


# Returns an array of samples for a note of specified frequency and duration.
def _createNote(hz, duration):
    SPS = 44100
    n = int(SPS * duration)
    note = stdarray.create1D(n + 1, 0.0)
    for i in range(n + 1):
        note[i] = math.sin(2 * math.pi * i * hz / SPS)
    return note


# Superposes arrays a and b, using respective weights aWeight and bWeight, and returns the
# superposed array.
def _superpose(a, b, aWeight, bWeight):
    c = stdarray.create1D(len(a), 0.0)
    for i in range(len(a)):
        c[i] = a[i] * aWeight + b[i] * bWeight
    return c


if __name__ == "__main__":
    main()
