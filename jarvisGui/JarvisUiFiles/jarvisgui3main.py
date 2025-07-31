import PyQt5.QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5 import QtGui
import speech_recognition as sr
import pyttsx3 , datetime, sys


from jarvisgui import Ui_JarvisGUI

def speak(audio):
    ui.updateGIFsDynamically("speaking")
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


class jarvisMainClass(QThread):
    def __intit__(self):
        super(jarvisMainClass, self).__init__()

    def run(self):
        self.runJarvis()

    def commands(self):
        ui.teminalPrint("Listening...")
        ui.updateGIFsDynamically("listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
            try :
                ui.updateGIFsDynamically("listening")
                cmd = r.recognize_google_cloud(audio, language='en-in')
                ui.teminalPrint(f"You just said : {cmd}\n")
            except:
                ui.updateGIFsDynamically("speaking")
                ui.teminalPrint('Please tell me again')
                speak('Please tell me again')
                cmd = 'none'
        return cmd
    
    def runJarvis(self):
        while True:
            self.query = self.commands().lower()
            if 'time' in self.query:
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                ui.teminalPrint(f"Sir, the time is {strTime}")
                speak(f"Sir, the time is {strTime}")


startExecution = jarvisMainClass()

class Ui_Jarvis(QMainWindow):
    def __init__(self):
        super(Ui_Jarvis, self).__init__()
        self.jarvisUI = Ui_JarvisGUI()
        self.jarvisUI.setupUi(self)
        self.runALLGIFs()


    def runALLGIFs(self):
        self.jarvisUI.speakingMovie = QtGui.QMovie("C:/Users/AsusVivobook15/Desktop/Python/Jarvis -The AI Assistant/jarvisGui/JarvisUiFiles/9d87081f5ed6b386126871dc70286a50.gif")
        self.jarvisUI.loadingLabel_2.setMovie(self.jarvisUI.speakingMovie)
        self.jarvisUI.speakingMovie.start()

        self.jarvisUI.loadingMovie = QtGui.QMovie("C:/Users/AsusVivobook15/Desktop/Python/Jarvis -The AI Assistant/jarvisGui/JarvisUiFiles/loadingui.gif")
        self.jarvisUI.loadingLabel.setMovie(self.jarvisUI.loadingMovie)
        self.jarvisUI.loadingMovie.start()

        startExecution.start()

    def updateGIFsDynamically(self, state):
        if state == "speaking":
            self.jarvisUI.loadingLabel_2.raise_()
            self.jarvisUI.loadingLabel_2.show()
            self.jarvisUI.loadingLabel.hide()

        elif state == "listening":
            self.jarvisUI.loadingLabel.raise_()
            self.jarvisUI.loadingLabel.show()
            self.jarvisUI.loadingLabel_2.hide()


    def teminalPrint(self, text):
        self.jarvisUI.terminalText.appendPlainText(text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Jarvis()
    ui.show()
    sys.exit(app.exec_())