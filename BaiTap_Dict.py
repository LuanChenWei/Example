dict = {
    'car': 'oto',
    'pen': 'bút',
    'girl': 'cô gái',
    'laptop': 'máy tính xách tay',
    'music player': 'máy nghe nhạc',
    'tablet': 'máy tính bảng'
}

# print(dict["car"])

def display_vnese(word_trans,eng):

    for key in word_trans.keys():
        if key == eng:
            return  word_trans.get(eng)


input_word = str(input("\nEnter word:"))

translated_word = display_vnese(dict,input_word)


if translated_word in dict.values():
    print(translated_word)
else:
    print('word is out of dictionary')

