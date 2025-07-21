import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia

# Speak + Print function
def speak(text):
    print(f"ELLA: {text}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female
    engine.say(text)
    engine.runAndWait()

# Greeting based on time
def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, Yashdeep!")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Yashdeep!")
    else:
        speak("Good Evening, Yashdeep!")
    speak("Ella, made by Yashdeep Yadav.")
    speak("I am your smart assistant. How may I help you today?")

# Listen from mic
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=6)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User: {query}")
        except Exception:
            speak("I didn't get that. Could you please repeat?")
            return "none"
    return query.lower()

# Respond to commands
def respond(query):
    if "hello" in query or "hi" in query:
        speak("Hello Yashdeep! How can I help you today?")

    elif "how are you" in query:
        speak("I'm doing great! How about you?")

    elif "i am fine" in query or "i'm fine" in query:
        speak("Glad to hear that!")

    elif "your name" in query:
        speak("I am Ella, your AI assistant, made by Yashdeep Yadav.")

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif "date" in query:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today is {today}")

    elif "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open gmail" in query:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "open instagram" in query:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")

    elif "open stackoverflow" in query:
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")

    elif "search" in query:
        speak("What should I search?")
        search_query = take_command()
        if search_query != "none":
            speak(f"Searching {search_query} on Google")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

    elif "who is" in query or "what is" in query:
        speak("Searching on Wikipedia")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn’t find anything on Wikipedia.")

    elif "bye" in query or "stop" in query or "exit" in query:
        speak("Goodbye Yashdeep! Have a great day.")
        return False

    else:
        speak("Sorry, I didn’t understand that.")
    return True

# Main Execution
if __name__ == "__main__":
    wish()
    while True:
        query = take_command()
        if query == "none":
            continue
        if not respond(query):
            break
