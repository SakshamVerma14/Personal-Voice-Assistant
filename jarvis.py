import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis SIR !Please tell me,how may I help you")


def takeCommand():
    # it takes microphone input from users and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        #r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Sender's email id', 'YOUR PASSWORD')
    server.sendmail('Sender's email id', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")
        elif 'play music' in query:
            music_dir = 'D:\\audio\\favourite'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"SIR , The time is{strTime}")
        elif 'open code' in query:
            codepath = 'D:\\Installed Softs\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)
        elif 'email to NAME' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "receiver's email id"
                sendEmail(to, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak("sorry my dear.I am unable to send this email")
        elif 'quit' in query:
            exit()
