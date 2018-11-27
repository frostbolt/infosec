KEYWORD = 'ПОЛЕТ'
ALPHABET = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЭЮЯ'

STRING_TO_ENCODE = 'КОДПЛЕЙФЕЙЕРАОСНОВАННАИСПОЛЬЗОВАНИИМАТРИЦЫБУКВ'
ENCODED_STRING = 'КЛКЕПЕШОБКЕРЭЛЧСКУЛЮЕТВМВКИММЮЗОТЖША'

def prepare_matrix keyword
	a = ALPHABET.split ''
	keyword.split('').each { |letter| a -= [letter] }
	(keyword.split('')+a).each_slice(6).to_a
end

M = prepare_matrix KEYWORD

5.times	do |i|
	puts M[i].join ' '	
end

def find_index e 
	i = M.join.split('').find_index e
	[Integer(i / 6),i % 6]
end

def playfairs string, step
	sliced = string.gsub('Ъ','Ь').gsub('Й','И').gsub('Ё','Е').split('').each_slice(2).to_a
	result_string = ''
	sliced.map do |pair|
		first_index = find_index(pair[0])
		second_index = find_index(pair[1])

		i = first_index[0][0]
		j = first_index[1][0]
		n = second_index[0][0]
		m = second_index[1][0]

		if i == n
			result_string += M[i][(j + step) % 6] + M[n][(m + step) % 6]
		elsif j == m				
			result_string += M[(i + step) % 5][j] + M[(n + step) % 5][m]
		else
			result_string += M[i][m] + M[n][j]
		end
	end
	result_string
end

puts playfairs(ENCODED_STRING, -1)
