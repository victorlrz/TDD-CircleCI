import re


def Add(numbers):
    res = 0
    substring = ','
    substring_to_avoid = ',\n'
    if numbers.find(substring) == -1 and numbers != '':
        res = int(numbers)
    if numbers.find(substring) == 1 and numbers != '' and numbers.find(substring_to_avoid) == -1:
        tab = re.split(",|\n", numbers)
        for i in tab:
            res += int(i)
    if numbers.find(substring_to_avoid) == 1:
        res = "WRONG INPUT"
    return res
