import numpy as np

ALPHABET, KEYWORD  = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ", "ПОЛЕТ"

def make_matrix():
	return np.reshape(list(dict.fromkeys(KEYWORD + ALPHABET)), (5,6))

def make_phrase(phrase, step):
	if step > 0:
		for i in range(0, len(phrase) - 1, 2):
			if phrase[i] == phrase[i+1]:
				phrase = phrase[:i+1] + 'Х' + phrase[i+1:]

		if len(phrase) % 2 != 0:
			phrase += 'Х'

		phrase = phrase.translate(''.maketrans('ЙЬЁ','ИЪЕ')).replace(' ', '')
	return zip(*([iter(phrase)] * 2))

def playfairs(step, phrase):
	result_string = ''
	z, f = (4, 5) if step == 1 else (1, 1)
	M = make_matrix()
	phrase = [''.join(i) for i in make_phrase(phrase, step)]

	for i, j in phrase:
		y1, x1 = list(map(np.asscalar, np.where(M == i)))
		y2, x2 = list(map(np.asscalar, np.where(M == j)))

		if x1 == x2:
			result_string += M[y1-z][x1] + M[y2-z][x2]
		elif y1 == y2:
			result_string += M[y1][x1-f] + M[y2][x2-f]
		else:
			result_string += M[y1][x2] + M[y2][x1]

	return result_string


phrase = "КОД ПЛЕЙФЕЙЕРА ОСНОВАН НА ИСПОЛЬЗОВАНИИ МАТРИЦЫ БУКВ"
encoded_phrase = "КЛКЕПЕШОБКЕРЭЛЧСКУЛЮЕТВМВКИММЮЗОТЖША"

print(make_matrix())
print(playfairs(1, phrase))
print(playfairs(-1, list(encoded_phrase)))
