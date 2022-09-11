import pandas as pd
import numpy as np
import sys

# Solution approchée - Algorithme glouton knapsack

Data = [('Action-1', 20, 5.5),
        ('Action-2', 30.54, 10.5),
        ('Action-3', 50, 15),
        ('Action-4', 70, 20),
        ('Action-5', 60, 17),
        ('Action-6', 8.0, 25),
        ('Action-7', 2.2, 72.5),
        ('Action-8', 26, 1.1),
        ('Action-9', 48.25, 0.13),
        ('Action-10', 34.54, 2.7),
        ]

data2 = [('Share-DUPH', 10.01, 12.25),
         ('Share-GTAN', 26.04, 38.06),
         ('Share-USUF', 9.25, 27.69),
         ('Share-CFOZ', 10.64, 38.21),
         ('Share-QLRX', 15.72, 27.47),
         ('Share-XJDT', 0.0, 37.11),
         ('Share-HKFP', 23.97, 19.66),
         ('Share-PPPH', 24.06, 38.2),
         ('Share-HLJY', 26.98, 5.54),
         ('Share-YKBD', 0.0, 22.75),
         ('Share-CTCR', 16.6, 12.4),
         ('Share-LMJG', 16.54, 29.82),
         ('Share-IGUH', 19.13, 14.3),
         ('Share-VIRY', 31.94, 1.84),
         ('Share-CZZS', 27.26, 31.2),
         ('Share-BGRQ', 25.39, 11.63),
         ('Share-SVAM', 18.37, 18.91),
         ('Share-IYAT', 14.95, 19.52),
         ('Share-NNSM', 12.03, 32.13),
         ('Share-VLWV', 3.7, 3.85),
         ('Share-XSSB', 22.12, 38.25),
         ]


def get_file_data(file):
    """csv_name_file = file
    with open(csv_name_file, "r") as f:
        lines = f.readlines()
        lst = [tuple(line.replace().strip().split(",")) for line in lines]
        return lst"""
    df = pd.read_csv(file)
    # print(df.to_string())
    de = list(df.itertuples(index=False, name=None))
    return de


def sac_a_dos_force_brute(capacite, elements, elements_selection=[]):
    if elements:
        val1, lstVal1 = sac_a_dos_force_brute(capacite, elements[1:], elements_selection)
        val = elements[0]
        if val[1] <= capacite:
            val2, lstVal2 = sac_a_dos_force_brute(capacite - val[1], elements[1:], elements_selection + [val])
            if val1 < val2:
                return val2, lstVal2

        return val1, lstVal1
    else:
        return sum([i[2] for i in elements_selection]), elements_selection


# Solution optimale - programmation dynamique
def sac_dos_dynamique(capacite, elements):
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite + 1):
            if elements[i - 1][1] <= w:
                matrice[i][w] = max(elements[i - 1][2] + matrice[i - 1][int(w - elements[i - 1][1])], matrice[i - 1][w])
            else:
                matrice[i][w] = matrice[i - 1][w]

    # Retrouver les éléments en fonction de la somme
    w = capacite
    n = len(elements)
    elements_selection = []
    print(w)
    print("-------")
    print(n)
    while w >= 0 and n >= 0:
        e = elements[n - 1]
        if matrice[n][int(w)] == matrice[n - 1][int(w - e[1])] + int(e[2]):
            elements_selection.append(e)

            w -= e[1]

        n -= 1

    return matrice[-1][-1], elements_selection


sys.setrecursionlimit(1500)

data_csv = get_file_data("datacsv.csv")
# print(data_csv)

print(sac_dos_dynamique(500, data2))
