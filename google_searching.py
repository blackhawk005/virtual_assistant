import speech_recognition as sr
import os
from gtts import gTTS
import random
import warnings
from selenium import webdriver


warnings.filterwarnings('ignore')

searches = []
# Record audio
def record_audio():
    r = sr.Recognizer()  # creating a recognizer object
    # Open the microphone and start recording
    with sr.Microphone() as source:
        print("I'm listening!")
        r.adjust_for_ambient_noise(source, duration=3)
        r.dynamic_energy_threshold = True
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

def get_html_search(text):
    word_list = text.split()
    #print(word_list)
    str = ''
    for i in range(0, len(word_list)):
        if i + 3 <= len(word_list) and word_list[i].lower() == 'google' and word_list[i + 1].lower() == 'search':
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
        if i + 3 <= len(word_list) and word_list[i].lower() == 'google' and word_list[i + 1].lower() == 'search':
            for j in range(i + 2, len(word_list)):
                str += word_list[j] + ' '
            return str
def get_further_search(text):
    word_list = text.split()
    for i in range(0, len(word_list)):
        if i + 3 <= len(word_list) - 1 and word_list[i].lower() == 'go' and word_list[i + 1].lower() == 'to':
            return word_list[i + 2]

def greeting(text):
    GREETING_INPUTS = ['hi', 'hey', 'how are you', 'hello']

    # Greeting responses
    GREETING_RESPONSES = ['HOWDY', 'HI', 'HOLA', 'YO', 'HEY THERE']

    for word in text.split():
        if word.lower() in GREETING_INPUTS or word.lower().isalnum():
            return random.choice(GREETING_RESPONSES)
    # if no greeting was detected, return empty string
    return ''
