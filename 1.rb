ALPHABET = ("А".."Я").to_a
message = "ИЦРХЭЫЩШШЩРЬЩЩМДРШУРМЮПРЭЪЩЬЭРЪРШШЩТЛЧРШКЭЗЩМЖВШЩРМЮЧЛСШЩРЬЩЩМДРШУР".split('')
STRANGE_PARINGS = %w{ЬЬ ЪЪ ЭЩ ЬЪ ЪЦ ЪЖ ФФ ЪШ ИЦ ЖФ ПБ АЫ ЙЫ ШЖ ЬК ЖШ ЬЧ ЪЧ ЙЪ ШЩ ЮЪ}

def cesar_decode(symbol, step)
	ALPHABET[(ALPHABET.find_index(symbol) + step + 1) % ALPHABET.size]
end

def has_strange_parings(str)
	for	paring in STRANGE_PARINGS
		return true if str.include? paring
	end
	false
end

results = []

(ALPHABET.size - 1).times { |n|
	temp = message.map { |e| cesar_decode(e, n+1) }
	puts "#{n}\t#{temp.join}" unless has_strange_parings temp.join
}