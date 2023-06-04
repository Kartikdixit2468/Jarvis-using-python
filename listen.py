# Made by kartik
import speech_recognition as sr
from speak import speak

def listen():
    """ This function provide our jarvis a ability to listen. """
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            query = recognizer.listen(source, phrase_time_limit=5, timeout=5)

        try:
            print('Recognizing...')
            query = recognizer.recognize_google(query, language="en-in")
            print(f"You said: {query}")
            return str(query).lower()

        except:
            speak("Sorry I can't recognize what you say")
            speak("Please Try Again\n")
            query = "none"
            return query.lower()
    except:
        speak("Sorry I cant listen you, Try another way - ")
        query = take_input()
        return query.lower()

def take_input():
    """ 
    This function is used as a backup for listen function
    When program cannot recognize the microphone,
    it allow user to write his query in the form of text
    """
    query = str(input("Enter the Query : "))
    return query.lower()


if __name__ == '__main__':

                #  For Testing  #
    # query = listen()
    # print(f"YOU: {query}")
    pass
