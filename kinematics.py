import numpy as np
from numpy import cos, sin, matrix

''''
theta   alpha   r   d
d=0.0880 [m], theta=90.0 [deg], r=0.0003 [m], alpha=90.0 [deg]
d=0.0000 [m], theta=-0.0 [deg], r=0.2101 [m], alpha=0.0 [deg]
d=0.0000 [m], theta=-0.0 [deg], r=0.2233 [m], alpha=0.0 [deg]


'''

def H_dht(theta, alpha, r, d):
    return matrix([
        [],
        [],
        [],
        []
    ])

def H_3d(theta, a):
    return matrix([
        [cos(theta), -sin(theta), 0, a.cos(theta)],
        [sin(theta), cos(theta), 0, a*sin(theta)],
        [0, 0, a],
        [0,0,0,1]
    ])
