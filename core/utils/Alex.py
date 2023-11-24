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
        engine.setProperty('rate', 180)
        engine.say(string)
        engine.runAndWait()
    
    def sound():
        winsound.Beep(900, 60) 
    def hi():
        play_sound('Hello. How are you')

    def open_google():
        play_sound('Open Google')
        webbrowser.open_new_tab('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    
    r = sr.Recognizer()
    how_are_you = ['خوبی','چه خبر','حالت خوبه','چه طوری','سلام']
    with sr.Microphone() as source:
        try:
            sound()
            audio_text2 = r.record(source, duration=3)
            text2 = r.recognize_google(audio_text2, language='eng')
            if text2 in how_are_you:
                hi()
            elif text2 in how_are_you:
                hi()
        except:
            pass                    
        
    
