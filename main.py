str1 = input().split()


def ka(word):
    countw = 0
    for c in word:
        if str(c).isalpha():
            countw += 1
    return countw


def ceasar(inp, k):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    out = ''
    for i in range(len(inp)):
        if inp[i] in eng_lower_alphabet:
            out += eng_lower_alphabet[(eng_lower_alphabet.find(inp[i]) + k) % 26]
        elif inp[i] in eng_upper_alphabet:
            out += eng_upper_alphabet[(eng_upper_alphabet.find(inp[i]) + k) % 26]
        elif inp[i] in rus_lower_alphabet:
            out += rus_lower_alphabet[(rus_lower_alphabet.find(inp[i]) + k) % 32]
        elif inp[i] in rus_upper_alphabet:
            out += rus_upper_alphabet[(rus_upper_alphabet.find(inp[i]) + k) % 32]

        else:
            out += inp[i]
    return out


print(*[ceasar(el, ka(el)) for el in str1])
