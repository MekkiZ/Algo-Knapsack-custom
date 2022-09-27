"""System module"""
import sys


Data = [('Action-1', 20, 5),
        ('Action-2', 30, 10),
        ('Action-3', 50, 15),
        ('Action-4', 70, 20),
        ('Action-5', 60, 17),
        ('Action-6', 8, 25),
        ('Action-7', 2, 7),
        ('Action-8', 26, 11),
        ('Action-9', 48, 13),
        ('Action-10', 34, 27),
        ('Action-11', 42, 17),
        ('Action-12', 38, 23),
        ('Action-13', 110, 9),
        ('Action-14', 14, 1),
        ('Action-15', 18, 3),
        ('Action-16', 8, 8),
        ('Action-17', 4, 12),
        ('Action-18', 10, 14),
        ('Action-19', 24, 21),
        ('Action-20', 114, 18),
        ]


def sac_a_dos_force_brute(capacite, elements, elements_selection=[]):
    # We use a recursive function, we have to show stop point. With this point with verify if you have elements,
    # if we have no element to traite. and we return the sum with element took

    if elements:

        # So if we have element in list, with call recursively the function
        val1, lstVal1 = sac_a_dos_force_brute(capacite, elements[1:], elements_selection)
        val = elements[0]
        if val[1] <= capacite:
            val2, lstVal2 = sac_a_dos_force_brute(capacite - val[1], elements[1:], elements_selection + [val])
            if val1 < val2:
                return val2, lstVal2

        return val1, lstVal1
    else:
        return sum([i[2] for i in elements_selection]), elements_selection


sys.setrecursionlimit(2000)

print(sac_a_dos_force_brute(500, Data))
