def get_google_search(text):
    word_list = text.split()
    for i in range(0, len(word_list)):
        if i + 3 <= len(word_list) - 1 and word_list[i].lower() == 'google' and word_list[i + 1].lower() == 'search':
            return word_list[i+2]
text_2 = 'google search third thing'
z = get_google_search(text_2)
print(z)