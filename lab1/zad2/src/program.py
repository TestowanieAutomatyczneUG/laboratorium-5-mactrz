import math

def roman(number):
    if number == 1:
        return "I"
    elif number == 2:
        return "II"
    elif number == 3:
        return "III"
    elif number == 4:
        return "IV"
    elif number == 5:
        return "V"
    elif number == 6:
        return "VI"
    elif number == 9:
        return "IX"
    else:
        napis = ""
        baseROM = ""
        base = 1
        while number != 0:
            if number >= 400:
                base = 400
                baseROM = "CD"
            elif number >= 100:
                base = 100
                baseROM = "C"
            elif number >= 90:
                base = 90
                baseROM = "XC"
            elif number >= 50:
                base = 50
                baseROM = "L"
            elif number >= 40:
                base = 40
                baseROM = "XL"
            elif number >= 10:
                base = 10
                baseROM = "X"
            elif number >= 9:
                base = 9
                baseROM = "IX"
            elif number >= 5:
                base = 5
                baseROM = "V"
            elif number >= 4:
                base = 4
                baseROM = "IV"
            elif number >= 1:
                base = 1
                baseROM = "I"

            howmany = number // base
            number = number - (howmany*base)
            napis += howmany * baseROM
        return napis
