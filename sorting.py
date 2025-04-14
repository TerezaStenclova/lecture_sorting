import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, 'r') as file_csv:
        reader = csv.DictReader(file_csv)
        data = {}

        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]

                else:
                    data[header].append(int(value))

        return data

def selection_sort(num_list, direction = 'ascending'):
    """
    vzestupně seřadit všechny prvky posloupnosti dle principů Selection Sor
    :param list num_list: libovolně dlouhý seznam celých čísel
    :param str direction: zda bude posloupnost seřazena vzestupně(ascending) nebo sestupně (descending)
    :return: seřazený seznam prvků
    """
    n = len(num_list)

    for i in range(n):
        min_max_idx = i
        for j in range(i+1,n):
            if direction == 'ascending':
                if num_list[j] < num_list[min_max_idx]:
                    min_max_idx = j
            elif direction == 'descending':
                if num_list[j] > num_list[min_max_idx]:
                    min_max_idx = j
        num_list[i], num_list[min_max_idx] = num_list[min_max_idx], num_list[i]
    return num_list

def bubble_sort(num_list):
    """
     vzestupně seřadit všechny prvky posloupnosti dle principů Bubble Sort.
     :param list num_list: libovolně dlouhý seznam celých číse
     :return: Funkce vrátí seřazený seznam číse
    """
    n = len(num_list)

    for i in range(n): #i pocet cyklu (vzdy posouvani jineho maxima)
        for j in range(0, n - i - 1): # -1... poseldní prvek už je na správném místě, -i ...kolik prvku na konci uz je ok -> kolik cyklu jsme prosly
            if num_list[j] > num_list[j + 1]: #porovnavani sousednich prvku v cele delce v ramci jednoho cyklu  a posunuti maxima na konec
                # Prohození prvků
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list

def insertion_sort(num_list):
    """
    vzestupně seřadit všechny prvky posloupnosti dle principů Insertion Sor
    :param list num_list: libovolně dlouhý seznam celých číse
    :return: Funkce vrátí seřazený seznam číse
    """
    n = len(num_list)
    for i in range(1, n):
        key = num_list[i]  # prvek, který chceme vložit na správné místo
        j = i - 1
        # Posunuj větší prvky doprava, dokud nenajdeš správné místo
        while j >= 0 and num_list[j] > key:
            num_list[j + 1] = num_list[j]
            j -= 1
        num_list[j + 1] = key  # vložení na správné místo
    return num_list

def main():
    data = read_data("numbers.csv")
    print(data)

    sorting_selection = selection_sort(data['series_1'], 'ascending')
    print(sorting_selection)

    sorting_bubble =  bubble_sort(data['series_1'])
    print(sorting_bubble)

    sorting_insertion = insertion_sort(data['series_1'])
    print(sorting_insertion)

    pass


if __name__ == '__main__':
    main()
