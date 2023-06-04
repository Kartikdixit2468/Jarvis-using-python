# Made by Kartik
from speak import speak
from listen import listen


flag_trans = True
flag_wiki = True
flag_speedt = True
flag_pywkh = True
flag_pywhatkit = True
flag_pyatg = True
flag_dt = True

try:
    from googletrans import Translator
except ModuleNotFoundError:
    flag_trans = False
try:
    import datetime
except ModuleNotFoundError:
    flag_dt = False
try:
    import wikipedia as wk
except ModuleNotFoundError:
    flag_wiki = False
try:
    from pywikihow import search_wikihow
except:
    flag_pywkh = False
try:
    import pyautogui as pg
except:
    flag_pyatg = False
try:
    from pywhatkit import search
except:
    flag_pywhatkit = False
try:
    import speedtest
except ModuleNotFoundError:
    flag_speedt = False


exit_res_list = [
                "Bye",
                "I am Going.",
                "Bye Sir",
                "Good Bye",
                "goodbye",
                "It'll be Nice To Meet You Again",
                "See You Later"
            ]

# Welcome function
def welcome():
    """ this function will help jarvis to greet the user """
    msg = "Morning sir, Your AI Assistant Jarvis here."
    speak(msg)

# Non-Input Functions

def time():
    """ This function tells jarvis time. """
    if flag_dt:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"It's {time}")
    else:
        speak("Sorry, dependencies are not installed at this moment \n Please install all the modules listed in requirements.txt.")


def date():
    " This function tell jarvis date. "
    if flag_dt:
        date = datetime.date.today()
        speak(date)
    else:
        speak("Sorry, dependencies are not installed at this moment \n Please install all the modules listed in requirements.txt.")

def check_speed():
    """ This function helps jarvis to calculate the upload and download speed """

    if flag_speedt:
        speak("Checking speed...")
        try:
            speed = speedtest.Speedtest()
            speak("Running speed test...")
            download_speed = speed.download()
            upload_speed = speed.upload()
            download_speed = int(download_speed/800000)
            upload_speed = int(upload_speed/800000)
            # print(download_speed)
            # print(upload_speed)
            speak(f"Your Download speed is {download_speed} Megabit per second and")
            speak(f"Your upload speed is {upload_speed} Megabit per second.")
        except speedtest.ConfigRetrievalError or Exception as e:
            speak("Something wrong happened,\nI'm unable to connect to internet at this time. ")
    else:
        speak("Sorry, dependencies are not installed at this moment \n Please install all the modules listed in requirements.txt.")

def day():
    " This function tell jarvis day. "
    if flag_dt:
        day = datetime.datetime.now().strftime("%A")
        speak(f"Today is {day}")
    else:
        speak("Sorry, dependencies are not installed at this moment \n Please install all the modules listed in requirements.txt.")

def non_input_functions(function):
    """ 
    This function returns the non input function  when called in program.

    function: Non-Input function name. (Only string input)

    """
    function = str(function)
    if function.lower() == "time":
        time()
    
    elif function.lower() == "date":
        date()
    
    elif function.lower() == "day":
        day()
    elif function.lower() == "screenshot":
        take_screenshot()
    
    elif function.lower() == "internet_speed":
        check_speed()
      
    elif function == "translate":
        translate_()

# Input Functions

def how_todo_with_steps(s_query):
    """"

    This function returns the searched text about query from wikipedia.
    s_query: Query to search.
    tag: Wikipedia (Needed)

    """
    
    if flag_pywkh:
        s_query = str(s_query).lower()
        removable_words = ["jarvis", "hii", "hello", "please", "please tell me", "tell me", "ok tell me", "ok"]
        for i in removable_words:
            s_query = str(s_query).replace(i, "")
        print(s_query)

        result = search_wikihow(s_query)
        result = result[0].summary
        speak(f"According to wikipedia:  {str(result)}")
    else:
        speak("Sorry, dependencies are not installed at this moment \n Please install all the modules listed in requirements.txt.")


def wikipedia_(s_query):
    """"

    This function returns the searched text about query from wikipedia.
    s_query: Query to search.
    tag: Wikipedia (Needed)

    """

    if flag_wiki:
        s_query = str(s_query).replace("what is ","")
        s_query = str(s_query).replace("Search on wikipedia","")
        s_query = str(s_query).replace("wikipedia","")
        s_query = str(s_query).replace("Search ","")
        s_query = str(s_query).replace("meaning of","")
        s_query = str(s_query).replace("who is","")
        s_query = str(s_query).replace("who","")
        s_query = str(s_query).replace("is","")
        s_query = str(s_query).replace("Jarvis","")
        try:
            result = wk.summary(s_query, sentences=2)
        except:
            search(s_query)
            result = "I found this on the web."
        speak(result)
    else:
        speak("Sorry, dependencies are not installed at this moment \n Please install all the modules listed in requirements.txt.")

def google_search(s_query):
    """"

    This function returns the searched text about query from google.
    s_query: Query to search.

    """

    if flag_pywhatkit:

        query = str(s_query)
        query = query.replace('jarvis', "")
        query = query.replace('google', "")
        query = query.replace('search', "")
        query = query.replace('the', "")
        query = query.replace('on', "")
        search(query)

    else:
        speak("Sorry, dependencies are not installed at this moment \n Please install all the modules listed in requirements.txt.")

def translate_(query='None' ,lang='hi' ,TransLang='en'):
    """
     This function translate line hindi to english.
    
    TransLang: language to which you want to translate. (Default: English)
    TransLang: language given in input. (Default: hindi)

    """
    
    if flag_trans:

        query = str(query)
        if query == 'None':
            speak("Tell Me The Text!")
            query = str(listen())
        if lang == 'hi' and TransLang == "en":
            traslate = Translator()
            result = traslate.translate(src='hi', text=query)
            text = result.text
        speak(f"Translated text is : {text}.")

    else:
        speak("Sorry, dependencies are not installed at this moment \n Please install all the modules listed in requirements.txt.")


def take_screenshot():
    """ This function helps jarvis to take the screenshot. """
    
    if flag_trans:

        speak("Ok Sir , What Should I Name That File ?")
        file_name = listen()
        file_name = file_name + ".png"
        path1 = "F:\\"+ file_name
        ss = pg.screenshot()
        ss.save(path1)
        speak("ScreenShot Saved") 

    else:
        speak("Sorry, dependencies are not installed at this moment \n Please install all the modules listed in requirements.txt.")


def input_functions(function, query):
    """ 
    This function returns the input function  when called in program.

    function: Input function name. (Only string input)
    query: input of function.

    """
    function = str(function).lower()
    if function == "wiki":
        wikipedia_(query)
    
    elif function == "google_search":
        google_search(query)
    
        
    elif function == "wikipedia":
        wikipedia_(query)

    
    elif function == "how_to":
        how_todo_with_steps(query)
    
        
    elif function == "feedback":
        feedback()


# other functions
def feedback():
    """ This function helps jarvis to take the feedback """
    speak('Thank You, for helping us let me know your feedback,\n ')
    feedback = str(listen())
    speak('Please tell me your name also.')
    name = str(listen())

    with open("feedback.txt", 'a') as file:
        data = f'\nFEEDBACK: {feedback}\nDATE: {datetime.date.today()}\nUSER: {name}'
        data = str(data)
        file.write(data)


if __name__ == "__main__":
    pass
