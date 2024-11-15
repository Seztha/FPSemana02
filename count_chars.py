sentence = input()
letras = {}
for letter in sentence:
    if letter in letras:
        letras[letter] += 1
    else:
        letras[letter] = 1

letras.pop(' ')
print(letras)