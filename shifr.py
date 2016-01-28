
dict_to_shifr = {'\xe0': '24',
                 '\xe1': '38',
                 '\xe2': '23',
                 '\xe3': '17',
                 '\xe4': '29',
                 '\xe5': '15',
                 '\xe6': '2A',
                 '\xe7': '1A',
                 '\xe8': '35',
                 '\xe9': '11',
                 '\xea': '14',
                 '\xeb': '28',
                 '\xec': '34',
                 '\xed': '16',
                 '\xee': '27',
                 '\xef': '25',
                 '\xf0': '26',
                 '\xf1': '33',
                 '\xf2': '36',
                 '\xf3': '13',
                 '\xf4': '21',
                 '\xf5': '1B',
                 '\xf6': '12',
                 '\xf7': '32',
                 '\xf8': '18',
                 '\xf9': '19',
                 '\xfa': '1C',
                 '\xfb': '22',
                 '\xfc': '37',
                 '\xfd': '2B',
                 '\xfe': '39',
                 '\xff': '31',
                 ' ': '41',
                 ',': '42',
                 '.': '43'}


def to_shifr(string):
    shifr_string = ''
    for i in string:
        for el in dict_to_shifr:
            if el == i:
                shifr_string += '+' + dict_to_shifr[i]
    shifr_string = shifr_string[1:]
    return shifr_string


def de_shifr(shifr_string):
    deshifr_string = ''
    for i in shifr_string.split('+'):
        for el in dict_to_shifr:
            if i == dict_to_shifr[el]:
                deshifr_string += el
    return deshifr_string
