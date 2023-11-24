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
    # def sound():
    #     winsound.Beep(900, 60) 
    # def hi():
    #     winsound.PlaySound('IOK.wav', winsound.SND_FILENAME)
    # def open_google():
    #     winsound.PlaySound('open.wav', winsound.SND_FILENAME)
    #     webbrowser.open_new_tab('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    # def weather():
    #     winsound.PlaySound('w.wav', winsound.SND_FILENAME)
    #     audio_text = r.record(source, duration=2)
    #     text = r.recognize_google(audio_text, language='fa-IR')
    #     op = webdriver.FirefoxOptions()
    #     op.add_argument('--start-maximized')
    #     driver = webdriver.Firefox(options=op)
    #     driver.get('https://www.irimo.ir/far/')
    #     input_ = driver.find_element(By.NAME,'query')
    #     input_.send_keys(text)
    #     input_.send_keys(Keys.ENTER)
    #     winsound.PlaySound('c.wav', winsound.SND_FILENAME)
    # def serch():
    #     sound()
    #     op = webdriver.ChromeOptions()
    #     op.add_argument('--start-maximized')
    #     driver = webdriver.Chrome(options=op)
    #     audio_text = r.record(source, duration=2)
    #     text = r.recognize_google(audio_text, language='fa-IR')
    #     driver.get('google.com')
    #     input_ = driver.find_element(By.ID,'q')
    #     input_.send_keys(text)
    #     input_.send_keys(Keys.ENTER)
    #     time.sleep(10)

    # def ax():
    #     winsound.PlaySound('redi.wav', winsound.SND_FILENAME)
    #     winsound.PlaySound('tree.wav', winsound.SND_FILENAME)
    #     winsound.PlaySound('tow.wav', winsound.SND_FILENAME)
    #     winsound.PlaySound('one.wav', winsound.SND_FILENAME)
    #     cap = cv2.VideoCapture(0)
    #     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    #     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    #     ret, frame = cap.read()
    #     cv2.imshow('preview', frame)
    #     winsound.PlaySound('ax.wav', winsound.SND_FILENAME)
    #     cv2.imwrite('selfie.jpg', frame)
    #     cv2.waitKey(0)
    #     cap.release()
    #     cv2.destroyAllWindows()

    # def testI():
    #     speed = speedtest.Speedtest()
    #     download_speed = speed.download()
    #     winsound.PlaySound('d.wav', winsound.SND_FILENAME)
    #     print(f'{round(download_speed/1_000_000, 2)} Mbps')
    #     upload_speed = speed.upload()
    #     winsound.PlaySound('u.wav', winsound.SND_FILENAME)
    #     print(f'{round(upload_speed/1_000_000, 2)} Mbps')
    # # <input type="search" class="" tabindex="-1" aria-hidden="true">
    
    # r = sr.Recognizer()
    # how_are_you = ['خوبی','چه خبر','حالت خوبه','چه طوری','سلام']
    # Weather = ['آب','هوا','دما',]
    # open_google_app = ['گوگل رو باز کن','گوگل را باز کن']
    # with sr.Microphone() as source:
    #     try:
    #         sound()
    #         audio_text2 = r.record(source, duration=3)
    #         text2 = r.recognize_google(audio_text2, language='fa-IR')
    #         if text2 in open_google_app:
    #             open_google()
    #         elif text2 in how_are_you:
    #             hi()
    #         elif text2 in Weather:
    #             weather()
    #         elif text2 == 'عکس بگیر':
    #             ax()
    #         elif text2 == 'سرعت نت':
    #             testI()
    #     except:
    #         pass                    
    #     print(text2)
    def PSP(string):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 180)
        engine.say(string)
        engine.runAndWait()
    sting = 'This is a python example in MEDIUM'
    PSP(sting)
