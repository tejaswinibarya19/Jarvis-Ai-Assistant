#importing libraries

import pyttsx3  #this provide engine which convert voice into text
import speech_recognition as sr # type: ignore
import datetime
import os
import webbrowser
import random
import requests 
import wikipedia  # type: ignore
import pywhatkit as kit # type: ignore
import smtplib
import time
import pyjokes # type: ignore
import instaloader # type: ignore
import pyautogui # type: ignore
import string as str
from pytube import YouTube # type: ignore
import shutil



#function 1) convert text to speech
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

#function 2 ) take command from user
def takecommand():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=15, phrase_time_limit=2) #timeout means how mmuch time it take to listen and recognizing and phrase time limit parameter means kitne der ka pause app le sakte ho bolte time
            # recognize speech using google to recognize clear input and give hindi output also

            try:
                    print("Recognizing...")
                    query = r.recognize_google(audio, language='en-in')
                    print(f"User Said : {query}")

                    if query.lower() == "jarvis stop":
                        speak("Okay Boss, I'll stop listening.")
                        break  # Exit the loop if the user says "stop listening"

                    if query.lower() == "jarvis":
                        speak("Yes Boss, How May I Help You?")

                    return query.lower()

            except sr.UnknownValueError:
                    print("Jarvis could not understand audio, speak clearly!!")
            except sr.RequestError as e:
                    print("Error; {0}".format(e))


#funtion 3) to wish
def wish():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute


    if hour>=5 and hour<=11.59:
        speak(f"Good Morning !! it's {hour}:{minute} AM")
        print(f"Good Morning !! it's {hour}:{minute} AM")
    elif hour>=12 and hour<=18:
        speak(f"Good Afternoon !! it's {hour}:{minute} PM")
        print(f"Good Afternoon !! it's {hour}:{minute} PM")
    else:
        speak(f"Good Evening !! it's {hour}:{minute} PM")
        print(f"Good Evening !! it's {hour}:{minute} PM")
    

#function 4 ) to send email
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com",587)  #open port
    server.ehlo()
    server.starttls()
    server.login("tejaswinibarya19gmail.com","topl lifp yluf cxrp")  # login id pass ( this password is used to bypass 2fa)
    server.sendmail("tejaswinibarya19@gmail.com", to , content) #to and content niche se uthayga
    server.close() 


#main body of jarvis
if __name__ == "__main__":
    speak("Initializing Jarvis") #listen for wake word jarvis
                                # obtain audio from the microphone
    wish()
    
    while True:

        query = takecommand().lower() #user jo bhi command dega usko kha store krwana hai with lower case

        #logic building for task
        if ("open notepad") in query:
            notepad = "C:\\WINDOWS\\system32\\notepad.exe" #without \\ open nahi hoga, it is used for finding files
            os.startfile(notepad)


        elif ("open command prompt") in query:
            os.system("start cmd")

            
        elif ("open camera") in query:
             os.system("start microsoft.windows.camera:")

        
        elif ("open chrome") in query:
            chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome)


        elif ("wikipedia") in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")  #replace query that can search in wikipedia
            result = wikipedia.summary(query, sentences = 2)  #speak and print result in sentences
            speak(f"according to wikipedia {result}")
            print(result)


        elif ("open youtube") in query:
            webbrowser.open("www.youtube.com")


        elif ("open facebook") in query:
            webbrowser.open("www.facebook.com")


        elif ("open instagram") in query:
            webbrowser.open("www.instagram.com")


        elif ("open linkedin") in query:
            webbrowser.open("www.linkedin.com")


        elif ("open google") in query:
            speak("Sir, what should i search on google ?")
            cmd = takecommand().lower()
            webbrowser.open(f"{cmd}")


        elif ("send message") in query:
            kit.sendwhatmsg("+919589654215", "hey there, this is Jarvis - AI Assistant ",14,45)


        elif ("send email to Tejaswini") in query:
            try :
                speak("what should i say ?")
                content = takecommand().lower()
                to = "tejaswinibarya@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to tejaswini")

            except Exception as e:
                speak("Sorry sir, i am not able to sent the email")
                print(e) 


        elif ("play music") in query:
            music_folder = "C:\\Users\\AsusVivobook15\\Music\\"
            songs = os.listdir(music_folder)
            rd = random.choice(songs) #playing random songs
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_folder, rd))

    
        elif ("find my ip address") in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"Your IP Address in {ip}")
            print(f"Your IP Address in {ip}")

        elif ("tell me joke") in query:
            jokes = pyjokes.get_joke(language="en")
            speak(jokes)
            print(jokes)

        # shutdown , restart or sleep the system

        elif ("shutdown the system") in query:
            os.system("shutdown /s /t 5")

        elif ("restart the system") in query:
            os.system("shutdown /r /t 5")

        elif ("sleep the system") in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        

    #########################  find location using ip address  ##########################


        elif ("where i am") in query or ("where we are") in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                # state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                print(f"sir i am not sure, but i think we are in {city} city of {country} country")

            except Exception as e:
                speak("sorry sir due to network issue i am unable to find where we are")
                pass


    #########################  check instagram profile  ##############################

        elif ("search instagram profile") in query or ("check instagram profile") in query:
            speak("sir, please enter the username correctly")
            username = input("Enter the username : ")
            webbrowser.open(f"www.instagram.com/{username}")
            speak(f"sir here is the profile of {username}")
            time.sleep(2)
            speak("sir would you like to download the profile picture of this account ?")
            condition = takecommand().lower()
            if "download" in condition:
                mod = instaloader.Instaloader()
                folder_path = 'C:\\Users\\AsusVivobook15\\Desktop\\Python\\Jarvis -The AI Assistant\\downloads\\instagram profiles\\'
                mod.download_profile(username, profile_pic_only=True)
                # Manually move the downloaded file to the desired folder
                for folder in os.listdir(): 
                    if folder.endswith(f'{username}') or folder.endswith('.jpg'):
                        shutil.move(folder, folder_path + folder)  # Move the file to the specified folder
                        break
                speak("Done sir, profile picture is downloaded and stored in main folder")
            else :
                speak("Got it sir!!")



    #########################  take screenshot  ##############################


        elif ("take screenshot") in query:
            speak("okay sir, please standby, taking screenshot in 3.... 2.... 1....")
            img = pyautogui.screenshot()
            folder_path = 'C:\\Users\\AsusVivobook15\\Desktop\\Python\\Jarvis -The AI Assistant\\screenshot\\'
            random_name = ''.join(random.choices(str.ascii_letters + str.digits, k=8)) + ".png"
            img.save(os.path.join(folder_path, random_name))
            speak("Done sir, screenshot is stored in main folder")


    
                