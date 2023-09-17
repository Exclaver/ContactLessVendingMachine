import speech_recognition
import pyttsx3
recognizer=speech_recognition.Recognizer()
def speech():
    global recognizer
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.5)
                audio=recognizer.listen(mic,timeout=5)

                text=recognizer.recognize_google(audio)
                text=text.lower()
                return text
                

        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            continue
        except speech_recognition.RequestError as e:
            print("Could not request results; {0}".format(e))