import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import psutil

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def execute_command(command):
    """Execute voice commands."""
    command = command.lower()
    
    # Opening Applications
    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    
    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")
    
    elif "open chrome" in command:
        speak("Opening Google Chrome")
        os.system("start chrome")
    
    elif "open word" in command:
        speak("Opening Microsoft Word")
        os.system("start winword")
    
    elif "open excel" in command:
        speak("Opening Microsoft Excel")
        os.system("start excel")
    
    elif "open powerpoint" in command:
        speak("Opening Microsoft PowerPoint")
        os.system("start powerpnt")
    
    elif "open paint" in command:
        speak("Opening Paint")
        os.system("mspaint")
    
    # Searching Online
    elif "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        speak(f"Searching for {query}")
        webbrowser.open(url)
    
    elif "search youtube for" in command:
        query = command.replace("search youtube for", "").strip()
        url = f"https://www.youtube.com/results?search_query={query}"
        speak(f"Searching YouTube for {query}")
        webbrowser.open(url)
    
    elif "search wikipedia for" in command:
        query = command.replace("search wikipedia for", "").strip()
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except wikipedia.exceptions.DisambiguationError:
            speak("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find any information on that.")
    
    # Close all applications
    elif "close all applications" in command or "close all apps" in command:
        for process in psutil.process_iter():
            try:
                process.terminate()
            except:
                pass
        speak("All applications have been closed.")
    
    # Exit Command
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    
    # Project-Related QnA
    elif "what is leo voice assistant" in command:
        speak("Leo Voice Assistant is a Python-based voice assistant that can perform various tasks like opening applications, searching the web, answering questions, and more.")
    
    elif "which libraries does leo voice assistant use" in command:
        speak("Leo Voice Assistant uses libraries such as pyttsx3 for text-to-speech, speech recognition for voice input, os for system commands, webbrowser for online searches, and Wikipedia API for fetching information.")
    
    elif "who developed leo voice assistant" in command:
        speak("Leo Voice Assistant was developed by Rakshith Bandikatte as a voice-controlled automation project.")
    
    elif "can leo assistant work offline" in command:
        speak("Yes, Leo Assistant can perform offline tasks like opening applications and responding to predefined questions. However, web searches and Wikipedia queries require an internet connection.")
    
    elif "how does leo recognize voice" in command:
        speak("Leo uses Google's speech recognition API to convert spoken words into text and process commands accordingly.")
    
    elif "what programming language is used in leo" in command:
        speak("Leo Voice Assistant is built using Python.")
    
    elif "what can leo do" in command:
        speak("Leo can open applications, perform web searches, fetch Wikipedia summaries, answer general knowledge and project-related questions, and more.")
    
    elif "can leo be integrated with smart devices" in command:
        speak("Currently, Leo is designed for personal computer automation. With further development, it can be integrated with smart devices.")
    
    elif "is leo voice assistant customizable" in command:
        speak("Yes, Leo is fully customizable. You can modify the code to add new features and improve its functionality.")
    
    elif "does leo support multiple languages" in command:
        speak("Currently, Leo only supports English. However, it can be extended to support multiple languages using additional libraries.")
    
    # General Knowledge QnA
    elif "who was the first president of india" in command:
        speak("Dr. Rajendra Prasad.")
    
    elif "what is the largest ocean on earth" in command:
        speak("Pacific Ocean.")
    
    elif "which planet is known as the red planet" in command:
        speak("Mars.")
    
    elif "who wrote the national anthem of india" in command:
        speak("Rabindranath Tagore.")
    
    elif "which is the longest river in the world" in command:
        speak("Nile River.")
    
    elif "who discovered gravity" in command:
        speak("Sir Isaac Newton.")
    
    elif "which is the smallest continent" in command:
        speak("Australia.")
    
    elif "who is known as the father of computers" in command:
        speak("Charles Babbage.")
    
    elif "what is the chemical symbol for water" in command:
        speak("H2O.")
    
    elif "which country is known as the land of the rising sun" in command:
        speak("Japan.")
    
    elif "how many bones are there in an adult human body" in command:
        speak("206.")
    
    elif "which gas do plants absorb during photosynthesis" in command:
        speak("Carbon Dioxide, also known as CO2.")
    
    elif "who invented the telephone" in command:
        speak("Alexander Graham Bell.")
    
    elif "what is the currency of japan" in command:
        speak("Japanese Yen.")
    
    elif "which is the national animal of india" in command:
        speak("The Bengal Tiger.")

    else:
        speak("Sorry, I didn't understand that.")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("There was an error connecting to the recognition service.")
        return ""

if __name__ == "__main__":
    speak("Hello, I am Leo. How can I assist you today?")
    while True:
        command = listen()
        if command:
            execute_command(command)