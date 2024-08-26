#!/usr/bin/env python
import math
from read_pdb import Atom, PDB

def dist(A, B):
    xdif = (atoms[B-1].x - atoms[A-1].x)**2
    ydif = (atoms[B-1].y - atoms[A-1].y)**2
    zdif = (atoms[B-1].z - atoms[A-1].z)**2
    return math.sqrt(xdif + ydif + zdif)

def ang(A, B, C):
    xba = atoms[A-1].x - atoms[B-1].x
    yba = atoms[A-1].y - atoms[B-1].y
    zba = atoms[A-1].z - atoms[B-1].z
    xbc = atoms[C-1].x - atoms[B-1].x
    ybc = atoms[C-1].y - atoms[B-1].y
    zbc = atoms[C-1].z - atoms[B-1].z
    dot = (xba*xbc) + (yba*ybc) + (zba*zbc)
    d_ab = dist(A, B)
    d_bc = dist(B, C)
    return (math.acos(dot/(d_ab*d_bc))) * 180 / math.pi

def dihe(A, B, C, D):
    xba = atoms[A-1].x - atoms[B-1].x
    yba = atoms[A-1].y - atoms[B-1].y
    zba = atoms[A-1].z - atoms[B-1].z
    xbc = atoms[C-1].x - atoms[B-1].x
    ybc = atoms[C-1].y - atoms[B-1].y
    zbc = atoms[C-1].z - atoms[B-1].z
    xcb = atoms[B-1].x - atoms[C-1].x
    ycb = atoms[B-1].y - atoms[C-1].y
    zcb = atoms[B-1].z - atoms[C-1].z
    xcd = atoms[D-1].x - atoms[C-1].x
    ycd = atoms[D-1].y - atoms[C-1].y
    zcd = atoms[D-1].z - atoms[C-1].z

    # Cross vectors
    Cbabc_x = (yba * zbc) - (zba * ybc)
    Cbabc_y = (zba * xbc) - (xba * zbc)
    Cbabc_z = (xba * ybc) - (yba * xbc)

    Ccbcd_x = (ycb * zcd) - (zcb * ycd)
    Ccbcd_y = (zcb * xcd) - (xcb * zcd)
    Ccbcd_z = (xcb * ycd) - (ycb * xcd)

    dot = (Cbabc_x * Ccbcd_x) + (Cbabc_y * Ccbcd_y) + (Cbabc_z * Ccbcd_z)
    Den = math.sqrt(Cbabc_x**2 + Cbabc_y**2 + Cbabc_z**2) * math.sqrt(Ccbcd_x**2     + Ccbcd_y**2 + Ccbcd_z**2 )

    i = yba * zcd - zba * ycd
    j = zba * xcd - xba * zcd
    k = xba * ycd - yba * xcd
    f = i * xbc + j * ybc + k * zbc

    if f >= 0:
        return (math.acos(dot / Den)) * 180 / math.pi
    else:
        return -1 * ((math.acos(dot / Den)) * 180 / math.pi)

if __name__ == '__main__':
    import sys
    pdb = PDB(sys.argv[1])
    atoms = pdb.get_atoms(to_dict=False) # if to_dict == True, atoms is the List of Atom dictionaries.

    # serial atom indices for bond, angle, and dihedral
    atm1 = 1
    atm2 = 2
    atm3 = 3
    atm4 = 4

    # calculate bond distance
    distance = dist(atm1, atm2)
    print("Distance:", distance)

    # calculate angle
    angle = ang(atm1, atm2, atm3)
    print("Angle:", angle)

    # calculate dihedral
    dihedral = dihe(atm1, atm2, atm3, atm4)
    print("Dihedral angle:", dihedral)
