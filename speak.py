# Made by Kartik
import pyttsx3

try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('vooices',voices[0].id)
    engine.setProperty('rate', 175)
except Exception as e:
    print(" Sorry this program is unable to initialize speaking device or voices in your pc, \ntherefore Jarvis can't speak. ")
    print(f"Error message: {e}")

def speak(query):
    """ This function gives ability to speak to our jarvis. """
    try:
        engine.say(text=query)
        print(f"Jarvis: {query}")
        engine.runAndWait()
    
    except Exception as e:
        print(" Sorry, Unfortunately jarvis can't speak. ")
        print(f"Error message: {e}")
        print(f"\nJarvis: {query}")

if __name__ == '__main__':
    pass 
