import pyperclip

unicode = "⁥⁥⁥"
tab = {
    "a": "а",
    "c": "с",
    "e": "е",
    "j": "ј",
    "l": "ӏ",
    "o": "о",
    "p": "р",
    "x": "х",
    "y": "у",
    "s": "ѕ"
}

string = list(input("enter to conv: "))

convertedstring = ""

for char in string:
    convertedchar = tab.get(char.lower(), char)
    convertedstring += convertedchar

convertedstring = unicode.join(convertedstring)

print(convertedstring)

pyperclip.copy(convertedstring)
