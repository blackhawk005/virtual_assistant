# This is the virtual assistant program that gets me the date, the current time and
# random greeting, and returns information on one person.
from programs import *
from google_searching import *

searches = []
while True:
    # record the audio
    text = record_audio()
    response = ''

    # Check for the wake words
    if wake_word(text):
        response = response + greeting(text) + '.'

        if 'date' in text:
            date = get_date()
            response = response + ' ' + date
        # day
        if 'day' in text:
            my_date = datetime.datetime.today()
            weekday = calendar.day_name[my_date.weekday()]
            response = response + 'It is ' + weekday
        # check time
        if 'time' in text:
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >= 12:
                meridiem = 'PM'
                hour = now.hour - 12
            else:
                meridiem = 'AM'
                hour = now.hour
            if now.minute < 10:
                minute = '0' + str(now.minute)
            else:
                minute = str(now.minute)

            response = response + ' ' + 'It is ' + str(hour) + ':' + str(minute) + ' ' + meridiem + '.'

        if 'who is' in text:
            person = get_person(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        if "wikipedia about" in text.lower():
            info = get_wiki_info(text)
            wiki = wikipedia.summary(info, sentences=10)
            response = response + ' ' + wiki

        if 'google search' in text.lower() or 'find information about' in text.lower():
            search_google = str(get_html_search(text))
            # create webdriver object
            driver = webdriver.Chrome('/Users/jarvis/Downloads/chromedriver')
            # get google.co.in
            driver.get("https://google.co.in/search?q=" + search_google)
            try:
                from googlesearch import search
            except ImportError:
                print("No module named 'google' found")
            # to search
            query = get_google_search(text)
            print(query)
            # print(search)
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                searches.append(j)
            # print(searches)
        if "go to" in text.lower():
            further = get_further_search(text)
            print(further)
            dictionary = {'first': 0,
                          'second': 1,
                          'third': 2,
                          'fourth': 3,
                          'fifth': 4,
                          'sixth': 5,
                          'seventh': 6,
                          'eight': 7,
                          'ninth': 8,
                          'tenth': 9}

            driver = webdriver.Chrome('/Users/jarvis/Downloads/chromedriver')
            driver.get(searches[dictionary[further]])
        if 'kill present search' in text.lower():
            response = 'All the present searches has been ended.'
            searches = []
        if 'you can go' in text:
            response = 'Okay. Awaiting for my next call. Till then STAY SAFE JAI HIND JAI BHARAT'
            assistant_response(response)
            break
        if 'shows searches' or 'show searches' in text.lower():
            print(searches)

        if "who am i" in text.lower() or 'who i am' in text.lower():
            response = response + ' ' + "You're Shinit Shetty."

        if 'you can go' in text:
            response = 'Okay. Awaiting for my next call. Till then STAY SAFE JAI HIND JAI BHARAT'
            assistant_response(response)
            break
    else:
        response = "Could'nt recognize. Please try again"

    assistant_response(response)
