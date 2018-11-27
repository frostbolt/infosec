# Шифр Виженера
import random
ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
STRING_TO_ENCODE = "НЕБЫВАЛЫЕСКИДКИНАВСЕКРИПТОВАЛЮТЫ"

def generate_key(length):
    result = ""
    for i in range(length):
        result += ALPHABET[random.randint(0, len(ALPHABET) - 1)]
    return result

KEYWORD = generate_key(random.randint(0, len(STRING_TO_ENCODE) - 1))

def vigenure(text, key, step):
    result_string = ""

    for i in range(len(text)):
        a = ALPHABET.find(text[i])
        if a == -1:
            raise Exception("Алфавит не содержит " + text[i])
        b = ALPHABET.find(key[i % len(key)])

        if b == -1:
            raise Exception("Алфавит не содержит " + key[i])

        c = (a + b*step) % len(ALPHABET)
        result_string += ALPHABET[c]
    return result_string


try:
	ENCODED_STRING = vigenure(STRING_TO_ENCODE, KEYWORD, 1)
	DECODED_STRING = vigenure(ENCODED_STRING, KEYWORD, -1)

except Exception as e:
	print(e)

else:
	print(KEYWORD)
	print(ENCODED_STRING)
	print(DECODED_STRING)
	print(DECODED_STRING == STRING_TO_ENCODE)