import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
from selenium import webdriver


warnings.filterwarnings('ignore')


# Record audio
def record_audio():
    r = sr.Recognizer()  # creating a recognizer object
    # Open the microphone and start recording
    with sr.Microphone() as source:
        print("I'm listening!")
        audio = r.listen(source)
    # Use google speech recogition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition couldnot understand the audio")
    except sr.RequestError as e:
        print("Request results form Google Speech Recognition service error" + e)

    return data


# Function to convert text to audio

def assistant_response(text):
    print(text)
    myobj = gTTS(text=text, lang='en', slow=False)

    # Save converted audio to file

    myobj.save('assistant_response.wav')

    os.system('mpg321 -q assistant_response.wav')


# Function for wake word

def wake_word(text):
    WAKE_WORDS = ['hey computer', 'okay computer', 'hi computer', 'computer', 'hey jarvis', 'okay jarvis', 'hi jarvis', 'jarvis', 'friday', 'hawk']

    text = text.lower()

    for phrase in WAKE_WORDS:
        if phrase in text.lower():
            return True
    # if no wake word is found
    return False


# a function to get the date

def get_date():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    month_num = now.month
    day_num = now.day

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                   'August', 'September', 'October', 'November', 'December']

    # A list of ordinal Numbers
    ordinal_numbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th',
                       '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st',
                       '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    return 'Today is' + " " + weekday + " " + month_names[month_num - 1] + " " + 'the' + " " + ordinal_numbers[
        day_num - 1] + " " + '.'


# A random greeting response

def greeting(text):
    GREETING_INPUTS = ['hi', 'hey', 'how are you', 'hello']

    # Greeting responses
    GREETING_RESPONSES = ['HOWDY', 'HI', 'HOLA', 'YO', 'HEY THERE']

    for word in text.split():
        if word.lower() in GREETING_INPUTS or word.lower().isalnum():
            return random.choice(GREETING_RESPONSES)
    # if no greeting was detected, return empty string
    return ''

# A function to get persons first and last name in the text
def get_wiki_info(text):
    word_list = text.split()
    # print(word_list)
    str = ''
    for i in range(0, len(word_list)):
        if i + 3 <= len(word_list) - 1 and word_list[i].lower() == 'wikipedia' and word_list[i + 1].lower() == 'about':
            for j in range(i + 2, len(word_list)):
                str += word_list[j] + ' '
            return str
def get_person(text):
    word_list = text.split()

    for i in range(0, len(word_list)):
        if i + 3 <= len(word_list) - 1 and word_list[i].lower() == 'who' and word_list[i + 1].lower() == 'is':
            return word_list[i + 2] + ' ' + word_list[i + 3] + '.'