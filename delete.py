def transliterate(text):
    translit_dict = {
        'a': 'ф',
        'b': 'и',
        'c': 'с',
        'd': 'в',
        'e': 'у',
        'f': 'а',
        'g': 'п',
        'h': 'р',
        'i': 'ш',
        'j': 'о',
        'k': 'л',
        'l': 'д',
        'm': 'ь',
        'n': 'т',
        'o': 'щ',
        'p': 'з',
        'q': 'й',
        'r': 'к',
        's': 'і',
        't': 'е',
        'u': 'г',
        'v': 'м',
        'w': 'ц',
        'x': 'ч',
        'y': 'н',
        'z': 'я',
        '[': 'х',
        ']': 'ї',
        ';': 'ж',
        "'": 'є',
        ',': 'б',
        '.': 'ю',
    }

    result = ''
    for char in text:
        if char.lower() in translit_dict:
            result += translit_dict[char.lower()]
        else:
            result += char
    return result


input_text = "ghbdsn"
output_text = transliterate(input_text)
print(output_text)
