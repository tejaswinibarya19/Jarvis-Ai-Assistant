#importing libraries

import pyttsx3  #this provide engine which convert voice into text
import speech_recognition as sr # type: ignore
import datetime
import os
import sys
import webbrowser
import random
import requests 
import wikipedia # type: ignore
import pywhatkit as kit # type: ignore
import smtplib
import time
import pyjokes # type: ignore
import instaloader # type: ignore
import pyautogui # type: ignore
import string as str
from pytube import YouTube # type: ignore
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets    
from PyQt5.QtCore import QTimer, QTime, QDate , Qt
from PyQt5.QtGui import QMovie  #Gif running with the help of this
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
# from jarvisui import Ui_JarvisGui  #class import from ui file
from jarvisui import Ui_MainWindow

#function 1) convert text to speech
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

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

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com",587)  #open port
    server.ehlo()
    server.starttls()
    server.login("tejaswinibarya19@gmail.com","topl lifp yluf cxrp")  # login id pass ( this password is used to bypass 2fa)
    server.sendmail("tejaswinibarya19@gmail.com", to , content) #to and content niche se uthayga
    server.close() 


#class creation
class MainThread(QThread): #class inherit
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

#function 2 ) take command from user
    def takecommand(self):
        r = sr.Recognizer()
        while True:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=15, phrase_time_limit=2) #timeout means how mmuch time it take to listen and recognizing and phrase time limit parameter means kitne der ka pause app le sakte ho bolte time
                # recognize speech using google to recognize clear input and give hindi output also

                try:
                        print("Recognizing...")
                        self.query = r.recognize_google(audio, language='en-in')
                        print(f"User Said : {self.query}")

                        if self.query.lower() == "jarvis stop":
                            speak("Okay Boss, I'll stop listening.")
                            break  # Exit the loop if the user says "stop listening"

                        if self.query.lower() == "jarvis":
                            speak("Yes Boss, How May I Help You?")

                        return self.query.lower()

                except sr.UnknownValueError:
                        print("Jarvis could not understand audio, speak clearly!!")
                except sr.RequestError as e:
                        print("Error; {0}".format(e))

#funtion 3) for task execution
    def TaskExecution(self):
#main body of jarvis
        speak("Initializing Jarvis") #listen for wake word jarvis
                                    # obtain audio from the microphone
        wish()
        
        while True:

            self.query = self.takecommand().lower() #user jo bhi command dega usko kha store krwana hai with lower case

            #logic building for task
            if ("open notepad") in self.query:
                notepad = "C:\\WINDOWS\\system32\\notepad.exe" #without \\ open nahi hoga, it is used for finding files
                os.startfile(notepad)


            elif ("open command prompt") in self.query:
                os.system("start cmd")

                
            elif ("open camera") in self.query:
                os.system("start microsoft.windows.camera:")

            
            elif ("open chrome") in self.query:
                chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chrome)


            elif ("wikipedia") in self.query:
                speak("searching wikipedia.....")
                self.query = self.query.replace("wikipedia", "")  #replace self.query that can search in wikipedia
                result = wikipedia.summary(self.query, sentences = 2)  #speak and print result in sentences
                speak(f"according to wikipedia {result}")
                print(result)


            elif ("open youtube") in self.query:
                webbrowser.open("www.youtube.com")


            elif ("open facebook") in self.query:
                webbrowser.open("www.facebook.com")


            elif ("open instagram") in self.query:
                webbrowser.open("www.instagram.com")


            elif ("open linkedin") in self.query:
                webbrowser.open("www.linkedin.com")


            elif ("open google") in self.query:
                speak("Sir, what should i search on google ?")
                cmd = self.takecommand().lower()
                webbrowser.open(f"{cmd}")


            elif ("send message") in self.query:
                number =int(input("Write the number : "))
                message = input("Enter the message you want to send : ")
                time_hour = int(input("Write Hour (24hr format) : "))
                time_min = int(input("Write Minute (24hr format): "))
                kit.sendwhatmsg(f"+91{number}", f"{message}" ,time_hour,time_min)


            elif ("send email to tejaswini") in self.query:
                try :
                    speak("what should i say ?")
                    content = self.takecommand().lower()
                    to = "tejaswinibarya@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent to tejaswini")

                except Exception as e:
                    speak("Sorry sir, i am not able to sent the email")
                    print(e) 


            elif ("play music") in self.query:
                music_folder = os.path.join(os.path.expanduser("~"), "Music")
                # Filter only .mp3 songs

                songs = [song for song in os.listdir(music_folder) if song.endswith('.mp3')] #os.listdir() — folder ke sare files deta hai.
                if songs:  # check if list is not empty
                    rd = random.choice(songs)  # pick one randomly
                    os.startfile(os.path.join(music_folder, rd))
                else:
                    print("No mp3 songs found in Music folder.")

        
            elif ("find my ip address") in self.query:
                ip = requests.get('https://api.ipify.org').text
                speak(f"Your IP Address in {ip}")
                print(f"Your IP Address in {ip}")

            elif ("tell me joke") in self.query:
                jokes = pyjokes.get_joke(language="en")
                speak(jokes)
                print(jokes)

            # shutdown , restart or sleep the system

            elif ("shutdown the system") in self.query:
                os.system("shutdown /s /t 5")

            elif ("restart the system") in self.query:
                os.system("shutdown /r /t 5")

            elif ("sleep the system") in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            

        #########################  find location using ip address  ##########################


            elif ("where i am") in self.query or ("where we are") in self.query:
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

            elif ("search instagram profile") in self.query or ("check instagram profile") in self.query:
                speak("sir, please enter the username correctly")
                username = input("Enter the username : ")
                webbrowser.open(f"www.instagram.com/{username}")
                speak(f"sir here is the profile of {username}")
                time.sleep(2)
                speak("sir would you like to download the profile picture of this account ?")
                condition = self.takecommand().lower()
                if "download" in condition:
                    mod = instaloader.Instaloader()
                    import os

                    # Dynamically get the Desktop path
                    base_path = os.path.join(os.path.expanduser("~"), "Desktop", "Python", "Jarvis -The AI Assistant", "downloads", "instagram profiles")
                    folder_path = base_path + '\\'
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


            elif ("take screenshot") in self.query:
                speak("okay sir, please standby, taking screenshot in 3.... 2.... 1....")
                img = pyautogui.screenshot()
                base_path = os.path.join(os.path.expanduser("~"), "Desktop", "Python", "Jarvis -The AI Assistant", "screenshots")
                folder_path = base_path + '\\'
                random_name = ''.join(random.choices(str.ascii_letters + str.digits, k=8)) + ".png"
                img.save(os.path.join(folder_path, random_name))
                speak("Done sir, screenshot is stored in main folder")


        ######################### download youtube music ###########################

            # elif ("download youtube music") in self.query:
            #     speak("Sir kindly provide the link")
            #     yt_url = input("Enter the URL of the video you want to download: ")
            #     try :
            #         yt = YouTube(yt_url)

            #         # 2. Get the first audio-only stream 
            #         audio_stream = yt.streams.filter(only_audio=True).first()

            #         # 3. Download the audio
            #         speak("Downloading...")
            #         audio_stream.download(output_path="C:\\Users\\AsusVivobook15\\Desktop\\Python\\Jarvis -The AI Assistant\\music\\") # Save in a 'music' folder

            #         speak("Download complete!")

            #         # # Change the file from .webm (or whatever it downloads as) to .mp3
            #         # base_name, _ = os.path.splitext(downloaded_file)
            #         # new_file_name = base_name + '.mp3'
            #         # os.rename(downloaded_file, new_file_name)
            #     except Exception as e:
            #         speak("sorry sir, unable to download due to an error")
            #         print(e)

startExecution = MainThread()

# this class is used to run the gui interface

# ... (other imports)

# ... (your existing Ui_MainWindow and MainThread classes)

startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.toggleStartStop)  # Connect only to toggleStartStop

        self.is_running = False  # Flag to track if the program is running
        self.original_button_geometry = self.ui.pushButton.geometry()


    def __del__(self):
        sys.stdout = sys.__stdout__

    def toggleStartStop(self):
        if not self.is_running:
            self.startTask()
        else:
            self.close()  # Close the application if it's already running

    def startTask(self):
        if not self.is_running:
            script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute paths to the images
            background_image_path = os.path.join(script_dir, "LCPT.gif")
            try:
                remove_icc_profile(background_image_path) # type: ignore
                # Load and start GIFs (make sure paths are correct)
                self.ui.movie = QtGui.QMovie("Jarvis/utils/images/LCPT.gif")  # Adjust the path if needed
                self.ui.label.setMovie(self.ui.movie)
                self.ui.movie.start()

                self.ui.movie_2 = QtGui.QMovie("Jarvis/utils/images/pngegg.png")  # Adjust the path if needed
                self.ui.label.setMovie(self.ui.movie)  # Assuming you have label_2
                self.ui.movie_2.start()

            except Exception as e:
                pass
                # Ensure the button stays in its original position after setting the icon
                self.ui.pushButton.setGeometry(self.original_button_geometry)

            # # Start the timer to update the time display
            # timer = QTimer(self)
            # timer.timeout.connect(self.showTime)
            # timer.start(1000)

            # Start the MainThread execution
            startExecution.start()
            self.is_running = True
            self.ui.pushButton.setText("Stop")
        else:
            # If already running, do nothing or provide feedback to the user
            print("Jarvis is already running.")

    # def showTime(self):
    #     current_time = QTime.currentTime()
    #     current_date = QDate.currentDate()
    #     label_time = current_time.toString('hh:mm:ss')
    #     label_date = current_date.toString(Qt.ISODate)
    #     # self.ui.textBrowser_2.setText(label_date)
    #     # self.ui.textBrowser_3.setText(label_time)

# application
app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())