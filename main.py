import pandas as pd
import csv
import math


def get_file_data(file):
    """
    This function traite data from csv and filter all price > 0 and delete all prices < 0 .
    :param file: Name of file in csv formation, write on string ( "xxxx.csv" ).
    :return: The data
    """
    df = pd.read_csv(file)
    # print(df.to_string())
    de = list(df.itertuples(index=False, name=None))
    list_fr = []
    for i in list(de):
        js = int(i[1] * 100)
        list_tuple = i[0], js, i[2]
        list_fr.append(list_tuple)
    list_data = [i for i in list_fr if i[1] >= 0]
    return list_data


# Solution optimale - programmation dynamique
def sac_dos_dynamique(capacite, elements):
    """
    This function is a algorithm knapsack for finance.
    :param capacite: It's determinate by the user, here we use 50000 cents ( 500 eu ).
    :param elements: We take with the first function the data .
    :return: A list with sum of price and profit and tuples contains all information of data took.
    """
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]
    for i in range(1, len(elements), 1):
        for w in range(1, capacite + 1):
            if elements[i - 1][1] <= w:
                matrice[i][w] = max(elements[i - 1][2] + matrice[i - 1][w - (elements[i - 1][1])], matrice[i - 1][w])
            else:
                matrice[i][w] = matrice[i - 1][w]

    # Retrouver les éléments en fonction de la somme
    w = capacite
    n = len(elements)
    elements_selection = []
    element_sum = []
    element_sum_profit = []
    while w >= 0 and n >= 0:
        e = elements[n - 1]
        if matrice[n][w] == matrice[n - 1][w - e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]
        n -= 1
    for i in elements_selection:
        element_sum.append(i[1])
        result_sum = float((math.fsum(element_sum)) // 100)
        element_sum_profit.append(i[2])
        result_sum_profit = float(math.fsum(element_sum_profit))
    return result_sum_profit, result_sum, elements_selection



v = get_file_data("datacsv2.csv")
print(sac_dos_dynamique(50000, v))

