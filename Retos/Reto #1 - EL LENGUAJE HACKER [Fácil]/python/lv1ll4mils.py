def hacker_languaje():
    phrase = input("Ingreasa la frase que sera convertida en lenguaje HACKER:\n")
    #print(phrase)

    _dict =  {"A": "4", "B": "I3", "C": "[", "D": ")",
                "E": "3", "F": "|=", "G": "&", "H": "#",
                "I": "1", "J": ",_|", "K": ">|", "L": "1",
                "M": "/\/\\", "N": "^/", "O": "0", "P": "|*",
                "Q": "(_,)", "R": "I2", "S": "5", "T": "7",
                "U": "(_)", "V": "\/", "W": "\/\/", "X": "><",
                "Y": "j", "Z": "2", "1": "L", "2": "Z",
                "3": "E", "4": "A", "5": "S", "6": "b",
                "7": "T", "8": "B", "9": "g", "0": "o"}


    hacker_phrase = ''
    for char in phrase:
        if char.upper() in _dict:
            hacker_phrase += _dict[char.upper()]
        else:
            hacker_phrase += char

    print("Frase en lenguaje Hacker:", hacker_phrase)

hacker_languaje()