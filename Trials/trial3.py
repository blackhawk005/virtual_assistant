# Python program to demonstrate
# selenium

from selenium import webdriver
def google_search(keyword):

    # create webdriver object
    driver = webdriver.Chrome()

    # enter keyword to search
    key = keyword

    # get google.co.in
    driver.get("https://google.co.in/search?q=" + key)


def get_html_search(text):
    word_list = text.split()
    #print(word_list)
    str = ''
    for i in range(0, len(word_list)):
        if i + 3 <= len(word_list) - 1 and word_list[i].lower() == 'google' and word_list[i + 1].lower() == 'search':
            for j in range(i+2, len(word_list)):
                if word_list[j].isalpha():
                    str += word_list[j] + '+'
                elif word_list[j] == '+':
                    str += '%2B'
                else:
                    str += word_list[j]
            return str
def get_google_search(text):
    word_list = text.split()
    str = ''
    for i in range(0, len(word_list)):
        if i + 3 <= len(word_list) - 1 and word_list[i].lower() == 'google' and word_list[i + 1].lower() == 'search':
            for j in range(i + 2, len(word_list)):
                str += word_list[j] + ' '
            return str
def get_further_search(text):
    word_list = text.split()
    for i in range(0, len(word_list)):
        if i + 3 <= len(word_list) - 1 and word_list[i].lower() == 'go' and word_list[i + 1].lower() == 'to':
            return word_list[i + 2]


searches = []
text = 'google search the tallest building'
text_2 = 'go to third site'
if ('google search' in text.lower() or 'find information about' in text.lower()):
    search_google = str(get_html_search(text))
    # create webdriver object
    driver = webdriver.Chrome()
    # get google.co.in
    driver.get("https://google.co.in/search?q=" + search_google)
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    # to search
    query = get_google_search(text)
    #print(search)
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        searches.append(j)
    print(searches)

if ("go to" in text_2.lower()):
    further = get_further_search(text_2)
    print(further)
    dict = {'first': 0, 'second': 1, 'third': 2, 'fourth': 3, 'fifth': 4, 'sixth': 5, 'seventh': 6, 'eight': 7,
            'ninth': 8, 'tenth': 9}

    driver = webdriver.Chrome()
    print(dict[further])
    driver.get(searches[dict[further]])


