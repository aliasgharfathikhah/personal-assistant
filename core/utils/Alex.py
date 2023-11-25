import speech_recognition as sr
import winsound
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import webbrowser
import cv2
import speedtest
import pyttsx3

def run():

    def play_sound(string):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 160)
        engine.say(string)
        engine.runAndWait()
    
    def sound():
        winsound.Beep(900, 60) 
    def hi():
        play_sound('Hi how are you ? Im Alex, how can I help you?')

    def open_google():
        play_sound('Opening, Google')
        webbrowser.open_new_tab('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    
    def taking_selfie():
        play_sound('Get ready')
        play_sound('1')
        play_sound('2')
        play_sound('3')
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        ret, frame = cap.read()
        cv2.imshow('preview', frame)
        play_sound('Your selfie looks beautiful')
        cv2.imwrite('selfie.jpg', frame)
        cv2.waitKey(0)
        cap.release()
        cv2.destroyAllWindows()

    def search():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            play_sound('What should I search?')
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='fa-IR')
                play_sound(f'You said : {text}')
            except:
                play_sound('Sorry could not recognize your voice')
        
        driver = webdriver.Firefox()
        driver.get('https://www.google.com')
        input_ = driver.find_element(By.NAME,'q')
        input_.send_keys(text)
        input_.send_keys(Keys.ENTER)
        
    r = sr.Recognizer()
    how_are_you = ['hello','Hello']
    open_google1 = ['Google',]
    taking_selfie1 = ['selfie','Selfie', 'photo', 'Photo']
    serch1 = ['search',]
    with sr.Microphone() as source:
        try:
            sound()
            audio_text2 = r.record(source, duration=3)
            text2 = r.recognize_google(audio_text2, language='eng')
            words_in_text2 = text2.split()
            for word in words_in_text2:
                if word in how_are_you:
                    hi()
                    break
                elif word in open_google1:
                    open_google()
                    break

                elif word in taking_selfie1:
                    taking_selfie()
                    break
                elif word in serch1:
                    search()
        except:
            pass                    
    # return text2
    
