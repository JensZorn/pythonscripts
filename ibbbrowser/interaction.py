from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import speech_recognition as sr

def main(browser):
    browser=browser
    while True:
        print("Klappt")
        r = sr.Recognizer()
        with sr.Microphone(sample_rate = 48000,
                                chunk_size = 2048) as source:
            r.adjust_for_ambient_noise(source)
            print ("Say Something")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="de")
                print ("you said: " + text)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        if text=="Daumen hoch":
            try:
                inputElement = browser.find_element_by_css_selector("button[class='icon gesture'][referenceid='personal_agree']").click()
            except:
                inputElement = browser.find_element_by_css_selector("button[class='icon gesture active'][referenceid='personal_agree']").click()
        if text=="Seite":
            try:
                inputElement = browser.find_element_by_css_selector("button[class='icon'][id='personal_tools']").click()
            except:
                inputElement = browser.find_element_by_css_selector("button[class='icon active'][id='personal_tools']").click()
        if text == "exit":
            break
