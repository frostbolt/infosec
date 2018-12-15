# Шифр Виженера
import random
ALPHABET = 'АБВГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
STRING_TO_ENCODE = "НЕБЫВАЛЫЕСКИДКИНАВСЕКРИПТОВАЛЮТЫ"

def generate_key(length):
    result = ""
    for i in range(length):
        result += ALPHABET[random.randint(0, len(ALPHABET) - 1)]

    return result

KEYWORD = generate_key(random.randint(1, len(STRING_TO_ENCODE) - 1))

def vigenure(text, key, step):
    result_string = ""

    for i in range(len(text)):
        a = ALPHABET.find(text[i])
        b = ALPHABET.find(key[i % len(key)])

        if a < 0:
            result_string += text[i]
        else:
            result_string += ALPHABET[(a + b*step) % len(ALPHABET)]

    return result_string

ENCODED_STRING = vigenure(STRING_TO_ENCODE, KEYWORD, 1)
DECODED_STRING = vigenure(ENCODED_STRING, KEYWORD, -1)

print(KEYWORD)
print(ENCODED_STRING)
print(DECODED_STRING)
print(DECODED_STRING == STRING_TO_ENCODE)