import sys

Data = [('Action-1', 20, 5.5),
        ('Action-2', 30.67, 10.5),
        ('Action-3', 50.34, 15),
        ('Action-4', 70.45, 20),
        ('Action-5', 60, 17),
        ('Action-6', 8, 25),
        ('Action-7', 2, 72.5),
        ('Action-8', 26, 1.1),
        ('Action-9', 48, 0.13),
        ('Action-10', 34, 2.7),
        ]


def sac_a_dos_force_brute(capacite, elements, elements_selection=[]):


    # We use a recurcive function, we have to show stop point.
    # With this point with verify if have elements, if we have no element to traite. and we return the sum with element took

    if elements:

        # So if we have lement in list, with call recursively the fucntion
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
