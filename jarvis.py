import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning....")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon....")

    else:
        speak("Good Evening")
        print("Good Evening....")

    speak("I AM JARVIS ,Sir please tell me how may i help you !!")


def takecommand():
    """It take microphone input and return string output"""

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        # r.energy_threshold = 500
        audio= r.listen(source)


        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please ..")
            return None

        return query


if __name__ == '__main__':

    wishme()
    while True:
        try:
            query=takecommand().lower()  #if query is empty then it will give  that why try-except Execption
        except Exception:
            # print("Some thing went wrong")
            continue

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace('wikipedai','')
            try:
                results= wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception:
                speak("Not found in Wikipedia")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'name' in query:
            speak("Aniket")

        elif 'open google' in query:
                    webbrowser.open("google.com")


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'music' in query:
            music_dir = r'D:\\songs'
            song=os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[0]))

        elif 'time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'python' in query:
            path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(path)

        elif "exit" in query:
            exit()