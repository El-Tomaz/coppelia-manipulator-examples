import numpy as np
from numpy import cos, sin, matrix

def R(q):

    q_rad = np.deg2rad(q)
    return np.array(
        [[np.cos(q_rad), -np.sin(q_rad)],
         [np.sin(q_rad), np.cos(q_rad)]]
    )


def Tx(q):
    return np.array()


def Ty(q):
    pass

# function to return Homogeneous transformation


def HT(theta_degree, a):

    theta = np.deg2rad(theta_degree)
   

    return np.array([
        [np.cos(theta), -np.sin(theta), a*np.cos(theta)],
        [np.sin(theta), np.cos(theta), a*np.sin(theta)],
        [0,       0,       1]
    ])


def H(theta, x, y):
    return np.matrix([
        [cos(theta), -sin(theta), x],
        [sin(theta), cos(theta), y],
        [0,0,1]
    ])
    
