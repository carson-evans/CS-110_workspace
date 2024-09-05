# Accepts sound samples, each characterized by a pitch and a duration, from standard input; and
# plays the sound using standard audio.

import math
import stdarray
import stdaudio
import stdio

SPS = 44100
NOTES_ON_SCALE = 12
CONCERT_A = 440.0
while not stdio.isEmpty():
    pitch = stdio.readInt()
    duration = stdio.readFloat()
    hz = CONCERT_A * math.pow(2, pitch / NOTES_ON_SCALE)
    n = int(SPS * duration)
    note = stdarray.create1D(n + 1, 0.0)
    for i in range(n + 1):
        note[i] = math.sin(2 * math.pi * i * hz / SPS)
    stdaudio.playSamples(note)
stdaudio.wait()
