import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

#print(voices[0].id)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wishMe():
    hour = int(datetime.datetime.now().hour)    

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")  

    speak("Jarvis at your service. How may i help you, Sir?")      

def takeCommand():

    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        #print (e)

        print ("Say that again please...")

        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('utshobhassan379@gmail.com', 'kotncogplpgmwvon')
    server.sendmail('utshobhassan379@gmail.com', to, content)
    server.close() 


if __name__ == "__main__":
    #speak 
    wishMe()
    
    while True:
    
    #if 1:
        query = takeCommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'play music' in query:
            music_dir = 'F:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = ("C:\\users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe") 
           # os.startfile(codePathelif 'open vs code' in query:
            os.startfile(codePath)

        elif 'open codeblocks' in query:
            codePath1 = ("C:\\Program Files\\CodeBlocks\\codeblocks.exe")
            os.startfile(codePath1)

        elif 'open opera mini' in query:
            codePath2 = ("C:\\Users\\ASUS\\AppData\\Local\\Programs\\Opera\\launcher.exe")
            os.startfile(codePath2)

        elif 'open spotify' in query:
            codePath3 =("C:\\Users\\ASUS\\Desktop\\Spotify.lnk")
            os.startfile(codePath3)

        elif 'open skype' in query:
            codePath4 = ("C:\\Users\\ASUS\\Desktop\\Skype.lnk")
            os.startfile(codePath4)

        elif 'open discord' in query:
            codePath5 = ("C:\\Users\\ASUS\\Desktop\\Discord.lnk")
            os.startfile(codePath5)

        elif 'open calculator' in query:
            codePath6 = ("C:\\Users\\ASUS\\Desktop\\Calculator.lnk")
            os.startfile(codePath6)

        elif 'open camera' in query:
            codePath7 = ("C:\\Users\\ASUS\\Desktop\\Camera.lnk")
            os.startfile(codePath7)

        elif 'open ms word' in query:
            codePath8 = ("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013.lnk")
            os.startfile(codePath8)

        elif 'open notepad' in query:
            codePath9 = ("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad.lnk")
            os.startfile(codePath9)

        elif 'open zoom' in query:
            codePath10 = ("C:\\Users\\ASUS\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
            os.startfile(codePath10)

        elif 'open torrent' in query:
            codePath11 = ("C:\\Users\\ASUS\\AppData\\Roaming\\uTorrent\\uTorrent.exe")
            os.startfile(codePath11)

        elif 'how are you' in query:

            speak("I am doing fine, Sir! Thanks for your concern. How about you, Sir?")
        
        elif 'teacher' in query:

            speak("Hello there ladies and gentlemen! It is an honor for me to meet you!")

        elif 'what can you do' in query:

            speak("Sir! I can do a lot of things on my own! Just try me!")

        elif 'listening' in query:

            speak("Sorry Sir. My bad!")

        elif 'thank you' in query:

            speak("My pleasure, Sir.")

        elif 'bye' in query:

            speak("Good-bye everyone! Hope to see you soon!")

        elif 'maya' in query:

            speak("Maya is your girlfriend, Sir. She is also your future wife. She is the love of your life!")

        elif 'love' in query:

            speak("Maya, Mr.Hassan loves you a lot. He loves you more than anything.'")

        elif 'sorry' in query:

            speak("Maya, please forgive Mr. Hassan. He feels sorry.")



        elif 'email to joy' in query:
            
            try:
                speak("What should i say, Sir?")
                content = takeCommand()
                to = "alexutshob@gmail.com"
                sendEmail(to, content)
                speak("Sir, your email has been sent!")
            
            except Exception as e:
                print(e)
                speak("Sorry Sir, failed to sent your email.")
    