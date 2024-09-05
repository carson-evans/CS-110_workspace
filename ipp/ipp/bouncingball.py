# Draws a bouncing ball using standard draw.

import stddraw

RADIUS = 0.05
DT = 1.0
PAUSE = 20
stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)
rx = 0.480
ry = 0.860
vx = 0.015
vy = 0.023
while True:
    if abs(rx + vx * DT) + RADIUS > 1.0:
        vx = -vx
    if abs(ry + vy * DT) + RADIUS > 1.0:
        vy = -vy
    rx += vx * DT
    ry += vy * DT
    stddraw.clear(stddraw.WHITE)
    stddraw.filledCircle(rx, ry, RADIUS)
    stddraw.show(PAUSE)
