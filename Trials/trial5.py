

#text = recordAudio()
#text = text.lower()

def getSearch(text):
    word_list = text.split()
    print(len(word_list))
    str = ''
    for i in range(0, len(word_list)):
        if i + 3 <= len(word_list) and word_list[i].lower() == 'google' and word_list[i + 1].lower() == 'search':
            for j in range(i+2, len(word_list)):
                str += word_list[j] + ' '
            return str

text = 'google search timepass'

if ('google search' in text):
    #get the keyword to be searched in google
    keyword = getSearch(text)
    #keyword = 'timepass'
    print(keyword)

    #create webdriver object
    #driver = webdriver.Firefox()

    #get google.co.in
    #driver.get("https://google.co.in/search?q=" + keyword)
