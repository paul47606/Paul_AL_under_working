import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good morning Paul')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon Paul')
    else:
        speak('Good Evening Paul')

    speak('I am jarvis Paul, Please tell me how may i help you.')


# it takes the microphone input from the and gives the string output.
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as sources:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(sources)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak('Say that again please...')
        return 'None'
    return query

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences = 2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open Youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open Google' in query:
            webbrowser.open('Google.com')

        elif 'open Youtube' in query:
            webbrowser.open('youtube.com')



