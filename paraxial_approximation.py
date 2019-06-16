import numpy as np


def ABCD_matrix(matrix_list):
    ABCD_m = matrix_list.pop()
    while matrix_list:
        ABCD_m = np.dot(ABCD_m, matrix_list.pop())
    return ABCD_m[0, 0], ABCD_m[0, 1], ABCD_m[1, 0], ABCD_m[1, 1]


def transfar_matrix(d, n):
    return np.matrix([[1, d/n],
                      [0, 1]])


def refraction_matrix(r, n1, n2):
    return np.matrix([[1, 0], [-(n2 - n1)/r, 1]])


def ABCD_cal(Lens, start_surface=0, end_surface=0):
    surf = Lens.surface_list
    start, end = start_surface, end_surface
    surf_matrix_list = []
    for i in range(start, end+1):
        if i == 0:
            n1 = 1
        else:
            n1 = surf[i].indexlist[surf[i-1].wavelength_list[0]]
        n2 = surf[i].indexlist[surf[i].wavelength_list[0]]
        d = surf[i].thickness
        r = surf[i].radius
        R = refraction_matrix(r, n1, n2)
        T = transfar_matrix(d, n2)
        surf_matrix_list.append(R)
        if i != end:
            surf_matrix_list.append(T)
    A, B, C, D = ABCD_matrix(surf_matrix_list)
    return A, B, C, D
